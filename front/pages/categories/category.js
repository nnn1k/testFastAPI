import {apiUrl, makeRequest} from '/front/js/utils.js';
import {formatDateTime} from '/front/js/timefunc.js'

document.addEventListener("DOMContentLoaded", function () {
    getCategory();
})


async function getCategory() {
    const category_id = location.pathname.split('/')[2]
    console.log(category_id)
    const response = await makeRequest({
        method: 'GET',
        url: `/api/categories/${category_id}`,
    })
    console.log(response)
    if (response.category) {
        printCategory(response.category)
    }
}

function printCategory(category) {
    const categoryContainer = document.getElementById('category');
    categoryContainer.innerHTML = '';
    const name = document.createElement('li')
    name.textContent = 'Название: ' + category.name
    categoryContainer.appendChild(name)
    const description = document.createElement('li')
    description.textContent = 'Описание: ' + category.description
    categoryContainer.appendChild(description)
    const created_at = document.createElement('li')
    created_at.textContent = 'Дата создания: ' + formatDateTime(category.created_at)
    categoryContainer.appendChild(created_at)
    const updated_at = document.createElement('li')
    updated_at.textContent =  'Дата обновления: ' + formatDateTime(category.updated_at)
    categoryContainer.appendChild(updated_at)
}


