-- Initialize Database
-- Andrew Gentile
-- 2021-01-21


-- Create Version Table
CREATE TABLE IF NOT EXISTS "versions" (
    id INT PRIMARY KEY,
    description TEXT,
    updated_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO "versions" (id, description) VALUES (
    0,
    'initialize database'
);
