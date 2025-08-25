<template>
  <nav class="navbar">
    <div class="navbar-brand">
    
      <h1>數學工具箱</h1>
    </div>
    <div class="navbar-menu">
      <a href="#home" class="navbar-item">首頁</a>
      <a href="#calculator" class="navbar-item">配方計算</a>
      <a href="#articles" class="navbar-item" @click.prevent="showDevelopingMessage">文章</a>
      <a href="#contact" class="navbar-item" @click.prevent="showContactModal">聯絡開發者</a>
    </div>
  </nav>

  <!-- 開發中提示 -->
  <div v-if="isDevelopingMessageVisible" class="modal-overlay" @click="isDevelopingMessageVisible = false">
    <div class="modal-content" @click.stop>
      <h3>功能開發中</h3>
      <p>此功能正在開發中，敬請期待！</p>
      <button @click="isDevelopingMessageVisible = false">關閉</button>
    </div>
  </div>

  <!-- 聯絡資訊 Modal -->
  <div v-if="isContactModalVisible" class="modal-overlay" @click="isContactModalVisible = false">
    <div class="modal-content" @click.stop>
      <h3>聯絡開發者</h3>
      <div class="social-links">
        <a href="https://github.com/yourusername" target="_blank" class="social-link">
          <i class="fab fa-github"></i> GitHub
        </a>
        <a href="https://www.linkedin.com/in/yourusername" target="_blank" class="social-link">
          <i class="fab fa-linkedin"></i> LinkedIn
        </a>
        <a href="mailto:your.email@example.com" class="social-link">
          <i class="fas fa-envelope"></i> Email
        </a>
      </div>
      <button @click="isContactModalVisible = false">關閉</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isDevelopingMessageVisible = ref(false)
const isContactModalVisible = ref(false)

const showDevelopingMessage = () => {
  isDevelopingMessageVisible.value = true
}

const showContactModal = () => {
  isContactModalVisible.value = true
}
</script>

<style scoped>
.navbar {
  padding: 1rem 2rem;
  background-color: #4a90e2;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar-brand h1 {
  margin: 0;
  font-size: 1.5rem;
}

.navbar-menu {
  display: flex;
  gap: 1.5rem;
}

.navbar-item {
  color: white;
  text-decoration: none;
  font-size: 1.1rem;
  transition: opacity 0.3s;
  cursor: pointer;
}

.navbar-item:hover {
  opacity: 0.8;
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
  background-color: #4a90e2;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.modal-content button:hover {
  background-color: #357abd;
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
  justify-content: center;
  gap: 0.5rem;
  padding: 0.8rem;
  background-color: #f5f5f5;
  border-radius: 4px;
  color: #2c3e50;
  text-decoration: none;
  transition: background-color 0.3s;
}

.social-link:hover {
  background-color: #e0e0e0;
}

@media (max-width: 768px) {
  .navbar {
    padding: 1rem;
  }

  .navbar-menu {
    gap: 1rem;
  }

  .navbar-item {
    font-size: 1rem;
  }

  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
}
</style>