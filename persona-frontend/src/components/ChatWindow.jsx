import { useState, useEffect } from "react"
import { getConversation } from "../services/Api";

function ChatWindow({ conversationID }) {

    const [conversation, setConversation] = useState([]);

    useEffect(() => {
        async function fetchConversation() {
            if (!conversationID) return ;
            const conversationDetails = await getConversation(conversationID);
            setConversation(conversationDetails.messages)
        }
        fetchConversation();
    }, [conversationID])

    return (
        <div className="h-full overflow-y-auto">
            {
                conversation.map(message => (
                    
                    <div key={message.id} className={`p-4 flex ${message.role === 'user' ? 'justify-end': 'justify-start'}`}>
                        <div className={`px-4 py-2 rounded-lg max-w-[70%] ${message.role === 'user' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-800 border border-gray-200'}`}>{ message.content }</div>
                    </div>
                ))
            }
        </div>
    )
}

export default ChatWindow
