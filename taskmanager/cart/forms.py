from django import forms



PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


#TODO форма корзины для пользователя
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


# TODO форма заказа
class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Адрес доставки', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(label='Номер телефона с кодом', widget=forms.TextInput(attrs={'class': 'form-control'}))
    coment = forms.CharField(label='Комментарий к заказу', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    tovar = CartAddProductForm()
