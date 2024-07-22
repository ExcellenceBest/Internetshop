from abc import ABC, abstractmethod


class Product:

    def __init__(self):

        self.title = None
        self.description = None
        self.work_time = None
        self.url = None


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_title(self, title):
        ...

    @abstractmethod
    def set_description(self, description):
        ...

    @abstractmethod
    def set_work_time(self, work_time):
        ...

    @abstractmethod
    def set_url(self, url):
        ...

    @abstractmethod
    def get_product(self):
        ...


class ProductBuilder(Builder):

    _product: Product

    def create(self):
        self._product = Product()

    def set_title(self, title):
        self._product.title = title

    def set_description(self, description):
        self._product.description = description

    def set_work_time(self, work_time):
        self._product.work_time = work_time

    def set_url(self, url):
        self._product.url = url

    def get_product(self):
        return self._product


class ProductCreator:

    def __init__(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, product: tuple) -> Product:
        self._builder.create()
        self._builder.set_title(product[1])
        self._builder.set_description(product[2])
        self._builder.set_work_time(product[3])
        self._builder.set_url(product[4])
        return self._builder.get_product()


class ProductsContainer:

    def __init__(self):
        self._products: list[Product] = []

    def create_list_product(self, data: list) -> None:
        builder = ProductBuilder()
        creator = ProductCreator(builder)

        for record in data:
            product = creator.make(record)
            (self._products.append(product))

    def add_product(self, product: Product):
        self._products.append(product)

    def get_list_product(self):
        return self._products
