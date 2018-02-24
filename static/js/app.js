var url = "/samples";


function buildPlot() {
    Plotly.d3.json(url, function(error, response) {

        console.log(response);
        var trace1 = {
            labels: response.map(data =>data.sample_values),
            values: response.map(data =>data.otu_ids),
            type: "pie"
        };

        var data = [trace1];

        var layout = {
            title:"Pie Chart",
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();
