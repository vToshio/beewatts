from django import forms    
from simulador.models.concessionaria import Concessionaria
from simulador.models.painel_solar import PainelSolar
from django.shortcuts import get_list_or_404

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
    conta_luz = forms.FloatField(
        label='Conta de Luz Atual (R$)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 49.90, 67.87...',
        }),
        required=True
    )
    area_disponivel = forms.FloatField(
        label='Área Total para Instalação (m²)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Esse campo é opcional',
        }),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        concessionarias = get_list_or_404(Concessionaria)
        paineis = get_list_or_404(PainelSolar)

        self.fields['concessionaria_usuario'].choices = [
            (conc.id, conc.nome) for conc in concessionarias
        ]
        self.fields['painel_usuario'].choices = [
            (painel.id, painel.nome) for painel in paineis
        ]
    