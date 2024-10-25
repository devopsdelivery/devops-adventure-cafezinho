from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import psycopg2


#connection = psycopg2.connect(database="postgres", user='postgres', password='postgres', host="localhost", port=5433)

def get_db_connection():
    try:
        connection = psycopg2.connect(
            database="postgres", 
            user='postgres', 
            password='postgres', 
            host="localhost", 
            port=5433
        )
        return connection
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

def add_movie(movie: dict):
    try:
        connection = get_db_connection()
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Define the SQL INSERT query
        insert_query = """
        INSERT INTO movie (imdbID, title, year, director, plot) 
        VALUES (%s, %s, %s, %s, %s);
        """
        
        # Execute the query with the provided data
        cursor.execute(insert_query, (movie['imdbID'], movie['title'], movie['year'], movie['director'], movie['plot']))
        
        # Commit the transaction
        connection.commit()
        
        print("Record inserted successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting into PostgreSQL", error)
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    add_movie()