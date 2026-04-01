import axios from 'axios';

let token_value = $state('')

export const token = {
     get value() {
          return token_value
     },
     set value(new_val) {
          token_value = new_val
     }
}

export function injectAuthToken() {
     const instance = axios.create({
          baseURL: 'http://127.0.0.1:8000'
     })

     instance.interceptors.request.use((config) => {
          config.headers.set('Authorization', `Bearer ${token_value}`)
          return config
     })
     return instance
}