// Screenshots of chosen slides of a built html deck, with the live sketches loaded (for checking them by eye).
// usage: NODE_PATH=$(npm root -g) node tools/shot.js _site/week03/index.html <outdir> 12 13 20
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [file, out, ...nums] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => console.log('page error:', String(e).slice(0, 200)));
  page.on('console', m => { if (m.type() === 'error') console.log('console:', m.text().slice(0, 200)); });
  await page.goto('file://' + path.resolve(file), { waitUntil: 'load' });
  await page.waitForFunction(() => window.Reveal && Reveal.isReady());
  await page.evaluate(() => document.fonts.ready);
  for (const n of nums) {
    await page.evaluate(i => Reveal.slide(i), Number(n) - 1);
    await page.waitForTimeout(400);
    const frames = await page.$$eval('.present iframe', fs => fs.map(f => f.getAttribute('src') || 'unloaded'));
    if (frames.length) {
      const fh = await page.$('.present .embed.sketch iframe');
      if (fh) {                                   // rest the mouse on the sketch so the still shows an interaction state
        const b = await fh.boundingBox();
        if (b) await page.mouse.move(b.x + b.width * 0.6, b.y + b.height * 0.4);
      }
      await page.waitForTimeout(2500);
    }
    await page.screenshot({ path: `${out}/slide-${String(n).padStart(2, '0')}.png` });
    console.log(`slide ${n}: ${frames.length ? 'iframes ' + frames.join(', ') : 'ok'}`);
  }
  await browser.close();
})();
