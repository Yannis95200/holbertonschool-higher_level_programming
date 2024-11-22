let button = document.querySelector('#add_item');
button.addEventListener('click', function() {
    let list = document.querySelector('.my_list');
    let newElement = document.createElement('li');
    newElement.textContent = 'Item';
    list.appendChild(newElement);
});
