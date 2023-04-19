<template>
  <q-layout view="hHh Lpr lfr">
    <q-header elevated class="bg-primary text-white">
      <NavBar />
    </q-header>

    <q-page-container>
      <q-page></q-page>
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
</style>
