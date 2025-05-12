const cep = document.querySelector('#id_cep')
const uf = document.querySelector('#id_uf')
const cidade = document.querySelector('#id_cidade')
const logradouro = document.querySelector('#id_logradouro')
const longitude = document.querySelector('#id_longitude')
const latitude = document.querySelector('#id_latitude')
const container_msg = document.querySelector('#container_msg')
const registrar = document.querySelector('#btn_registrar')

function validar_cep(cep) {
    const filtro = /^\d{8}$/;
    return filtro.test(cep);
};

function limpar_campos() {
    uf.value = ''
    cidade.value = ''
    logradouro.value = ''
    latitude.value = ''
    longitude.value = ''
}

cep.addEventListener('focusout', async () => {
    let valor_cep = cep.value.trim()

    if (validar_cep(valor_cep)) {
        container_msg.innerHTML = ''

        try {
            const response = await fetch(`https://brasilapi.com.br/api/cep/v2/${valor_cep}`)
            const data = await response.json()
            
            if (data.hasOwnProperty('cep')) {
                console.log(data)
                uf.value = data['state']
                cidade.value = data['city']
                logradouro.value = data['street']
                latitude.value = data['location']['coordinates']['latitude']
                longitude.value = data['location']['coordinates']['longitude']
                registrar.setAttribute('type', 'submit')
            } else {
                limpar_campos()
                registrar.setAttribute('type', 'button')
                container_msg.innerHTML = '<p class="text-danger">CEP não encontrado!</p>'
            }
        } catch (e) {
            limpar_campos()
            console.error(e)
        }
    } else {
        limpar_campos()
        registrar.setAttribute('type', 'button')
        container_msg.innerHTML = '<p class="text-danger">CEP Inválido!</p>'
    }
})