from django import forms    

class CepForm(forms.Form):
    cep = forms.RegexField(
        label='CEP',
        regex=r'^([\d]{8})$',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 12345678, 13245248...',
            'required': 'required'
        })
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True,
            'required': 'required'
        })
    )
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True,
            'required': 'required'
        })
    )
    logradouro = forms.CharField(
        label='Logradouro',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True,
            'required': 'required'
        })
    )

class EnderecoForm(forms.Form):
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Exemplo: SP, RJ, BA, GO...',
            'required': 'required'
        })
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Exemplo: São Paulo, Campinas, Natal...',
            'required': 'required'
        })
    )
    logradouro = forms.CharField(
        label='Logradouro',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: Rua Fulano de Tal...',
            'required': 'required'
        })
    )
    cep = forms.RegexField(
        label='CEP',
        regex=r'^([\d]{8})$',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True,
            'required': 'required'
        })
    )