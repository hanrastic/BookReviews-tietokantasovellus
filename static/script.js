
function checkForEmptyFields(form){

    if (! form.book_name.value) {
        alert("Please type in name for a book")
        return false
    }

    if (!checkForEmptyCategories(form)) {
        return false;
    }
    
    if (!checkForRating(form)) {
        return false;
    }

    return true
}

function checkForEmptyCategories() {
    
    var categories = document.getElementById('categories').children;  

    for (var i = 0; i < categories.length; i++) {
        if (categories[i].tagName == 'INPUT' && categories[i].type == 'checkbox') {
            if (categories[i].checked) {
                return true;
            }
        }
    }

    alert("Please select atleast one category");
    return false;

}

function checkForRating() {

    var stars = document.getElementById('rating').children;

    for (var i = 0; i < stars.length; i++) {
        if (stars[i].type === 'radio' && stars[i].checked) {
            return true; 
        }
    }
    alert("Please select rating");
    return false;

}