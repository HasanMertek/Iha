from django import forms
from .models import IHA, Customer, Rental
class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = ['isim', 'model', 'saatlik_fiyat', 'mevcut']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['baslangic_saati', 'bitis_saati']
        labels = {
            'baslangic_saati': 'Başlangıç Saati',
            'bitis_saati': 'Bitiş Saati',
        }
        widgets = {
            'baslangic_saati': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'bitis_saati': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'surname', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True