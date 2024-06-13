CREATE TABLE IF NOT EXISTS wizard (
    id UUID PRIMARY KEY, 
    first_name varchar, 
    last_name varchar
);

CREATE TABLE IF NOT EXISTS elixir (
    id UUID PRIMARY KEY, 
    name varchar, 
    effect varchar,
    side_effects varchar,
    characteristics varchar,
    time varchar,
    difficulty varchar,
    ingredients UUID[],
    inventors UUID[],
    manufacturer varchar
);

CREATE TABLE IF NOT EXISTS ingredient (
    id UUID PRIMARY KEY, 
    name varchar
);