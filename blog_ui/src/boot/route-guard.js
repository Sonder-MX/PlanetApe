import { boot } from 'quasar/wrappers'
import { useLoginRegiStore } from 'stores/login-regi'

export default boot(({ router }) => {
  const loginStore = useLoginRegiStore()
  router.beforeEach((to, from, next) => {
    if (to.name !== 'EditCreate') {
      next()
    } else {
      if (loginStore.isLogin && (loginStore.isSuperuser || loginStore.isStaff)) {
        if (loginStore.tokenIsExpired) {
          loginStore.refreshToken()
        }
        if (loginStore.isLogin) {
          next()
        } else {
          next({ name: 'ArticleList' })
        }
      } else {
        next({ name: 'ArticleList' })
      }
    }
  })
})
