function sidebar_button(){
    var sidebar = document.querySelector('.sidebar');
    var button = document.querySelector('button');
    // var text = link.querySelector('span');

    if (sidebar.classList.contains('expanded')) {
        // Reset CSS properties
        sidebar.style.width = '5.5vh';
        button.style.transform = 'rotate(90deg)';
        sidebar.classList.remove('expanded');
    } else {
        // Apply new CSS properties
        sidebar.style.width = '20vh';
        button.style.transform = 'rotate(0deg)';
        sidebar.classList.add('expanded');
    }
}

function showComment(){
    comForm = document.getElementById('commentForm');
    if (comForm.style.display === "none")
        comForm.style.display = "block";
    else
        comForm.style.display = "none";
}

function EditThread(){
    editForm = document.getElementById('EditForm');
    if (editForm.style.display === "none")
        editForm.style.display = "block";
    else
        editForm.style.display = "none";
}