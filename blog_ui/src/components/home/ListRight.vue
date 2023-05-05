<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card">
      <div class="q-pa-xl text-center text-h5 bg-light-blue-4 text-white">
        <q-icon name="bi-list-stars" />
        日点赞
      </div>
      <q-list>
        <q-item clickable v-for="li in allList" :key="li.id">
          <q-item-section avatar>
            <q-icon :color="iconObj[li.id - 1].color" :name="iconObj[li.id - 1].name" />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ li.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>

    <q-card class="my-card">
      <div class="q-pa-xl text-center text-h5 bg-orange-4 text-green">
        <q-icon name="bi-list-stars" />
        周点赞
      </div>
      <q-list>
        <q-item clickable v-for="li in allList" :key="li.id">
          <q-item-section avatar>
            <q-icon :color="iconObj[li.id - 1].color" :name="iconObj[li.id - 1].name" />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ li.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>

    <q-card class="my-card">
      <div class="q-pa-xl text-center text-h5 bg-red-4 text-black">
        <q-icon name="bi-list-stars" />
        月点赞
      </div>
      <q-list>
        <q-item clickable v-for="li in allList" :key="li.id">
          <q-item-section avatar>
            <q-icon :color="iconObj[li.id - 1].color" :name="iconObj[li.id - 1].name" />
          </q-item-section>
          <q-item-section>
            <q-item-label>{{ li.title }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-card>
  </div>
</template>

<script setup>
import { ref } from "vue"

const iconObj = ref([
  { id: 1, name: "bi-1-circle-fill", color: "red" },
  { id: 2, name: "bi-2-circle-fill", color: "orange" },
  { id: 3, name: "bi-3-circle-fill", color: "blue" },
])
const allList = ref([
  { id: 1, title: "MySQL基础教程" },
  { id: 2, title: "机器学习高频面试题" },
  { id: 3, title: "Django基础学习" },
])
</script>

<style scoped lang="scss">
.my-card {
  width: 100%;
}
</style>
