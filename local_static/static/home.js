function checkNewMessages() {
    const url = "http://" + imDomain + "/api/num-unread/" + userId + "/";
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
                    // console.log("BAD RESPONSE")
                    // console.log(result)
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
