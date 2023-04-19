<template>
  <q-toolbar class="nav-bar">
    <span class="text-h6 q-mr-xl">
      <strong>
        <router-link :to="{ name: 'ArticleList' }"> 猿星球 </router-link>
      </strong>
    </span>
    <q-tabs align="left" inline-label v-model="navTab">
      <q-tab name="home" icon="bi-house" label="首页" />
      <q-tab name="news" icon="bi-newspaper" label="新闻专栏" />
      <q-tab name="about" icon="bi-filter-circle" label="关于小站" />
      <q-tab name="help" icon="bi-info-square" label="帮助文档" />
    </q-tabs>
    <q-space />
    <div class="nav-search">
      <q-input dark dense standout v-model="searchKey">
        <template v-slot:append>
          <q-icon v-if="searchKey" name="bi-x" class="cursor-pointer" @click="celarSearch" />
          <q-icon name="bi-search" class="cursor-pointer" @click="searchEvent" />
        </template>
      </q-input>
    </div>
    <div v-if="!loginRegiStore.isLogin">
      <q-btn color="secondary" label="登录 / 注册" @click="loginRegiStore.isShowLogin = true" />
    </div>

    <div v-if="loginRegiStore.isLogin">
      <q-btn-dropdown flat dense>
        <template v-slot:label>
          <q-avatar>
            <img :src="loginRegiStore.avatar" />
          </q-avatar>
        </template>

        <q-list>
          <q-item dense clickable v-close-popup @click="logout"> 退出登录 </q-item>
          <q-item
            v-if="
              loginRegiStore.isLogin &&
              (loginRegiStore.isStaff || loginRegiStore.isSuperuser) &&
              isShowPublish
            "
            dense
            v-close-popup
            clickable
            @click="toEditCreate">
            发布文章
          </q-item>
        </q-list>
      </q-btn-dropdown>
    </div>
    <slot></slot>
  </q-toolbar>
</template>

<script setup>
import { useLoginRegiStore } from "stores/login-regi"
import { useSearchUrlStore } from "stores/search-url"
import { computed, ref } from "vue"
import { useRoute, useRouter } from "vue-router"

let searchKey = ref("")
let navTab = ref("home")
const loginRegiStore = useLoginRegiStore()
const searchUrl = useSearchUrlStore()
const route = useRoute()
const router = useRouter()

// 跳转到编辑创建页面
const toEditCreate = () => router.push({ name: "EditCreate" })

// 除了编辑和创建页面，其他页面都显示发布文章按钮
const isShowPublish = computed(() => route.name !== "EditCreate")

const searchEvent = () => {
  searchKey.value = searchKey.value.trim()
  searchUrl.setSearch(searchKey.value)
}

const celarSearch = () => {
  searchKey.value = ""
  searchUrl.setSearch("")
}

const logout = () => {
  router.go(0)
  loginRegiStore.logout()
}
</script>

<style scoped lang="scss">
.nav-bar {
  padding: 0 5vw;
  a {
    color: white;
    text-decoration: none;
  }
}

.nav-search {
  margin-right: 20px;
}

.active-tab {
  background-color: aqua;
}
</style>
