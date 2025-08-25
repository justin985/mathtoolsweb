export async function runSOS(expr) {
  let res = await fetch("/api/sos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ expr })
  })
  return await res.json()
}
