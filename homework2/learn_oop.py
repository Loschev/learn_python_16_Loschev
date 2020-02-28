# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def coordinates(self):
#         print(f'Координаты это: x {self.x}, y {self.y}')
#
#     def __repr__(self):
#         return f'Point x: {self.x}, y: {self.y}'
#
#
# my_point = Point(1, 3)
#
# my_point.coordinates()
#
# my_point.x = 10
# my_point.y = -5
#
# my_point.coordinates()
#
# print(my_point)


class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=0):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть 2 символа или более')
        self.price = abs(float(price))
        self.stock = abs(float(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def descounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Тут можем взаиможействовать с бухгалтерской или учетной системой
        self.stock -= items_count

    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Название продукта {self.name}, цена {self.price}, остаток на складе {self.stock}>'


class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=0):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color

    def get_color(self):
        return f'Цвет корпуса {self.color}'

    def get_memory(self):
        # Выводим размер памяти в гигабайтах
        pass

    def __repr__(self):
        return f'<Название телефона {self.name}, цена {self.price}, остаток на складе {self.stock}>'


class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=0):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'Цвет корпуса {self.color} и тип ткани {self.texture}'

    def __repr__(self):
        return f'<Название дивана {self.name}, цена {self.price}, остаток на складе {self.stock}>'


my_phone = Phone('iPhone', 6000, 'Черный')
print(my_phone)
print(my_phone.color)

sofa1 = Sofa('Диван1', 34000, 'Желтый', 'Велюр')
print(sofa1)
print(sofa1.color, sofa1.texture)

print(sofa1.get_color())
print(my_phone.get_color())