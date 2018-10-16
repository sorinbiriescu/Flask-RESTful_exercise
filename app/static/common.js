"use strict";
document.addEventListener("DOMContentLoaded", function(event) { 

let request = fetch("http://localhost:8000/message/")

request.then( function(response) {
    // console.log(response.json())
    response.json().then (
        function(json) {
            show_results(json)
        }
    )
});

document.querySelector("#btn_delete_message").onpointerdown()

function show_results (json) {
    let test_div = document.querySelector("#test")
    let message_list = document.createElement("ul")
    test_div.appendChild(message_list)

    for(let result of json) {
        message_list.innerHTML += "<li>" + result.id + " - " + result.message + " - " + result.message_author + "<a href='#' class='alert button' id='btn_delete_message'>Alert Btn</a></li>" 

        // console.log(result)
    }
};

});
  