<template>
  <div class="product-card">
    <img :src="image" alt="產品圖片" class="product-image" />

    <div class="product-info">
      <h3>{{ name }}</h3>
      <p>{{ description }}</p>
      <p>{{ ingredients }}</p>
      <p class="price">單價：{{ price }} 元</p>
    </div>

    <div class="quantity-control">
      <button @click="decrease">-</button>
      <span>{{ quantity }}</span>
      <button @click="increase">+</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  image: String,
  name: String,
  description: String,
  ingredients: String,
  price: Number,
  quantity: {
    type: Number,
    default: 0
  }
})

const emit = defineEmits(['update-quantity'])

function increase() {
  emit('update-quantity', props.quantity + 1)
}

function decrease() {
  if (props.quantity > 0) {
    emit('update-quantity', props.quantity - 1)
  }
}
</script>

<style scoped>
.product-card {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  border: 1px solid black;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
}

.product-image {
  width: 120px;
  height: auto;
  margin-right: 1rem;
}

.product-info {
  flex: 1;
}

.product-info h3 {
  margin: 0;
  font-weight: bold;
}

.price {
  font-weight: bold;
}

.quantity-control {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.quantity-control button {
  border: 1px solid black;
  background: none;
  width: 30px;
  height: 30px;
  cursor: pointer;
}
</style>
