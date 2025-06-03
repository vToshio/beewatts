const cep = document.querySelector('#id_cep')
const uf = document.querySelector('#id_uf')
const cidade = document.querySelector('#id_cidade')
const logradouro = document.querySelector('#id_logradouro')
const container_msg = document.querySelector('#container_msg')
const container_submit = document.querySelector('#container_submit')
const registrar = document.querySelector('#btn_registrar')

function validar_cep(cep) {
    const filtro = /^\d{8}$/;
    return filtro.test(cep);
}

function limpar_campos() {
    uf.value = ''
    cidade.value = ''
    logradouro.value = ''
    registrar.setAttribute('type', 'button')
}

cep.addEventListener('focusout', async () => {
    let valor_cep = cep.value.trim()

    if (validar_cep(valor_cep)) {
        container_msg.innerHTML = ''
        try {
            const response = await fetch(`https://viacep.com.br/ws/${valor_cep}/json/`)
            const data = await response.json()

            if (!data.erro) {
                uf.value = data['uf']
                cidade.value = data['localidade']
                logradouro.value = data['logradouro']

                if (uf.value.trim() !== '' && cidade.value.trim() !== '') {
                    registrar.setAttribute('type', 'submit')
                } else {
                    registrar.setAttribute('type', 'button')
                    container_msg.innerHTML = '<p class="text-danger">Informações incompletas para este CEP.</p>'
                }

            } else {
                limpar_campos()
                container_msg.innerHTML = '<p class="text-danger">CEP não encontrado!</p>'
            }
        } catch (e) {
            limpar_campos()
            container_msg.innerHTML = '<p class="text-danger">Erro ao buscar CEP!</p>'
            console.error(e)
        }

    } else if (!valor_cep) {
        limpar_campos()
        container_msg.innerHTML = '<p class="text-danger">Preencha o campo CEP!</p>'
    } else {
        limpar_campos()
        container_msg.innerHTML = '<p class="text-danger">CEP Inválido! Digite 8 números.</p>'
    }
})

registrar.addEventListener('click', () => {
    if (registrar.getAttribute('type') === 'button') {
        container_msg.innerHTML = '<p class="text-danger">Preencha o CEP corretamente para habilitar o cadastro!</p>'
        return
    }

    let spinner = document.createElement('div')
    spinner.setAttribute('class', 'd-flex justify-content-center mt-3')
    spinner.innerHTML = '<div class="spinner-border text-warning" role="status"><span class="visually-hidden">Carregando...</span></div>'
    registrar.classList.add('d-none')
    container_submit.appendChild(spinner)
})
