from django.forms import ModelForm
from django import forms
from karzav.models import karzav_card

class FormKarzav(ModelForm):
    mst_name = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('mst_name', flat=True).distinct(), label='Месторождение')
    comp_name = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('comp_name', flat=True).distinct(), label='Компания')
    vn_name = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('vn_name', flat=True).distinct(), label='Вид нидропользования')
    status = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('status', flat=True).distinct(), label='Статус')
    oblast = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('oblast', flat=True).distinct(), label='Область')
    raion = forms.ModelChoiceField(queryset=karzav_card.objects.values_list('raion', flat=True).distinct(), label='Район')

    class Meta:
        model = karzav_card
        fields = ('mst_name', 'comp_name', 'vn_name', 'status', 'oblast', 'raion')

class HidresForm(forms.Form):
    hidres = forms.CharField(max_length=100)