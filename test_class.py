from add_casses import *


def test_category_init():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.name == "Электроника"
    assert category.description == "Вся электроника"
    assert category.products == [product]
    assert category.total_categories == 1
    assert category.total_unique_products == {"Смартфон"}


def test_product_init():
    product = Product("Смартфон", "Телефон", 10000, 5)
    assert product.name == "Смартфон"
    assert product.description == "Телефон"
    assert product.price == 10000
    assert product.quantity == 5
    assert product.get_name() == 'Смартфон'
    assert product.get_price() == 10000
    assert product.get_quantity() == 5
    assert product.get_description() == "Телефон"
def test_category_add_product():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.products == [product]
    assert category.total_unique_products == {'Смартфон'}

def test_category_add_product_duplicate():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.products == [product]
    assert category.description == "Вся электроника"

def test_category_remove_product():
    category = Category("Электроника", "Вся электроника")
    product1 = Product("Смартфон",  "Телефон", 10000, 5)
    product2 = Product("Телевизор", "Плазменый", 20000, 4)
    category.add_product(product1)
    category.add_product(product2)
    assert category.total_unique_products == {'Смартфон', 'Телевизор'}
    category.remove_product(product1)
    assert category.total_unique_products == {'Телевизор'}
    assert category.get_products()