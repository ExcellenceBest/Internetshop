from django.shortcuts import render
from django.http import HttpRequest
from basket.database import DBConnect, PGProductsManager
from basket.products import ProductsContainer, ProductBuilder, ProductCreator


def main(request: HttpRequest):
    try:
        connect = DBConnect.get_connect_all(dbname='shop',
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
            connect_2 = DBConnect.get_connect_all(dbname='shop',
                                                host='localhost',
                                                port=5432,
                                                user='postgres',
                                                password='week0497')

            builder = ProductBuilder()
            builder.create()
            builder.set_title(title)
            product = builder.get_product()
            data = PGProductsManager.read(connect_2, product)
            count = len(data) if data is not None else 0
            context = {
                'data': data,
                'count': count,

            }

        return render(request,
                      template_name='basket.html',
                      context=context)

def in_basket(request: HttpRequest):
    connect = DBConnect.get_connect_3(dbname='shop',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    product_id = request.POST.get('product_id', '')
    query = """ UPDATE shampoo
                SET quantity = quantity + 1
                WHERE shampoo_id = shampoo_id """
    cursor.execute(query, product_id)
    cursor.close()
    cursor = connect.cursor()
    query = """ SELECT *
                    FROM shampoo
                    WHERE shampoo_id = shampoo_id """
    cursor.execute(query, product_id)
    data = cursor.fetchall()
    params = (data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6])
    container = ProductsContainer()
    container.create_list_product(data)


    cursor.close()
    cursor = connect.cursor()
    query = """ INSERT INTO basket(shampoo_id, sh_title, sh_view, manufacturer, description, price, quantity)
                                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    print(data)
    cursor.execute(query, params)
    cursor.close()
    connect.commit()
    return render(request, 'end_pay.html')
