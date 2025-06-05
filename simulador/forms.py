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
            'placeholder': 'Insira seu CEP (apenas números)',
        }),
        required=True
    )
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control bg-secondary-subtle',
            'readonly': True,
            'placeholder': 'Aguarde o preenchimento automático'
        }),
        required=True
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control bg-secondary-subtle',
            'readonly': True,
            'placeholder': 'Aguarde o preenchimento automático'
        }),
        required=True
    )
    logradouro = forms.CharField(
        label='Logradouro',
        widget = forms.TextInput(attrs={
            'class': 'form-control bg-secondary-subtle',
            'readonly': True,
            'placeholder': 'Campo opcional'
        }),
        required=False
    )

class DadosIniciaisForm(forms.Form):
    concessionaria_usuario = forms.ChoiceField(
        label='Concessionária',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Escolha a sua concessionária de energia',
        }),
        required=True
    )
    painel_usuario = forms.ChoiceField(
        label='Painel Solar',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Escolha qual painel deseja simular',
        }),
        required=True
    )
    conta_luz = forms.FloatField(
        label='Conta de Luz Atual (R$)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Insira sua conta de luz (R$)',
        }),
        required=True
    )
    area_disponivel = forms.FloatField(
        label='Área Total para Instalação (m²)',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Insira a área disponível (m²)',
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
    