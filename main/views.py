from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
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
    if request.method == "POST":
        name = request.POST.get('name', '')
        last_name = request.POST.get('last_name', '')
        age = request.POST.get('age', 1)
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # builder = ProductBuilder()
        # builder.create()
        # builder.set_title(name)
        # builder.set_view(last_name)
        # builder.set_manufacturer(age)
        # builder.set_description(phone)
        # builder.set_price(email)
        # builder.set_quantity(password)
        # product = builder.get_product()

    params = (name, last_name, age, phone, email, password)
    query = """ INSERT INTO reg(first_name, last_name, age, phone, email, pass)
                             VALUES (%s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, params)
    connect.commit()
    cursor.close()

    # context = {
    #     'data': product,
    #
    # }

    # return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")
    return render(request, template_name='registr.html')

