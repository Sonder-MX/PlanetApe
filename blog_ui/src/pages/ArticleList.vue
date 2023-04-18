<template>
  <div class="q-mt-sm">
    <q-carousel
      v-model="slide"
      transition-prev="scale"
      transition-next="scale"
      animated
      control-color="white"
      navigation
      padding
      arrows
      infinite
      :autoplay="2000"
      height="200px"
      class="bg-teal-5 text-white shadow-1 rounded-borders">
      <q-carousel-slide name="one" class="column no-wrap flex-center">
        <q-icon name="bi-rocket-takeoff-fill" size="56px" color="red-13" />
        <div class="q-mt-md text-center">猿星球，一款干净简洁的IT技术交流论坛</div>
      </q-carousel-slide>
      <q-carousel-slide name="two" class="column no-wrap flex-center">
        <q-icon name="bi-bell-slash-fill" size="56px" color="light-green-13" />
        <div class="q-mt-md text-center">无广告、无弹窗</div>
      </q-carousel-slide>
      <q-carousel-slide name="three" class="column no-wrap flex-center">
        <q-icon name="bi-stars" size="56px" color="yellow" />
        <div class="q-mt-md text-center">高质量博文</div>
      </q-carousel-slide>
      <q-carousel-slide name="four" class="column no-wrap flex-center">
        <q-icon name="bi-chat-square-heart" size="56px" color="orange" />
        <div class="q-mt-md text-center">和谐的社区</div>
      </q-carousel-slide>
    </q-carousel>
  </div>
  <q-page padding>
    <q-card>
      <q-tabs
        v-model="tabName"
        dense
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
        inline-label
        narrow-indicator
        @update:model-value="handleTabChange">
        <q-tab name="default" icon="bi-list-task" label="默认" />
        <q-tab name="latest" icon="bi-calendar3" label="最新发布" />
        <q-tab name="likes" icon="bi-star-fill" label="最多点赞" />
        <q-tab name="comments" icon="bi-chat-left-text" label="最多评论" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tabName" animated>
        <q-tab-panel :name="tabName">
          <div class="row items-start q-gutter-lg">
            <q-card class="my-card" flat v-for="artc in aticleLists" :key="artc.id">
              <!-- 一条文章 -->
              <router-link :to="{ name: 'ArticleDetail', params: { id: artc.id } }">
                <q-card-section horizontal class="a-article">
                  <q-card-section class="col-3 flex flex-center" v-if="artc.title_img">
                    <q-img class="rounded-borders" :src="artc.title_img.img" />
                  </q-card-section>
                  <q-card-section class="q-pt-xs" style="width: 100%">
                    <div class="text-caption q-gutter-sm">
                      <q-badge
                        :color="randColor()"
                        :label="tg"
                        v-for="tg in artc.tags"
                        :key="tg.index" />
                      <span style="position: absolute; right: 2vw">
                        {{ new Date(artc.created).toLocaleDateString() }}
                      </span>
                    </div>
                    <div class="text-h6 q-mt-sm q-mb-xs">{{ artc.title }}</div>
                    <div class="text-caption text-grey-10">{{ artc.part_cont }}</div>
                    <div class="text-caption text-grey q-mt-sm text-right q-gutter-lg">
                      <span>
                        <q-icon name="bi-person-fill"></q-icon> {{ artc.author.username }}
                      </span>
                      <span>
                        <q-icon name="bi-hand-thumbs-up-fill"></q-icon> {{ artc.like_count }}</span
                      >
                      <span>
                        <q-icon name="bi-chat-square-text"></q-icon> {{ artc.comment_count }}</span
                      >
                    </div>
                  </q-card-section>
                </q-card-section>
              </router-link>
            </q-card>
          </div>
        </q-tab-panel>
      </q-tab-panels>

      <!-- 分页器 -->
      <div class="q-pa-lg flex flex-center">
        <q-pagination
          v-model="pageName"
          color="light-blue"
          :max="10"
          :max-pages="6"
          boundary-numbers
          direction-links
          boundary-links
          @update:model-value="handlePageChange" />
      </div>
    </q-card>
    <div class="q-mb-xl"></div>
  </q-page>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue'
import { api } from 'boot/axios'

let slide = ref('one')
let pageName = ref(1)
let tabName = ref('default')
let aticleLists = ref([])
const crList = ['primary', 'secondary', 'accent', 'positive', 'negative']

const randColor = () => {
  return crList[Math.floor(Math.random() * crList.length)]
}

// 处理tab切换
const handleTabChange = (val) => {
  tabName.value = val
}

// 处理分页器切换
const handlePageChange = (val) => {
  pageName.value = val
}

onBeforeMount(() => {
  api.get('article').then((res) => {
    aticleLists.value = res.data.results
  })
})
</script>

<style scoped lang="scss">
.my-card {
  width: 100%;
  a {
    text-decoration: none;
    color: rgb(39, 39, 39);
  }
}

.a-article {
  cursor: pointer;
}

.a-article:hover {
  background-color: $grey-2;
}
</style>
