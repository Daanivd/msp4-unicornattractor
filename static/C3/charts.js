     var chart = c3.generate({
            bindto: '#chart',
            point: {
                focus: {
                    expand: {
                        enabled: false
                    }
                },
                r: 16
            },
            data: {
                x: 'Timeline',
                xFormat: '%Y-%m-%d %H:%M:%S',
                columns: {{ featureDevData | safe }},
                type: 'scatter'
            },
            axis: {
                x: {
                    type: 'timeseries',
                    min: '2017-01-01 00:00:00',
                    max: new Date().getFullYear() + '-12-31 23:59:59',
                    padding: {top: 0, bottom: 0},
                    tick: {
                        format: '%Y-%m'
                    },
        
                },
                y: {
                    tick: {
                        format: d3.format("01d"),
                    }
                }
            },
            color: {
                pattern: ['pink']
            },
        });

        // BUG RESOLVEMENT TIME HISTOGRAM
        var histogram = c3.generate({
            bindto: '#bugHistogram',
            data: {
                x: 'bugT',
                columns: {{ bugData | safe }},
                type: 'bar'

            },
            axis: {
                x: {
                    type: 'bar',
                    tick: {

                    }
                    
                },
                y: {
                    tick: {
                        values: [1, 2, 3, 4, 5, 6, 7]
                    }

                }
            },
            bar: {
                width: {
                    ratio: 0.75
                }

            },

            color: {
                pattern: ['pink']
            }

        });



        var labels = {{ featureVarData | safe }};
        var series = chart.internal.main.selectAll('.' + c3.chart.internal.fn.CLASS.circles);


        // get the parent of the the <circles> to add <text as siblings>
        var g = d3.selectAll('.c3-circles-Number-of-Features-over-Time');
        
        //Get all circle tags
        var circles = d3.selectAll('circle')._groups[0];; //first had [0]

        //go to each circle and add a text label for it
        for (var i = 0; i < circles.length; i++) {
            //fetch x-coordinate
            var x = circles[i].cx;
            //fetch y-coordinate
            var y = circles[i].cy;

            //create and append the text tag
            g.append('text')
                .attr('y', y.baseVal.value) 
                .attr('x', x.baseVal.value)
                .attr('text-anchor', 'middle')
                .attr('class', 'c3-text c3-text-' + i)
                .text(labels[i]) 
        };