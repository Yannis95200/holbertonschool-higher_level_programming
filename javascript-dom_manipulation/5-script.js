let button = document.querySelector('#update_header');
button.addEventListener('click', function() {
    let header = document.querySelector('header');
    header.textContent = 'New Header!!!';
});
