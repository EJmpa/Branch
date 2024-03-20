import axios from 'axios';

export const login = async (username, password) => {
  try {
    const response = await axios.post('/auth/login', { username, password });
    if (response.status === 200) {
      localStorage.setItem('user', JSON.stringify(response.data));
      return response.data;
    } else {
      throw new Error('Invalid username or password');
    }
  } catch (error) {
    console.error(error);
    throw error;
  }
}

export const logout = () => {
  localStorage.removeItem('user');
}