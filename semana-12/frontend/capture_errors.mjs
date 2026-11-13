import puppeteer from "puppeteer-core";
import fs from "node:fs";
import path from "node:path";

const outDir = "/home/antigravity/israelhuamanh/projects-dae/semana-12/docs/capturas";

async function run() {
  const browser = await puppeteer.launch({
    executablePath: "/usr/bin/google-chrome",
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu", "--window-size=1280,800"]
  });

  try {
    // 1. CORS error capture (http://127.0.0.1:5173/)
    console.log("Capturing Error CORS provocado (127.0.0.1 vs localhost)...");
    const pageCors = await browser.newPage();
    await pageCors.setViewport({ width: 1200, height: 800, deviceScaleFactor: 2 });
    await pageCors.goto("http://127.0.0.1:5173/", { waitUntil: "domcontentloaded" });
    // Wait for the banner-error showing CORS rejection
    await pageCors.waitForSelector(".banner-error", { timeout: 10000 });
    await pageCors.screenshot({ path: path.join(outDir, "captura_4_error_cors_provocado.png") });
    console.log("  Saved captura_4_error_cors_provocado.png");
    await pageCors.close();

    // 2. Server down / Network error with Delete button or 500 error
    console.log("Capturing Servidor Apagado / Falla de red en acción...");
    const pageDown = await browser.newPage();
    await pageDown.setViewport({ width: 1200, height: 800, deviceScaleFactor: 2 });
    await pageDown.goto("http://localhost:5173/", { waitUntil: "domcontentloaded" });
    await pageDown.waitForSelector("table", { timeout: 10000 });
    
    // Check 'Apagar el servidor'
    const downCheckbox = await pageDown.waitForSelector("fieldset.network-panel label:nth-of-type(1) input");
    await downCheckbox.click();

    // Now click 'Eliminar' on the first exam
    const deleteBtn = await pageDown.waitForSelector("table tbody tr:first-child button");
    await deleteBtn.click();

    // Wait for actionError banner to appear
    await pageDown.waitForSelector(".banner-error", { timeout: 5000 });
    await pageDown.screenshot({ path: path.join(outDir, "captura_6_error_servidor_apagado.png") });
    console.log("  Saved captura_6_error_servidor_apagado.png");
    await pageDown.close();

  } finally {
    await browser.close();
  }
}

run().catch(err => {
  console.error("Error:", err);
  process.exit(1);
});
