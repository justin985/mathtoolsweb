<template>
  <nav class="navbar">
    <div class="navbar-brand">
      <h1>數學工具箱</h1>
    </div>
    <div class="navbar-menu">
      <a href="#home" class="navbar-item">首頁</a>
      <a href="#calculator" class="navbar-item">配方</a>
      <a href="#articles" class="navbar-item" @click.prevent="showDevelopingMessage">文章</a>
      <a href="#contact" class="navbar-item" @click.prevent="showContactModal">聯絡資訊</a>
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
  background-color: #4a90e2;
}

.social-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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