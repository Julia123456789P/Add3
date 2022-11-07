from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm, ContactForm
from django.core.mail import send_mail
from django.contrib import messages


#TODO обработчик добавление товара в корзину
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


#TODO обработчик удаление товара из корзины
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


#TODO обработчик отображение корзины в текущей сессии
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})



def zakaz(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['phone'], form.cleaned_data['name'], 'skribachka1@mail.ru', ['skribachka1@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('create')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'cart/zakaz.html', {'form': form})

# # TODO заказ
# def zakaz(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data['name']
#             # phone = form.cleaned_data['phone']
#             # address = form.cleaned_data['address']
#             # coment = form.cleaned_data['coment']
#             # html = render_to_string('cart/email/contactform.html', {
#             #     name: name,
#             #     phone: phone,
#             #     address: address,
#             #     coment: coment,
#             # })
#             mail = send_mail(form.cleaned_data['name'],  form.cleaned_data['phone'], 'skribachka1@mail.ru', ['skribachka1@mail.ru'], fail_silently=False)
#             if mail:
#                 messages.success(request, 'Заказ отправлен')
#                 return redirect('cart:cart_detail')
#             else:
#                 messages.error(request, 'Ошибка отправки')
#         else:
#             messages.error(request, 'Ошибка при заполнении формы')
#     else:
#         form = ContactForm()
#     return render(request, 'cart/zakaz.html', {'form': form})