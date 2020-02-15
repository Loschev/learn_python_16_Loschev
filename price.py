def price_with_discount(price, discount, product_id=None):
    """
    :param price: Цена товара
    :param discount: Скидка товара
    :param product_id: ID продукта
    :return: Вывод цены с посчитанной скидкой
    """
    if price >= 0:
        if 0 <= discount < 100:
            return price - price * discount / 100
        else:
            raise ValueError(f'Неправильная скидка "{discount}" для товара "{product_id}"')
    else:
        raise ValueError(f'Неправильная цена "{price}" для товара "{product_id}"')


print(price_with_discount(1000, 50))
print(price_with_discount(100, 5))
print(price_with_discount(-1, 5, 123))
print(price_with_discount(100, 105, 432))
