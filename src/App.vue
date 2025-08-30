<template>
  <div class="app-container" role="application" aria-label="數學工具箱應用">
    <header role="banner">
      <NavBar />
    </header>
    <main role="main" aria-label="主要內容區">
      <article class="calculator-container">
        <QuadraticCalculator />
      </article>
    </main>
    <footer role="contentinfo" class="app-footer">
      <p>&copy; 2024 數學工具箱. 保留所有權利.</p>
    </footer>
  </div>
</template>

<script setup>
import NavBar from './components/NavBar.vue'
import QuadraticCalculator from './components/QuadraticCalculator.vue'
</script>

<style>
@import '@mdi/font/css/materialdesignicons.css';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f5f5f5;
  margin: 0;
  padding: 0;
  min-height: 100vh;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
  padding-top: 4rem;
  flex: 1;
}

.calculator-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  width: 100%;
}

.app-footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem;
  margin-top: auto;
}
</style>
