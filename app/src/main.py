from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import requests


app = FastAPI()

url = "https://www.omdbapi.com"
key = "4bfcb60e"

favorites = []


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1> Which Movie? </h1>
    <form action="/submit/" method="post">
        <input type="text" name="name" placeholder="Search Movie" required>
        <button type="submit">Submit</button>
    </form>
    """


def search_movie(params: dict)->dict:
    
    all_data = requests.get(url=url, params=params).json()

    if "False" in all_data["Response"]:
        return 
    else:
        return all_data

@app.post("/submit/", response_class=HTMLResponse)
def submit(name: str = Form(...)):

    response = requests.get(url, params={"apikey": key, "t": name})
    data = response.json()

    if response.status_code == 200 and data.get("Response") == "True":
        add_to_favorites(data)
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
        return """
        <h1>Movie not found</h1>
        <a href="/">Search another movie</a>
        """
    

@app.get("/favorites", response_class=HTMLResponse)
def view_favorites():
    if not favorites:
        return "<h1>No favorite movies yet</h1><a href='/'>Search for movies</a>"
    favorites_html = "<h1>Favorite Movies</h1><ul>"
    for movie in favorites:
        favorites_html += f"<li>{movie['Title']} ({movie['Year']})</li>"
    favorites_html += "</ul><a href='/'>Search for more movies</a>"
    return favorites_html

def add_to_favorites(movie: dict):
    favorites.append(movie)