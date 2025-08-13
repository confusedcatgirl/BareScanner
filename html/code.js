password = "";

function addChar(char) {
    if (passin.innerText.length < 4) {
        passin.innerText += "●";
        password += char;
    }
}

function removeLastChar() {
    if (passin.innerText.length > 0) {
        passin.innerText = passin.innerText.substring(0, passin.innerText.length - 1);
        password = password.substring(0, password.length - 1);
    }
}

function checkPass() {
    console.log(password)

    fetch("http://127.0.0.1:5000/api").then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log(data);
    }).catch(function(err) {
        console.log('Fetch Error :-S', err);
    });
}