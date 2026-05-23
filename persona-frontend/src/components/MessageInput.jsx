import { useState } from "react";
import { sendMessage, createConversation } from "../services/Api";

function MessageInput({ conversationID, onMessageSent, setConversationID }) {
    
    const [message, setMessage] = useState("")
    const [model, setModel] = useState("gpt-4o")

    async function handleSend() {
        let activeConversationID = conversationID;
        if (!conversationID) {
            activeConversationID = await createConversation();
            setConversationID(activeConversationID);
        }
        await sendMessage(activeConversationID, message, model);
        onMessageSent(activeConversationID);
        setMessage("");
    }

    return (
        <div className="flex items-center gap-2 p-4 bg-white border-t border-gray-300">
            <label htmlFor="userMessage"></label>
            <input className="flex-1 px-3 py-2 rounded-lg border border-gray-300 outline-none" type="text" name="userMessage" value={message} onChange={e => setMessage(e.target.value)}/>
            <label htmlFor="models"></label>
            <select className="px-3 py-2 rounded-lg border border-gray-300 bg-white" name="models" id="models" value={model} onChange={e => setModel(e.target.value)}>
                <option value="gpt-4o">gpt-4o</option>
                <option value="gpt-4o-mini">gpt-4o-mini</option>
            </select>
            <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 font-medium cursor-pointer" onClick={handleSend}>Send</button>
        </div>
    )
}

export default MessageInput