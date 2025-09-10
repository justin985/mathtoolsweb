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