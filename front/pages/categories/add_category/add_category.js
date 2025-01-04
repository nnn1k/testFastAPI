import {apiUrl, makeRequest} from '../../../js/utils.js';

async function add_category() {
    const name = document.getElementById('name').value
    const description = document.getElementById('description').value
    const response = await makeRequest({
        method: 'POST',
        url: '/api/categories/',
        data: {
            name,
            description
        }
    })
    if (response){
        window.location.href = apiUrl + '/profile'
    }
}
window.add_category = add_category