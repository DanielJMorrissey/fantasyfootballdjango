window.addEventListener("DOMContentLoaded", init);

function init(event){
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    if(username != null && password != null){
        username.addEventListener("change", usernameCheck);
        password.addEventListener("change", passwordCheck);
    }
}

function usernameCheck(event){
    var usernameError = document.getElementById("usernameError");
    var username = document.getElementById("username").value;
    var submit = document.getElementById("submit");
    if(usernameError != null && submit != null){
        if(username.length == 0){
            usernameError.innerHTML = "Please provide a username!"
            submit.disabled = true;
        } else{
            usernameError.innerHTML = "";
            submit.disabled = false;
        }
    }
}

function passwordCheck(event){
    var passwordError = document.getElementById("passwordError");
    var password = document.getElementById("password").value;
    var submit = document.getElementById("submit");
    if(passwordError != null && submit != null){
        if(password.length == 0){
            passwordError.innerHTML = "Please provide a password";
            submit.disabled = true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
        }
    }
}