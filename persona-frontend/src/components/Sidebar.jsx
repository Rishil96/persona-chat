import { useState, useEffect } from "react"
import { getConversations } from "../services/Api.js"

function Sidebar() {
    // State variables to get conversations from backend
    const [conversations, setConversations] = useState([])
    
    useEffect(() => {
        async function fetchConversations() {
            const conversationsList = await getConversations();
            setConversations(conversationsList);
        }
        fetchConversations();
    }, [])
    return (
        <div className="h-full w-full text-gray-100 bg-gray-900 p-4">
            <div>
                <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg w-full">
                    New Chat
                </button>
            </div>
            <div className="mt-4">
                <ul>
                    {
                        conversations.map(conv => (
                            <li key={conv.conversation_id} className="px-3 py-2 rounded-lg hover:bg-gray-700 cursor-pointer">{conv.title}</li>
                        ))
                    }
                </ul>
            </div>
        </div>
    )
}

export default Sidebar
