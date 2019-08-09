           var chart = c3.generate({
                bindto: '#featureChart',
    data: {
        x: 'Timeline',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: {{featureDevData|safe}},
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        },
        y: {
            tick:{
            values: [1,2,3,4]
            }
            
        }
    },
    color: {
        pattern: ['pink']
    }
});

var histogram = c3.generate({
bindto: '#bugHistogram',
    data: {
        x: 'bugT',
        columns: {{bugData|safe}},
        type: 'bar'
        
    },
    axis: {
        x: {
            type: 'bar',
            tick: {
                
            }
        },
        y: {
            tick:{
            values: [1,2,3,4]
            }
            
        }
    },
    bar: {
        width: {
            ratio: 0.15 
        }
    
    },
    
    color: {
        pattern: ['pink']
    }
    
});
    