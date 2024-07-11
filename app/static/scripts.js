$(document).ready(function() {
    $('#calculator-form').on('submit', function(event) {
        event.preventDefault();
        const formData = $(this).serialize();

        $.post('/', formData, function(data) {
            $('#result').html(`<h2 class="text-center">Result: ${data.result}</h2>`);
        }, 'json').fail(function() {
            $('#result').html('<h2 class="text-center text-danger">Error: Invalid input or operation</h2>');
        });
    });

    $('#clear-button').on('click', function() {
        $('#calculator-form')[0].reset();
        $('#result').html('');
    });

    $('#plot-form').on('submit', function(event) {
        event.preventDefault();
        const formData = $(this).serialize();

        $.post('/plot', formData, function(data) {
            if (data.success) {
                $('#plot-result').html(`<div id="plot"></div>`);
                Plotly.newPlot('plot', data.graph_data, {
                    title: 'Graph',
                    xaxis: { title: 'X-axis' },
                    yaxis: { title: 'Y-axis' }
                });
            } else {
                $('#plot-result').html('<h2 class="text-center text-danger">Error: Could not plot the graph</h2>');
            }
        }, 'json').fail(function() {
            $('#plot-result').html('<h2 class="text-center text-danger">Error: Could not plot the graph</h2>');
        });
    });
});
