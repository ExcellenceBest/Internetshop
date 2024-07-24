from abc import ABC, abstractmethod


class Product:

    def __init__(self):

        self.title = None
        self.view = None
        self.manufacturer = None
        self.description = None
        self.price = None
        self.quantity = None


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_title(self, title):
        ...

    @abstractmethod
    def set_view(self, view):
        ...

    @abstractmethod
    def set_manufacturer(self, manufacturer):
        ...

    @abstractmethod
    def set_description(self, description):
        ...

    @abstractmethod
    def set_price(self, price):
        ...

    @abstractmethod
    def set_quantity(self, quantity):
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

    def set_view(self, view):
        self._product.view = view

    def set_manufacturer(self, manufacturer):
        self._product.manufacturer = manufacturer

    def set_description(self, description):
        self._product.description = description

    def set_price(self, price):
        self._product.price = price

    def set_quantity(self, quantity):
        self._product.quantity = quantity

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
        self._builder.set_view(product[2])
        self._builder.set_manufacturer(product[3])
        self._builder.set_description(product[4])
        self._builder.set_price(product[5])
        self._builder.set_quantity(product[6])
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
