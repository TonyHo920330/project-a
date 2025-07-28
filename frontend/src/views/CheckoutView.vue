<template>
  <div class="checkout-page">
    <!-- 上方：結帳內容 -->
    <div class="checkout-content">
      <h2>取貨資訊</h2>

      <!-- 商品清單 -->
      <div class="product-list">
        <div
          v-for="(item, index) in safeProducts"
          :key="item.name || index"
          class="checkout-item"
        >
          <div class="item-left">
            <p class="item-name">{{ item.name }}</p>
            <p class="item-qty">數量：{{ item.quantity }}</p>
          </div>
          <p class="item-price">小計：{{ item.price * item.quantity }} 元</p>
        </div>
      </div>

      <!-- 取貨日期 -->
      <div class="pickup-section">
        <h3>取貨日期</h3>
        <input
          type="date"
          v-model="pickupDate"
          :min="today"
          class="pickup-date"
        />
      </div>
    </div>

    <!-- 下方：總金額 + 按鈕 -->
    <div class="checkout-bottom">
      <p>總共 {{ totalItems }} 項商品，總金額：{{ totalPrice }} 元</p>
      <button class="checkout-btn" @click="finishPayment">前往結帳</button>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed, ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 模擬購物車資料 (正式應用應從 Vuex / Pinia / API 取得)
const products = reactive([
  {
    image: 'https://via.placeholder.com/120',
    name: '招牌肉粽',
    price: 50,
    quantity: 2
  },
  {
    image: 'https://via.placeholder.com/120',
    name: '素食粽',
    price: 45,
    quantity: 1
  }
])

// 過濾掉數量為 0 或不合法的商品
const safeProducts = computed(() =>
  (products || []).filter((item) => item && item.quantity > 0)
)

// 總數量與總金額
const totalItems = computed(() =>
  safeProducts.value.reduce((sum, item) => sum + (item?.quantity || 0), 0)
)

const totalPrice = computed(() =>
  safeProducts.value.reduce(
    (sum, item) => sum + (item?.quantity || 0) * (item?.price || 0),
    0
  )
)

// 取貨日期
const pickupDate = ref('')
const today = new Date().toISOString().split('T')[0]

function finishPayment() {
  if (!pickupDate.value) {
    alert('請選擇取貨日期')
    return
  }
  alert(`已完成結帳！取貨日期：${pickupDate.value}，總金額：${totalPrice.value} 元`)
  router.push('/order') // 完成後回到訂購頁
}
</script>

<style scoped>
.checkout-page {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.checkout-content {
  flex: 1;
  padding: 1rem;
  overflow-y: auto;
}

.product-list {
  margin-top: 1rem;
  border-top: 1px solid #ccc;
  padding-top: 0.5rem;
}

.checkout-item {
  display: flex;
  justify-content: space-between;
  padding: 0.3rem 0;
  border-bottom: 1px solid #eee;
}

.item-left {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.item-name {
  font-weight: bold;
}

.item-price {
  font-weight: bold;
  text-align: right;
}

.pickup-section {
  margin-top: 1.2rem;
}

.pickup-section input {
  margin-top: 0.3rem;
  padding: 0.4rem;
  width: 100%;
}

.checkout-bottom {
  border-top: 1px solid #ccc;
  padding: 0.8rem;
  background: #f8f8f8;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.checkout-btn {
  background: #333;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  cursor: pointer;
}
</style>
