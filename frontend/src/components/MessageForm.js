import React, { useState } from 'react';

const MessageForm = ({ addMessage }) => {
  const [message, setMessage] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!message) return;
    addMessage(message);
    setMessage('');
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={message}
        onChange={e => setMessage(e.target.value)}
        placeholder="Type a message"
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default MessageForm;