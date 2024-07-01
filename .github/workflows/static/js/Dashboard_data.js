// Função para fazer uma solicitação AJAX para obter os dados do backend
function getDataAndRenderCharts() {
    // Fazer uma solicitação AJAX para o endpoint '/dados_dashboard' na sua aplicação Flask
    fetch('/dados_dashboard')
        .then(response => response.json())
        .then(data => {
            // Preencher os gráficos com os dados recebidos
            fillChartsWithData(data);
        })
        .catch(error => console.error('Erro ao obter dados do dashboard:', error));
}

// Função para preencher os gráficos com os dados recebidos
function fillChartsWithData(data) {
    // Preencher o gráfico de Velocímetro (cadastrosVelocimetro)
    cadastrosVelocimetro.data.datasets[0].data = [data.totalCadastros];

    // Preencher o gráfico de Pizza (estadoCivilPizza)
    estadoCivilPizza.data.labels = data.estadosCivil;
    estadoCivilPizza.data.datasets[0].data = data.proporcaoMembrosPorEstadoCivil;

    // Preencher o gráfico de Barras (funcoesIgrejaBarras)
    funcoesIgrejaBarras.data.labels = data.funcoesIgreja;
    funcoesIgrejaBarras.data.datasets[0].data = data.proporcaoMembrosPorFuncao;

    // Atualizar os gráficos
    cadastrosVelocimetro.update();
    estadoCivilPizza.update();
    funcoesIgrejaBarras.update();
}

// Chamada à função para obter os dados e preencher os gráficos quando a página é carregada
window.onload = function() {
    getDataAndRenderCharts();
};