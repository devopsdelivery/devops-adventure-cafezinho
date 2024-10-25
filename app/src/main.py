from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
import requests
from ..db.database import database, connect_db, disconnect_db, add_movie, get_favorites

app = FastAPI()

omdb_url = "https://www.omdbapi.com"
omdb_key = "4bfcb60e"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <h1> Which Movie? </h1>
    <form action="/submit/" method="post">
        <input type="text" name="name" placeholder="Search Movie" required>
        <button type="submit">Submit</button>
    </form>
    """

# Route to search and add a movie to favorites
@app.post("/submit/", response_class=HTMLResponse)
async def submit(name: str = Form(...)):
    response = requests.get(omdb_url, params={"apikey": omdb_key, "t": name})
    data = response.json()

    if response.status_code == 200 and data.get("Response") == "True":
        await add_movie(data)
        return f"""
        <h1>Movie: {data['Title']}</h1>
        <p>Year: {data['Year']}</p>
        <p>Director: {data['Director']}</p>
        <p>Plot: {data['Plot']}</p>
        <a href="/">Search another movie</a>
        <br>
        <a href="/favorites">View Favorites</a>
        """
    else:
        raise HTTPException(status_code=404, detail="Movie not found")

# Route to view favorite movies
@app.get("/favorites", response_class=HTMLResponse)
async def view_favorites():
    favorite_movies = await get_favorites()

    if not favorite_movies:
        return "<h1>No favorite movies yet</h1><a href='/'>Search for movies</a>"
    
    favorites_html = "<h1>Favorite Movies</h1><ul>"
    for movie in favorite_movies:
        favorites_html += f"<li>{movie['title']} ({movie['year']})</li>"
    favorites_html += "</ul><a href='/'>Search for more movies</a>"
    
    return favorites_html

# Startup and shutdown events to connect and disconnect the database
@app.on_event("startup")
async def startup():
    await connect_db()

@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
