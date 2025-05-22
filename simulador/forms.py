from django import forms    
from simulador.models.concessionaria import Concessionaria
from simulador.models.painel_solar import PainelSolar

class EnderecoForm(forms.Form):
    cep = forms.RegexField(
        label='CEP',
        regex=r'^([\d]{8})$',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 12345678, 13245248...',
        }),
        required=True
    )
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True,
        }),
        required=True
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True,
        }),
        required=True
    )
    logradouro = forms.CharField(
        label='Logradouro',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True
        }),
        required=False
    )

class DadosIniciaisForm(forms.Form):
    consumo_usuario = forms.IntegerField(
        label='Consumo Atual (kWh)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 244, 264, 300...',
        }),
        required=True
    )
    area_disponivel = forms.FloatField(
        label='Área Total para Instalação (m²)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 39.90, 300.00, 230.50...',
        }),
        required=True
    )
    concessionaria_usuario = forms.ChoiceField(
        label='Concessionária',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Escolha a sua concessionária de energia!',
        }),
        required=True
    )
    painel_usuario = forms.ChoiceField(
        label='Painel Solar',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Escolha qual painel deseja simular!',
        }),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['concessionaria_usuario'].choices = [
            (conc.id, conc.nome) for conc in Concessionaria.objects.all()
        ]
        self.fields['painel_usuario'].choices = [
            (painel.id, painel.nome) for painel in PainelSolar.objects.all()
        ]
    