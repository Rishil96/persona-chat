import './App.css'
import Sidebar from './components/Sidebar.jsx'
import ChatWindow from './components/ChatWindow.jsx'
import { useState } from 'react'

function App() {
	const [conversationID, setConversationID] = useState(null)
	return (
		<div className="flex h-screen">
			<div className="w-64 bg-gray-900">
				<Sidebar onSelectConversation={setConversationID} />
			</div>
			<div className="flex-1 bg-gray-200 overflow-hidden">
				<ChatWindow conversationID={conversationID}/>
			</div>
		</div>
	)
}

export default App
