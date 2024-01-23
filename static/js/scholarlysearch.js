/**
 * JavaScript to support Scholarly Search
 */

$(document).ready( function() {
     setup();
});

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

      $('#contact-tab').on("click", function (e) {
        e.preventDefault()
        $(this).tab('show')
      })

}

function loadSearch() {

    $("#search-content").html("");

    var url = "search/";

    var data = {};

    $.ajax({
        url: url,
        cache: false
      })
      .done(function( xhr ) {
          $( "#search-content" ).html( xhr );
    });

}