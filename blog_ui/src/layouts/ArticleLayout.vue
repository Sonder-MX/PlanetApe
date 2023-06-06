<template>
  <q-layout view="hHh Lpr lfr">
    <q-header elevated class="bg-primary text-white">
      <NavBar :isShowSearch="true" />
    </q-header>

    <q-drawer show-if-above :v-model="true" side="left" bordered class="bg-grey-2">
      <ListLeft />
    </q-drawer>

    <q-drawer show-if-above :v-model="true" side="right" bordered class="bg-grey-2">
      <ListRight />
    </q-drawer>

    <q-page-container>
      <router-view />
      <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
        <q-btn fab icon="bi-chevron-compact-up" color="accent" />
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
import ListLeft from "components/home/ListLeft.vue"
import ListRight from "components/home/ListRight.vue"
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
