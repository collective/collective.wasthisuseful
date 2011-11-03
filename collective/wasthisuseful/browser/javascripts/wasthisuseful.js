var wasthisuseful = {

    /* When "No" is clicked (information is not useful), show the comment field 
     * and submit button. */
    expandForm: function() {
        $('#useful input:radio[value="0"]').click(function() {
            jq(this).parent().find(".comments").fadeIn();
        }); 
    } // no comma after last item

}

jq(document).ready(function() {
    wasthisuseful.expandForm();
});

