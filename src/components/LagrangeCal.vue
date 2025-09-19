<template>
  <div class="calculator-container" id="calculator">
    <h2>拉格朗日乘數計算器</h2>
    <div class="input-container">
      <input
        v-model="equation"
        class="math-input"
        type="text"
        placeholder="輸入方程式"
      />
    </div>
    
    <!-- 數學鍵盤 -->
    <div class="math-keyboard">
      <div class="keyboard-row">
        <button @click="appendInput('+')" style="color:#2c3e50">+</button>
        <button @click="appendInput('-')" style="color:#2c3e50">-</button>
        <button @click="appendInput('*')" style="color:#2c3e50">*</button>
        <button @click="appendInput('/')" style="color:#2c3e50">/</button>
        <button @click="appendInput('^')" style="color:#2c3e50">^</button>
        <button @click="appendInput('^2')" style="color:#2c3e50">²</button>
      </div>
      <div class="keyboard-row">
        <button @click="appendInput('x')" style="color:#2c3e50">x</button>
        <button @click="appendInput('y')" style="color:#2c3e50">y</button>
        <button @click="appendInput('λ')" style="color:#2c3e50">λ</button>
        <button @click="appendInput('(')" style="color:#2c3e50">(</button>
        <button @click="appendInput(')')" style="color:#2c3e50">)</button>
        <button @click="clearInput()" style="color:#2c3e50">C</button>
      </div>
    </div>

    <button class="calculate-btn" @click="calculate">
      計算！
    </button>

    <!-- 範例方塊 -->
    <div class="examples">
      <div class="example-cards">
        <div class="example-card" @click="useExample('x^2 + y^2')">
          <div class="example-text">x² + y²</div>
          <div class="example-desc">目標函數</div>
        </div>
        <div class="example-card" @click="useExample('x + y - 1')">
          <div class="example-text">x + y - 1 = 0</div>
          <div class="example-desc">約束條件</div>
        </div>
      </div>
    </div>

    <div v-if="result" class="result">
      <div class="result-title">結果</div>
      <div style="color:#2c3e50" class="result-field" v-html="renderedResult"></div>
    </div>

    <!-- 常見問題 -->
    <div class="faq-section">
      <h3>常見問題</h3>
      <div class="faq-items">
        <div class="faq-item">
          <h4>如何使用？</h4>
          <p>1. 輸入目標函數</p>
          <p>2. 輸入約束條件</p>
          <p>3. 點擊計算按鈕</p>
        </div>
        <div class="faq-item">
          <h4>支援哪些輸入格式？</h4>
          <p>1. 變數：使用 x, y, λ 表示</p>
          <p>2. 指數：使用 ^ 符號，如 x^2 表示 x²</p>
          <p>3. 乘法：使用 * 符號，如 2*x 表示 2x</p>
          <p>4. 可以使用括號 ( ) 來分組</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import katex from 'katex'
import 'katex/dist/katex.min.css'

const equation = ref('')
const result = ref('')

// KaTeX 渲染
const renderedResult = computed(() => {
  if (!result.value) return ''
  try {
    return katex.renderToString(result.value, {
      throwOnError: false,
      displayMode: true
    })
  } catch {
    return result.value
  }
})

const appendInput = (value) => {
  equation.value += value
}

const clearInput = () => {
  equation.value = ''
}

const useExample = (example) => {
  equation.value = example
}

const calculate = async () => {
  if (!equation.value.trim()) {
    result.value = '請輸入方程式'
    return
  }

  try {
    // TODO: 實現拉格朗日乘數法計算邏輯
    result.value = '計算結果將在這裡顯示'
  } catch (err) {
    console.error('計算錯誤:', err)
    result.value = "錯誤：" + err.message
  }
}
</script>

<style scoped>
.calculator-container {
  width: 100%;
  max-width: 600px;
  margin: 200px auto 0 auto;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  min-height: calc(100vh - 70px);
}

.input-container {
  margin-bottom: 1rem;
}

.math-input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1.1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.math-keyboard {
  margin-bottom: 1rem;
}

.keyboard-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.keyboard-row button {
  flex: 1;
  margin: 0 0.25rem;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  cursor: pointer;
}

.calculate-btn {
  width: 100%;
  padding: 0.75rem;
  font-size: 1.1rem;
  color: white;
  background: #2c3e50;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 1rem;
}

.examples {
  margin: 1rem 0;
}

.example-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
}

.example-card {
  padding: 1rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  cursor: pointer;
}

.example-text {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}

.example-desc {
  font-size: 0.9rem;
  color: #666;
}

.result {
  margin: 1rem 0;
  padding: 1rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
}

.result-title {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.faq-section {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
}

.faq-section h3 {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  text-align: center;
  font-size: 1.4rem;
}

.faq-items {
  display: grid;
  gap: 1.5rem;
}

.faq-item h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.faq-item p {
  color: #666;
  margin: 0.25rem 0;
}
</style>