export async function runSOS(expr) {
  let res = await fetch("http://143.198.85.94:5000/sos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ expr })
  })
  return await res.json()
}
