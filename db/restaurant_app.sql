DROP TABLE IF EXISTS meals;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS ingredients;

CREATE TABLE meals (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  cost_price int,
  selling_price int,
  qty_available int,
  qty_sold int
  -- Lookup Wizard to create a drop down list of ingredients?
  -- supplier_id INT REFERENCES supplier(id)
  -- not sure how to reference supplier id when table only pulls ingredient id?
);


-- CREATE TABLE orders (
--   id SERIAL PRIMARY KEY,
--   order_number INT,
--   order_raised datetime DEFAULT CURRENT_TIMESTAMP,
--   meals_id INT REFERENCES meals(id),
--   order_qty INT
-- );


CREATE TABLE ingredients (
  id SERIAL PRIMARY KEY,
  ingredient_name VARCHAR(255),
  description VARCHAR(255),
  -- could change later to ingredient category; make like meat, veg etc.
  supplier_name VARCHAR(255),
  -- cost_price int,
  -- selling_price int,
  -- removed above and changed to profit margin as per below to simplify
  profit_margin_on_ingredient_portion int,
  ingredient_portions_available int,
  qty_of_ingredient_portion_sold int
  -- Lookup Wizard to create a drop down list of ingredients?
  -- supplier_id INT REFERENCES supplier(id)
);



-- tables, orders and dishes - start with dishes. 
-- Manual incr. and desc. functions initially (stock taking for dishes initially)
