import re

from django import forms
from django.core.exceptions import ValidationError

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value

    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        pattern = r'^[A-Z]{3}-\d{4}$'  # Exemplo de regex para uma placa de carro no formato ABC-1234
        if not re.match(pattern, plate):
            raise ValidationError('Placa inválida. O formato correto é ABC-1234.')
        return plate
        