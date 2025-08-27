export async function runSOS(expr) {
  try {
    let res = await fetch("http://143.198.85.94:5000/sos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ expr })
    })
    
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`)
    }
    
    const data = await res.json()
    if (data.error) {
      throw new Error(data.error)
    }
    
    return data
  } catch (error) {
    console.error('API Error:', error)
    return { error: `計算出錯：${error.message}` }
  }
}
