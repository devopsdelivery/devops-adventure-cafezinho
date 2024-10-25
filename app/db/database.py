import os
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Fetch the database URL from environment variables for security
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost/movies")

# Initialize database and metadata
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

# Create an engine and connect to the database
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        metadata.create_all(connection)
    print("Database and table created successfully.")
except SQLAlchemyError as e:
    print(f"Error: {e}")
