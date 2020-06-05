var signin_btn = document.getElementById('signin_btn');
var signup_btn = document.getElementById('signup_btn');
var signin = document.getElementById('signin');
var signup = document.getElementById('signup');
var closes = document.getElementsByClassName('modal-close');



signin_btn.onclick = function() {
    signin.style.display = 'block';
}

signup_btn.onclick = function() {
    signup.style.display = 'block';
}

for (let index = 0; index < closes.length; index++) {
    const close = closes[index];
    close.onclick =closeW
}


function closeW(event){
    signin.style.display = 'none';
    signup.style.display = 'none';
    event.stopPropagation();
}
