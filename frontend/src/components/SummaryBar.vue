<template>
  <div class="summary-bar">
    <div class="summary-left">
      <p>已選 {{ totalItems }} 項商品</p>
      <ul class="summary-list">
        <li
          v-for="(item, index) in safeProducts"
          :key="item.name || index"
        >
          {{ item.name }}：{{ item.quantity }} 個
        </li>
      </ul>
    </div>
    <div class="summary-right">
      <p>總金額：{{ totalPrice }} 元</p>
      <button class="checkout-btn" @click="$emit('checkout')">前往結帳</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  products: {
    type: Array,
    default: () => []
  },
  totalItems: {
    type: Number,
    default: 0
  },
  totalPrice: {
    type: Number,
    default: 0
  }
})

const safeProducts = computed(() =>
  (props.products || []).filter(
    (item) => item && item.quantity !== undefined && item.quantity > 0
  )
)
</script>

<style scoped>
.summary-bar {
  border-top: 1px solid black;
  padding: 0.5rem;
  background: #f8f8f8;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.summary-left {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  text-align: left;
}

.summary-list {
  list-style: none;
  padding: 0;
  margin: 0;
  font-size: 0.85rem;
}

.summary-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.3rem;
}

.checkout-btn {
  background: #333;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;
}
</style>
