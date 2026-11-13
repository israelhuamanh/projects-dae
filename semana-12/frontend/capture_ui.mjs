import puppeteer from "puppeteer-core";
import fs from "node:fs";
import path from "node:path";

const outDir = "/home/antigravity/israelhuamanh/projects-dae/semana-12/docs/capturas";
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

async function run() {
  const browser = await puppeteer.launch({
    executablePath: "/usr/bin/google-chrome",
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu", "--window-size=1280,800"]
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 800, deviceScaleFactor: 2 });

    console.log("1. Capturing Estado de Carga (Skeleton)...");
    // To reliably capture skeleton, let's navigate to localhost:5173
    // We can evaluate before unload or set slow network
    await page.goto("http://localhost:5173/", { waitUntil: "domcontentloaded" });
    // Wait for skeleton or trigger a slow reload
    const skeletonEl = await page.waitForSelector(".skeleton", { timeout: 3000 }).catch(() => null);
    if (skeletonEl) {
      await page.screenshot({ path: path.join(outDir, "captura_1_carga_skeleton.png") });
      console.log("  Saved captura_1_carga_skeleton.png");
    } else {
      console.log("  Skeleton went too fast, setting slow network and reloading...");
      // Click 'Red lenta' checkbox
      const slowBox = await page.waitForSelector("input[type=checkbox]:nth-of-type(2)");
      await slowBox.click();
      // Click Reintentar or reload
      await page.reload({ waitUntil: "domcontentloaded" });
      await page.waitForSelector(".skeleton");
      await page.screenshot({ path: path.join(outDir, "captura_1_carga_skeleton.png") });
      console.log("  Saved captura_1_carga_skeleton.png (slow mode)");
    }

    console.log("2. Capturing Datos Listados (Ready state)...");
    await page.waitForSelector("table", { timeout: 10000 });
    await page.screenshot({ path: path.join(outDir, "captura_2_cuestionarios_datos.png") });
    console.log("  Saved captura_2_cuestionarios_datos.png");

    console.log("3. Capturing Alta de Cuestionario (Examen Final DAE - Israel Huaman)...");
    const input = await page.waitForSelector("#exam-title");
    await input.type("Examen Final DAE - Israel Huaman");
    const submitBtn = await page.waitForSelector("button[type=submit]");
    await submitBtn.click();
    await page.waitForFunction(() => {
      const rows = Array.from(document.querySelectorAll("table tbody tr td"));
      return rows.some(td => td.textContent.includes("Israel Huaman"));
    }, { timeout: 10000 });
    await page.screenshot({ path: path.join(outDir, "captura_3_alta_cuestionario.png") });
    console.log("  Saved captura_3_alta_cuestionario.png");

    console.log("4. Capturing Error de Validación 400 (campo vacío)...");
    // Submit with empty title
    await input.click({ clickCount: 3 });
    await page.keyboard.press("Backspace");
    await submitBtn.click();
    await page.waitForSelector(".banner-error", { timeout: 5000 });
    await page.screenshot({ path: path.join(outDir, "captura_5_error_validacion_400.png") });
    console.log("  Saved captura_5_error_validacion_400.png");

    console.log("5. Capturing Servidor Apagado (Network Error + Reintentar)...");
    // Check 'Apagar el servidor'
    const downBox = await page.waitForSelector("fieldset.network-panel label:nth-of-type(1) input");
    const isDown = await page.evaluate(el => el.checked, downBox);
    if (!isDown) await downBox.click();
    // Click reload button or trigger request
    // Let's delete or reload
    // Let's reload page with server down
    await page.reload({ waitUntil: "networkidle0" });
    await page.waitForSelector(".banner-error", { timeout: 5000 });
    await page.screenshot({ path: path.join(outDir, "captura_6_error_servidor_apagado.png") });
    console.log("  Saved captura_6_error_servidor_apagado.png");

    console.log("6. Capturing Error CORS provocado (127.0.0.1 vs localhost)...");
    // Open http://127.0.0.1:5173/ where origin is not allowed in corsPolicy
    const page2 = await browser.newPage();
    await page2.setViewport({ width: 1200, height: 800, deviceScaleFactor: 2 });
    await page2.goto("http://127.0.0.1:5173/", { waitUntil: "networkidle0" });
    await page2.waitForSelector(".banner-error", { timeout: 5000 });
    await page2.screenshot({ path: path.join(outDir, "captura_4_error_cors_provocado.png") });
    console.log("  Saved captura_4_error_cors_provocado.png");
    await page2.close();

  } finally {
    await browser.close();
  }
}

run().catch(err => {
  console.error("Error running script:", err);
  process.exit(1);
});
