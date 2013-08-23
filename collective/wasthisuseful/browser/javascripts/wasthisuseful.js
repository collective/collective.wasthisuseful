var wtu = {

    thumbs: function() {
        
        $("#div-submit").click(function() {
           $("#form-comment").attr('value', $("#div-comment").attr('value'));  
           $('#usefulness-form').submit();
        });
        
        $('.javascript-only').css('display', 'inline');
        $('#usefulness-form').hide();

        $('.relevance a').click(function(e) {
            
            e.preventDefault();
            
            // reset, read thumb, and check according field
            $('input[name=useful]').attr('checked', false);

            var thumb = $(this).attr('class');
            var up = $('.up');
            var down = $('.down');
            var whynot = $("#why-not-useful");
            
            if( thumb == 'up' ) {
                up.css('background-position', '5px -30px');
                down.css('background-position', '-50px 0');
                whynot.hide();
                $('input#yes').attr('checked', true);
                $('#usefulness-form').submit();
            } else {
                down.css('background-position', '-50px -30px');
                up.css('background-position', '5px 0');
                $('input#no').attr('checked', true);
                whynot.fadeIn();
            }
        }); 
    }
};

$(document).ready(function() {
    wtu.thumbs();
});

