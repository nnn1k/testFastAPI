import {apiUrl, makeRequest} from '../../../js/utils.js';

async function auth() {
    let login = document.getElementById("login").value
    let password = document.getElementById("password").value
    const response = await makeRequest({
        method: 'POST',
        url: '/api/auth/login',
        data: {
            login,
            password
        }
    })
    console.log('response:', response)
    if (response.user) {
        window.location.href = apiUrl + '/profile'
    }
}
window.auth = auth;