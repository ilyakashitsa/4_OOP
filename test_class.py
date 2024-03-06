from add_casses import Product, Category


def test_category_init():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.name == "Электроника"
    assert category.description == "Вся электроника"
    assert category.total_categories == 1
    assert category.total_unique_products == {"Смартфон"}


def test_product_init():
    product = Product("Смартфон", "Телефон", 10000, 5)
    assert product.name == "Смартфон"
    assert product.description == "Телефон"
    assert product.quantity == 5
    assert product.get_name() == 'Смартфон'
    assert product.get_price() == 10000
    assert product.get_quantity() == 5
    assert product.get_description() == "Телефон"


def test_category_add_product():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.total_unique_products == {'Смартфон'}


def test_category_add_product_duplicate():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.description == "Вся электроника"


def test_category_remove_product():
    category = Category("Электроника", "Вся электроника")
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    product2 = Product("Телевизор", "Плазменый", 20000, 4)
    category.add_product(product1)
    category.add_product(product2)
    assert category.total_unique_products == {'Смартфон', 'Телевизор'}
    category.remove_product(product1)
    assert category.total_unique_products == {'Телевизор'}
    assert category.get_products()


def test_product_create_duplicate():
    products_list = []
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    product2 = Product("Смартфон", "Телефон", 15000, 3)
    product3 = Product("Планшет", "Планшет", 8000, 8)
    products_list.append(product1)
    assert Product.create_product("Смартфон", "Телефон", 15000, 3, products_list) == product1
    assert product1.get_price() == 15000
    assert product1.get_quantity() == 8
    products_list.append(product3)
    assert Product.create_product("Планшет", "Планшет", 8000, 8, products_list) == product3


def test_product_price_setter():
    product = Product("Смартфон", "Телефон", 10000, 5)
    product.set_price(12000)
    assert product.get_price() == 12000
    product.set_price(0)
    assert product.get_price() == 12000


def test_category_products_info():
    category = Category("Электроника", "Вся электроника")
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    product2 = Product("Телевизор", "Плазменый", 20000, 4)
    category.add_product(product1)
    category.add_product(product2)
    expected_info = [
        "Смартфон, 10000 руб. Остаток: 5 шт.",
        "Телевизор, 20000 руб. Остаток: 4 шт."
    ]
    assert category.get_products_info() == expected_info


def test_create_product_new():
    products_list = []
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    products_list.append(product1)
    new_product = Product.create_product("Планшет", "Планшет", 8000, 8, products_list)
    assert isinstance(new_product, Product)
    assert new_product.name == "Планшет"
    assert new_product.description == "Планшет"
    assert new_product.get_price() == 8000
    assert new_product.get_quantity() == 8


def test_category_get_products():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.get_products() == [product]
