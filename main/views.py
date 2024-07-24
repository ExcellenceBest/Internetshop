from django.shortcuts import render
from django.http import HttpRequest
from basket.database import DBConnect, PGProductsManager
from basket.products import ProductBuilder

def main(request: HttpRequest):
    return render(request, 'home.html')

def redirect(request: HttpRequest):
    return render(request, '404.html')

def registration(request: HttpRequest):

    return render(request, 'reg.html')

def registr(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='clients',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='week0497')

    cursor = connect.cursor()
    if request.method == "GET":
        name = request.GET.get('name', '')
        last_name = request.GET.get('name', '')
        age = request.GET.get('name', '')
        phone = request.GET.get('name', '')
        email = request.GET.get('name', '')
        password = request.GET.get('name', '')

        builder = ProductBuilder()
        builder.create()
        builder.set_title(name)
        builder.set_view(last_name)
        builder.set_manufacturer(age)
        builder.set_description(phone)
        builder.set_price(email)
        builder.set_quantity(password)
        product = builder.get_product()

    params = (product.title, product.view, product.manufacturer, product.description, product.price, product.quantity)
    query = """ INSERT INTO reg(first_name, last_name, age, phone, email, pass)
                            VALUES (%s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, params)
    cursor.close()

    context = {
        'data': product,

    }



    return render(request, template_name='home.html', context=context)

