<template>
  <div class="q-pl-xl q-pt-lg q-pr-sm">
    <q-scroll-area style="height: 70vh">
      <q-list bordered padding class="rounded-borders bg-white">
        <q-item
          clickable
          v-ripple
          active-class="active-category"
          :active="atvItem === -1"
          @click="handleCategoryClick(-1, '')">
          <q-item-section avatar>
            <q-icon name="bi-list-nested" />
          </q-item-section>
          <q-item-section> 所有文章 </q-item-section>
        </q-item>

        <q-item
          clickable
          v-ripple
          v-for="category in categoryList"
          :key="category.id"
          active-class="active-category"
          :active="atvItem === category.id"
          @click="handleCategoryClick(category.id, category.title)">
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
import { api } from "boot/axios"
import { useSearchUrlStore } from "stores/search-url"
import { onBeforeMount, ref } from "vue"

let atvItem = ref(-1)
const categoryList = ref([])
const searchUrl = useSearchUrlStore()

const handleCategoryClick = (cid, cname) => {
  atvItem.value = cid
  searchUrl.category = cname
}

onBeforeMount(async () => {
  const { data } = await api.get("category/")
  categoryList.value = data
})
</script>

<style scoped lang="scss">
.active-category {
  background-color: #a0deff79;
  color: $primary;
}
</style>
