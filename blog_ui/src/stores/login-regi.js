import { defineStore } from 'pinia'
import { api } from 'boot/axios'
// import { nfy } from 'src/utils/u-notify'

export const useLoginRegiStore = defineStore('LoginRegi', {
  state: () => ({
    // dialog
    isShowLogin: false,

    // user info
    uname: localStorage.getItem('pa.username') || '',
    avatar: 'http://127.0.0.1:8000' + localStorage.getItem('pa.avatar') || '',
    // token
    token: localStorage.getItem('pa.token') || '',
    tokenRefresh: localStorage.getItem('pa.token.refresh') || '',
    tokenExpire: Number(localStorage.getItem('pa.token.expire')) || 0,
    // is staff
    isStaff: JSON.parse(localStorage.getItem('pa.is_staff')) || false,
    // is superuser
    isSuperuser: JSON.parse(localStorage.getItem('pa.is_superuser')) || false,
    // is login
    isLogin: JSON.parse(localStorage.getItem('pa.is_login')) || false,
  }),

  getters: {
    tokenIsExpired: (state) => {
      const current = new Date().getTime() / 1000
      return state.tokenExpire < current
    },
  },

  actions: {
    refreshToken() {
      if (this.tokenRefresh !== '') {
        api
          .post('token/refresh/', { refresh: this.tokenRefresh })
          .then(({ data }) => {
            localStorage.setItem('pa.token', data.access)
            localStorage.setItem('pa.token.expire', data.expire)
            this.token = data.access
            this.tokenExpire = data.expire
            this.isLogin = true
          })
          .catch(() => {
            localStorage.clear()
            this.isLogin = false
          })
      }
    },
    logout() {
      localStorage.clear()
      this.isLogin = false
    },
  },
})
