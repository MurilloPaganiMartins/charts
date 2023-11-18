
var bg_color = []
var border_color = []

function gera_cor(qtd=1){

    for(let i = 0; i < qtd; i++){
        let r = Math.random() * 255;
        let g = Math.random() * 255;
        let b = Math.random() * 255;
        bg_color.push(`rgba(${r}, ${g}, ${b}, ${0.2})`)
        border_color.push(`rgba(${r}, ${g}, ${b}, ${1})`)
    }

}


function renderiza_tmp(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('tmp').getContext('2d');
        //var cores_tmp = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Média em Celsius',
                    data: data.data_temperatura,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }]
            },
        });
    })
}


function renderiza_hum(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('hum').getContext('2d');
        //var cores_hum = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Média da Humidade',
                    data: data.data_humidade,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }]
            },
        });
    })
}


function renderiza_lux(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('lux').getContext('2d');
        //var cores_lux = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Média em Lux',
                    data: data.data_lux,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }]
            },
        });
    })
}


function renderiza_combo(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){

        const ctx = document.getElementById('combo').getContext('2d');
        //var cores_lux = gera_cor(qtd=12)
        const myChart = new Chart(ctx, {

            data: {

                datasets: [{
                    type: 'bar',
                    label: 'Média em Lux',
                    data: data.data_lux,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }, {
                    type: 'line',
                    label: 'Média da Humidade',
                    data: data.data_humidade,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }, {
                    type: 'bar',
                    label: 'Média em Célsius',
                    data: data.data_temperatura,
                    backgroundColor: bg_color,
                    borderColor: border_color,
                    borderWidth: 1
                }],
                 labels: data.labels,
            },
        });
    })
}
