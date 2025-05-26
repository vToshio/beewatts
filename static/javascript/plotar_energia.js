const energia_gerada = parseInt(document.getElementById('energia_gerada').value)
const energia_consumida = parseInt(document.getElementById('energia_consumida').value)
const ctx_energia = document.getElementById('grafico_energia').getContext('2d')

let grafico_energia = new Chart(ctx_energia, {
    type: 'bar',
    data: {
        labels: ['Energia Gerada', 'Energia Consumida'],
        datasets: [{
            label: 'kWh/mês',
            data: [energia_gerada, energia_consumida],
            backgroundColor: [
                'rgba(25, 135, 84, 0.7)',    // Verde (Gerada)
                'rgba(255, 193, 7, 0.7)'     // Amarelo (Consumida)
            ],
            borderColor: [
                'rgba(25, 135, 84, 1)',
                'rgba(255, 193, 7, 1)'
            ],
            borderWidth: 2,
            borderRadius: 10,
            barPercentage: 0.6,
            categoryPercentage: 0.5
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.dataset.label + ': ' + context.formattedValue + ' kWh';
                    }
                }
            },
            title: {
                display: false
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    stepSize: 50
                }
            }
        }
    }
});