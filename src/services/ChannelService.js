import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json'
  }
})

export default {
  getChannels() {
    return apiClient.get('/channels')
  },
  getMessages(channel) {
    return apiClient.get('/' + channel)
  },
  postUsername(usr) {
    return apiClient.post('/login', { username: usr })
  }
}
