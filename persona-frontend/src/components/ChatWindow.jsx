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
        <div>
            {
                conversation.map(message => (
                    <div key={message.id}>{ message.content }</div>
                ))
            }
        </div>
    )
}

export default ChatWindow
