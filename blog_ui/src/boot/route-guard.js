import { boot } from "quasar/wrappers"
import { loginAuth, useLoginRegiStore } from "stores/login-regi"

export default boot(({ router }) => {
  const loginStore = useLoginRegiStore()
  router.beforeEach((to, from, next) => {
    if (to.name !== "EditCreate") {
      next()
    } else {
      if (loginStore.isLogin && (loginStore.isSuperuser || loginStore.isStaff)) {
        loginAuth().then((resp) => {
          if (resp) {
            next()
          } else {
            next({ name: "ArticleList" })
          }
        })
      } else {
        next({ name: "ArticleList" })
      }
    }
  })
})
