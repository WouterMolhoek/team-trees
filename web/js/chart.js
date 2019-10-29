let xLabels = [];
let yMoney = [];

// Innitialize chart
makeChart();

let chart;

async function makeChart() {
    await getData();
    const ctx = document.getElementById('myChart');
    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: xLabels,
            datasets: [{
                label: 'Team Trees Raise 🌳',
                data: yMoney
            }]
        },
        options: {
            responsive: 'true',
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    ticks: {
                        beginAtZero: true,
                        max: 20000000
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Money'
                    }
                }]
            }
        }
    });
}

async function getData() {
    const response = await fetch('../data/data.json');
    let data = await response.json();
    
    for (let i = 0; i < data.trees.length; i++) {
        xLabels.push(data.trees[i][0]);
        yMoney.push(data.trees[i][1]);
    }
}

// Call python webscrape function every 30 seconds
setInterval(() => {
    eel.getAmount();
    updateData();
}, 30000)


// Update curent data 
async function updateData() {
    const response = await fetch('../data/data.json');
    let data = await response.json();

    addData(chart, data.trees[data.trees.length - 1][0], data.trees[data.trees.length - 1][1]);
}

// Add new data to the chart
function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}