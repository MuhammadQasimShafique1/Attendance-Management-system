// ================================
// Login Validation
// ================================

function validateLogin(){

    let username = document.getElementById("username");

    let password = document.getElementById("password");

    if(username==null || password==null)

        return true;

    if(username.value.trim()===""){

        alert("Enter Username");

        username.focus();

        return false;

    }

    if(password.value.trim()===""){

        alert("Enter Password");

        password.focus();

        return false;

    }

    return true;

}

// ================================
// Register Validation
// ================================

function validateRegister(){

    let fullname=document.getElementById("fullname");

    let username=document.getElementById("username");

    let email=document.getElementById("email");

    let password=document.getElementById("password");

    let confirm=document.getElementById("confirm_password");

    if(fullname && fullname.value.trim()===""){

        alert("Enter Full Name");

        fullname.focus();

        return false;

    }

    if(username && username.value.trim()===""){

        alert("Enter Username");

        username.focus();

        return false;

    }

    if(email && email.value.trim()===""){

        alert("Enter Email");

        email.focus();

        return false;

    }

    if(email){

        let pattern=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if(!pattern.test(email.value)){

            alert("Invalid Email Address");

            email.focus();

            return false;

        }

    }

    if(password && password.value.length<6){

        alert("Password must be at least 6 characters");

        password.focus();

        return false;

    }

    if(confirm && password.value!=confirm.value){

        alert("Passwords do not match");

        confirm.focus();

        return false;

    }

    return true;

}

// ================================
// Phone Validation
// ================================

function validatePhone(phone){

    let pattern=/^[0-9]{10,15}$/;

    return pattern.test(phone);

}

// ================================
// Only Numbers
// ================================

function onlyNumber(evt){

    let ch=String.fromCharCode(evt.which);

    if(!(/[0-9]/.test(ch))){

        evt.preventDefault();

    }

}

// ================================
// Password Strength
// ================================

function passwordStrength(){

    let password=document.getElementById("password");

    let strength=document.getElementById("strength");

    if(!password || !strength)

        return;

    let value=password.value;

    if(value.length<6){

        strength.innerHTML="Weak";

        strength.style.color="red";

    }

    else if(value.length<10){

        strength.innerHTML="Medium";

        strength.style.color="orange";

    }

    else{

        strength.innerHTML="Strong";

        strength.style.color="green";

    }

}