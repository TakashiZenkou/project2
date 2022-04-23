<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import Registration from './components/Registration.vue';
</script>

<template>
  <AppHeader :key="$route.fullPath"/>

  <main>
    <RouterView/>
  </main>
  
</template>

<style>
body {

  background-color: rgb(226, 223, 223);
  -ms-overflow-style: none;  
  scrollbar-width: none; 


}

.container::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.container {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>