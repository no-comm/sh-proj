addr = window.location.href.split("/").slice(-1).join();
a = 0;
urls = ["main", "login", "friends", "register", "im", "news", "logout", "settings", "add_post", "get_posts", "user", "404"];
for (const element of urls) {
    if (addr == element){
        a = a + 1;
    };
    
    
};
if (a = 0){window.location = "/404";}
function wall_user(){
    var xhr = window.XMLHttpRequest;
    var body = addr;
    var a = new xhr();
    var b = new xhr();
    var c = new xhr();
    a.open("POST", '/user');
    a.onreadystatechange = () => {
        res = a.responseText;
        if (res == "False"){
            window.location = "/404";
        };
    
    
        var body = addr;
        c.open("POST", '/get_username');
        c.onreadystatechange = () => {
            if (c.responseText){
                console.log(c.responseText);

        document.getElementById("username").innerHTML = JSON.parse(c.responseText).join(" ");
    };};c.setRequestHeader('Content-Type', 'application/text');
    c.send(body);
    
    
    
        var body = addr;
        b.open("POST", '/get_posts');
        b.onreadystatechange = () => {
        if (b.responseText){
            posts = JSON.parse(b.responseText).reverse();
            document.getElementById("posts").innerHTML = "";
            for (i of posts){
                document.getElementById("posts").innerHTML += "<dt>"+i+"</dt>"
            };
        };
        };
        b.setRequestHeader('Content-Type', 'application/text');
        b.send(body);
    
    };
    a.setRequestHeader('Content-Type', 'application/text');
    a.send(body);
    
};
if (addr>0){
    wall_user();
};
if (addr=="main"){
    var xhr = window.XMLHttpRequest;
    var body = localStorage.getItem("token");
    var a = new xhr();
    var b = new xhr();
    var c = new xhr();
    a.open("POST", '/get_my_id');
    a.onreadystatechange = () => {
        res = a.responseText;
    
    
        var body = res;
        localStorage.setItem("id", body);
        
    
    
    
        
    
    };
    a.setRequestHeader('Content-Type', 'application/text');
    a.send(body);

    var body = localStorage.getItem("id");
    if (body){
        c.open("POST", '/get_username');
        c.onreadystatechange = () => {
            console.log(c.responseText);
            if (c.responseText){
        document.getElementById("username").innerHTML = JSON.parse(c.responseText).join(" ");
        localStorage.setItem("username", JSON.parse(c.responseText).join(" "));
        };
    // else {window.location = "/login"};
        };
        c.setRequestHeader('Content-Type', 'application/text');
        c.send(body);
        };
    if (body){
    b.open("POST", '/get_posts');
    b.onreadystatechange = () => {
    if (b.responseText){
        posts = JSON.parse(b.responseText).reverse();
        document.getElementById("posts").innerHTML = "";
        var username = localStorage.getItem("username");
        for (i of posts){
            document.getElementById("posts").innerHTML += "<dt>"+'<div style="color:blue;">'+username+"</div>"+i+"</dt>";
        };
    };
    };
    b.setRequestHeader('Content-Type', 'application/text');
    b.send(body);
    };
    
};
