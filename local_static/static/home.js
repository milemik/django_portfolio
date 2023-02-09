function checkNewMessages() {
    function createBaseUrl() {
        let urlObj = new URL(document.URL);
        return `${urlObj.protocol}//${urlObj.host}`;
    }

    let baseUrl = createBaseUrl();

    const url =`${baseUrl}/api/num-unread/`;
    const docTag = document.getElementById("newMessages")

    fetch(url, {
        method: "GET",
        headers: {'Content-Type': 'application/json'},
        mode: "same-origin"
    })
        .then(
            response => {
                let result = response.json();
                let status_code = response.status;
                if (status_code !== 200) {
                } else {
                    result.then(data => {
                        if ( data.unread > 0) {
                            docTag.innerHTML = "inbox " + data.unread;
                        } else {
                            docTag.innerHTML = "inbox";
                        }
                    });
                }
            }
        );
}

checkNewMessages()
