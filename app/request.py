import urllib.request,json
from .models import Book


# Getting the book base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['BOOKS_URL']


def get_books(category):
    '''
    Function that gets the json response to our url request
    '''
    get_books_url = base_url.format(category)

    with urllib.request.urlopen(get_books_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)
        

        book_results = None

        if get_books_response['items']:

            book_results_list = get_books_response['items']
            book_results = process_results(book_results_list)

            print(book_results)

            


    return book_results

def process_results(book_list):
    '''
    Function  that processes the book result and transform them to a list of Objects

    Args:
        book_list: A list of dictionaries that contain book details

    Returns :
        book_results: A list of book objects
    '''
    
    book_results = []

    for item in book_list:
        # print(item['volumeInfo']['description'])
        
        id = item['id']
        title = item['volumeInfo']['title']
        author = item['volumeInfo'].get('authors') 
        book_description = item['volumeInfo'].get('description')
        thumbnail = item['volumeInfo']['imageLinks']['thumbnail']
        webReaderLink = item['accessInfo']['webReaderLink']


        if thumbnail:
            book_object = Book(id,title,author,book_description,thumbnail,webReaderLink)
            print(book_object.author)
            book_results.append(book_object)

    return book_results


def get_book(id):
    get_book_details_url = base_url.format(id)

    with urllib.request.urlopen(get_book_details_url) as url:
        book_details_data = url.read()
        book_details_response = json.loads(book_details_data)

        print(book_details_response)


        book_object = None

        if book_details_response:

            items = book_details_response['items']

            for item in items:

                id = item['id']
                title = item['volumeInfo']['title']
                author = item['volumeInfo'].get('authors') 
                book_description = item['volumeInfo'].get('description')
                thumbnail = item['volumeInfo']['imageLinks']['thumbnail']
                webReaderLink = item['accessInfo']['webReaderLink']

         
                if thumbnail:
                    book_object = Book(id,title,author,book_description,thumbnail,webReaderLink)
           
           
    return book_object




