let token = localStorage.getItem("token");
post = document.getElementById("public_post");


function handleClick() {
    input = document.getElementById("name-17fb");
    s = input.value.replace(/^\s+|\s+$/g, '')
    if(s){
    var xhr = new XMLHttpRequest();

    var body = token +
      '|' + input.value;
    
    xhr.open("POST", '/add_post');
    xhr.setRequestHeader('Content-Type', 'application/text');
    
    
    xhr.send(body);
    window.location="/main";
    };
}
post.addEventListener('click', handleClick);