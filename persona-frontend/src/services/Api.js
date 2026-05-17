export async function getConversations() {
    const response = await fetch("http://localhost:8000/conversations/");
    const data = await response.json();
    return data;
}

export async function getConversation(conversationID) {
    const response = await fetch(`http://localhost:8000/conversations/${conversationID}`);
    const data = await response.json();
    return data;
}

export async function sendMessage(conversationID, userMessage, modelName) {
    const response = await fetch(
        `http://localhost:8000/conversations/${conversationID}/messages`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(
                {
                    "user_message": userMessage,
                    "model_name": modelName
                }
            )
        }
    )
    const data = await response.json();
    return data;
}
