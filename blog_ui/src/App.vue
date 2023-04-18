<template>
  <q-scroll-area class="fullscreen">
    <router-view />

    <!-- 登录Dialog -->
    <Login />
  </q-scroll-area>
</template>

<script setup>
import Login from './components/Login.vue'
</script>
