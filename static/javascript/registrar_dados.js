checkbox = document.querySelector('#informar_area')
campo_area = document.querySelector('#id_area_disponivel')
campo_conta = document.querySelector('#id_conta_luz')

function mudar_status() {
    if (checkbox.checked) 
        campo_area.disabled = false
    else
        campo_area.disabled = true
}

function limpar_campos() {
    campo_area.value = ''
    campo_conta.value = ''
}

checkbox.addEventListener('change', mudar_status)
document.addEventListener('DOMContentLoaded', () => {
    campo_area.disabled = true
    limpar_campos()
})