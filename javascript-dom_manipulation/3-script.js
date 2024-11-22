let button = document.querySelector('#toggle_header');
button.addEventListener('click', function() {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});

