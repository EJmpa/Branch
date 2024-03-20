import React from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import './assets/styles/App.css';
import Chat from './components/Chat';
import MessageForm from './components/MessageForm';
import Login from './components/Login';
import Signup from './components/Signup';

function App() {
  const navigate = useNavigate();

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/chat" element={<Chat />} />
          <Route path="/message" element={<MessageForm />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/" element={<Chat />} />
        </Routes>
        {navigate('/')}
      </div>
    </Router>
  );
}

export default App;