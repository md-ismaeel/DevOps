const element = document.querySelector(".render");

async function fetchData() {
    try {
        console.log("Fetching data...");

        const res = await fetch("http://frontend-host:3000/get-data");
        console.log("Response:", res);

        const result = await res.json();
        console.log("Result:", result);

        const { success, message, data } = result;
        console.log(success, message, data.data);

        if (!Array.isArray(data.data)) {
            element.textContent = "Invalid data format";
            return;
        }

        const messageElement = document.createElement("h1");
        messageElement.textContent = message;
        element.appendChild(messageElement);

        const ele = document.createElement("div");

        data.data.forEach(item => {
            const p = document.createElement("p");
            p.innerHTML = item.name ?? "No name";
            ele.appendChild(p);
        });

        element.appendChild(ele);

    } catch (error) {
        console.error("Error:", error);
        const p = document.createElement("p");
        p.textContent = "Something went wrong";
        element.appendChild(p);
    }
}

fetchData();
