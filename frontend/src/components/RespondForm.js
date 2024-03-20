import React, { useState } from 'react';
import axios from 'axios';

const RespondForm = ({ onRespond }) => {
  const [content, setContent] = useState('');
  const [agentId, setAgentId] = useState('');
  const [messageId, setMessageId] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!content || !agentId || !messageId) return;

    const url = '/messages/respond';
    const data = { agent_id: agentId, message_id: messageId, content };

    try {
      const response = await axios.post(url, data);
      onRespond(response.data);
      setContent('');
      setAgentId('');
      setMessageId('');
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={agentId}
        onChange={e => setAgentId(e.target.value)}
        placeholder="Agent ID"
      />
      <input
        type="text"
        value={messageId}
        onChange={e => setMessageId(e.target.value)}
        placeholder="Message ID"
      />
      <input
        type="text"
        value={content}
        onChange={e => setContent(e.target.value)}
        placeholder="Type a response"
      />
      <button type="submit">Send</button>
    </form>
  );
}

export default RespondForm;