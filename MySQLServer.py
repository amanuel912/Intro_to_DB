import mysql.connector
def create_tables():
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
            # 2. ALL TABLE CREATION STATEMENTS AS STRINGS
            table_queries = [
                # AUTHORS TABLE
                """
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INT PRIMARY KEY AUTO_INCREMENT,
                    author_name VARCHAR(215)
                )
                """,

                # BOOKS TABLE
                """
                CREATE TABLE IF NOT EXISTS Books (
                    book_id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(130),
                    author_id INT,
                    price DOUBLE,
                    publication_date DATE,
                    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
                )
                """,

                # CUSTOMERS TABLE
                """
                CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INT PRIMARY KEY AUTO_INCREMENT,
                    customer_name VARCHAR(215),
                    email VARCHAR(215),
                    address TEXT
                )
                """,

                # ORDERS TABLE
                """
                CREATE TABLE IF NOT EXISTS Orders (
                    order_id INT PRIMARY KEY AUTO_INCREMENT,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                )
                """,

                # ORDER_DETAILS TABLE
                """
                CREATE TABLE IF NOT EXISTS Order_Details (
                    orderdetailid INT PRIMARY KEY AUTO_INCREMENT,
                    order_id INT,
                    book_id INT,
                    quantity DOUBLE,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (book_id) REFERENCES Books(book_id)
                )
                """
            ]

            # 3. EXECUTE ALL TABLE CREATION QUERIES
            for query in table_queries:
                cursor.execute(query)

            connection.commit()
            print("All tables created successfully!")

    except mysql.connector.Error as err:
        print("Error while creating tables:", err)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_tables()
