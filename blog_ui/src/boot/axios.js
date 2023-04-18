import axios from 'axios'
// import { boot } from "quasar/wrappers"

export const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  timeout: 3000,
})

// // 在请求发起前拦截每个请求，判断token的有效时间是否已经过期，若已过期，则将请求挂起，先刷新token后再继续请求
// api.interceptors.request.use((config) => {
//   const token = localStorage.getItem('access.myblog')
//   if (token) {
//     config.headers.Authorization = `Bearer ${token}`
//   }
//   return config
// })

// // 在响应拦截器中判断token是否过期，若过期，则刷新token
// api.interceptors.response.use((response) => {
//   return response
// })
