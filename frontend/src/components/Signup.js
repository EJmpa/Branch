import React, { useState } from 'react';
import axios from 'axios';

const Signup = ({ onSignup }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [role, setRole] = useState('customer');

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!username || !password || !name || (role === 'customer' && (!email || !phone))) return;

    const url = `/auth/signup/${role}`;
    const data = role === 'customer' ? { customer_name: name, email, phone, username, password } : { agent_name: name, username, password };

    try {
      const response = await axios.post(url, data);
      onSignup(response.data);
      setUsername('');
      setPassword('');
      setName('');
      setEmail('');
      setPhone('');
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <select value={role} onChange={e => setRole(e.target.value)}>
        <option value="customer">Customer</option>
        <option value="agent">Agent</option>
      </select>
      <input type="text" value={name} onChange={e => setName(e.target.value)} placeholder="Name" />
      <input type="text" value={username} onChange={e => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
      {role === 'customer' && (
        <>
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
          <input type="text" value={phone} onChange={e => setPhone(e.target.value)} placeholder="Phone" />
        </>
      )}
      <button type="submit">Sign Up</button>
    </form>
  );
}

export default Signup;