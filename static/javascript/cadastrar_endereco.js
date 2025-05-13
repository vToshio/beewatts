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
};

function limpar_campos() {
    uf.value = ''
    cidade.value = ''
    logradouro.value = ''
}


cep.addEventListener('focusout', async () => {
    let valor_cep = cep.value.trim()

    if (validar_cep(valor_cep)) {
        container_msg.innerHTML = ''
        try {
            const response = await fetch(`https://viacep.com.br/ws/${valor_cep}/json/`)
            const data = await response.json()
            
            if (data.hasOwnProperty('cep')) {
                uf.value = data['uf']
                cidade.value = data['localidade']
                logradouro.value = data['logradouro']
            } else {
                limpar_campos()
                container_msg.innerHTML = '<p class="text-danger">CEP não encontrado!</p>'
            }
        } catch (e) {
            limpar_campos()
            console.error(e)
        }
    } else if (!valor_cep) {
        container_msg.innerHTML = '<p class="text-danger">Preencha todos os campos obrigatórios!</p>';
    } else {
        limpar_campos()
        container_msg.innerHTML = '<p class="text-danger">CEP Inválido!</p>'
    }
})

registrar.addEventListener('click', () => {
    if (!cep.value || !uf.value || !cidade.value) {
        container_msg.innerHTML = '<p class="text-danger">Preencha todos os campos obrigatórios!</p>';
        return;
    }

    let spinner = document.createElement('div')
    spinner.setAttribute('class', 'd-flex justify-content-center mt-3')
    spinner.innerHTML = '<div class="spinner-border text-warning" role="status"><span class="visually-hidden">Carregando...</span></div>'
    container_submit.appendChild(spinner)
})