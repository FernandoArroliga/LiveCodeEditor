// Homepage events
var menuList = document.getElementById("menuList");
var docsButton = document.getElementById("docsButton");
var codeButton = document.getElementById("codeButton");

// Function for menuList
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

// Function for docsButton
docsButton.addEventListener("click", function() {
    window.location.href = "tutorials";
});

// Function for start button
codeButton.addEventListener("click", function() {
    window.location.href = "coding";
});

