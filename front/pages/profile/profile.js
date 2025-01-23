import {apiUrl, makeRequest} from '/front/js/utils.js';
import {formatDateTime} from '/front/js/timefunc.js'

document.addEventListener("DOMContentLoaded", function () {
    getMe();
})


async function getMe() {
    const response = await makeRequest({
        method: 'GET',
        url: '/api/users/me',
    })
    if (response.user) {
        getCategories(response.user.categories)
        getUserInfo(response.user)
    }
}

function getCategories(categories) {
    const categoriesContainer = document.getElementById('categories');
    categoriesContainer.innerHTML = '';
    categories.forEach(category => {
        const categoryName = document.createElement('li')
        const nameLink = document.createElement('a')
        categoryName.className = 'category-name'
        nameLink.textContent = category.name
        nameLink.title = 'Подробнее'
        nameLink.href = apiUrl + '/categories/' + category.id
        categoryName.appendChild(nameLink)
        categoriesContainer.appendChild(categoryName);
    });
}

function getUserInfo(user) {
    document.getElementById('name').innerHTML = 'Привет, ' + user.login;
    const userInfo = document.getElementById('user-info')
    const nickname = document.createElement('li')
    nickname.textContent = 'Псевдоним: ' + user.nickname
    userInfo.appendChild(nickname)
    const email = document.createElement('li')
    email.textContent = 'Почта: ' + user.email
    userInfo.appendChild(email)
}