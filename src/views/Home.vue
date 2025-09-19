<template>
  <div class="home">
    <header class="hero">
      <h1>數學工具箱</h1>
      <p>簡單、快速、準確的數學解題助手</p>
    </header>

    <main class="features">
      <div class="feature-section algebra">
        <h2>代數工具</h2>
        <div class="feature-content">
          <i class="mdi mdi-function-variant"></i>
          <p>處理方程式、多項式和矩陣運算</p>
          <router-link to="/sostools" class="feature-button">配方計算器</router-link>
          <router-link to="/lagrange" class="feature-button">拉格朗日計算器</router-link>
          <div class="coming-soon">
            <span>即將推出：</span>
            <ul>
              <li>多項式計算</li>
              <li>矩陣運算</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="feature-section geometry">
        <h2>幾何工具</h2>
        <div class="feature-content">
          <i class="mdi mdi-shape-polygon-plus"></i>
          <p>探索幾何圖形和三角函數</p>
          <div class="coming-soon">
            <span>即將推出：</span>
            <ul>
              <li>三角函數計算</li>
              <li>圓錐曲線繪製</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="feature-section number-theory">
        <h2>數論工具</h2>
        <div class="feature-content">
          <i class="mdi mdi-numeric"></i>
          <p>探索數的本質和規律</p>
          <div class="coming-soon">
            <span>即將推出：</span>
            <ul>
              <li>質因數分解</li>
              <li>同餘方程求解</li>
            </ul>
          </div>
        </div>
      </div>
    </main>

    <footer class="contact-section">
      <h3>聯絡我們</h3>
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
    </footer>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  document.title = '數學工具箱 - 您的數學解題助手'
})
</script>

<style scoped>
@import '@mdi/font/css/materialdesignicons.css';

.home {
  min-height: 100vh;
  background-color: #f8fafc;
}

.hero {
  text-align: center;
  padding: 3rem;
  background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
  color: white;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.25rem;
  opacity: 0.9;
}

.features {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
}

.feature-section {
  background: white;
  border-radius: 1rem;
  padding: 2rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.feature-section:hover {
  transform: translateY(-4px);
}

.feature-section h2 {
  color: #1e3a8a;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.feature-content {
  text-align: center;
}

.feature-content i {
  font-size: 3rem;
  color: #3b82f6;
  margin-bottom: 1rem;
}

.feature-content p {
  color: #64748b;
  margin-bottom: 1.5rem;
}

.feature-button {
  display: inline-block;
  background-color: #3b82f6;
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 0.5rem;
  text-decoration: none;
  transition: background-color 0.3s ease;
  margin-bottom: 1.5rem;
}

.feature-button:hover {
  background-color: #2563eb;
}

.coming-soon {
  background-color: #f1f5f9;
  padding: 1rem;
  border-radius: 0.5rem;
  text-align: left;
}

.coming-soon span {
  display: block;
  color: #64748b;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.coming-soon ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.coming-soon li {
  color: #94a3b8;
  padding: 0.25rem 0;
}

.contact-section {
  background-color: #1e293b;
  color: white;
  padding: 2rem;
  text-align: center;
}

.contact-section h3 {
  font-size: 1.5rem;
  margin-bottom: 2rem;
}

.social-links {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  max-width: 800px;
  margin: 0 auto;
}

.social-link {
  display: flex;
  align-items: center;
  padding: 0.8rem 1.2rem;
  border-radius: 0.5rem;
  color: white;
  text-decoration: none;
  transition: transform 0.3s ease;
}

.social-link i {
  font-size: 1.5rem;
  margin-right: 0.5rem;
}

.social-link.facebook {
  background-color: #1877f2;
}

.social-link.instagram {
  background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
}

.social-link.email {
  background-color: #3b82f6;
}

.social-link:hover {
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }

  .hero p {
    font-size: 1rem;
  }

  .features {
    grid-template-columns: 1fr;
    padding: 2rem 1rem;
  }

  .social-links {
    grid-template-columns: 1fr;
  }
}

  .feature-section {
    padding: 1.5rem;
  }

  .social-links {
    flex-direction: column;
    align-items: stretch;
  }

  .social-link {
    justify-content: center;
  }

</style>