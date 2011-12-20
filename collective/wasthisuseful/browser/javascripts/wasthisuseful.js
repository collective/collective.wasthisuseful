var wtu = {

    thumbs: function() {
        
        jq("#div-submit").click(function() {
           jq("#form-comment").attr('value', jq("#div-comment").attr('value'));  
           jq('#usefulness-form').submit();
        });
        
        jq('.javascript-only').show();
        jq('#usefulness-form').hide();
        
        jq('.relevance a').click(function(e) {
            
            e.preventDefault();
            
            // reset, read thumb, and check according field
            jq('input[name=useful]').attr('checked', false);
            thumb = jq(this).attr('class');
            
            if( thumb == 'up' ) {
                jq('.up').css('background-position', '5px -30px');
                jq('.down').css('background-position', '-50px 0');
                jq('.content .details .update').css('height', '1em');
                jq("#why-not-useful").hide();
                jq('input#yes').attr('checked', true);
                jq('#usefulness-form').submit();
            } else {
                jq('.down').css('background-position', '-50px -30px');
                jq('.up').css('background-position', '5px 0');
                jq('input#no').attr('checked', true);
                jq('.content .details .update').css('height', '4em');
                jq("#why-not-useful").fadeIn();
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

