<template>
  <q-toolbar class="nav-bar">
    <span class="text-h6 q-mr-xl">
      <strong>
        <router-link :to="{ name: 'ArticleList' }"> 猿星球 </router-link>
      </strong>
    </span>
    <q-tabs align="left" inline-label>
      <q-route-tab icon="bi-house" label="首页" />
      <q-route-tab icon="bi-newspaper" label="新闻" />
      <q-route-tab icon="bi-patch-question" label="问答" />
      <q-route-tab icon="bi-columns-gap" label="专栏" />
      <q-btn-dropdown auto-close stretch flat label="其他" dropdown-icon="bi-caret-down">
        <q-list>
          <q-item clickable>
            <q-item-section>关于</q-item-section>
          </q-item>
          <q-item clickable>
            <q-item-section>帮助</q-item-section>
          </q-item>
        </q-list>
      </q-btn-dropdown>
    </q-tabs>
    <q-space />
    <div class="nav-search">
      <q-input dark dense standout v-model="searchKey">
        <template v-slot:append>
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
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useLoginRegiStore } from 'src/stores/login-regi'

let searchKey = ref('')
const loginRegiStore = useLoginRegiStore()
const route = useRoute()
const router = useRouter()

// 跳转到编辑创建页面
const toEditCreate = () => router.push({ name: 'EditCreate' })

// 除了编辑和创建页面，其他页面都显示发布文章按钮
const isShowPublish = computed(() => route.name !== 'EditCreate')

const searchEvent = () => {
  searchKey.value = searchKey.value.trim()
  if (searchKey.value) {
    console.log(searchKey.value)
  }
}

const logout = () => {
  loginRegiStore.logout()
  router.go(0)
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
</style>
