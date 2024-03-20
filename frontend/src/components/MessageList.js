import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MessageItem from './MessageItem';

const MessageList = ({ onMessageSelect }) => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const fetchMessages = async () => {
      try {
        const response = await axios.get('/messages'); // replace with your actual backend route
        setMessages(response.data.messages);
      } catch (error) {
        console.error(error);
      }
    }

    fetchMessages();
  }, []);

  return (
    <div>
      {messages.map(message => (
        <MessageItem key={message.id} message={message} onClick={() => onMessageSelect(message)} />
      ))}
    </div>
  );
}

export default MessageList;