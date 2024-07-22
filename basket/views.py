from django.shortcuts import render
from django.http import HttpRequest
from basket.database import DBConnect, ProductsContainer, PGProductsManager
from basket.products import ProductBuilder

def main(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='shop',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    query = """ SELECT * FROM shampoo """
    cursor.execute(query)
    container = ProductsContainer()
    container.create_list_product(cursor.fetchall())
    data = container.get_list_product()
    count = len(data) if data is not None else 0
    cursor.close()

    # cursor = connect.cursor()
    # query = """ SELECT name_genre, translation FROM genres """
    # cursor.execute(query)
    # genres = {item[0]: "http://127.0.0.1:8000/catalog/genre/" + item[1] + '/' for item in cursor.fetchall()}
    # cursor.close()

    context = {
        "data": data,
        "count": count,
    }

    return render(request, template_name='basket.html', context=context)




def redirect(request: HttpRequest):
    return render(request, '404.html')


def search_product(request):
    connect = DBConnect.get_connect(dbname='shop',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')
    cursor = connect.cursor()
    query = """ SELECT sh_title, description FROM shampoo """
    cursor.execute(query)
    products = {item[1]: item[0] for item in cursor.fetchall()}
    cursor.close()

    if request.method == "GET":
        title = request.GET.get('title', '')

        if not title:
            context = {
                'count': 0,
                'products': products,
            }
        else:
            connect = DBConnect.get_connect(dbname='work',
                                            host='localhost',
                                            port=5432,
                                            user='postgres',
                                            password='week0497')

            builder = ProductBuilder()
            builder.create()
            builder.set_title(title)
            product = builder.get_product()
            data = PGProductsManager.read(connect, product)
            count = len(data) if data is not None else 0
            context = {
                'data': data,
                'count': count,

            }

        return render(request,
                      template_name='basket1.html',
                      context=context)
