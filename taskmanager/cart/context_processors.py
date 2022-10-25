from .cart import Cart


#TODO принимает request запрос и возвращает словарь (доступ к переменным глобально во всех шаблонах)
def cart(request):
    return {'cart': Cart(request)}