from django import forms

CARS = ((1, 'Audi RS7 Perfomance'), (2, 'Cadilac Escalade ESV Sport Platinum'), (3, 'Audi RSQ8'))

class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = forms.CharField(label='Телефон')
    email = forms.EmailField(label='Почта')
    car = forms.ChoiceField(label='Авто', choices=CARS)
    coment = forms.CharField(label='Комментарий', widget=forms.Textarea)