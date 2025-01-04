import {apiUrl, makeRequest} from '../js/utils.js';

document.getElementById('logout').addEventListener('click', function (event){
    event.preventDefault()

    const response = makeRequest({
        method: 'POST',
        url: '/api/auth/logout'
    })

    window.location.href = apiUrl + '/login'

})