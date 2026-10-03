const theme = document.querySelector('#theme-toggle');
const body = document.querySelector('body');
const chatHistory = document.querySelector(".chat-history");
const submit_btn = document.querySelector('#submit-btn');
const form = document.querySelector(".chat-input");
const input = document.querySelector("#text-input");
const header = document.querySelector('header');
const heading = document.querySelector('.heading')

// change theme
theme.addEventListener('click',() => {
    let theme1 = body.getAttribute('class');
    
    if (theme1 === 'dark'){
        body.classList.remove('dark');
        body.classList.add('light');
        theme.innerText = '🌙'
        theme.style.backgroundColor = 'black'
    }
    else{
        body.classList.remove('light');
        body.classList.add('dark');
        theme.innerText = '☀️'
        theme.style.backgroundColor = 'white'
    }
})






//asking  aura
const askAura = async (prompt) => {
    try {
        const response = await fetch("http://127.0.0.1:8000/ask_aura", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prompt: prompt
            })
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        
        const data = await response.json();
        
        console.log("API DATA:", data);
        console.log("RESPONSE:", data.response);
        return data.message;

    } catch (error) {
        console.error(error);
        return "Sorry, Aura se response nahi aa raha.";
    }
};

//chat history

function addMessage(message, type) {
    const msg = document.createElement("div");

    msg.classList.add("message", type);
    msg.innerText = message;

    chatHistory.appendChild(msg);
}

function addLoader() {
    const loader = document.createElement("div");

    loader.classList.add("message", "ai", "loader");

    loader.innerHTML = `
        <span></span>
        <span></span>
        <span></span>
    `;

    chatHistory.appendChild(loader);

    chatHistory.scrollTop = chatHistory.scrollHeight;

    return loader;
}



form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const text = input.value.trim();
    input.value = "";
    
    if (!text) return;

    addMessage(text, "user");
    
    const loader = addLoader();
    
    const res = await askAura(text);

    loader.remove();

    if (res) {
        addMessage(res, "ai");
    }

});
