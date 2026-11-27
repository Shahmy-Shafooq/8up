CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seller_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    category TEXT,
    in_stock INTEGER DEFAULT 1,
    image TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
