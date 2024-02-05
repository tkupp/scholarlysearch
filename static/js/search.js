/**
 * JavaScript to support Scholarly Elsevier Search
 */

$(document).ready( function() {
    setupElsevier();
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