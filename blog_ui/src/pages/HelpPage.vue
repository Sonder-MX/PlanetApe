<template>
  <q-layout view="hHh Lpr lFr">
    <q-header elevated class="bg-primary text-white">
      <NavBar />
    </q-header>

    <q-page-container>
      <q-page>
        <div class="bg-grey-1" style="margin: 0 20%">
          <div class="q-mx-xl">
            <q-intersection v-for="hl in helpLeft" :key="hl.hid" transition="scale">
              <q-card class="q-mx-md q-my-lg" bordered>
                <q-card-section>
                  <div class="text-overline text-orange-9">Tip {{ hl.hid }}</div>
                  <div class="text-h6">{{ hl.title }}</div>
                </q-card-section>
                <q-card-actions>
                  <q-space />
                  <q-btn
                    round
                    flat
                    dense
                    :icon="hl.isShow ? 'bi-caret-down-fill' : 'bi-caret-up-fill'"
                    @click="hl.isShow = !hl.isShow" />
                </q-card-actions>

                <q-slide-transition>
                  <div v-show="hl.isShow">
                    <q-separator />
                    <q-card-section
                      class="text-subitle1 text-weight-bold text-deep-purple-14"
                      style="text-indent: 1.5rem">
                      {{ hl.content }}
                    </q-card-section>
                  </div>
                </q-slide-transition>
              </q-card>
            </q-intersection>
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
import NavBar from "components/NavBar.vue"
import { ref } from "vue"

const helpLeft = ref([
  {
    hid: 1,
    title: "账号密码忘记如何找回？",
    content: "若忘记账号密码，请及时联系管理员进行找回。管理员邮箱：888@gmail.com",
    isShow: false,
  },
  {
    hid: 2,
    title: "如何认证为博主？",
    content: "由于技术有限，若想成为博主，需要联系管理员进行认证。管理员邮箱：888@gmail.com",
    isShow: false,
  },
  {
    hid: 3,
    title: "如何发布文章？",
    content:
      "若想发布文章，需要先认证为博主，认证通过后即可发布文章。在发布文章时，需要填写文章标题、文章内容、文章标签、文章分类。文章内容仅支持Markdown语法。",
    isShow: false,
  },
  {
    hid: 4,
    title: "如何举报有违规内容的文章？",
    content:
      "违规内容包括但不限于：色情、暴力、政治等。若发现有违规内容的文章，请及时联系管理员进行举报。管理员邮箱：888@gamil.com",
    isShow: false,
  },
  {
    hid: 5,
    title: "如何成为文章质检员？",
    content: "若想成为文章质检员，需要联系管理员进行授权。管理员邮箱：888@gmail.com",
    isShow: false,
  },
  {
    hid: 6,
    title: "猿星球的定位是什么？",
    content: "猿星球是一个开源的技术社区，致力于为开发者提供一个交流学习的平台。",
    isShow: false,
  },
  {
    hid: 7,
    title: "猿星球的技术栈是什么？",
    content: "猿星球的技术栈为Vue3 + Vite + Quasar + Django + Django Rest Framework + Sqlite3。",
    isShow: false,
  },
])
</script>

<style scoped lang="scss">
.foot-a {
  a {
    color: black;
    text-decoration: none;
    margin: 0 8px;
  }
}
</style>
