DROP TABLE IF EXISTS movie;

CREATE TABLE movie (
    imdbID INTEGER PRIMARY KEY,
    title VARCHAR(255),
    year VARCHAR(255),
    director VARCHAR(255),
    plot VARCHAR(255)
);


-- Create the favorites table
CREATE TABLE favorites (
    id SERIAL PRIMARY KEY,                
    movie_id INTEGER REFERENCES movie(imdbID) 
);