function Sidebar() {
    return (
        <div className="h-full w-full text-gray-100 bg-gray-900 p-4">
            <div>
                <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg w-full">
                    New Chat
                </button>
            </div>
            <div className="mt-4">
                <ul>
                    <li className="px-3 py-2 rounded-lg hover:bg-gray-700 cursor-pointer">Conversation 1</li>
                    <li className="px-3 py-2 rounded-lg hover:bg-gray-700 cursor-pointer">Conversation 2</li>
                    <li className="px-3 py-2 rounded-lg hover:bg-gray-700 cursor-pointer">Conversation 3</li>
                </ul>
            </div>
        </div>
    )
}

export default Sidebar