<template>
  <q-layout view="hHh Lpr lfr">
    <q-header elevated class="bg-primary text-white">
      <NavBar />
    </q-header>

    <q-page-container>
      <q-page class="cont-page">
        <div class="row">
          <!-- 每天60秒读懂世界 -->
          <div class="col-5">
            <q-card bordered style="height: 100%">
              <q-card-section>
                <div class="text-h6">{{ shortNews.name }}</div>
              </q-card-section>
              <q-separator inset />
              <q-card-section class="short-news" v-for="sn in shortNews.data" :key="sn.index">
                {{ sn }}
              </q-card-section>

              <q-inner-loading
                :showing="shortNews.isLoding"
                label="获取第三方数据中...."
                label-class="text-teal"
                label-style="font-size: 1.1em" />
            </q-card>
          </div>

          <!-- 新闻api -->
          <div class="col-7 q-pl-lg">
            <div class="q-pa-lg text-h5">甘肃省每日新闻</div>
            <q-separator inset />
            <div class="row items-start q-mt-sm q-gutter-md">
              <q-card v-if="gansuNews.isLoding" flat style="width: 100%; height: 50vh">
                <q-inner-loading
                  :showing="gansuNews.isLoding"
                  label="获取第三方数据中...."
                  label-class="text-teal"
                  label-style="font-size: 1.1em" />
              </q-card>
              <q-card
                flat
                bordered
                v-for="gsn in gansuNews.data"
                :key="gsn.index"
                style="width: 100%">
                <q-img v-if="gsn.hasImg" :src="gsn.imgsrc" :ratio="16 / 4" />
                <q-card-section>
                  <div class="text-h6">
                    <a :href="gsn.url" target="_blank" class="gansu-news">
                      {{ gsn.title }}
                    </a>
                  </div>
                  <div class="text-right q-gutter-x-md">
                    <span class="text-pink">来源: {{ gsn.source }}</span>
                    <span class="text-primary">发布时间: {{ gsn.ptime }}</span>
                  </div>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </div>
      </q-page>
      <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
        <q-btn fab icon="bi-chevron-compact-up" color="info" />
      </q-page-scroller>
    </q-page-container>

    <q-footer elevated class="bg-blue-grey-2 text-black">
      <q-toolbar>
        <span class="text-overline">猿星球</span>
        <q-space />
        <div class="foot-a text-h6">
          <a href="https://github.com/Sonder-MX/PlanetApe" target="_blank">
            <q-icon name="bi-github"></q-icon>
          </a>
          <a href="#" target="_blank"> <q-icon name="bi-envelope-at-fill"></q-icon> </a>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import axios from "axios"
import NavBar from "components/NavBar.vue"
import { onBeforeMount, reactive } from "vue"

let shortNews = reactive({
  isLoding: true,

  name: "",
  data: [],
})

let gansuNews = reactive({
  isLoding: true,

  data: [],
})

const getShortNews = () => {
  axios.get("https://api.vvhan.com/api/60s?type=json").then(({ data }) => {
    shortNews.name = data.name
    shortNews.data = data.data
    shortNews.isLoding = false
  })
}

const getGanSuNews = () => {
  axios
    .get(
      "https://v.api.aa1.cn/api/api-tplist/go.php/api/News/local_news?name=%E7%94%98%E8%82%83%E7%9C%81_%E5%85%B0%E5%B7%9E%E5%B8%82&page=0"
    )
    .then(({ data }) => {
      gansuNews.data = data.data
      gansuNews.isLoding = false
    })
}

onBeforeMount(() => {
  getShortNews()
  getGanSuNews()
})
</script>

<style scoped lang="scss">
div,
span,
p {
  caret-color: transparent;
}

.foot-a {
  a {
    color: black;
    text-decoration: none;
    margin: 0 8px;
  }
}

.cont-page {
  padding-top: 10px;
  margin: 0 14%;
  background-color: rgba(243, 238, 238, 0.5);
}

.short-news:hover {
  background-color: rgba(243, 238, 238, 0.5);
  cursor: default;
}

.gansu-news {
  color: rgb(24, 23, 65);
  text-decoration: none;
}
</style>
