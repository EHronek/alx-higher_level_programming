$(document).ready(function() {
    $('#add_item').on('click', function() {
        $('ul.my_list').append('<li>Item</li>');
    });
    
    $('#remove_item').on('click', function() {
        if ($('ul.my_list li').length > 0) {
            $('ul.my_list li:last').remove();
        }
    });

    $('#clear_list').on('click', function() {
        $('ul.my_list').empty();
    });
});