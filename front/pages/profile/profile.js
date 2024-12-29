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
        document.getElementById('name').innerHTML += response.user.nickname;
         const categoriesContainer = document.getElementById('categories');
         categoriesContainer.innerHTML = '';
         response.user.categories.forEach(category => {
                const categoryElement = document.createElement('div');
                categoryElement.innerHTML = `
                <h3>Название:  ${category.name}</h3>
                <p>Описание:  ${category.description}</p>
                <p>Дата создания:  ${formatDateTime(category.created_at)}</p>
                <p>Дата обновления:  ${formatDateTime(category.updated_at)}</p>`;
                categoriesContainer.appendChild(categoryElement);
            });
    }
}
