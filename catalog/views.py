from django.shortcuts import render
from django.http import HttpRequest

from basket.database import DBConnect
from catalog.fotos import ProductBuilder, ProductsContainer
from basket.database import PGProductsManager


def main(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='works',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    query = """ SELECT * FROM blonds """
    cursor.execute(query)
    container = ProductsContainer()
    container.create_list_product(cursor.fetchall())
    data = container.get_list_product()
    cursor.close()



    context = {
        "data": data

    }

    return render(request, template_name='catalog.html', context=context)


def likes(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='works',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    if request.method == "POST":
        counter = request.POST.get('name', '')


    params = counter
    query = """ UPDATE blonds 
         UPDATE mobile_devices
         SET counter = counter + 1
         WHERE url = 'https://avatars.mds.yandex.net/i?id=7d1d3280b2c6393280fe8f55a0f3016c676661f66b90c621-5859721-images-thumbs&n=13' """

    cursor.execute(query, params)
    connect.commit()
    cursor.close()
def redirect(request: HttpRequest):
    return render(request, '404.html')

