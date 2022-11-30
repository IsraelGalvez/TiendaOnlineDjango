from .models import Carrito
from django import forms

class CarritoForm(forms.Form):
    cantidad = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'input_number1'
            }
        )
    )

    producto = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'class': 'input_number2'
            }
        )
    )

    def clean_count(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 1:
            raise forms.ValidationError("Ingrese una cantidad mayor a cero")