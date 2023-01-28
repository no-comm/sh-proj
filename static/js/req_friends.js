my_id = localStorage.getItem("id");
var xhr = window.XMLHttpRequest;
var a = new xhr();
var c = new xhr();
last = "";

a.open("POST", '/my_friend');
a.onreadystatechange = () => {
    function name(ids){
        c.open("POST", '/get_username');
        c.onreadystatechange = () => {
            if (c.responseText){
                console.log(c.responseText);
                if (JSON.parse(c.responseText).join(" ")+"Удалить из друзей" != last){
                document.getElementById("list_friend").innerHTML += '<dt id="fr">'+'<a class="ids" href=/'+ids+" id="+ids+">"+JSON.parse(c.responseText).join(" ")+"</a>"+'<button id="del_friend" class="u-btn u-btn-round u-btn-submit u-button-style u-radius-18 u-btn-6">Удалить из друзей</button>'+"</dt>"
                last = document.getElementById("fr").textContent
                var btns = document.querySelectorAll('button')
                btns.forEach(function(btn) {
                btn.addEventListener('click', function(e) {
                    handleClick(ids)
                })
                })
                }
                
        };
        };
        c.setRequestHeader('Content-Type', 'application/text');
        
        c.send(ids);
        
    }
    if (a.responseText) {
    for (var i in JSON.parse(a.responseText)){
        name(JSON.parse(a.responseText)[i])
    };
}
};
a.setRequestHeader('Content-Type', 'application/text');
a.send(my_id);

function handleClick(id) {
        var xhr = window.XMLHttpRequest;
        var a = new xhr();
        a.open("POST", '/del_friend');
        a.onreadystatechange = () => {
            console.log(11);
        }
        a.setRequestHeader('Content-Type', 'application/text');
        a.send([my_id, id]);

    }

    