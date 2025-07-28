<template>
  <div class="order-page">
    <!-- 上方：產品清單 -->
    <div class="product-list">
      <ProductCard
        v-for="(item, index) in products"
        :key="item.name || index"
        :image="item.image"
        :name="item.name"
        :description="item.description"
        :ingredients="item.ingredients"
        :price="item.price"
        :quantity="item.quantity"
        @update-quantity="(newQty) => updateQuantity(index, newQty)"
      />
    </div>

    <!-- 下方：SummaryBar -->
    <SummaryBar
      :products="products"
      :totalItems="totalItems"
      :totalPrice="totalPrice"
      @checkout="goCheckout"
    />
  </div>
</template>

<script setup>
import { reactive, computed } from 'vue'
import { useRouter } from 'vue-router'
import ProductCard from '../components/ProductCard.vue'
import SummaryBar from '../components/SummaryBar.vue'

const router = useRouter()

const products = reactive([
  {
    image: 'https://via.placeholder.com/120',
    name: '招牌肉粽',
    description: '香氣十足、口感紮實',
    ingredients: '糯米、五花肉、香菇、鹹蛋黃',
    price: 50,
    quantity: 0
  },
  {
    image: 'https://via.placeholder.com/120',
    name: '素食粽',
    description: '健康養生好選擇',
    ingredients: '糯米、香菇、豆干、花生',
    price: 45,
    quantity: 0
  }
])

function updateQuantity(index, newQty) {
  if (products[index]) {
    products[index].quantity = newQty
  }
}

const totalItems = computed(() =>
  products.reduce((sum, item) => sum + (item?.quantity || 0), 0)
)

const totalPrice = computed(() =>
  products.reduce((sum, item) => sum + (item?.quantity || 0) * (item?.price || 0), 0)
)

function goCheckout() {
  router.push('/checkout')
}
</script>

<style scoped>
.order-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.product-list {
  flex: 1;
  overflow-y: auto;
  padding: 0.5rem;
}
</style>
