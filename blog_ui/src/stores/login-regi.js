import { api } from "boot/axios"
import { defineStore } from "pinia"

export async function loginAuth() {
  let hasLogin = false
  const expiredTime = Number(localStorage.getItem("pa.token.expire"))
  const current = new Date().getTime()
  const refreshToken = localStorage.getItem("pa.token.refresh")
  // 初始 token 未过期
  if (expiredTime > current) {
    hasLogin = true
  } else if (refreshToken !== null) {
    try {
      let response = await api.post("token/refresh/", { refresh: refreshToken })
      localStorage.setItem("pa.token", response.data.access)
      localStorage.setItem("pa.token.expire", response.data.expire)
      localStorage.setItem("pa.is_login", true)
      hasLogin = true
    } catch (err) {
      localStorage.clear()
      hasLogin = false
      localStorage.setItem("navTab", "home")
    }
  } else {
    localStorage.clear()
    hasLogin = false
    localStorage.setItem("navTab", "home")
  }
  return hasLogin
}

export const useLoginRegiStore = defineStore("LoginRegi", {
  state: () => ({
    // dialog
    isShowLogin: false,

    // user info
    uname: localStorage.getItem("pa.username") || "",
    avatar: "http://127.0.0.1:8000" + localStorage.getItem("pa.avatar") || "",
    // token
    token: localStorage.getItem("pa.token") || "",
    tokenRefresh: localStorage.getItem("pa.token.refresh") || "",
    tokenExpire: Number(localStorage.getItem("pa.token.expire")) || 0,
    // is staff
    isStaff: JSON.parse(localStorage.getItem("pa.is_staff")) || false,
    // is superuser
    isSuperuser: JSON.parse(localStorage.getItem("pa.is_superuser")) || false,
    // is login
    isLogin: JSON.parse(localStorage.getItem("pa.is_login")) || false,
  }),

  getters: {
    getToken: (state) => {
      return state.token
    },
  },

  actions: {
    logout() {
      localStorage.clear()
      this.isLogin = false
      localStorage.setItem("navTab", "home")
    },
  },
})
