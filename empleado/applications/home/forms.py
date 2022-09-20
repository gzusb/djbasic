from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):

    class Meta:
        model = Prueba
        # fields = ('__all__')
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        widgets = {
            'cantidad': forms.TextInput(
                attrs = {
                    'placeholder': 'Enter texto here'
                }
            )
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']

        if 's' not in titulo:
            raise forms.ValidationError('"Titulo" must contain the letter "s"')
        return titulo
"""
    def clean_cantidad(self):
        titulo = self.cleaned_data['titulo']
        subtitulo = self.cleaned_data['subtitulo']
        cantidad = self.cleaned_data['cantidad']
        print("-"*30)
        print("cleaned_data: ", self.cleaned_data)
        print("titulo: ", titulo)
        print("subtitulo: ", subtitulo)
        print("cantidad: ", cantidad)
        print("-"*30)

        if cantidad < 10:
            raise forms.ValidationError('Set number greater than 10')
        return cantidad
"""
