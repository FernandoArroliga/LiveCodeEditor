var menuList = document.getElementById("menuList");

menuList.style.maxHeight = "0px";

function togglemenu(){

    if(menuList.style.maxHeight == "0px")
        {
            menuList.style.maxHeight = "130px";
        }
    else 
        {
            menuList.style.maxHeight = "0px";
        }
}


var docsButton = document.getElementById("docsButton");

docsButton.addEventListener("click", function() {
    window.location.href = "docs.html";
});
