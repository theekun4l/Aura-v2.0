const askAura = async (prompt) => {
    const response = await fetch("http://127.0.0.1:8000/ask_aura", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            prompt: prompt
        })
    });

    const data = await response.json();
    return data;
};

const test = async () => {
    const result = await askAura("what is python?");
    console.log(result);
};

test();