import {apiUrl, makeRequest} from '../../../js/utils.js';

async function update_user() {
    const nickname = document.getElementById('nickname').value
    const email = document.getElementById('email').value
    const response = await makeRequest({
        method: 'PUT',
        url: '/api/users/me',
        data: {
            nickname: nickname ? nickname : null,
            email: email ? email : null,
        }
    })
    if (response.user){
        window.location.href = apiUrl + '/profile'
    }
}
window.update_user = update_user