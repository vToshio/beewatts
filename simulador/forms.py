from django import forms    

class EnderecoForm(forms.Form):
    cep = forms.RegexField(
        label='CEP',
        regex=r'^([\d]{8})$',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 12345678, 13245248...',
            'required': 'required'
        })
    )
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True,
            'required': 'required'
        })
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': True,
            'required': 'required'
        })
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
    pass