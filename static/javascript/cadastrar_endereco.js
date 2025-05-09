const cep = document.querySelector('#id_cep')
const uf = document.querySelector('#id_uf')
const cidade = document.querySelector('#id_cidade')
const bairro = document.querySelector('#id_bairro')

function validar_cep(cep) {
    filtro = /^([\d]{8})$/;
    return filtro.test(cep);
};

document.addEventListener('DOMContentLoaded', () => {
    cep.addEventListener('focusout', async () => {
        let valor_cep = cep.value

        console.log(validar_cep(valor_cep))
    })
})