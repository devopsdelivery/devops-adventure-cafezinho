import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from databases import Database

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/movies")

# Initialize database connection and metadata
database = Database(DATABASE_URL)
metadata = MetaData()

# Define the 'favorites' table schema
favorites = Table(
    "favorites",
    metadata,
    Column("imdbID", Integer, primary_key=True),
    Column("title", String(255), nullable=False),
    Column("year", String(4), nullable=False),
    Column("director", String(255)),
    Column("plot", String),
)

# Create an engine to manage the table structure
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Function to connect and disconnect the database
async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()

# Function to add a movie to favorites
async def add_movie(movie):
    query = favorites.insert().values(
        imdbID=movie["imdbID"],
        title=movie["Title"],
        year=movie["Year"],
        director=movie["Director"],
        plot=movie["Plot"]
    )
    await database.execute(query)

# Function to retrieve all favorite movies
async def get_favorites():
    query = favorites.select()
    return await database.fetch_all(query)

# Optional: Function to get connection details for debugging
def get_connection_info():
    return {
        "database": os.path.basename(DATABASE_URL.split("/")[-1]),
        "user": DATABASE_URL.split(":")[1].split("//")[-1],
        "host": DATABASE_URL.split("@")[-1].split(":")[0],
        "port": DATABASE_URL.split(":")[-1].split("/")[0],
    }

# Example usage of get_connection_info (this could be called in your main application)
if __name__ == "__main__":
    connection_info = get_connection_info()
    print("Database Connection Info:")
    print(f"Database Name: {connection_info['database']}")
    print(f"User: {connection_info['user']}")
    print(f"Host: {connection_info['host']}")
    print(f"Port: {connection_info['port']}")
