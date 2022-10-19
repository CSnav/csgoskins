

const urlSearchParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlSearchParams.entries());

// Click on Box
// Triggers onclick=redirect(this)
// redirect will take the current query string, the newly clicked box, and either append or remove it depending on whether its in the list or not


function redirect(changed_filter) {
    let newstring = urlSearchParams.toString();
    newstring = newstring.replace(/\+/g, '%20'); 
    newstring = decodeURIComponent(newstring);      
    let index = newstring.indexOf(changed_filter.value); 
    if(index != -1) {
        if(index == 0) {
            if(index + changed_filter.value.length != newstring.length) {
                newstring = "?" + newstring.replace(changed_filter.value+"&", "");
            } else {
                newstring = newstring.replace(changed_filter.value, "");
            }
        } else if(newstring[index-1] === "&") {
            newstring = "?" + newstring.replace("&"+changed_filter.value, "");
        }
    } else {
        if(Object.keys(params).length === 0) {
            newstring = "?"+changed_filter.value; 
        } else {
            newstring = "?" + newstring + "&" + changed_filter.value;
        }
    }
   window.location.replace(window.location.pathname + newstring); 
    console.log(newstring);
}


window.onload = function updateUI() {
    let newstring = urlSearchParams.toString();
    newstring = newstring.replace(/\+/g, '%20'); 
    newstring = decodeURIComponent(newstring);      
    let param_list = newstring.split("&");
    console.log(param_list);
    for(let i = 0; i < param_list.length; i++) {
        let fieldparam = param_list[i].split("=");
        if(fieldparam[0] === "search") {
            let tempelem = document.getElementById("search");
            tempelem.value = fieldparam[1];
        }
        let elem = document.getElementById("box_" + fieldparam[0] + "_" + fieldparam[1]);
        if(elem != null)
            elem.checked = true;
    }
};


function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + JSON.stringify(value) + expires + "; path=/";
}

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}


function addToTempList(elem) {
    type = elem.getAttribute("type");
    name = elem.getAttribute("name");
    console.log(elem);
    console.log(type);
    console.log(name);

    let tempList = [];
    if(getCookie("" + type) != "") {
        tempList = JSON.parse(getCookie("" + type));
    }
    tempList.push(name);
    createCookie(type, tempList, 60);
}

function remFromTempList(elem) {
    type = elem.getAttribute("type");
    name = elem.getAttribute("name");
    tempList = JSON.parse(getCookie(type));
    index = tempList.indexOf(name);
    if(index != -1) {
        tempList.splice(index, 1);
    }
    createCookie(type, tempList, 60);
} 
