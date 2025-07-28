<template>
  <div id="app">
    <Navbar />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
</script>

<style>
/* 如果要讓 Footer 黏在最底部 */
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1; /* 撐開中間內容區 */
}
</style>
