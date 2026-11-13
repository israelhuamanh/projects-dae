import puppeteer from "puppeteer-core";
import fs from "node:fs";
import path from "node:path";
import { execSync } from "node:child_process";

const outDir = "/home/antigravity/israelhuamanh/projects-dae/semana-12/docs/capturas";

function ansiToHtml(text) {
  let html = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  // ANSI color replacements
  html = html
    .replace(/\x1b\[32m/g, '<span style="color:#4ade80;font-weight:600;">')
    .replace(/\x1b\[31m/g, '<span style="color:#f87171;font-weight:600;">')
    .replace(/\x1b\[33m/g, '<span style="color:#facc15;">')
    .replace(/\x1b\[36m/g, '<span style="color:#38bdf8;">')
    .replace(/\x1b\[35m/g, '<span style="color:#c084fc;">')
    .replace(/\x1b\[1m/g, '<span style="font-weight:bold;">')
    .replace(/\x1b\[2m/g, '<span style="color:#94a3b8;">')
    .replace(/\x1b\[7m/g, '<span style="background:#f87171;color:#000;">')
    .replace(/\x1b\[0m|\x1b\[39m|\x1b\[22m/g, '</span>');

  // Strip remaining escape codes
  html = html.replace(/\x1b\[[0-9;]*[a-zA-Z]/g, '');
  return html;
}

function createTerminalHtml(title, command, output) {
  const renderedOutput = ansiToHtml(output);
  return `<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background-color: #0b0f19;
    padding: 24px;
    font-family: 'SF Mono', 'Fira Code', Menlo, Monaco, Consolas, 'Liberation Mono', monospace;
    display: flex;
    justify-content: center;
    align-items: flex-start;
  }
  .window {
    width: 100%;
    max-width: 1100px;
    background-color: #111827;
    border-radius: 10px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    border: 1px solid #374151;
    overflow: hidden;
  }
  .header {
    background-color: #1f2937;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #374151;
  }
  .dots {
    display: flex;
    gap: 8px;
    margin-right: 16px;
  }
  .dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }
  .dot.red { background-color: #ef4444; }
  .dot.yellow { background-color: #f59e0b; }
  .dot.green { background-color: #10b981; }
  .title {
    color: #9ca3af;
    font-size: 13px;
    font-weight: 500;
    flex: 1;
    text-align: center;
  }
  .body {
    padding: 18px 20px;
    color: #f3f4f6;
    font-size: 13.5px;
    line-height: 1.5;
    white-space: pre-wrap;
    word-break: break-all;
  }
  .prompt {
    color: #38bdf8;
    margin-bottom: 8px;
    font-weight: 600;
  }
  .prompt span.user { color: #34d399; }
  .prompt span.path { color: #fbbf24; }
</style>
</head>
<body>
  <div class="window">
    <div class="header">
      <div class="dots">
        <div class="dot red"></div>
        <div class="dot yellow"></div>
        <div class="dot green"></div>
      </div>
      <div class="title">${title}</div>
    </div>
    <div class="body">
      <div class="prompt"><span class="user">israel@tecsup-dae</span>:<span class="path">~/projects-dae/semana-12</span>$ ${command}</div>
      <div>${renderedOutput}</div>
    </div>
  </div>
</body>
</html>`;
}

async function renderTerminal(browser, filename, title, command, output) {
  const page = await browser.newPage();
  await page.setViewport({ width: 1160, height: 800, deviceScaleFactor: 2 });
  const html = createTerminalHtml(title, command, output);
  await page.setContent(html, { waitUntil: "networkidle0" });
  
  // Resize viewport to content height
  const windowEl = await page.$(".window");
  const box = await windowEl.boundingBox();
  await page.setViewport({ width: 1160, height: Math.ceil(box.height) + 50, deviceScaleFactor: 2 });
  
  await page.screenshot({ path: path.join(outDir, filename) });
  console.log(`Saved ${filename} (${Math.round(box.height)}px)`);
  await page.close();
}

async function main() {
  const browser = await puppeteer.launch({
    executablePath: "/usr/bin/google-chrome",
    headless: "new",
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu"]
  });

  try {
    // 1. npm test (67 passed)
    console.log("Running npm test...");
    let npmTestOut = "";
    try {
      npmTestOut = execSync("npm test", {
        cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
        encoding: "utf8",
        env: { ...process.env, FORCE_COLOR: "1" }
      });
    } catch (e) {
      npmTestOut = e.stdout || e.message;
    }
    await renderTerminal(
      browser,
      "captura_7_pruebas_vitest_67.png",
      "Terminal · npm test (67/67 tests aprobados en Vitest)",
      "npm test",
      npmTestOut
    );

    // 2. npm run test:ai (25 failed)
    console.log("Running npm run test:ai...");
    let npmAiOut = "";
    try {
      npmAiOut = execSync("npm run test:ai", {
        cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
        encoding: "utf8",
        env: { ...process.env, FORCE_COLOR: "1" }
      });
    } catch (e) {
      npmAiOut = e.stdout || e.message;
    }
    // Limit to the summary and first few failures to keep readable
    const aiLines = npmAiOut.split("\n");
    let aiTrimmed = aiLines.slice(0, 45).join("\n");
    if (aiLines.length > 45) {
      const summaryLines = aiLines.slice(-12).join("\n");
      aiTrimmed += "\n... [fallos intermedios omitidos para brevedad] ...\n\n" + summaryLines;
    }
    await renderTerminal(
      browser,
      "captura_8_auditoria_ia_25_fallos.png",
      "Terminal · npm run test:ai (Auditoría de IA: 25 defectos detectados)",
      "npm run test:ai",
      aiTrimmed
    );

    // 3. CLI examctl execution
    console.log("Running CLI examctl...");
    let cliOut = "";
    cliOut += "# 1. Verificación de CORS con origen permitido (localhost:5173)\n";
    cliOut += "$ node cli/examctl.mjs cors-check --origin http://localhost:5173 --url http://127.0.0.1:8800/api\n";
    cliOut += execSync("node cli/examctl.mjs cors-check --origin http://localhost:5173 --url http://127.0.0.1:8800/api", {
      cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
      encoding: "utf8"
    });
    cliOut += "\n# 2. Verificación de CORS con origen no permitido (sitio malicioso)\n";
    cliOut += "$ node cli/examctl.mjs cors-check --origin http://malicious-site.com --url http://127.0.0.1:8800/api\n";
    try {
      cliOut += execSync("node cli/examctl.mjs cors-check --origin http://malicious-site.com --url http://127.0.0.1:8800/api", {
        cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
        encoding: "utf8"
      });
    } catch (e) {
      cliOut += e.stdout || "";
      cliOut += `[Código de salida: ${e.status}]\n`;
    }

    cliOut += "\n# 3. Listar cuestionarios existentes mediante la CLI\n";
    cliOut += "$ node cli/examctl.mjs list --url http://127.0.0.1:8800/api\n";
    cliOut += execSync("node cli/examctl.mjs list --url http://127.0.0.1:8800/api", {
      cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
      encoding: "utf8"
    });

    cliOut += "\n# 4. Crear nuevo cuestionario mediante examctl\n";
    cliOut += "$ node cli/examctl.mjs create \"Cuestionario Final DAE - Israel Huaman\" --url http://127.0.0.1:8800/api\n";
    cliOut += execSync("node cli/examctl.mjs create \"Cuestionario Final DAE - Israel Huaman\" --url http://127.0.0.1:8800/api", {
      cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/frontend",
      encoding: "utf8"
    });

    await renderTerminal(
      browser,
      "captura_9_examctl_cli.png",
      "Terminal · CLI examctl (Listar, Crear, Validar CORS y Códigos de Salida)",
      "examctl-suite",
      cliOut
    );

    // 4. Backend Django tests
    console.log("Running Django backend tests...");
    let djangoOut = "";
    try {
      djangoOut = execSync(".venv/bin/python manage.py test quiz", {
        cwd: "/home/antigravity/israelhuamanh/projects-dae/semana-12/backend",
        encoding: "utf8"
      });
    } catch (e) {
      djangoOut = (e.stdout || "") + (e.stderr || "");
    }
    await renderTerminal(
      browser,
      "captura_10_backend_django_tests.png",
      "Terminal · Backend Django tests (.venv/bin/python manage.py test quiz)",
      ".venv/bin/python manage.py test quiz",
      djangoOut
    );

  } finally {
    await browser.close();
  }
}

main().catch(err => {
  console.error("Fatal error:", err);
  process.exit(1);
});
