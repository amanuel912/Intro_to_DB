import mysql.connector
def create_db():
    try:
        # 1. CONNECT DIRECTLY INTO THE DATABASE
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin@2323",
            database="alx_book_store"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
            connection.commit()
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print("Error while creating db:", err)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_db()
