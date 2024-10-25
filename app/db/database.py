from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import psycopg2


connection = psycopg2.connect(database="postgres", user='postgres', password='postgres', host="localhost", port=5433)


cursor = connection.cursor()

sql_context ="""
select * from favorites;
"""

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
        INSERT INTO favorites (imdbID, title, year, director, plot) 
        VALUES (%s, %s, %s, %s, %s);
        """
        
        # Execute the query with the provided data
        cursor.execute(insert_query, (movie["imdbID"], movie["title"], movie["year"], movie["director"], movie["plot"]))
        
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

def add_favorite(imdbID):
    try:
        connection = get_db_connection()
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Define the SQL SELECT query
        search_query = """
        SELECT * FROM movie WHERE imdbID = %s;
        """
        
        # Execute the query with the provided imdbID
        cursor.execute(search_query, (imdbID,))
        
        # Fetch the result
        movie = cursor.fetchone()
        
        if movie:
            print("Movie found:", movie)
        else:
            print("Movie not found")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while fetching from PostgreSQL", error)
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()

def remove_movie(imdbID):
    try:
        connection = get_db_connection()
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Define the SQL DELETE query
        delete_query = """
        DELETE FROM favorites WHERE imdbID = %s;
        """
        
        # Execute the query with the provided imdbID
        cursor.execute(delete_query, (imdbID,))
        
        # Commit the transaction
        connection.commit()
        
        print("Record deleted successfully")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while deleting from PostgreSQL", error)
    finally:
        # Close the cursor and connection
        if connection:
            cursor.close()
            connection.close()



cursor.execute(sql_context)

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)


