// One quiet oscillator feeds the audible output and the measured FFT.
const W = 1200, H = 700;
let ctx = null, oscillator = null, analyser = null;
let running = false, starting = false, generation = 0, frequency = 220, tone = 'sine';
let timeData, freqData, history = [], lastRow = 0;
const BINS = 72, ROWS = 42, LOW = 80, HIGH = 8000;
function setup() { createCanvas(W, H); textFont('monospace'); }
function label(s, x, y, size = 20) { noStroke(); fill('#000B1C'); textSize(size); text(s, x, y); }
function draw() {
  background(255);
  label('ONE SOUND / THREE VIEWS', 40, 35, 25);
  label('Waveform: signal amplitude over time (latest FFT window)', 40, 75);
  stroke('#CCDADA'); line(40, 145, 1160, 145);
  if (running && analyser) {
    analyser.getFloatTimeDomainData(timeData);
    analyser.getFloatFrequencyData(freqData);
    stroke('#246E70'); noFill(); beginShape();
    for (let i = 0; i < timeData.length; i++) vertex(40 + i * 1120 / (timeData.length - 1), 145 - timeData[i] * 1600);
    endShape();
    if (millis() - lastRow >= 60) {
      history.unshift(Array.from({length: BINS}, (_, i) => {
        const hz = LOW * Math.pow(HIGH / LOW, i / (BINS - 1));
        const bin = Math.min(freqData.length - 1, Math.round(hz * analyser.fftSize / ctx.sampleRate));
        // Display range is -100..-20 dBFS, not perceptual loudness.
        return constrain((freqData[bin] + 100) / 80, 0, 1);
      }));
      history = history.slice(0, ROWS); lastRow = millis();
    }
  }
  label('Spectrum: frequency (log scale) / relative level in dBFS', 40, 220);
  const current = history[0] || Array(BINS).fill(0);
  for (let i = 0; i < BINS; i++) {
    noStroke(); fill('#246E70'); rect(40 + i * 1120 / BINS, 330 - current[i] * 90, 1120 / BINS - 2, current[i] * 90);
  }
  for (const [hz, textLabel] of [[80,'80 Hz'],[220,'220'],[1000,'1k'],[8000,'8k']]) {
    const bin = Math.log(hz / LOW) / Math.log(HIGH / LOW) * (BINS - 1);
    textAlign(CENTER);
    label(textLabel, 40 + bin * 1120 / BINS + (1120 / BINS - 2) / 2, 355, 17);
    textAlign(LEFT);
  }
  label('Waterfall: older windows recede / peak height = relative level', 40, 395);
  // Perspective projection keeps axes legible without a WebGL dependency.
  for (let row = history.length - 1; row >= 0; row--) {
    const depth = row / (ROWS - 1), scale = 1 - depth * 0.28;
    stroke(36, 110, 112, 255 - depth * 120); noFill(); beginShape();
    for (let i = 0; i < BINS; i++) vertex(65 + depth * 135 + i * 1030 / (BINS - 1) * scale, 540 - depth * 95 - history[row][i] * 58);
    endShape();
  }
  label('NOW', 40, 565, 17); label('PAST', 1060, 440, 17);
  if (!running) label('Press PLAY to hear the signal and stream its analysis.', 180, 495, 24);
  const buttons = [[40,180,running?'STOP':'PLAY'],[245,145,'LOWER'],[405,145,'HIGHER'],[565,185,tone.toUpperCase()]];
  for (const [x,w,s] of buttons) { noStroke(); fill('#000B1C'); rect(x,585,w,44,5); fill(255); textSize(19); text(s,x+18,615); }
  label(frequency + ' Hz', 790, 615, 23);
  label('Quiet start / Escape stops / no microphone or recording', 40, 690, 17);
}
async function playAudio() {
  if (starting || running) return;
  starting = true;
  const token = ++generation;
  try {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    const local = ctx;
    await local.resume();
    if (generation !== token || ctx !== local || local.state === 'closed') return;
    oscillator = ctx.createOscillator(); const gain = ctx.createGain();
    analyser = ctx.createAnalyser(); analyser.fftSize = 2048; analyser.smoothingTimeConstant = 0;
    timeData = new Float32Array(analyser.fftSize); freqData = new Float32Array(analyser.frequencyBinCount);
    oscillator.type = tone; oscillator.frequency.value = frequency;
    gain.gain.setValueAtTime(0, ctx.currentTime); gain.gain.linearRampToValueAtTime(0.035, ctx.currentTime + 0.03);
    oscillator.connect(gain); gain.connect(analyser); analyser.connect(ctx.destination);
    history = []; oscillator.start(); running = true;
  } catch (error) {
    if (generation === token) stopAudio();
    console.error('Audio could not start', error);
  } finally { if (generation === token) starting = false; }
}
function stopAudio() {
  generation++; running = false; starting = false;
  if (ctx) ctx.close(); ctx = null; oscillator = null; analyser = null; history = [];
}
function mousePressed() {
  if (mouseY < 585 || mouseY > 629) return;
  if (mouseX >= 40 && mouseX < 220) { if (running || starting) stopAudio(); else playAudio(); }
  else if (mouseX >= 245 && mouseX < 550) {
    frequency = constrain(frequency * (mouseX < 390 ? 0.5 : 2), 110, 1760);
    if (oscillator) oscillator.frequency.setTargetAtTime(frequency, ctx.currentTime, 0.025);
  } else if (mouseX >= 565 && mouseX < 750) {
    tone = ['sine','triangle','sawtooth'][(['sine','triangle','sawtooth'].indexOf(tone) + 1) % 3];
    if (oscillator) oscillator.type = tone;
  }
}
function keyPressed() { if (keyCode === 27) stopAudio(); }
// Consume Escape before the embed forwards it to Reveal's overview handler.
window.addEventListener('keydown', e => {
  if (e.key === 'Escape') { stopAudio(); e.preventDefault(); e.stopImmediatePropagation(); }
}, true);
document.addEventListener('visibilitychange', () => { if (document.hidden) stopAudio(); });
window.addEventListener('pagehide', stopAudio);
window.addEventListener('message', e => { if (e.source === window.parent && e.data === 'slide:stop') stopAudio(); });
