from Les_Book.config.mysqlconnection import connectToMySQL
from Les_Book import BASE_DE_DATOS
from flask import flash


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.year = data['year']
        self.img = data['img']
        self.comments = data['comments']
    
    
    @classmethod
    def all_book(cls):
        query = "SELECT * FROM books;"
        return connectToMySQL(BASE_DE_DATOS).query_db(query)    
           
    @classmethod
    def search(cls, data):
        query = "SELECT * FROM books WHERE title = %(title)s;"
        results = connectToMySQL(BASE_DE_DATOS).query_db(query, data)
        
        books = []  
        
        for result in results:
            book = Book(result)  # Crea un objeto Book para cada resultado
            books.append(book)  # Agrega el libro a la lista
        

        return books  # Devuelve la lista de libros encontrados

    @classmethod
    def add(cls, data):
        query = """
            INSERT INTO books(title,author,year,img, comments)
            VALUES(%(title)s,%(author)s, %(year)s,%(img)s,%(comments)s); 
        """
        id_book = connectToMySQL(BASE_DE_DATOS).query_db(query, data)   
        return id_book
    
    
    @classmethod
    def delete(cls, data):
        query = """
            DELETE FROM books WHERE ID = %(id)s;
        """
        return connectToMySQL(BASE_DE_DATOS).query_db(query, data)
        

    @classmethod
    def book_id(cls, data):
        query="""
            SELECT * FROM books WHERE ID = %(id)s;
        """
        
        return connectToMySQL(BASE_DE_DATOS).query_db(query, data)
    
    @classmethod
    def edit(cls, data):
        query = """
            UPDATE books
            set title = %(title)s, author = %(author)s, year = %(year)s, img = %(img)s, comments = %(comments)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(BASE_DE_DATOS).query_db(query, data)
    
    @classmethod
    def get_one_edit(cls, data):
        query = """
            SELECT * FROM books WHERE id = %(id)s;
        """
        result = connectToMySQL(BASE_DE_DATOS).query_db(query, data)
        book = Book(result[0])
        return book
    
