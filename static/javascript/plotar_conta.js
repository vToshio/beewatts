const conta_antiga = parseFloat(document.getElementById('conta_antiga').value)
const conta_nova = parseFloat(document.getElementById('conta_nova').value)
const ctx_conta = document.getElementById('grafico_conta').getContext('2d')

let grafico_conta = new Chart(ctx_conta, {
    type: 'doughnut',
    data: {
        labels: ['Conta de Energia Antiga', 'Conta de Energia Nova'],
        datasets: [{
            label: 'R$/mês',
            data: [conta_antiga, conta_nova],
            backgroundColor: [
                'pink',
                'blue'
            ],
            borderWidth: 2,
            borderRadius: 10,
        }],
    }   
});