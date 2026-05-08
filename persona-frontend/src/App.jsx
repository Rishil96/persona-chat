import './App.css'
import Sidebar from './components/Sidebar.jsx'

function App() {

  return (
    <>
      <div className="flex h-screen">
        <div className="w-64 bg-gray-900">
          <Sidebar/>
        </div>
        <div className="flex-1 bg-gray-50">
          Chat Window Placeholder
        </div>
      </div>
    </>
  )
}

export default App
