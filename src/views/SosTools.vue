<template>
  <div class="sos-tools">
    <main class="calculator-container">
      <QuadraticCalculator />
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import QuadraticCalculator from '../components/QuadraticCalculator.vue'

onMounted(() => {
  document.title = '數學工具箱 - 配方計算器'
  document.querySelector('meta[name="description"]').content = '免費的在線配方計算器，幫助您快速解決二次方程式的配方問題。操作簡單，計算準確，適合學生和教師使用。'
  document.querySelector('meta[name="keywords"]').content = '配方計算器,二次方程式,數學工具,配方法,代數計算,在線計算器'
})
</script>

<style scoped>
.sos-tools {
  min-height: 100vh;
  background-color: #f8fafc;
}

.calculator-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

@media (max-width: 768px) {
  .top-bar {
    padding: 1rem;
  }

  .calculator-container {
    padding: 1rem;
  }
}
</style>