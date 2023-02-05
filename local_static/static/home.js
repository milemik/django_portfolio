function checkNewMessages() {
    let http_req = "https://";
    if (imDomain.includes("localhost")) {
        http_req = "http://";
    }
    const url = http_req + imDomain + "/api/num-unread/" + userId + "/";
    const docTag = document.getElementById("newMessages")

    fetch(url, {
        method: "GET",
        headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        mode: "cors"
    })
        .then(
            response => {
                let result = response.json()
                let status_code = response.status;
                if (status_code !== 200) {
                } else {
                    result.then(data => {
                        if ( data.unread > 0) {
                            docTag.innerHTML = "inbox " + data.unread;
                        } else {
                            docTag.innerHTML = "inbox";
                        }
                    })
                }
            }
        )
}

checkNewMessages()
