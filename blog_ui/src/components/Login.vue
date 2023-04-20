<template>
  <div class="q-gutter-sm">
    <q-dialog
      v-model="loginRegiStore.isShowLogin"
      persistent
      transition-show="slide-down"
      transition-hide="slide-up">
      <q-card style="width: 700px; max-width: 80vw" class="bg-white">
        <q-card-actions align="right">
          <span class="text-h5" style="position: absolute; left: 10px">
            <q-icon name="bi-rocket-takeoff-fill" color="info" />
            ~登录猿星球获取最佳体验
          </span>
          <q-btn round flat icon="bi-x" v-close-popup />
        </q-card-actions>

        <q-separator />

        <q-tab-panels v-model="tabName" animated>
          <!-- 登录 -->
          <q-tab-panel name="sign-in">
            <q-card class="my-card" flat>
              <q-card-section horizontal>
                <q-card-section class="col-7">
                  <div class="text-center text-h5">登 录</div>
                  <div class="q-mt-xl">
                    <q-form class="q-gutter-md" ref="inForm" @submit="loginSubmit">
                      <q-input
                        filled
                        type="email"
                        v-model="email"
                        label="邮箱"
                        lazy-rules
                        :rules="[(val) => !!val || '请输入邮箱地址']" />

                      <q-input
                        v-model="upwd1"
                        filled
                        label="密码"
                        :type="isPwd ? 'password' : 'text'"
                        lazy-rules
                        :rules="[
                          (val) => (val.length >= 8 && val.length <= 20) || '密码长度为8~20位',
                        ]">
                        <template v-slot:append v-if="upwd1">
                          <q-icon
                            :name="isPwd ? 'bi-eye' : 'bi-eye-slash'"
                            class="cursor-pointer"
                            @click="isPwd = !isPwd" />
                        </template>
                      </q-input>

                      <div class="text-center q-mt-xl">
                        <q-btn type="submit" color="primary" style="padding: 0 50px">
                          <q-icon name="bi-send" size="sm" left />
                          登 录
                        </q-btn>
                      </div>
                    </q-form>
                  </div>
                </q-card-section>

                <q-separator vertical />

                <q-card-section style="width: 100%">
                  <div class="q-ma-lg">
                    <p class="text-h6 text-center">欢迎使用 猿星球</p>
                    <q-img src="/icons/logo.png"></q-img>
                  </div>
                  <q-card-actions class="login-change-btn">
                    <q-btn
                      style="position: absolute; right: 28px"
                      outline
                      color="cyan-8"
                      size="sm"
                      @click="tabName = 'sign-up'">
                      还没有账号？去注册
                    </q-btn>
                  </q-card-actions>
                </q-card-section>
              </q-card-section>
            </q-card>
          </q-tab-panel>

          <!-- 注册 -->
          <q-tab-panel name="sign-up">
            <q-card class="my-card" flat>
              <q-card-section horizontal>
                <q-card-section style="width: 100%">
                  <div class="q-ma-lg">
                    <p class="text-h6 text-center">欢迎使用 猿星球</p>
                    <q-img src="/icons/logo.png"></q-img>
                  </div>
                  <q-card-actions class="login-change-btn">
                    <q-btn
                      style="position: absolute; left: 28px"
                      outline
                      color="cyan-8"
                      size="sm"
                      @click="tabName = 'sign-in'">
                      已有账号？去登录
                    </q-btn>
                  </q-card-actions>
                </q-card-section>

                <q-separator vertical />

                <!-- 注册 -->
                <q-card-section class="col-7">
                  <div class="text-center text-h5">注 册</div>
                  <div class="q-mt-xl">
                    <q-form class="q-gutter-md" ref="upForm" @submit="signUpSubmit">
                      <q-input
                        dense
                        filled
                        type="email"
                        v-model="email"
                        label="邮箱"
                        lazy-rules
                        :rules="[(val) => !!val || '请输入邮箱地址']" />
                      <q-input
                        dense
                        filled
                        v-model="username"
                        label="昵称"
                        lazy-rules
                        :rules="[
                          (val) =>
                            (val.length >= 1 && val.length <= 12) || '请输入用户昵称，长度1~12位',
                        ]" />

                      <q-input
                        v-model="upwd1"
                        dense
                        filled
                        label="密码"
                        :type="isPwd ? 'password' : 'text'"
                        lazy-rules
                        :rules="[
                          (val) => (val.length >= 8 && val.length <= 20) || '密码长度为8~20位',
                        ]">
                        <template v-slot:append v-if="upwd1">
                          <q-icon
                            :name="isPwd ? 'bi-eye' : 'bi-eye-slash'"
                            class="cursor-pointer"
                            @click="isPwd = !isPwd" />
                        </template>
                      </q-input>

                      <q-input
                        v-model="upwd2"
                        dense
                        filled
                        label="确认密码"
                        :type="isPwd ? 'password' : 'text'"
                        lazy-rules
                        :rules="[(val) => (val.length >= 8 && val.length <= 20) || errMsg.upwd2]">
                        <template v-slot:append v-if="upwd2">
                          <q-icon
                            :name="isPwd ? 'bi-eye' : 'bi-eye-slash'"
                            class="cursor-pointer"
                            @click="isPwd = !isPwd" />
                        </template>
                      </q-input>

                      <div class="text-center q-mt-lg">
                        <q-btn color="primary" style="padding: 0 50px" type="submit">
                          <q-icon name="bi-send" size="sm" left />
                          注 册
                        </q-btn>
                      </div>
                    </q-form>
                  </div>
                </q-card-section>
              </q-card-section>
            </q-card>
          </q-tab-panel>
        </q-tab-panels>

        <div class="text-center q-pa-sm">
          <span class="text-red">*</span>
          注册登录即表示同意
          <a href="#">用户协议</a> 和 <a href="#">隐私政策</a>
        </div>
      </q-card>
    </q-dialog>
  </div>
</template>

<script setup>
import { api } from "boot/axios"
import { nfy } from "src/utils/u-notify"
import { useLoginRegiStore } from "stores/login-regi"
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"

const loginRegiStore = useLoginRegiStore()
const inForm = ref(null)
const upForm = ref(null)
let tabName = ref("sign-in") // 登录注册tab名称
let isPwd = ref(true) // 密码是否可见
let email = ref("")
let username = ref("")
let upwd1 = ref("")
let upwd2 = ref("")
let errMsg = reactive({
  upwd2: "密码长度为8~20位",
  // inEmaill: { isShow: false, msg: '' },
})
const router = useRouter()

const loginSubmit = () => {
  api
    .post("token/", { email: email.value, password: upwd1.value })
    .then(({ data }) => {
      localStorage.setItem("pa.token", data.access)
      localStorage.setItem("pa.token.refresh", data.refresh)
      localStorage.setItem("pa.username", data.username)
      localStorage.setItem("pa.avatar", data.avatar)
      localStorage.setItem("pa.token.expire", data.expire)
      localStorage.setItem("pa.is_staff", data.is_staff)
      localStorage.setItem("pa.is_superuser", data.is_superuser)
      localStorage.setItem("pa.is_login", true)
      email.value = ""
      upwd1.value = ""
      loginRegiStore.isShowLogin = false
      nfy("positive", `欢迎 ~ ${data.username}`)
      setTimeout(() => {
        router.go(0)
      }, 500)
    })
    .catch(() => {
      nfy("negative", "登录失败, 请检查用户名或密码！")
      upwd1.value = ""
    })
}

const signUpSubmit = () => {
  if (upwd1.value !== upwd2.value) {
    upwd2.value = ""
    errMsg.upwd2 = "两次密码不一致！"
    return
  }
  api
    .post("user/register/", {
      email: email.value,
      username: username.value,
      password: upwd1.value,
      password2: upwd2.value,
    })
    .then(() => {
      tabName.value = "sign-in"
      // email.value = ""
      username.value = ""
      upwd1.value = ""
      upwd2.value = ""
      nfy("positive", "注册成功！去登录吧！")
    })
    .catch((err) => {
      const resp = err.response.data
      if (resp.email) {
        if (resp.email[0].includes("已存在")) {
          nfy("negative", "该邮箱已被注册！")
          return
        }
        nfy("negative", resp.email[0])
        return
      }
      if (resp.username) {
        nfy("negative", "该昵称已被注册！")
        return
      }
      nfy("negative", "注册失败！")
    })
}
</script>

<style scoped lang="scss">
.my-card {
  width: 100%;
}

.login-change-btn {
  margin: 50px 0 0 0;
}
</style>
