CREATE SCHEMA analitics;

SET search_path=analitics;

CREATE TABLE Ship (
  id SERIAL PRIMARY KEY ,
  data_ship text[] NOT NULL,
  max_weight real NOT NULL CONSTRAINT positive_max_weight CHECK (max_weight>0),
  max_stock int NOT NULL
);

COPY Ship (max_weight, max_stock, data_ship) FROM '/tmp/db_tables_csv/ship.csv' DELIMITER ',' CSV;

CREATE TABLE Visit (
  id SERIAL PRIMARY KEY,
  port_departure JSONB NOT NULL,
  date_departure timestamp DEFAULT localtimestamp NOT NULL,
  year_departure int NOT NULL,
  season_departure varchar(6) NOT NULL,
  port_arrival JSONB NOT NULL,
  date_arrival timestamp NOT NULL,
  year_arrival int NOT NULL,
  season_arrival varchar(6) NOT NULL,
  id_ship int REFERENCES Ship(id) NOT NULL
);

COPY Visit (port_departure, date_departure, year_departure, season_departure, port_arrival, date_arrival, year_arrival, season_arrival, id_ship) FROM '/tmp/db_tables_csv/visit.csv' DELIMITER ',' CSV;

DROP TABLE Cargo

CREATE TABLE Cargo (
  id SERIAL PRIMARY KEY,
  id_visit int REFERENCES Visit(id) NOT NULL,
  category_product character varying(255) NOT NULL,
  name_product TEXT NOT NULL,
  data_product JSONB NOT NULL
);

COPY Cargo (id_visit, category_product, name_product, data_product) FROM '/tmp/db_tables_csv/cargo.csv' DELIMITER ',' CSV;
	
	