import express from 'express';
import redis from 'redis';
import { promisify } from 'util';
import kue from 'kue';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

let reservationEnabled = true;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats;
}

const queue = kue.createQueue();

const app = express();

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat')
    .save((err) => {
      if (err) {
        return res.json({ status: 'Reservation failed' });
      }
      console.log(`Seat reservation job ${job.id} created`);
      res.json({ status: 'Reservation in process' });
    });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();
    seats--;
    if (seats < 0) {
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat(seats);
      if (seats === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
  res.json({ status: 'Queue processing' });
});

app.listen(1245, async () => {
  console.log('Server running on port 1245');
  await reserveSeat(50);
});

