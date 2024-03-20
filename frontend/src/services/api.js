import axios from 'axios';

const API_URL = '/api';

// Auth Service
export function login(username, password) {
  return axios.post(`${API_URL}/auth/login`, {
    username,
    password
  });
}

/*export function authenticateAgent(username, password) {
  return axios.post(`${API_URL}/auth/agent`, {
    username,
    password
  });
}
*/

export function signupCustomer(customerName, email, phone, username, password) {
    return axios.post(`${API_URL}/auth/signup/customer`, {
      customer_name: customerName,
      email,
      phone,
      username,
      password
    });
}



export function signupAgent(agentName, username, password) {
    return axios.post(`${API_URL}/auth/signup/agent`, {
      agent_name: agentName,
      username,
      password
    });
}

// Customer Service
export function updateCustomerUsername(customerId, newUsername) {
    return axios.post(`${API_URL}/customer/${customerId}/update_username`, {
      username: newUsername
    });
}

// Message Service
export function sendMessage(customerId, agentId, content) {
    return axios.post(`${API_URL}/messages/send`, {
      customer_id: customerId,
      agent_id: agentId,
      content: content
    });
}
  
  
export function respondToMessage(agentId, messageId, content) {
    return axios.post(`${API_URL}/messages/respond`, {
      agent_id: agentId,
      message_id: messageId,
      content: content
    });
}
  
export function getMessages(customerId, agentId) {
    return axios.get(`${API_URL}/messages/customer/${customerId}/agent/${agentId}`);
}
  
export function deleteMessage(messageId) {
    return axios.delete(`${API_URL}/messages/${messageId}`);
}
  
export function updateMessage(messageId, content) {
    return axios.put(`${API_URL}/messages/${messageId}`, {
        content: content
    });
}