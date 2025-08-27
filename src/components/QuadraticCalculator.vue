<template>
  <div class="calculator-container" id="calculator">
    <h2>配方計算器</h2>
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
        <button @click="appendInput('z')" style="color:#2c3e50">z</button>
        <button @click="appendInput('(')" style="color:#2c3e50">(</button>
        <button @click="appendInput(')')" style="color:#2c3e50">)</button>
        <button @click="clearInput()" style="color:#2c3e50">C</button>
      </div>
      
    </div>

    <button class="calculate-btn" @click="calculate">
      配方！
    </button>

    <!-- 範例方塊 -->
    <div class="examples">
     
      <div class="example-cards">
        <div class="example-card" @click="useExample('x^2 + 2*x + 1')">
          <div class="example-text">x² + 2x + 1</div>
          <div class="example-desc">單變數</div>
        </div>
        <div class="example-card" @click="useExample('(x + y)^2 +x+y+ 3')">
          <div class="example-text">(x + y)² + x + y + 3</div>
          <div class="example-desc">雙變數</div>
        </div>
        <div class="example-card" @click="useExample('(x^2+y^2+z^2)^2-3*(x^3*y+y^3*z+z^3*x)')">
          <div class="example-text">(x² + y² + z²)² - 3(x³y + y³z + z³x)</div>
          <div class="example-desc">三變數</div>
        </div>
      </div>
    </div>

    <div v-if="result" class="result">
      <div class="result-title">注意到＝</div>
      <div style="color:#2c3e50" class="result-field" v-html="renderedResult"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import katex from 'katex'
import 'katex/dist/katex.min.css'
import { runSOS } from '../api/m2.js'

const equation = ref('')
const result = ref('')

// 抓出 sosPoly solveSOS f 的結果
function extractSOSResult(raw) {
  if (!raw) return '請輸入多項式'

  try {
    // 提取 coefficients 部分
    const coeffMatch = raw.match(/coefficients\s*=>\s*{([^}]+)}/);
    if (!coeffMatch || !coeffMatch[1]) {
      console.error('無法提取 coefficients:', raw)
      return '無法解析結果，請檢查輸入格式'
    }
    const coefficients = coeffMatch[1].trim().split(',').map(c => c.trim())

    // 提取 generators 部分
    const genMatch = raw.match(/generators\s*=>\s*{([^}]+)}/);    
    if (!genMatch || !genMatch[1]) {
      console.error('無法提取 generators:', raw)
      return '無法解析結果，請檢查輸入格式'
    }

    const generators = genMatch[1].trim()
    if (!generators) {
      console.error('generators 為空')
      return '無法分解為平方和'
    }
    
    // 處理每個項，以逗號分隔
    let terms = generators.split(',')
    terms = terms.map((term, index) => {
      term = term.trim()
      if (!term) return null

      // ❌ 不要移除括號（這行移除）
      // term = term.replace(/^\(|\)$/g, '')

      // 分數係數 例如 (1/2)*x -> \frac{1}{2}x
      term = term.replace(/(\d+)\/(\d+)\*/g, (_, p1, p2) => `\\frac{${p1}}{${p2}}`)

      // 加減號（保持）
      term = term.replace(/\+/g, '+').replace(/-/g, '-')

      // 變量乘號去掉
      term = term.replace(/\*/g, '')

      // ✅ 外層用中括號，內層原括號保留
      term = `[${term}]^2`

      // 乘上對應的係數
      const coeff = coefficients[index]
      if (coeff && coeff !== '1') {
        if (coeff.includes('/')) {
          const [num, den] = coeff.split('/').map(s => s.trim())
          return `\\frac{${num}}{${den}}${term}`
        } else {
          return `${coeff}${term}`
        }
      }
      return term
    }).filter(Boolean)

    if (terms.length === 0) {
      console.error('沒有有效的項')
      return '解析結果為空，請檢查輸入'
    }

    return terms.join(' + ')
  } catch (error) {
    console.error('解析錯誤:', error, '\n原始輸出:', raw)
    return '解析結果時出錯，請檢查輸入格式'
  }
}


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
    result.value = '請輸入多項式'
    return
  }

  try {
    const res = await runSOS(equation.value)
    console.log('M2 輸出:', res)  // 添加日誌
    
    if (res.error && !res.output) {
      result.value = "錯誤：" + res.error
    } else if (res.output) {
      const cleaned = extractSOSResult(res.output)
      result.value = cleaned
    } else {
      result.value = '無法獲取計算結果'
    }
  } catch (err) {
    console.error('請求錯誤:', err)  // 添加錯誤日誌
    result.value = "錯誤：" + err.message
  }
}
</script>

<style scoped>
.calculator-container {
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  min-height: 100vh;
}

@media (min-width: 768px) {
  .calculator-container {
    width: 90%;
    max-width: 800px;
    margin: 5vh auto;
    min-height: auto;
  }
}

h2 {
  color: #2c3e50;
  text-align: center;
  margin-bottom: 1rem;
}

.input-container {
  margin-bottom: 1.5rem;
}

.math-input {
  width: 100%;
  min-height: 50px;
  font-size: 1.2rem;
  padding: 0.5rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  transition: border-color 0.3s;
}

.math-input:focus {
  border-color: #4a90e2;
  outline: none;
}

.calculate-btn {
  width: 100%;
  padding: 0.8rem;
  font-size: 1.1rem;
  color: white;
  background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.calculate-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(74, 144, 226, 0.3);
}

.calculate-btn:active {
  transform: translateY(0);
  box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3);
}

.calculate-btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 5px;
  height: 5px;
  background: rgba(255, 255, 255, 0.5);
  opacity: 0;
  border-radius: 100%;
  transform: scale(1, 1) translate(-50%);
  transform-origin: 50% 50%;
}

.calculate-btn:active::after {
  animation: ripple 1s ease-out;
}

@keyframes ripple {
  0% {
    transform: scale(0, 0);
    opacity: 0.5;
  }
  100% {
    transform: scale(100, 100);
    opacity: 0;
  }
}

.result {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #ffffff;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.result-title {
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.result-field {
  width: 100%;
  max-height: 300px;
  padding: 0.5rem;
  background-color: rgb(255, 255, 255);
  border-radius: 4px;
  overflow-x: auto;
  overflow-y: auto;
  word-wrap: break-word;
  line-height: 1.5;
}

/* 數學鍵盤樣式 */
.math-keyboard {
  margin: 1rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.keyboard-row {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
}

.keyboard-row button {
  width: 3rem;
  height: 3rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: white;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.2s;
}

.keyboard-row button:hover {
  background-color: #f5f5f5;
}

.keyboard-row button:active {
  background-color: #e0e0e0;
  transform: scale(0.95);
}

/* 範例方塊樣式 */
.examples {
  margin-top: 2rem;
}

.examples h3 {
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.example-cards {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  padding: 0.5rem;
  -webkit-overflow-scrolling: touch;
}

.example-card {
  flex: 0 0 auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s;
  background-color: white;
  min-width: 150px;
}

.example-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.example-text {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
  color: #2c3e50;
}

.example-desc {
  font-size: 0.9rem;
  color: #666;
}

@media (max-width: 768px) {
  .keyboard-row button {
    width: 2.5rem;
    height: 2.5rem;
    font-size: 1rem;
  }

  .example-cards {
    gap: 0.5rem;
  }

  .example-card {
    min-width: 120px;
    padding: 0.8rem;
  }

  .example-text {
    font-size: 1rem;
  }

  .example-desc {
    font-size: 0.8rem;
  }

  .result-field {
    max-height: 200px;
    font-size: 0.9rem;
  }
}
</style>