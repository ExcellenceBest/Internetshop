from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from basket.database import DBConnect
from catalog.fotos import ProductsContainer


def main(request: HttpRequest):
    connect1 = DBConnect.get_connect_2(dbname='works',
                                       host='localhost',
                                       port=5432,
                                       user='postgres',
                                       password='valera123')

    cursor = connect1.cursor()
    query = """ SELECT * FROM blonds
                    ORDER BY foto_id"""
    cursor.execute(query)
    container = ProductsContainer()
    container.create_list_product(cursor.fetchall())
    data = container.get_list_product()
    cursor.close()

    context = {
        "data": data
    }

    return render(request, 'catalog.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')


def likes(request: HttpRequest):
    connect = DBConnect.get_connect_3(dbname='works',
                                      host='localhost',
                                      port=5432,
                                      user='postgres',
                                      password='valera123')

    cursor = connect.cursor()
    foto_id = request.POST.get('foto_id', '')
    query = """ UPDATE blonds
                SET counter = counter + 1
                WHERE foto_id = %s """
    cursor.execute(query, foto_id)
    cursor.close()
    connect.commit()
    return HttpResponseRedirect('/catalog/')
