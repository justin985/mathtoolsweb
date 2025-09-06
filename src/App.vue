<template>
  <div class="app-container" role="application" aria-label="數學工具箱應用" @click="handleContainerClick">
    <aside class="sidebar" :class="{ 'sidebar-open': isSidebarOpen }" role="navigation" aria-label="主導航選單" @click.stop>
      <div class="sidebar-header">
        <img src="/vite.svg" alt="Logo" class="sidebar-logo" />
        <h2>數學工具箱</h2> <!-- 不要改大小-->
      </div>
      <nav class="sidebar-nav">
        <div class="nav-section">
          <h2>代數</h2>
          <a href="#quadratic" class="nav-item active">配方計算器</a>
          <a href="#" class="nav-item disabled">多項式計算</a>
          <a href="#" class="nav-item disabled">矩陣運算</a>
        </div>
        <div class="nav-section">
          <h2>幾何</h2>
          <a href="#" class="nav-item disabled">三角函數</a>
          <a href="#" class="nav-item disabled">圓錐曲線</a>
        </div>
        <div class="nav-section">
          <h2>數論</h2>
          <a href="#" class="nav-item disabled">質因數分解</a>
          <a href="#" class="nav-item disabled">同餘方程</a>
        </div>
      </nav>
    </aside>

    <div class="main-content">
      <header class="top-bar" role="banner">
        <button class="menu-toggle" @click="toggleSidebar" aria-label="切換選單">
          <i class="mdi mdi-menu"></i>
        </button>
        <div class="user-section">
          <a href="#contact" @click.prevent="showContactModal" class="contact-link">
            <i class="mdi mdi-email"></i>
            聯絡資訊
          </a>
        </div>
      </header>

      <main role="main" aria-label="主要內容區">
        <article class="calculator-container">
          <QuadraticCalculator />
        </article>
      </main>
    </div>

    <!-- 聯絡資訊 Modal -->
    <div v-if="isContactModalVisible" class="modal-overlay" @click="isContactModalVisible = false">
      <div class="modal-content" @click.stop>
        <h3>聯絡資訊</h3>
        <div class="social-links">
          <a href="https://www.facebook.com/share/1F4hJ9PAgY/?mibextid=wwXIfr" target="_blank" class="social-link facebook">
            <i class="mdi mdi-facebook"></i>
            <span>Facebook</span>
          </a>
          <a href="https://www.instagram.com/justin_chien626?igsh=MXdmNGVsajhsY2pzbA%3D%3D&utm_source=qr" target="_blank" class="social-link instagram">
            <i class="mdi mdi-instagram"></i>
            <span>Instagram</span>
          </a>
          <a href="mailto:justin980626@example.com" class="social-link email">
            <i class="mdi mdi-email"></i>
            <span>Email</span>
          </a>
        </div>
        <button @click="isContactModalVisible = false">關閉</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import QuadraticCalculator from './components/QuadraticCalculator.vue'

const isSidebarOpen = ref(false)
const isContactModalVisible = ref(false)

const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const handleContainerClick = () => {
  if (isSidebarOpen.value) {
    isSidebarOpen.value = false
  }
}

const showContactModal = () => {
  isContactModalVisible.value = true
}
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
  min-height: 100vh;
}

.sidebar {
  width: 280px;
  background-color: #1a1f2c;
  color: #fff;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  overflow-y: auto;
  transition: transform 0.3s ease;
  z-index: 1000;
}

.sidebar-header {
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-logo {
  width: 32px;
  height: 32px;
}

.sidebar-nav {
  padding: 1.5rem 0;
}

.nav-section {
  margin-bottom: 2rem;
}

.nav-section h2 {
  padding: 0 1.5rem;
  font-size: 0.9rem;
  text-transform: uppercase;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.nav-item {
  display: block;
  padding: 0.75rem 1.5rem;
  color: #94a3b8;
  text-decoration: none;
  transition: all 0.3s ease;
}

.nav-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
  color: #fff;
}

.nav-item.active {
  background-color: #2563eb;
  color: #fff;
}

.nav-item.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.main-content {
  flex: 1;
  margin-left: 280px;
  min-height: 100vh;
  background-color: #f5f5f5;
  transition: margin-left 0.3s ease;
}

.top-bar {
  background-color: #fff;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #1a1f2c;
  cursor: pointer;
}

.user-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #1a1f2c;
  text-decoration: none;
  font-size: 0.9rem;
}

.contact-link i {
  font-size: 1.2rem;
}

.calculator-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  width: 100%;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2000;
}

.modal-content {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  max-width: 90%;
  width: 400px;
  text-align: center;
}

.modal-content h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.modal-content button {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  background-color: #2563eb;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.modal-content button:hover {
  background-color: #1d4ed8;
}

.social-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin: 1.5rem 0;
}

.social-link {
  display: flex;
  align-items: center;
  padding: 0.8rem 1.2rem;
  border-radius: 8px;
  color: white;
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 1.1rem;
}

.social-link i {
  font-size: 1.5rem;
  margin-right: 0.8rem;
}

.social-link.facebook {
  background-color: #3b5998;
}

.social-link.instagram {
  background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
}

.social-link.email {
  background-color: #2563eb;
}

.social-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar-open {
    transform: translateX(0);
  }

  .main-content {
    margin-left: 0;
  }

  .menu-toggle {
    display: block;
  }

  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
}
</style>
