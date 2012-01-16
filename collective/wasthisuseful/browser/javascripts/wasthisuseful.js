var wtu = {

    thumbs: function() {
        
        jq("#div-submit").click(function() {
           jq("#form-comment").attr('value', jq("#div-comment").attr('value'));  
           jq('#usefulness-form').submit();
        });
        
        jq('.javascript-only').css('display', 'inline');
        jq('#usefulness-form').hide();
        
        jq('.relevance a').click(function(e) {
            
            e.preventDefault();
            
            // reset, read thumb, and check according field
            jq('input[name=useful]').attr('checked', false);

            var thumb = jq(this).attr('class');
            var up = jq('.up');
            var down = jq('.down');
            var whynot = jq("#why-not-useful");
            
            if( thumb == 'up' ) {
                up.css('background-position', '5px -30px');
                down.css('background-position', '-50px 0');
                whynot.hide();
                jq('input#yes').attr('checked', true);
                jq('#usefulness-form').submit();
            } else {
                down.css('background-position', '-50px -30px');
                up.css('background-position', '5px 0');
                jq('input#no').attr('checked', true);
                whynot.fadeIn();
            }
        })    
    },
    
    /* When "No" is clicked (information is not useful), show the comment field 
     * and submit button. */
    expandForm: function() {
        jq('#useful input:radio[value="0"]').click(function() {
            jq(this).parent().find(".comments").fadeIn();
        }); 
    } // no comma after last item

}

jq(document).ready(function() {
    wtu.expandForm();
    wtu.thumbs();
});

