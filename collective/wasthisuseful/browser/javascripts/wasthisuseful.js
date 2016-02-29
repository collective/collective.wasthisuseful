var wtu = {

    thumbs: function() {
        
        $('.javascript-only').css('display', 'inline');

        $('.relevance a').click(function(e) {
            
            e.preventDefault();
            
            var up = $('.up');
            var down = $('.down');
            var whynot = $("#not-useful-form");
            if($(this).hasClass('up')) {
                down.removeClass('active');
                up.addClass('active');
                whynot.hide();
                $("#useful-form input[type='submit']").click();
            } else if($(this).hasClass('down')) {
                up.removeClass('active');
                down.addClass('active');
                whynot.fadeIn();
            }
        }); 
    }
};

$(document).ready(function() {
    wtu.thumbs();
});

