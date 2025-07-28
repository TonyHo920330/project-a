<template>
  <footer class="footer">
    <div class="footer-container">
      <!-- 聯絡資訊 -->
      <div class="footer-section">
        <h3>聯絡我們</h3>
        <p>電話：02-1234-5678</p>
        <p>Email：info@example.com</p>
      </div>

      <!-- 地址 -->
      <div class="footer-section">
        <h3>地址</h3>
        <p>台北市中正區假路 123 號 5 樓</p>
      </div>

      <!-- 營業時間 -->
      <div class="footer-section">
        <h3>營業時間</h3>
        <p>週一 ~ 週五：09:00 - 18:00</p>
        <p>週六：10:00 - 16:00</p>
        <p>週日：公休</p>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2025 我的商店. All Rights Reserved.</p>
    </div>
  </footer>
</template>

<script setup>
/* 靜態內容，不需邏輯 */
</script>

<style scoped>
.footer {
  background: #333;
  color: white;
  padding: 1rem;
  font-size: 0.9rem;
}

.footer-container {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;           /* 間隔縮小 */
  text-align: left;      /* 全部靠左對齊 */
}

.footer-section {
  margin-bottom: 0.5rem;
}

.footer-section h3 {
  margin-bottom: 0.3rem;
  font-size: 1rem;
  border-bottom: 1px solid #555;
  display: inline-block;
  padding-bottom: 0.2rem;
}

.footer-bottom {
  text-align: left;       /* 也靠左對齊 */
  margin-top: 0.5rem;
  border-top: 1px solid #555;
  padding-top: 0.3rem;
  font-size: 0.8rem;
}

/* 平板/桌面版調整成橫排，但間隔不大 */
@media (min-width: 768px) {
  .footer-container {
    flex-direction: row;
    justify-content: flex-start;  /* 靠左排列 */
    gap: 2rem;                     /* 各區塊之間間距縮小 */
  }
}
</style>
