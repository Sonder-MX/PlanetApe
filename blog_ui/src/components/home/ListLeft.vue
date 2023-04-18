<template>
  <div class="q-pl-xl q-pt-lg q-pr-sm">
    <q-scroll-area style="height: 70vh">
      <q-list bordered padding class="rounded-borders bg-white">
        <q-item clickable v-ripple>
          <q-item-section avatar>
            <q-icon name="bi-list-nested" />
          </q-item-section>
          <q-item-section> 所有文章 </q-item-section>
        </q-item>

        <q-item clickable v-ripple v-for="category in categoryList" :key="category.id">
          <q-item-section avatar>
            <q-icon :name="`bi-${category.icon_name}`" size="sm" />
          </q-item-section>
          <q-item-section> {{ category.title }} </q-item-section>
        </q-item>
      </q-list>
    </q-scroll-area>
  </div>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue'
import { api } from 'boot/axios'

const categoryList = ref([])

onBeforeMount(async () => {
  const { data } = await api.get('category/')
  categoryList.value = data
})
</script>

<style scoped></style>
