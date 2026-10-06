// Build the published page: inline core.js into page.html at the /*CORE*/ marker.
// Usage: node build.js   (writes super-ihara-zeta-primer.html next to the sources)
const fs = require('fs'); const path = require('path'); const here = __dirname;
const core = fs.readFileSync(path.join(here, 'core.js'), 'utf8').replace(/if \(typeof module[^\n]*\n/, '');
const page = fs.readFileSync(path.join(here, 'page.html'), 'utf8');
fs.writeFileSync(path.join(here, 'super-ihara-zeta-primer.html'), page.replace('/*CORE*/', () => core));
console.log('built super-ihara-zeta-primer.html');
