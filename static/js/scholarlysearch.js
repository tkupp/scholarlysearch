/**
 * JavaScript to support Scholarly Search
 */

/**
 * This function executes upon page load up.
 */
$(document).ready( function() {
     setup();
});

/**
 * Setup listeners and actions for the Scholarly Search UI page. 
 * This sets up the tab functionality. 
 * 
 */
function setup() {

    // Kill any existing listeners.
    $('#home-tab').off("click");
    $('#search-tab').off("click");
    $('#contact-tab').off("click");

    // Load new tab listeners

    $('#home-tab').on("click", function (e) {
        e.preventDefault()
        $(this).tab('show')
      })

    $('#search-tab').on("click", function (e) {
        e.preventDefault()
        $(this).tab('show')
        loadSearch();
      })

      $('#documentation-tab').on("click", function (e) {
        e.preventDefault()
        $(this).tab('show');
      })

}

/**
 *  Load up the 'search' UI page and return the content to the 'search-content' div
 */
function loadSearch() {

    // Empty out the existing div content.
    $("#search-content").html("");

    var url = "search/";
    var data = {};

    // Call the url and load the page into the search-content div
    $.ajax({
        url: url,
        cache: false
      })
      .done(function( xhr ) {
          $( "#search-content" ).html( xhr );
    });

}

