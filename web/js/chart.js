let xLabels = [];
let yMoney = [];

// Innitialize chart
makeChart();

async function makeChart() {
    await getData();
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: xLabels,
            datasets: [{
                label: 'Trees',
                data: yMoney
            }]
        },
        options: {
            responsive: 'true',
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

// Call python webscrape function every 10 seconds
setInterval(() => {
    eel.getAmount();
    makeChart();
}, 10000)