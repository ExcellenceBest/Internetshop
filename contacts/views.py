from django.shortcuts import render
from django.http import HttpRequest
from contacts.contacts import ProductsContainer
from basket.database import DBConnect
from datetime import date


def redirect(request: HttpRequest):
    return render(request, '404.html')


def main(request: HttpRequest):
    connect1 = DBConnect.get_connect_all(dbname='shop',
                                         host='localhost',
                                         port=5432,
                                         user='postgres',
                                         password='valera123')

    cursor = connect1.cursor()
    query = """ SELECT * FROM commentaries """
    cursor.execute(query)
    container = ProductsContainer()
    container.create_list_product(cursor.fetchall())
    data = container.get_list_product()
    cursor.close()
    context = {
        "data": data
    }
    return render(request, 'contacts.html', context=context)


def comment(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='shop',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='valera123')

    cursor = connect.cursor()

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comm = request.POST.get('comm', '')
        comment_date = date.today()


    params = (email, name, comm, comment_date)
    query = """ INSERT INTO commentaries(email, name, comment, comment_date)
                                 VALUES (%s, %s, %s, %s)"""

    cursor.execute(query, params)
    connect.commit()
    cursor.close()
    return render(request, template_name='comment.html')
