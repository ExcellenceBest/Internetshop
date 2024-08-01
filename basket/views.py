from django.shortcuts import render
from django.http import HttpRequest
from basket.database import DBConnect, PGProductsManager
from basket.products import ProductsContainer, ProductBuilder


def main(request: HttpRequest):
    try:
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
    except ValueError as e:
        print(e)
    context = {
        "data": data,
        "count": count,
    }

    return render(request, template_name='basket.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')


def search_product(request):

    if request.method == "POST":
        title = request.POST.get('title', '')

        if not title:
            context = {
                'count': 0,

            }
        else:
            connect = DBConnect.get_connect(dbname='shop',
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
                      template_name='basket.html',
                      context=context)

def in_basket(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='shop',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    quantity = request.POST.get('quantity', '')
    query = """ UPDATE blonds
                SET quantity = quantity - 1
                WHERE counter = %s"""
    cursor.execute(query, quantity)
    cursor.close()
    connect.commit()
    return render(request, 'end_pay.html')
