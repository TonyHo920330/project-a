<template>
  <nav class="navbar">
    <!-- 上方固定列 -->
    <div class="navbar-header">
      <div class="logo">大甲肉粽</div>
      <button class="menu-toggle" @click="toggleMenu">☰</button>
    </div>

    <!-- 展開選單 -->
    <ul class="nav-links" :class="{ active: isOpen }">
      <li><router-link to="/order">訂購產品</router-link></li>
      <li><router-link to="/review">訂單查詢</router-link></li>
    </ul>
  </nav>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const isOpen = ref(false)

function toggleMenu() {
  isOpen.value = !isOpen.value
}
</script>

<style scoped>
/* ========== 手機直向為主 ========== */
.navbar {
  background: #333;
  color: white;
  padding: 0.5rem;
}

.navbar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1rem;
}

.menu-toggle {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

/* nav-links 預設隱藏 */
.nav-links {
  list-style: none;
  padding: 0;
  margin: 0;
  display: none;
}

.nav-links li {
  border-top: 1px solid #555;
}

.nav-links li a {
  display: block;
  padding: 0.8rem 0;       /* 只保留上下 padding，拿掉左右 */
  padding-left: 0;          /* 不要預設縮排 */
  margin-left: 0;           /* 移除額外間距 */
  color: white;
  text-decoration: none;
}

.nav-links li a:hover {
  background: #444;
}

/* active class 顯示 */
.nav-links.active {
  display: block;
}

/* ========== 限制只有手機直向顯示 ========== */
@media (min-width: 768px) {
  .navbar {
    display: none; /* 平板以上不顯示 */
  }
}
</style>
