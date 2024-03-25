import pytest
from src.product import Product
from src.categories import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_product_price_setter():
    product = Product("Смартфон", "Телефон", 10000, 5)
    product.set_price(12000)
    assert product.get_price() == 12000
    product.set_price(0)
    assert product.get_price() == 12000


def test_product_set_negative_price():
    product = Product("Test Product", "Описание", 10.0, 5)
    product.set_price(-5)
    assert product.get_price() == 10.0


def test_category_get_products():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.products == [product]


def test_category_get_products_empty():
    category = Category("Test Category", "Описание")
    assert category.get_products_info() == []


def test_category_len_method():
    category = Category("Электроника", "Вся электроника")
    assert len(category) == 0
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert len(category) == 1


def test_category_str_representation():
    category = Category("Электроника", "Вся электроника")
    assert str(category) == "Электроника, количество продуктов: 0 шт."
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert str(category) == "Электроника, количество продуктов: 1 шт."


def test_product_str_representation():
    product = Product("Смартфон", "Телефон", 10000, 5)
    assert str(product) == "Смартфон, 10000 руб. Остаток: 5 шт."


def test_product_addition():
    product1 = Product("Смартфон", "Телефон", 100, 5)
    product2 = Product("Ноутбук", "Лэптоп", 200, 2)
    result = product1 + product2
    assert result == (100 * 5) + (200 * 2)


def test_product_get_description():
    product = Product("Test Product", "Описание", 10.0, 5)
    assert product.get_description() == "Описание"


def test_product_create_product():
    products_list = []
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    products_list.append(product1)
    new_product = Product.create_product("Смартфон", "Телефон", 15000, 3, products_list)
    assert new_product is product1
    assert product1.get_price() == 15000
    assert product1.get_quantity() == 8


def test_add_same_product_class():
    product1 = Product("Test Product 1", "Описание", 10.0, 5)
    product2 = Product("Test Product 2", "Описание", 20.0, 10)
    result = product1 + product2
    assert result == (10.0 * 5) + (20.0 * 10)


def test_add_different_product_class():
    product = Product("Test Product", "Описание", 10.0, 5)
    smartphone = Smartphone("iPhone 14", "Описание", 500.0, 1, "Высокая",
                            "Модель", 128, "Черный")
    with pytest.raises(TypeError):
        product + smartphone


def test_add_product_empty_list():
    products_list = []
    new_product = Product.create_product("Планшет", "Планшет", 8000, 8, products_list)
    assert isinstance(new_product, Product)
    assert new_product.name == "Планшет"
    assert new_product.description == "Планшет"
    assert new_product.get_price() == 8000
    assert new_product.get_quantity() == 8


def test_add_non_product_class():
    product = Product("Test Product", "Описание", 10.0, 5)
    non_product = "Это не продукт"
    with pytest.raises(TypeError):
        product + non_product


def test_category_init():
    category = Category("Электроника", "Вся электроника")
    product = Product("Смартфон", "Телефон", 10000, 5)
    category.add_product(product)
    assert category.name == "Электроника"
    assert category.description == "Вся электроника"
    assert category.total_categories == 5
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
    assert category.description == "Вся электроника"


def test_add_product_with_zero_quantity():
    category = Category("Test Category", "Описание")
    product = Product("Test Product", "Описание", 10.0, 0)
    with pytest.raises(ValueError):
        category.add_product(product)


def test_category_remove_product():
    category = Category("Электроника", "Вся электроника")
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    product2 = Product("Телевизор", "Плазменый", 20000, 4)
    category.add_product(product1)
    category.add_product(product2)
    assert category.total_unique_products == {'Смартфон', 'Телевизор'}
    category.remove_product(product1)
    assert category.total_unique_products == {'Телевизор'}


def test_category_remove_non_existing_product():
    category = Category("Test Category", "Описание")
    product = Product("Test Product", "Описание", 10.0, 5)
    with pytest.raises(ValueError):
        category.remove_product(product)


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


def test_create_product():
    products_list = []
    product1 = Product("Смартфон", "Телефон", 10000, 5)
    products_list.append(product1)
    new_product = Product.create_product("Планшет", "Планшет", 8000, 8, products_list)
    assert isinstance(new_product, Product)
    assert new_product.name == "Планшет"
    assert new_product.description == "Планшет"
    assert new_product.get_price() == 8000
    assert new_product.get_quantity() == 8


def test_smartphone():
    smartphone = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10,
                            "Высокая", "iPhone 13", 128, "Серый")
    assert smartphone.name == "iPhone 13"
    assert smartphone.description == "Смартфон от Apple"
    assert smartphone.get_price() == 999.99
    assert smartphone.quantity == 10
    assert smartphone.capacity == "Высокая"
    assert smartphone.model == "iPhone 13"
    assert smartphone.internal_memory == 128
    assert smartphone.color == "Серый"
    expected_string = "iPhone 13, 999.99 руб. Остаток: 10 шт."
    assert str(smartphone) == expected_string


def test_smartphone_additional_info():
    smartphone = Smartphone("iPhone 13", "Смартфон от Apple", 999.99, 10,
                            "Высокая", "iPhone 13", 128, "Серый")
    assert smartphone.get_additional_info() == "Характеристики: Высокая, iPhone 13, 128GB, Серый"


def test_lawn_grass():
    lawn_grass = LawnGrass("Газонная трава", "Трава для газона", 5.99, 100,
                           "Россия", "2-3 недели", "Зеленый")
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Трава для газона"
    assert lawn_grass.get_price() == 5.99
    assert lawn_grass.quantity == 100
    assert lawn_grass.country_of_origin == "Россия"
    assert lawn_grass.germination_period == "2-3 недели"
    assert lawn_grass.color == "Зеленый"
    expected_string = "Газонная трава, 5.99 руб. Остаток: 100 шт."
    assert str(lawn_grass) == expected_string


def test_lawn_grass_additional_info():
    lawn_grass = LawnGrass("Газонная трава", "Трава для газона", 5.99, 100,
                           "Россия", "2-3 недели", "Зеленый")
    assert lawn_grass.get_additional_info() == "Характеристики: Россия, 2-3 недели, Зеленый"


def test_addition():
    product1 = Product("Test Product 1", "Описание", 10.0, 5)
    product2 = Product("Test Product 2", "Описание", 20.0, 10)
    result = product1 + product2
    assert result == (10.0 * 5) + (20.0 * 10)


def test_add_invalid():
    product = Product("Test Product", "Описание", 10.0, 5)
    smartphone = Smartphone("iPhone 14", "Описание",
                            500.0, 1, "Высокая", "Модель", 128, "Черный")
    with pytest.raises(TypeError):
        product + smartphone


def test_add_invalid_non_product():
    category = Category("Test Category", "Описание")
    non_product = "Это не продукт"
    with pytest.raises(TypeError):
        category.add_product(non_product)


def test_add_product_valid():
    category = Category("Test Category", "Описание")
    product = Product("Test Product", "Описание", 10.0, 5)
    category.add_product(product)
    assert product in category.products


def test_add_product_invalid():
    category = Category("Test Category", "Описание")
    non_product = "Это не продукт"
    with pytest.raises(TypeError):
        category.add_product(non_product)


def test_calculate_average_price_with_no_products():
    category = Category("Test Category", "Описание")
    assert category.calculate_average_price() == 0


def test_calculate_average_price_with_products():
    category = Category("Test Category", "Описание")
    product1 = Product("Product 1", "Description", 10.0, 5)
    product2 = Product("Product 2", "Description", 20.0, 10)
    category.add_product(product1)
    category.add_product(product2)
    assert category.calculate_average_price() == pytest.approx((10.0 + 20.0) / 2, abs=1e-2)
