/* data route */
// var url = "/samples/"+samplenameselect;
// var samplenameselect = document.getElementById("nameSampleSelect");


function optionChanged(value){
    console.log(value)
    return buildPie(value);
    return buildBubblePlot(value);
};

function buildPie(chosenSample) {

    Plotly.d3.json(`/samples/${chosenSample}`, function(error, response) {
        
        console.log(response);

        var data = [{
            labels: response[0]['otu_ids'],
            values: response[0]['sample_values'],
            type: 'pie'
        }];
       

        console.log(data);  

        var layout = {
            title: "Top 10 samples by otu_id",    
        };

        console.log(layout);
    Plotly.newPlot("pie", data, layout);
    });
};

defaultSample = 'BB_940'
buildPie(defaultSample);
    
    // function updatePlotly(newdata) {
    //     var PIE = document.getElementById("pie");
    //     Plotly.restyle(PIE, "values", [newdata]);
    // };

    





// function buildPlot(chosenSample) {
//     Plotly.d3.json(url, function(error, response) {
//         console.log(response);
            

//         // bubble chart
// var trace1 = {
//     x: response.map(data => data.otu_ids),
//     y: response.map(data => data.sample_values),
//     mode: 'markers',
//     marker: {
//       size: response.map(data => data.sample_values),
//     }
//   };
  
//   var data = [trace1];
  
//   var layout = {
//     title: 'Marker Size',
//     showlegend: false,
//     height: 600,
//     width: 600
//   };
  
//   Plotly.newPlot('myDiv', data, layout);
// }



//     function updatePlotly(newdata) {
//         var PIE = document.getElementById("pie");
//         Plotly.restyle(PIE, "values", [newdata]);
//     }

//     function optionChanged(namesample) {
//         var nameSampleSelect = document.getElementById("selDataset");
//     }
//     updatePlotly(namesample);

// });

// buildPlot();
    