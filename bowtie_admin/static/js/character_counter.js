(function($) {

    $.fn.characterCounter = function() {

        var _count = function(source, destination, max_length) {
            var counter = source.val().length.toString();
            if(max_length != null) {
                counter += " / " + (max_length - source.val().length).toString();
            }
            destination.html(counter);
        };

        this.each(function(index, element) {

            var counter_id = $(this).attr('id');
            var source_id = counter_id.replace('-counter','');
            var source = $('#' + source_id);

            var max_length = source.attr('maxlength');
            var destination = $(this).find('.counter');

            source.keyup(function() {
                _count(source, destination, max_length)
            });

            source.change(function() {
                _count(source, destination, max_length)
            });
        });
    };
    $(function() {
        $('.character-counter').each(function() {
            $(this).characterCounter();
        });
    });
})(django.jQuery);
