/**
 * JavaScript to support Scholarly Elsevier Search
 */

$(document).ready( function() {
    setupElsevier();
    setupArxiv();
});

function setupElsevier() {

    $("#elsevierQueryRunButton").off("click");

    $("#elsevierQueryRunButton").on("click", function() {

        var url = "search/searchElsevier";

        var input = $("#elsevierQueryInput").val();

        var data = {
            q: input
        }

        $.ajax({
            method: "GET",
            url: url,
            data: data
        }).done(function( xhr ) {
            $("#queryResults").html(xhr);

            $("#elsevierQueryResultsTable").DataTable();
        });

    });

}

/**
 *  Provide functionality for running the Arxiv search page.
 * 
 */
function setupArxiv() {

    $("arxivQueryRunButton").off("click");

    $("#arxivQueryRunButton").on("click", function() {

        var url = "search/searchArxiv";

        var input = $("#arxivQueryInput").val();

        var data = {
            q: input
        }

        $.ajax({
            method: "GET",
            url: url,
            data: data
        }).done(function( xhr ) {
            $("#queryResults").html(xhr);

            $("#arxivQueryResultsTable").DataTable();
        });

    });

}
