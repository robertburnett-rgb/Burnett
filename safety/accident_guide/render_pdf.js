// Render guide.html to an A4 PDF and report any page whose content overflows the sheet.
// Usage: node render_pdf.js [out.pdf]
const path = require('path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  const src = path.join(__dirname, 'guide.html');
  const out = path.resolve(process.argv[2] || path.join(__dirname, '..', 'accident_investigation_guide.pdf'));
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + src, { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.evaluate(() => document.fonts.ready);

  const report = await page.evaluate(() =>
    [...document.querySelectorAll('.page')].map((p, i) => {
      const kids = [...p.children].filter(c => !c.classList.contains('pf'));
      const used = kids.reduce((h, c) => h + c.getBoundingClientRect().height, 0);
      const pf = p.querySelector('.pf').getBoundingClientRect().height;
      return { page: i + 1, sheet: Math.round(p.clientHeight), content: Math.round(used + pf), slack: Math.round(p.clientHeight - used - pf) };
    })
  );
  console.table(report);

  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('wrote', out);
})();
