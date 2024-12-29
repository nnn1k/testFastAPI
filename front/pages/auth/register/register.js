import {apiUrl, makeRequest} from '../../../js/utils.js';

async function register() {
    let nickname = document.getElementById("nickname").value
    let email = document.getElementById("email").value
    let login = document.getElementById("login").value
    let password = document.getElementById("password").value

    const response = await makeRequest({
        method: 'POST',
        url: '/api/auth/register',
        data: {
            nickname,
            email,
            login,
            password
        }
    });

    console.log('response:', response);
    if (response.user) {
        window.location.href = apiUrl + '/profile';
    }
}

window.register = register;