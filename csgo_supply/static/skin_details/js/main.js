

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


function updateUI() {
    let newstring = urlSearchParams.toString();
    newstring = newstring.replace(/\+/g, '%20'); 
    newstring = decodeURIComponent(newstring);      
    let param_list = newstring.split("&");
    for(let i = 0; i < param_list.length; i++) {
        let param_name = param_list[i].split("=")[1];
        let elem = document.getElementById("box_" + param_name);
        elem.checked = true;
    }
    console.log("done updating")
}
