 
//                 var chart = c3.generate({
                    
//                     bindto: '#chart',
//                     point: {
//                         focus: {
//                             expand: {
//                                 enabled: false
//                             }
//                         },
//                         r: 16
//                     },
//                     data: {
//                         x: 'Timeline',
//                         xFormat: '%Y-%m-%d %H:%M:%S',
//                         columns: {{ featureDevData | safe }},
//                         type: 'scatter'
//                     },
//                     axis: {
//                         x: {
//                             type: 'timeseries',
//                             tick: {
//                                 format: '%Y-%m-%d'
//                             }
//                         },
//                         y: {
//                             tick: {
//                                 values: [1, 2, 3, 4]
//                             }
//                         }
//                     },
//                     color: {
//                         pattern: ['pink']
//                     },
//                 });

// // BUG RESOLVEMENT TIME HISTOGRAM
//                 var histogram = c3.generate({
//                     bindto: '#bugHistogram',
//                     data: {
//                         x: 'bugT',
//                         columns: {{ bugData | safe }},
//                         type: 'bar'

//                     },
//                     axis: {
//                         x: {
//                             type: 'bar',
//                             tick: {

//                             }
//                         },
//                         y: {
//                             tick: {
//                                 values: [1, 2, 3, 4]
//                             }

//                         }
//                     },
//                     bar: {
//                         width: {
//                             ratio: 0.15
//                         }

//                     },

//                     color: {
//                         pattern: ['pink']
//                     }

//                 });
                
                
              
//   var labels = {{featureVarData|safe}};
//   var series = chart.internal.main.selectAll('.' + c3.chart.internal.fn.CLASS.circles);

   
//   // get the parent of the the <circles> to add <text as siblings>
//   var g = d3.selectAll('.c3-circles-Number-of-Features-over-Time');
//   console.log(g);
//   //Get all circle tags
//   var circles = d3.selectAll('circle')._groups[0];; //first had [0]
  
//   //go to each circle and add a text label for it
//   for(var i = 0; i < circles.length; i++){
//     //fetch x-coordinate
//     var x = circles[i].cx;
//     //fetch y-coordinate
//     var y = circles[i].cy;

//   //create and append the text tag
//     g.append('text')
//       .attr('y', y.baseVal.value)  // (-15) places the tag above the circle, adjust it according to your need
//       .attr('x', x.baseVal.value)
//       .attr('text-anchor', 'middle')
//       .attr('class', 'c3-text c3-text-'+i)
//       .text(labels[i]) // the text that needs to be added can be hard coded or fetched for the original data.
//       //Since I am using a JSON to plot the data, I am referencing it and using the key of the value to be shown.
//   };

  
  