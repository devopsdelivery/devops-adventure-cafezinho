from fastapi import FastAPI, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse
import requests
from database import add_movie

app = FastAPI()

OMDB_URL = "https://www.omdbapi.com"
OMDB_KEY = "4bfcb60e"


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <h1>Which Movie?</h1>
    <form action="/submit/" method="post">
        <input type="text" name="name" placeholder="Search Movie" required>
        <button type="submit">Submit</button>
    </form>
    """


# Route to search and add a movie to favorites
@app.post("/submit/", response_class=HTMLResponse)
async def submit(name: str = Form(...)):
    # Make a request to the OMDb API to fetch movie details
    response = requests.get(OMDB_URL, params={"apikey": OMDB_KEY, "t": name})
    
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Failed to connect to OMDb API")
    
    data = response.json()
    if data.get("Response") == "True":
        movie = {
            "imdbID": int(data.get("imdbID", "0").lstrip("tt")),
            "title": data.get("Title", "N/A"),
            "year": data.get("Year", "N/A"),
            "director": data.get("Director", "N/A"),
            "plot": data.get("Plot", "N/A"),
        }

        await add_movie(movie)

        return f"""
        <h1>Movie: {movie['title']}</h1>
        <p>Year: {movie['year']}</p>
        <p>Director: {movie['director']}</p>
        <p>Plot: {movie['plot']}</p>
        <a href="/">Search another movie</a>
        <br>
        <a href="/favorites">View Favorites</a>
        """
    else:
        raise HTTPException(status_code=404, detail="Movie not found")
