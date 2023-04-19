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
    console.log("token没有过期")
  } else if (refreshToken !== null) {
    try {
      let response = await api.post("token/refresh/", { refresh: refreshToken })
      localStorage.setItem("pa.token", response.data.access)
      localStorage.setItem("pa.token.expire", response.data.expire)
      localStorage.setItem("pa.is_login", true)
      hasLogin = true
      console.log("token过期， 刷新成功")
    } catch (err) {
      localStorage.clear()
      hasLogin = false
      console.log("token过期， 刷新失败")
    }
  } else {
    localStorage.clear()
    hasLogin = false
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
    refreshToken() {
      if (this.tokenRefresh !== "") {
        api
          .post("token/refresh/", { refresh: this.tokenRefresh })
          .then(({ data }) => {
            localStorage.setItem("pa.token", data.access)
            localStorage.setItem("pa.token.expire", data.expire)
            // this.token = data.access
            // this.tokenExpire = data.expire
            // this.isLogin = true
            localStorage.setItem("pa.is_login", true)
            console.log("refresh token success")
          })
          .catch(() => {
            console.log("refresh token failed")
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
