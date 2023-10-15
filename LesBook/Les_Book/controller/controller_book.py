from flask import render_template, request, redirect
from Les_Book import app
from Les_Book.models.model_book import Book


@app.route('/', methods=['GET'])
def get_books():
    list_books = Book.all_book()
    return render_template('index.html', list_books=list_books)


@app.route('/search', methods=['POST'])
def search_books():
    title = request.form.get('title')  # Obtén el título del formulario
    data = {"title": title}

    books = Book.search(data)

    return render_template('search.html', books=books)

@app.route('/add', methods=['GET'])
def add_book():
    return render_template('add.html')

@app.route('/add/book', methods=['POST'])
def add_new_book():
    data = {
        **request.form
    }
    book_created = Book.add(data)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    data = {
        'id' : id
    }
    Book.delete(data)
    return redirect('/')
    
    
@app.route('/book/<int:id>', methods=['GET'])
def book_info(id):
    data = {
        'id' : id
    }
    book = Book.book_id(data)
    return render_template('book.html', book = book)

@app.route('/edit/book/<int:id>', methods=['GET'])
def get_edit_book(id):
    data = {
        'id' : id
    }
    book = Book.get_one_edit(data)
    return render_template('edit.html', book = book)

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    data = {
        **request.form,
        'id' : id
    }
    Book.edit(data)
    return redirect('/')