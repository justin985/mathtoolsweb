<template>
  <NavBar />
  <main>
    <QuadraticCalculator />
  </main>
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

main {
  min-height: 100vh;
  background-color: #f5f5f5;
  display: flex;
  flex-direction: column;
}
</style>
