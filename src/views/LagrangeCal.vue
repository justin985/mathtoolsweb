<template>
  <div class="lagrange-page">
    <LagrangeCal />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import LagrangeCal from '../components/LagrangeCal.vue'

onMounted(() => {
  document.title = '拉格朗日乘數計算器 - SOS Tools'
  
  // 設置 meta 標籤
  const metaDescription = document.querySelector('meta[name="description"]')
  if (metaDescription) {
    metaDescription.setAttribute('content', '使用拉格朗日乘數法求解條件極值問題的線上計算工具。支援多變數函數和約束條件的輸入，提供直觀的計算結果顯示。')
  }

  const metaKeywords = document.querySelector('meta[name="keywords"]')
  if (metaKeywords) {
    metaKeywords.setAttribute('content', '拉格朗日乘數法,條件極值,最佳化,數學工具,線上計算器')
  }
})
</script>

<style scoped>
.lagrange-page {
  min-height: 100vh;
  background-color: #f8fafc;
}
</style>