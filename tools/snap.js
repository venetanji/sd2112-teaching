// Snapshot live p5.js sketches: the still that the PowerPoint and the PDF show where the html deck runs the sketch.
// usage: NODE_PATH=$(npm root -g) node tools/snap.js <page.html> <out.png> <canvas w> <canvas h> [more quadruples...]
// The still is taken 1.5 s after load with the mouse resting at 60 % / 40 % of the canvas, no click: design the
// sketch so that this resting state is a good picture. tools/snap.py drives this for whole decks.
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const args = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  for (let i = 0; i + 3 < args.length; i += 4) {
    const [file, out] = [args[i], args[i + 1]];
    const cw = Number(args[i + 2]), ch = Number(args[i + 3]);
    const page = await browser.newPage({ viewport: { width: cw, height: ch }, deviceScaleFactor: 2 });
    page.on('pageerror', e => console.log(`error in ${path.basename(file)}: ${String(e).slice(0, 200)}`));
    page.on('console', m => { if (m.type() === 'error') console.log(`console in ${path.basename(file)}: ${m.text().slice(0, 200)}`); });
    await page.goto('file://' + path.resolve(file) + '?snap', { waitUntil: 'load' });
    await page.waitForSelector('canvas', { timeout: 8000 }).catch(() => console.log(`no canvas in ${path.basename(file)}`));
    await page.mouse.move(Math.round(cw * 0.6), Math.round(ch * 0.4));
    await page.waitForTimeout(1500);
    const c = await page.$('canvas');
    if (c) await c.screenshot({ path: out, omitBackground: false }); else await page.screenshot({ path: out });
    console.log(`snap: ${path.basename(out)}`);
    await page.close();
  }
  await browser.close();
})();
