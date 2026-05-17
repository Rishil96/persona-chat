import { useState } from "react";
import { sendMessage } from "../services/Api";

function MessageInput({ conversationID, onMessageSent }) {
    
    const [message, setMessage] = useState("")
    const [model, setModel] = useState("gpt-4o")

    async function handleSend() {
        const data = await sendMessage(conversationID, message, model);
        onMessageSent();
        setMessage("");
    }

    return (
        <div>
            <label htmlFor="userMessage"></label>
            <input type="text" name="userMessage" value={message} onChange={e => setMessage(e.target.value)}/>
            <label htmlFor="models"></label>
            <select name="models" id="models" value={model} onChange={e => setModel(e.target.value)}>
                <option value="gpt-4o">gpt-4o</option>
                <option value="gpt-4o-mini">gpt-4o-mini</option>
            </select>
            <button onClick={handleSend}>Send</button>
        </div>
    )
}

export default MessageInput