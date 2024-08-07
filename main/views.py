import psycopg2
from django.shortcuts import render
from django.http import HttpRequest
from basket.database import DBConnect

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

        params = (name, last_name, age, phone, email, password)
        query = """ INSERT INTO cls(first_name, last_name, age, phone, email, pass)
                                 VALUES (%s, %s, %s, %s, %s, %s)"""

        cursor.execute(query, params)
        connect.commit()
        cursor.close()



        return render(request, template_name='registr.html')
