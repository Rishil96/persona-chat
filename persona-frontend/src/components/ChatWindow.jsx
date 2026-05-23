import { useState, useEffect } from "react"
import { getConversation } from "../services/Api";
import MessageInput from "../components/MessageInput"

function ChatWindow({ conversationID, setConversationID }) {

    const [conversation, setConversation] = useState([]);

    useEffect(() => {
        async function fetchConversation() {
            if (!conversationID) {
                setConversation([]);
                return ;
            }
            const conversationDetails = await getConversation(conversationID);
            setConversation(conversationDetails.messages)
        }
        fetchConversation();
    }, [conversationID])

    async function handleMessageSent(activeConversationID) {
        const id = activeConversationID || conversationID
        const conversationDetails = await getConversation(id);
        setConversation(conversationDetails.messages)
    }

    if (!conversationID) {
        return (
            <div className="flex flex-col h-full">
                <div className="flex-1 flex items-center justify-center text-gray-400">
                    <p className="text-xl">
                        Select a conversation or start a new one!
                    </p>
                </div>
                <div>
                    <MessageInput conversationID={null} onMessageSent={handleMessageSent} setConversationID={setConversationID}/>
                </div>
            </div>
        )
    }

    return (
        <div className="flex flex-col h-full">
            <div className="flex-1 overflow-y-auto">
                {
                    conversation.map(message => (
                        
                        <div key={message.id} className={`p-4 flex ${message.role === 'user' ? 'justify-end': 'justify-start'}`}>
                            <div className={`px-4 py-2 rounded-lg max-w-[70%] ${message.role === 'user' ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-800 border border-gray-200'}`}>{ message.content }</div>
                        </div>
                    ))
                }
            </div>
            <div>
                <MessageInput conversationID={conversationID} onMessageSent={handleMessageSent} setConversationID={setConversationID}/>
            </div>
        </div>
    )
}

export default ChatWindow
