const docTag = document.getElementById("newMessages");

function checkNewMessages() {
    function createBaseUrl() {
        let urlObj = new URL(document.URL);
        return `${urlObj.protocol}//${urlObj.host}`;
    }

    let baseUrl = createBaseUrl();

    const url =`${baseUrl}/api/num-unread/`;


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
                    // return
                } else {
                    result.then(data => {
                        console.log(data.unread)
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

if (docTag !== null) {
    checkNewMessages();
}

