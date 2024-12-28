
sid = document.getElementById('ctoken').innerHTML

// подключения к вебсокету, sid - идентификатор сокета, он хранится в самом HTML файле с атрибутом hidden
const sSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/tgcon/'
    + sid
    + '/'
);



sSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        username = data.message.username
        password = data.message.token
        form = document.getElementById("tgauth_form")
        form.querySelector(`input[name="username"]`).setAttribute('value', username)
        form.querySelector(`input[name="password"]`).setAttribute('value', password)
        form.submit()
        // при получении сообщения от вебсокета скрипт заполняет форму,
        // которая скрыта в HTML документе и вызывает функцию submit(), отправляя данные для авторизации.
};

sSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
