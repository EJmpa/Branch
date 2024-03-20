import React, { useState, useEffect } from 'react';
import MessageForm from './MessageForm';
import MessageList from './MessageList';
import RespondForm from './RespondForm';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [selectedMessage, setSelectedMessage] = useState(null);

  // Fetch messages from the server when the component mounts
  useEffect(() => {
    fetch('/api/messages')
      .then(response => response.json())
      .then(data => setMessages(data))
      .catch(error => console.error('Error:', error));
  }, []);

  const addMessage = (message) => {
    setMessages([...messages, message]);
  }

  return (
    <div>
      <h2>Chat</h2>
      <MessageList messages={messages} onMessageSelect={setSelectedMessage} />
      {selectedMessage && <RespondForm message={selectedMessage} />}
      <MessageForm addMessage={addMessage} />
    </div>
  );
}

export default Chat;