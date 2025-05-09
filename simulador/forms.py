from django import forms    

class EnderecoForm(forms.Form):
    cep = forms.RegexField(
        label='CEP',
        regex=r'([\d]{8})',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex: 12345678, 13245248...'
        })
    )
    uf = forms.CharField(
        label='UF',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True
        })
    )
    cidade = forms.CharField(
        label='Cidade',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True
        })
    )
    bairro = forms.CharField(
        label='Bairro',
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'disabled': True
        })
    )