CREATE TABLE calendar (
	date DATE,
	recipe_id INT,
	meal_type INT,
	servings DECIMAL,
    PRIMARY KEY (date, recipe_id, meal_type)
);

CREATE TABLE recipes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	link VARCHAR(1024)
);

CREATE TABLE meal_types (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255)
);

CREATE TABLE units (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255)
);

CREATE TABLE ingredients (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	base_amount DECIMAL,
	unit_id INT,
	calories DECIMAL,
	fat DECIMAL,
	saturated_fat DECIMAL,
	unsaturated_fat DECIMAL,
	carbohydrates DECIMAL,
	fiber DECIMAL,
	sugar DECIMAL,
	protein DECIMAL,
	sodium DECIMAL,
	cholesteral DECIMAL
);

CREATE TABLE recipe_ingredients (
	recipe_id INT,
	ingredient_id INT,
    PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE conversions (
	to_unit_id INT,
	from_unit_id INT,
	multiplier DECIMAL,
    PRIMARY KEY (to_unit_id, from_unit_id)
);
