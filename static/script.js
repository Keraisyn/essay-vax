function unplagiarize() {

    const text = document.getElementById("text-area").value;
    console.log(text);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/unplagiarize", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        text: text
    }));

    xhr.onload = function() {
        var data = JSON.parse(this.responseText);
        console.log(data);
        document.getElementById("main-title").innerHTML = data.text;
    }
}