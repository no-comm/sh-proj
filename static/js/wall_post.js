var xhr = window.XMLHttpRequest;
var a = new xhr();
var c = new xhr();
function ss(i){
    c.open("POST", '/get_username');
    c.onreadystatechange = () => {
        if (c.responseText){
            

    let username = JSON.parse(c.responseText).join(" ");
    console.log(username)
    return username;
};};
c.setRequestHeader('Content-Type', 'application/text');
c.send(i[0]);

}

a.open("POST", '/wall_post');
    a.onreadystatechange = () => {
        
    
        console.log(a.responseText)
        for (i of JSON.parse(a.responseText)){
            //let user = ss(i)
            c.open("POST", '/get_username');
    c.onreadystatechange = () => {
        if (c.responseText){
            

    var username = JSON.parse(c.responseText).join(" ");
    localStorage.setItem("username", username);
};};
c.setRequestHeader('Content-Type', 'application/text');
c.send(i[0]);
let username = localStorage.getItem("username");
            console.log(username)
            
            document.getElementById("wall").innerHTML += "<dt>"+'<div class="frame" alt="">'+'<a href="/'+i[0]+'">'+username+"</a>"+' '+i[2]+'<img id="btn" class="btn" src="../static/images/like.png"/>'+"</div>"+'<div>'+i[1]+'</div>'+"</dt>"
            console.log(i)
        }
        var res = decodeURIComponent(JSON.parse(a.responseText))
        
        //document.getElementById("wall").innerHTML = res
    
    }
    a.setRequestHeader('Content-Type', 'application/text');
    a.send("");