<template>
  <div class="fullscreen bg-blue-5 text-white text-center q-pa-md flex flex-center">
    <div>
      <div style="font-size: 15vh">迷路了？？？</div>
      <div class="text-h3" style="opacity: 0.4">这里什么也没有...</div>
      <q-btn
        class="q-mt-xl text-weight-bolder"
        color="white"
        text-color="blue"
        unelevated
        :to="{ name: 'ArticleList' }"
        label="点击返回首页"
        no-caps />
    </div>
  </div>
</template>

<script setup></script>
