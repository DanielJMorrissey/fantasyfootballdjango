window.addEventListener("DOMContentLoaded", init);

function init(event){
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    if(username != null && password != null){
        username.addEventListener("input", usernameCheck);
        password.addEventListener("input", passwordCheck);
        username.addEventListener("change", usernameCheck);
        password.addEventListener("change", passwordCheck);
        password.addEventListener("change", passwordLengthCheck);
    }
}

function usernameCheck(event){
    var usernameError = document.getElementById("usernameError");
    var username = document.getElementById("username").value;
    var submit = document.getElementById("submit");
    if(usernameError != null && submit != null){
        username.innerHTML = username.trim()
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
        } else if(password.search(/[0-9]/) == -1){
            passwordError.innerHTML = "Password must contain a number";
            submit.disabled = true;
        } else if(password.search(/[A-Z]/g) == -1){
            passwordError.innerHTML = "Password must contain an upper case letter";
            submit.disabled = true;
        } else if(password.search(/[a-z]/g) == -1){
            passwordError.innerHTML = "Password must contain a lower case letter";
            submit.disabled = true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
        }
    }
}

function passwordLengthCheck(event){
    var passwordError = document.getElementById("passwordError");
    var password = document.getElementById("password").value;
    var submit = document.getElementById("submit");
    if(passwordError != null && submit != null){
        console.log("in 1st if")
        if(password.length < 7){
            console.log("in 2nd if")
            event.preventDefault();
            passwordError.innerHTML = "Password must be at least 7 characters long!";
            submit.disabled = true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
        }
    }
}

        