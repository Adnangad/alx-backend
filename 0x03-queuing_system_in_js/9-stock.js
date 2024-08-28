import redis from "redis";
const { promisify } = require("util");
const express = require("express");

const client = redis.createClient();
client.on("connect", () => {
  console.log(`Successfully connected to the Redis server`);
});
client.on("error", (error) => {
  console.error(`Redis error: ${error}`);
  throw error;
});

const get = promisify(client.get).bind(client);
const set = promisify(client.set).bind(client);

const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.Id === id);
}

async function reserveStockById(ItemId, stock) {
  const key = `item.${ItemId}`;
  await set(key, stock);
}

async function getCurrentReservedStockById(ItemId) {
  const key = `item.${ItemId}`;
  const val = await get(key);
  return val;
}

const PORT = 1245;
const app = express();

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

app.get("/list_products/:itemId(\\d+)", async (req, res) => {
  const itemid = Number(req.params.itemId);
  const item = getItemById(itemid);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reservedStock = await getCurrentReservedStockById(itemid);
  const currentStock = reservedStock !== null ? reservedStock : item.stock;

  res.json({
    Id: item.Id,
    name: item.name,
    price: item.price,
    stock: currentStock,
  });
});

app.get("/reserve_product/:itemId(\\d+)", async (req, res) => {
  const itemid = Number(req.params.itemId);
  const item = getItemById(itemid);

  if (!item) {
    return res.json({ status: "Product not found" });
  }

  const reservedStock = await getCurrentReservedStockById(itemid);
  const currentStock =
    reservedStock !== null ? reservedStock : item.currentQuantity;

  if (currentStock <= 0) {
    return res.json({ status: "Not enough stock available", itemId: item.Id });
  }

  const newStock = currentStock - 1;
  await reserveStockById(itemid, newStock);

  res.json({ status: "Reservation confirmed", itemId: item.Id });
});

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
