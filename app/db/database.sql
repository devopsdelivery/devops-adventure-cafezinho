DROP TABLE IF EXISTS favorites;

CREATE TABLE favorites (
    imdbID INTEGER PRIMARY KEY,
    title VARCHAR(255),
    year VARCHAR(255),
    director VARCHAR(255),
    plot VARCHAR(255)
);
