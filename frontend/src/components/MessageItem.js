import React from 'react';

const MessageItem = ({ message, onClick }) => (
  <div onClick={onClick}>
    <h2>{message.title}</h2>
    <p>{message.content}</p>
  </div>
);

export default MessageItem;