// Function to retrieve a cookie value by its name
function getUserResponse(){
    
    var userText = $('#chat-input').val();
    var userHTML = "<p class='userText'>User: <span>"+userText+"</span></p>";
     $('#chat-input').val(""),
     $('#chat-container').append(userHTML)

}

$('#send-btn').click(function(){
    getUserResponse();
})