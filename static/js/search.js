/**
 * JavaScript to support Scholarly Elsevier Search
 */

/**
 * This function executes upon page load up.
 */
$(document).ready( function() {
    setupElsevier();
    setupArxiv();
});

/**
 * Setup listeners and action for the Elsevier UI page. 
 * This will listen for the query button being pushed, then will 
 * execute the query to teh upstream service.
 * 
 */
function setupElsevier() {

    // Destroy and existing listeners. This is needed so that multiple listeners aren't
    // created in some situations.
    $("#elsevierQueryRunButton").off("click");

    // Create a listener for the the elsevier run button being clicked.
    $("#elsevierQueryRunButton").on("click", function() {

        var url = "search/searchElsevier";
        var input = $("#elsevierQueryInput").val();

        var data = {
            q: input
        }

        // Run the upstream query and populate the queryResults div with the results.
        $.ajax({
            method: "GET",
            url: url,
            data: data
        }).done(function( xhr ) {
            $("#queryResults").html(xhr);

            // Datatable is used to provided a more functional interface over standard html tables.
            // Reference: https://datatables.net/examples/index
            $("#elsevierQueryResultsTable").DataTable();
        });

    });

}

/**
 * Setup listeners and action for the Arxiv UI page. 
 * This will listen for the query button being pushed, then will 
 * execute the query to teh upstream service.
 * 
 */
function setupArxiv() {

    // Destroy and existing listeners. This is needed so that multiple listeners aren't
    // created in some situations.
    $("arxivQueryRunButton").off("click");

    // Create a listener for the the arxiv run button being clicked.
    $("#arxivQueryRunButton").on("click", function() {

        var url = "search/searchArxiv";
        var input = $("#arxivQueryInput").val();

        var data = {
            q: input
        }

        // Run the upstream query and populate the queryResults div with the results.
        $.ajax({
            method: "GET",
            url: url,
            data: data
        }).done(function( xhr ) {
            $("#queryResults").html(xhr);

            // Datatable is used to provided a more functional interface over standard html tables.
            // Reference: https://datatables.net/examples/index
            $("#arxivQueryResultsTable").DataTable();
        });

    });

}
