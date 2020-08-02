from django import forms
MAX_AMOUNT = 20


class CartAddProductForm(forms.Form):
    def set_amount(self, amount: int):
        am = amount
        if MAX_AMOUNT < amount:
            am = MAX_AMOUNT
        self.fields['quantity'].choices = [(i, str(i)) for i in range(1, am + 1)]

    quantity = forms.TypedChoiceField(choices=[(i, str(i)) for i in range(1, 6)], coerce=int, label='Количество')
