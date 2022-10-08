window.addEventListener("DOMContentLoaded", init);

function init(){
    var username = document.getElementById("username");
    var password = document.getElementById("password");
    if(username != null && password != null){
        username.addEventListener("input", usernameCheck);
        password.addEventListener("input", passwordCheck);
        username.addEventListener("change", usernameCheck);
        password.addEventListener("change", passwordCheck);
        password.addEventListener("change", passwordLengthCheck);
    }
    var regUsername = document.getElementById("regUsername");
    var regTeamName = document.getElementById("regTeamName");
    var regPassword = document.getElementById("regPassword");
    var regPasswordConfirm = document.getElementById("regPasswordConfirm");
    var regEmail = document.getElementById("regEmail");
    if(regUsername != null && regTeamName != null && regPassword != null && regPasswordConfirm != null && regEmail != null){
        regUsername.addEventListener("input", regUsernameCheck);
        regUsername.addEventListener("change", regUsernameCheck);
        regTeamName.addEventListener("input", regTeamNameCheck);
        regTeamName.addEventListener("change", regTeamNameCheck);
        regPassword.addEventListener("input", regPasswordCheck);
        regPassword.addEventListener("change", regPasswordCheck);
        regPasswordConfirm.addEventListener("input", regPasswordConfirmCheck);
        regPasswordConfirm.addEventListener("change", regPasswordConfirmCheck);
        regEmail.addEventListener("input", regEmailCheck);
        regEmail.addEventListener("change", regEmailCheck);
    }
    var regForm = document.getElementById("regForm");
    if(regForm != null){
        regForm.addEventListener("submit", regFormCheck);
    }
}

function regFormCheck(event){
    var regUsername = regUsernameCheck();
    var regTeamName = regTeamNameCheck();
    var regPassword = regPasswordCheck();
    var regPasswordConfirm = regPasswordConfirmCheck();
    var regEmail = regEmailCheck();
    var regError = document.getElementById("regError");
    var regSubmit = document.getElementById("regSubmit");
    if(regError != null && regSubmit != null){
        if(regUsername == true || regTeamName == true || regPassword == true || regPasswordConfirm == true || regEmail == true){
            event.preventDefault();
            regError.innerHTML = "A field has not been entered correctly";
            regSubmit.disabled = true;
        }
    } else{
            regError.innerHTML = "";
            regSubmit.disabled = false;
        }
}

function regEmailCheck(){
    var regEmail = document.getElementById("regEmail").value;
    var regSubmit = document.getElementById("regSubmit");
    var regEmailError = document.getElementById("regError");
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if(regSubmit != null && regEmailError != null){
        if(regEmail.length == 0){
            regEmailError.innerHTML = "Please provide an email";
            regSubmit.disabled = true;
            return true;
        } else if(!regEmail.match(validRegex)){
            regEmailError.innerHTML = "Please provide a properly formatted email";
            regSubmit.disabled = true;
            return true;
        } else{
            regEmailError.innerHTML = "";
            regSubmit.disabled = false;
            return false;
        }
    }
}

function usernameCheck(){
    var usernameError = document.getElementById("usernameError");
    var username = document.getElementById("username").value;
    var submit = document.getElementById("submit");
    if(usernameError != null && submit != null){
        username.innerHTML = username.trim()
        if(username.length == 0){
            usernameError.innerHTML = "Please provide a username!"
            submit.disabled = true;
            return true;
        } else{
            usernameError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function regUsernameCheck(){
    var usernameError = document.getElementById("regError");
    var username = document.getElementById("regUsername").value;
    var submit = document.getElementById("regSubmit");
    if(usernameError != null && submit != null){
        username.innerHTML = username.trim()
        if(username.length == 0){
            usernameError.innerHTML = "Please provide a username!"
            submit.disabled = true;
            return true;
        } else{
            usernameError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function regTeamNameCheck(){
    var regTeamNameError = document.getElementById("regError");
    var regTeamName = document.getElementById("regTeamName").value;
    var submit = document.getElementById("regSubmit");
    if(regTeamNameError != null && submit != null){
        regTeamName.innerHTML = regTeamName.trim()
        if(regTeamName.length == 0){
            regTeamNameError.innerHTML = "Please provide a team name!"
            submit.disabled = true;
            return true;
        } else{
            regTeamNameError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function passwordCheck(){
    var passwordError = document.getElementById("passwordError");
    var password = document.getElementById("password").value;
    var submit = document.getElementById("submit");
    if(passwordError != null && submit != null){
        if(password.length == 0){
            passwordError.innerHTML = "Please provide a password";
            submit.disabled = true;
            return true;
        } else if(password.search(/[0-9]/) == -1){
            passwordError.innerHTML = "Password must contain a number";
            submit.disabled = true;
            return true;
        } else if(password.search(/[A-Z]/g) == -1){
            passwordError.innerHTML = "Password must contain an upper case letter";
            submit.disabled = true;
            return true;
        } else if(password.search(/[a-z]/g) == -1){
            passwordError.innerHTML = "Password must contain a lower case letter";
            submit.disabled = true;
            return true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function regPasswordConfirmCheck(){
    var regPasswordConfirmError = document.getElementById("regError");
    var regPasswordConfirm = document.getElementById("regPasswordConfirm").value; 
    var regPassword = document.getElementById("regPassword").value;
    var submit = document.getElementById("regSubmit");
    if(regPasswordConfirmError != null && submit != null){
        if(regPasswordConfirm != regPassword){
            regPasswordConfirmError.innerHTML = "Passwords do not match";
            submit.disabled = true;
            return true;
        } else{
            regPasswordConfirmError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function regPasswordCheck(){
    var passwordError = document.getElementById("regError");
    var password = document.getElementById("regPassword").value;
    var submit = document.getElementById("regSubmit");
    if(passwordError != null && submit != null){
        if(password.length == 0){
            passwordError.innerHTML = "Please provide a password";
            submit.disabled = true;
            return true;
        } else if(password.search(/[0-9]/) == -1){
            passwordError.innerHTML = "Password must contain a number";
            submit.disabled = true;
            return true;
        } else if(password.search(/[A-Z]/g) == -1){
            passwordError.innerHTML = "Password must contain an upper case letter";
            submit.disabled = true;
            return true;
        } else if(password.search(/[a-z]/g) == -1){
            passwordError.innerHTML = "Password must contain a lower case letter";
            submit.disabled = true;
            return true;
        } else if(password.length < 7){
            passwordError.innerHTML = "Password must be at least 7 characters long!";
            submit.disabled = true;
            return true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

function passwordLengthCheck(){
    var passwordError = document.getElementById("passwordError");
    var password = document.getElementById("password").value;
    var submit = document.getElementById("submit");
    if(passwordError != null && submit != null){
        if(password.length < 7){
            passwordError.innerHTML = "Password must be at least 7 characters long!";
            submit.disabled = true;
            return true;
        } else{
            passwordError.innerHTML = "";
            submit.disabled = false;
            return false;
        }
    }
}

        