from abc import ABC, abstractmethod
from .products import Product, ProductsContainer
import psycopg2


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance


class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def create(connect, product: Product):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, product: Product):
        ...

    @staticmethod
    @abstractmethod
    def update(connect, old_product: Product, new_product: Product):
        ...

    @staticmethod
    @abstractmethod
    def delete(connect, product: Product):
        ...


class PGProductsManager(DBManager):

    @staticmethod
    def create(connect, product: Product):
        # Вызвать запрос вставки данных из объекта в таблицу
        ...

    @staticmethod
    def read(connect, product: Product) -> list[Product]:

        try:
            with connect.cursor() as cursor:

                params = (product.title, )
                query = """SELECT * 
                           FROM products
                           WHERE title = %s"""
                cursor.execute(query, params)
                data = cursor.fetchall()

                if data:
                    container = ProductsContainer()
                    container.create_list_product(data)
                    return container.get_list_product()
                else:
                    raise Exception(f"Не найдена запись с параметрами {params}")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, index_old_product: int, new_product: Product):
        # Обновить данные о книге в таблице
        ...

    @staticmethod
    def delete(connect, product: Product):
        # Удалить продукт
        ...
