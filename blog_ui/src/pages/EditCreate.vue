<template>
  <q-layout view="hHh Lpr lfr">
    <q-header elevated class="bg-primary text-white">
      <NavBar />
    </q-header>

    <q-drawer show-if-above side="left" bordered class="bg-grey-2"> </q-drawer>

    <q-drawer show-if-above side="right" bordered class="bg-grey-2"> </q-drawer>

    <q-page-container>
      <q-page>
        <ContText />
      </q-page>
    </q-page-container>

    <q-footer elevated class="bg-blue-grey-2 text-black">
      <q-toolbar>
        <span class="text-overline">猿星球</span>
        <q-space />
        <div class="foot-a text-h6">
          <a href="#" target="_blank"> <q-icon name="bi-github"></q-icon> </a>
          <a href="#" target="_blank"> <q-icon name="bi-envelope-at-fill"></q-icon> </a>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import NavBar from 'components/NavBar.vue'
import ContText from 'components/edit-create/ContText.vue'
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
