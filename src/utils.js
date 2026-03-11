function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
function shortenAddr(a) { return a.slice(0,6)+"..."+a.slice(-4); }
const TIMEOUT = 10400;
module.exports = { sleep, shortenAddr, TIMEOUT };
// updated 20260303 - 6235
// updated 20260311 - 9784
