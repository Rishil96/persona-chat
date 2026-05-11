import './App.css'
import Sidebar from './components/Sidebar.jsx'
import { useState } from 'react'

function App() {
	const [conversationID, setConversationID] = useState(null)
	return (
		<div className="flex h-screen">
			<div className="w-64 bg-gray-900">
				<Sidebar onSelectConversation={setConversationID} />
			</div>
			<div className="flex-1 bg-gray-50">
				Chat Window Placeholder
			</div>
		</div>
	)
}

export default App
