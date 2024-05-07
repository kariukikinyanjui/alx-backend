import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

const app = express();

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.id);
  res.json({ ...item, currentQuantity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    return res.status(404).json({ status: 'Product not found' });
  }
  const currentQuantity = await getCurrentReservedStockById(item.id);
  if (currentQuantity <= 0) {
    return res.status(403).json({ status: 'Not enough stock available', itemId: item.id });
  }
  await reserveStockById(item.id, currentQuantity - 1);
  res.json({ status: 'Reservation confirmed', itemId: item.id });
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

