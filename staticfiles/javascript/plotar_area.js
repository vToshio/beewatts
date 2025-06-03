document.addEventListener('DOMContentLoaded', () => {
    const area_utilizada = parseFloat(document.getElementById('area_utilizada').value)
    const area_disponivel = parseFloat(document.getElementById('area_disponivel').value) - area_utilizada
    const ctx_area = document.getElementById('grafico_area').getContext('2d')


    let grafico_area = new Chart(ctx_area, {
        type: 'doughnut',
        data: {
            labels: ['Área Utilizada', 'Área Disponível'],
            datasets: [{
                label: 'R$/mês',
                data: [area_utilizada, area_disponivel],
                backgroundColor: [
                    'rgb(255, 38, 71)',
                    'rgb(47, 207, 121)',
                ],
                borderWidth: 2,
                borderRadius: 10,
            }],
        }   
    });
})