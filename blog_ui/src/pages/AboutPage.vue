<template>
  <q-layout view="hHh Lpr lfr">
    <q-header elevated class="bg-primary text-white">
      <NavBar />
    </q-header>

    <q-page-container>
      <q-page style="margin: 0 12%">
        <div class="bg-blue-grey-1 q-px-xl q-py-md" style="height: 85vh">
          <q-card flat bordered>
            <q-card-section horizontal>
              <q-card-section class="q-pt-xs">
                <div class="text-overline">猿星球 - 致力于为开发者提供一个交流学习的平台</div>
                <div class="text-h5 q-mt-sm q-mb-xs text-info">
                  <q-icon name="bi-people-fill" />
                  关于我们
                </div>
                <div class="intr-info">
                  猿星球致力于为开发者提供一个交流学习的平台，我们希望能够为开发者提供一个开放的平台，让开发者能够在这里分享自己的知识，学习他人的知识，让开发者能够在这里找到志同道合的朋友，一起学习，一起进步。
                </div>
                <div class="intr-info">
                  猿星球是一个开源项目，我们希望能够让更多的开发者参与到这个项目中来，一起为开发者提供一个更好的平台。
                </div>
                <div class="intr-info">
                  猿星球目前虽然只有两位开发小伙伴，但是我们希望能够有更多的开发者能够加入到这个项目中来，一起为开发者提供一个更好的平台。
                </div>
                <div class="intr-info text-right">
                  开源地址：<a target="_blank" href="https://github.com/Sonder-MX/PlanetApe">
                    Github
                  </a>
                </div>
              </q-card-section>

              <q-card-section class="col-4 flex flex-center">
                <q-img class="rounded-borders" src="logo.png" />
              </q-card-section>
            </q-card-section>

            <!-- 介绍开发栈 -->
            <q-card-section>
              <div class="text-h5 q-mt-sm q-mb-xs text-info">
                <q-icon name="bi-cassette-fill" />
                技术开发栈
              </div>
              <div class="intr-info q-mt-sm">
                猿星球是一个前后端分离的项目，前端使用了
                <span class="text-weight-bold text-orange-10">
                  Vue3 + Vite + Quasar + SCSS + Pinia + Vue Router + Axios
                </span>
                等技术开发栈, 后端使用
                <span class="text-weight-bold text-orange-10">
                  Django + Django Rest Framework + Django Filter + Sqlite3
                </span>
                等技术开发栈。
              </div>
            </q-card-section>
          </q-card>
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
</script>

<style scoped lang="scss">
.foot-a {
  a {
    color: black;
    text-decoration: none;
    margin: 0 8px;
  }
}

.intr-info {
  padding: 5px 0;
  text-indent: 1.5rem;
}
</style>
