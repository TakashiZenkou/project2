<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import Registration from './components/Registration.vue';
</script>

<template>
  <AppHeader />

  <main>
    <RouterView/>
  </main>
  
  <AppFooter />
</template>

<style>
body {
  padding-top: 75px;
  background-color: rgb(226, 223, 223);
}
</style>