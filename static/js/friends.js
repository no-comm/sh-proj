function add_friend(id){
    var xhr = window.XMLHttpRequest;
    var a = new xhr();
    my_id = localStorage.getItem("id");
    a.open("POST", '/add_friends');
    a.onreadystatechange = () => {
        console.log(a.responseText)

    };
    a.setRequestHeader('Content-Type', 'application/text');
    a.send([my_id, id]);
}

function handleClick(e) {
    e = e || window.event;
    var target = e.target || e.srcElement;
    if(target.id == "search"){
    
    input = document.getElementById("name-0e35");
    s = input.value.replace(/^\s+|\s+$/g, '');
    if(s){
    var xhr = window.XMLHttpRequest;
    var a = new xhr();
    var body = input.value;
    a.open("POST", '/friends');
    a.onreadystatechange = () => {
        if (a.responseText){
            document.getElementById("jumans").innerHTML = "";
            console.log(JSON.parse(a.responseText))
        for (var i in JSON.parse(a.responseText)){
            document.getElementById("jumans").innerHTML += "<dt id="+JSON.parse(a.responseText)[i]+'>'+"<a href=/"+JSON.parse(a.responseText)[i]+">"+i+"</a>"+'<button class="u-btn u-btn-round u-btn-submit u-button-style u-radius-18 u-btn-6">Добавить в друзья</button>'+"</dt>"
            
        };
        var btns = document.querySelectorAll('button')
            btns.forEach(function(btn) {
              btn.addEventListener('click', function(e) {
                add_friend(e.target.parentNode.id)
              })
            })
    };

    };
    a.setRequestHeader('Content-Type', 'application/text');
    a.send(body);
    

    };
};
};
document.getElementById("search").addEventListener('click', handleClick);



