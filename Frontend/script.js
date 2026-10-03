const theme = document.querySelector('#theme-toggle');
const body = document.querySelector('body');
const chatHistory = document.querySelector(".chat-history");
const submit_btn = document.querySelector('#submit-btn');
const form = document.querySelector(".chat-input");
const input = document.querySelector("#text-input");
const header = document.querySelector('header');
const heading = document.querySelector('.heading');
const mic = document.querySelector(".mic");

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
        return data;

    } catch (error) {
        console.error(error);
        return {type:'error',message:"Sorry, Aura se response nahi aa raha."};
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
        if (res.type === 'open_url'){
            const url = res.url;
            const msg = res.message;
            addMessage(msg, "ai");
            window.open(url,"_blank");
        }
        else if(res.type === 'response'){
            const msg = res.message;
            addMessage(msg,'ai');
        }
        else if (res.type === 'error'){
            const msg = res.message;
            addMessage(`${res.type}:${msg}`);
        }
    }

});
//aura voice
const speak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);

    utterance.lang = "en-IN";
    utterance.rate = 1;
    utterance.pitch = 1;

    speechSynthesis.speak(utterance);
};

//mic feature

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = "en-US";
recognition.continuous = false;
recognition.interimResults = true;

mic.addEventListener("click", () => {
    console.log("mic is clicked");
    recognition.start();
});

const notify = document.createElement('div');
notify.classList.add('notify');
notify.innerText = 'Aura is listening say something';

recognition.onstart = () => {
    console.log("recording started");
    body.appendChild(notify)
};

recognition.onresult = async (e) => {
    
    const result = e.results[0][0];
    const transcript = e.results[0][0].transcript;
    
    if (e.results[0].isFinal) {
        const res = await askAura(transcript);

    
        // loader.remove();
        
        if (res) {
            
            if (res.type === 'open_url'){
                const url = res.url;
                const msg = res.message;
                speak(msg);
                window.open(url,"_blank");
            }

            else if(res.type === 'response'){
                const msg = res.message;
                speak(msg);
            }

            else if (res.type === 'error'){
                const msg = res.message;
                speak(`${res.type}:${msg}`)
            }
    }}
    
};

recognition.onerror = (e) => {
    console.log("Speech error:", e.error);
};

recognition.onend = () => {
    notify.remove()
    console.log("recording ended");
};