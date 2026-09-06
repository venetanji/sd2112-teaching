"""
SD2112 · Artificial Intelligence in Design · Week 06 — the slide spec.

    python deck/week06.py            # builds _site/week06/ (html deck + pdf), export/week06*.pptx, export/preview/
    python deck/week06.py --html     # only the html deck
    python tools/build_all.py        # everything, as the GitHub Actions workflows run it

Sound machines: what a machine hears (a waveform, a spectrogram, MIDI), rules that play (a step
sequencer, the Illiac Suite's generate-and-test and its Markov table), models that listen (a picture
of sound, a language of sound; Suno, AIVA, Udio), voices and who owns a sound (three cases, two years
of lawsuits), a sound spec for a product, the activity "Thirty seconds for a product", a mock quiz of
eight questions spread through the second half, the reflection draft check and Challenge 5.
Four live p5.js sketches with sound (a spectrogram of the microphone, additive timbre, a sequencer, a
Markov melody) run in the html deck; the pptx and the PDF show their snapshots. Thirteen ClassPoint activities (the
recap, the vote, eight mock questions, three captures); the three chapter quick checks are a show of hands.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'tools'))

import figures_week06 as F                              # noqa: E402
from deckgen import build_all, INK, WHITE, PAPER, TEAL, ORANGE, VIOLET, PINK, YELLOW, YELLOWS, VIOLETS, TEALS, ORANGES, PINKS, MUTED  # noqa: E402
from layouts import (title, end, agenda, section, statement, quote, content, cards, question, timeline,   # noqa: E402
                     journey, activity, video, two_col, figure_slide, code_slide, sketch_slide, live, finalize)
from course import SITE, PLAYLIST, GENAI, JOURNEY, footer  # noqa: E402

FOOTER = footer(6)

# ───────────────────────── the live sketches (p5.js, with p5.sound) ─────────────────────────
# Audio starts on the first click (userStartAudio: the browser's rule). Before the click every sketch draws
# its picture silently, so the snapshot the pptx and the PDF use is never empty.

# (a) a spectrogram of the microphone: time across, frequency up (log scale), loudness as darkness
SPECTRO_CODE = """// a live spectrogram: time across, frequency up (log scale), loudness as darkness
const W = 1400, H = 500, ROWS = 120, COLS = 432;      // the picture: 120 rows of frequency, 432 slices of time
const LO = 50, HI = 8000;                             // the vertical axis, in Hz
const X0 = 80, X1 = W - 24, Y0 = 108, Y1 = H - 48;    // the picture; the waveform strip sits above it
let spec, fft, mic, osc, mode = 'demo', t = 0, lastLoud = 0, moved = false, SPEC = [];
let status = 'click to start: your microphone, or a built-in sweep';

function setup() {
  createCanvas(W, H); pixelDensity(1); frameRate(30);
  spec = createGraphics(COLS, ROWS); spec.pixelDensity(1); spec.background(244);   // small; drawn scaled up
  for (let i = 0; i < COLS; i++) { t++; pushColumn(demoAmp); }   // pre-filled: never an empty picture
}

function rowFreq(r) { return LO * pow(HI / LO, r / (ROWS - 1)); }     // row 0 = 50 Hz, row 119 = 8 kHz
function freqY(f) { return Y1 - (Y1 - Y0) * log(f / LO) / log(HI / LO); }
function yFreq(y) { return LO * pow(HI / LO, (Y1 - constrain(y, Y0, Y1)) / (Y1 - Y0)); }

function demoF0() { return 180 * pow(2, 1.6 * pow(abs(sin(t / 60)), 1.2)); }   // a tone rising and falling
function demoAmp(r) {                                   // its harmonics, as one slice of a spectrogram
  let f = rowFreq(r), a = 0.05, f0 = demoF0();
  for (let k = 1; k <= 4; k++) { let d = abs(log(f / (f0 * k))) / 0.06; a += exp(-d * d) / k; }
  return a;
}
function liveAmp(r) {                                   // the FFT of the microphone (or of the sweep)
  let i = round(rowFreq(r) / (sampleRate() / 2) * SPEC.length);
  return constrain(SPEC[i] / 255 * 1.5, 0, 1);
}

function pushColumn(ampOf) {   // scroll the picture left by one slice, paint one new slice at the right edge
  spec.loadPixels();
  let p = spec.pixels, w = spec.width;
  for (let y = 0; y < ROWS; y++) {              // one pixel per row and slice: 432 × 120, cheap to move
    let s = y * w * 4; p.copyWithin(s, s + 4, s + w * 4);
    let v = 244 - constrain(ampOf(ROWS - 1 - y), 0, 1) * 244;   // dark = loud; low frequencies at the bottom
    let i = (y * w + w - 1) * 4; p[i] = p[i + 1] = p[i + 2] = v; p[i + 3] = 255;
  }
  spec.updatePixels();
}

function draw() {
  t++;
  if (mode === 'demo') pushColumn(demoAmp);
  else { SPEC = fft.analyze(); pushColumn(liveAmp); }
  if (mode === 'mic' && mic.getLevel() > 0.01) lastLoud = millis();
  if (mode === 'mic' && millis() - lastLoud > 3000) sweep('quiet for 3 s: a built-in sweep instead');
  if (mode === 'sweep') osc.freq(moved ? yFreq(mouseY) : 200 * pow(2, 2.5 * (0.5 + 0.5 * sin(t / 45))), 0.05);
  background(255);
  image(spec, X0, Y0, X1 - X0, Y1 - Y0);       // the small buffer, scaled to the picture
  waveform(); axes(); readout();
}

function waveform() {           // the strip on top: the last few hundred samples, pressure over time
  let wf = mode === 'demo' ? null : fft.waveform();
  stroke(0, 11, 28); strokeWeight(1.5); noFill();
  beginShape();
  for (let i = 0; i < 400; i++) {
    let v = wf ? wf[floor(i / 400 * wf.length)] : demoWave(i);
    vertex(X0 + i / 400 * (X1 - X0), 58 - v * 30);
  }
  endShape();
}
function demoWave(i) { let f0 = demoF0(), s = 0; for (let k = 1; k <= 4; k++) s += sin(TWO_PI * f0 * k * i * 3 / 44100) / k; return s / 2; }

function axes() {
  noStroke(); fill(90); textFont('JetBrains Mono'); textSize(14); textAlign(LEFT, BASELINE);
  fill(237, 109, 36); text('WAVEFORM · pressure over time', X0, 24);
  text('SPECTROGRAM · time across · frequency up · dark = loud', X0, Y0 - 12);
  fill(90); textAlign(RIGHT, CENTER);
  for (let f of [100, 200, 500, 1000, 2000, 5000]) {
    let y = freqY(f); stroke(200); line(X0 - 6, y, X0, y); noStroke();
    text(f >= 1000 ? f / 1000 + ' kHz' : f + ' Hz', X0 - 10, y);
  }
  textAlign(LEFT, BASELINE); text('time →', X0, H - 18);
  textAlign(RIGHT, BASELINE); text(status, X1, 24);
}

function readout() {            // mouse y = a frequency, and the nearest note
  if (mouseY < Y0 || mouseY > Y1) return;
  let f = yFreq(mouseY);
  stroke(237, 109, 36); strokeWeight(1.5); line(X0, mouseY, X1, mouseY);
  noStroke(); fill(237, 109, 36); textSize(16); textAlign(RIGHT, BOTTOM);
  text('≈ ' + round(f) + ' Hz · ' + noteName(f), X1 - 8, mouseY - 4);
}
function noteName(f) {
  const N = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
  let m = round(69 + 12 * log(f / 440) / log(2));          // MIDI number: A4 = 69 = 440 Hz
  return N[((m % 12) + 12) % 12] + (floor(m / 12) - 1);
}

function mouseMoved() { moved = true; }
function mousePressed() {       // audio starts on a click
  if (mode !== 'demo') return;
  userStartAudio();
  fft = new p5.FFT(0.8, 1024);
  status = 'asking for the microphone…';
  try {
    mic = new p5.AudioIn();
    mic.start(() => { fft.setInput(mic); mode = 'mic'; lastLoud = millis() + 1500; status = 'microphone: live · speak, whistle, clap'; },
              () => sweep('no microphone: a built-in sweep'));
  } catch (e) { mic = null; sweep('no microphone here: a built-in sweep'); }
}
function sweep(why) {           // the fallback: a sawtooth that sweeps, or follows the mouse
  if (mic) mic.stop();
  osc = new p5.Oscillator('sawtooth'); osc.amp(0.12); osc.start(); fft.setInput(osc);
  mode = 'sweep'; status = why + ' · mouse y = its pitch';
}"""

# (b) additive synthesis: a timbre is which harmonics, and how loud
ADD_CODE = """// a timbre is which harmonics, and how loud: mouse x = how many, mouse y = how fast they fade
const W = 1400, H = 500, F0 = 220, MAX = 16;
let oscs = [], on = false, moved = false;

function setup() { createCanvas(W, H); frameRate(30); }

function harmonics() {                                   // the recipe of the sound
  let n = moved ? floor(map(mouseX, 0, W, 1, MAX + 0.99)) : 6;       // how many sines: 1 .. 16
  let fall = moved ? map(mouseY, 0, H, 0.4, 2.2) : 1.2;               // how fast they fade: 1 / k^fall
  let amps = [];
  for (let k = 1; k <= n; k++) amps.push(1 / pow(k, fall));
  return amps;
}

function draw() {
  background(255); let amps = harmonics(), sum = amps.reduce((a, b) => a + b);
  textFont('JetBrains Mono'); noStroke(); fill(237, 109, 36); textSize(14); textAlign(LEFT, BASELINE);
  text('THE WAVE · the sines added up · 9 ms', 40, 30);
  text('THE SPECTRUM · one bar per sine', 820, 30);
  // left: the summed wave, two cycles of 220 Hz
  stroke(225); line(40, 240, 760, 240);
  stroke(0, 11, 28); strokeWeight(2); noFill(); beginShape();
  for (let i = 0; i <= 720; i++) {
    let t = i / 720 * 2 / F0, s = 0;
    for (let k = 0; k < amps.length; k++) s += amps[k] * sin(TWO_PI * F0 * (k + 1) * t);
    vertex(40 + i, 240 - s / sum * 150);
  }
  endShape();
  // right: the spectrum
  for (let k = 0; k < MAX; k++) {
    let x = 820 + k * 34, a = k < amps.length ? amps[k] : 0;
    noStroke(); fill(k < amps.length ? color(0, 11, 28) : color(225));
    rect(x, 400 - a * 300, 24, a * 300 + 1);
    fill(90); textSize(12); textAlign(CENTER, BASELINE); text((k + 1) * F0, x + 12, 420);
  }
  fill(90); textSize(14); textAlign(LEFT, BASELINE); text('Hz', 820 + MAX * 34 + 4, 420);
  fill(0, 11, 28); textSize(16);
  text(amps.length + (amps.length > 1 ? ' harmonics' : ' harmonic: a sine') + ' · amplitude of harmonic k = 1 / k^' + nf(moved ? map(mouseY, 0, H, 0.4, 2.2) : 1.2, 1, 1), 40, 440);
  fill(90); textSize(14);
  text(amps.length == 1 ? 'one sine: the purest tone there is, and the dullest' : amps.length < 5 ? 'few, fast-fading harmonics: soft, flute-like' : amps.length < 11 ? 'more harmonics: brighter, reedier' : 'many harmonics: buzzing, saw-like', 40, 466);
  textAlign(RIGHT, BASELINE); text(on ? 'playing · move the mouse' : 'click to hear it', W - 40, 30);
  if (on) for (let k = 0; k < MAX; k++) oscs[k].amp(k < amps.length ? 0.35 * amps[k] / sum : 0, 0.05);
}

function mouseMoved() { moved = true; }
function mousePressed() {                                // sixteen sines, started once, then only their volumes change
  if (on) return;
  userStartAudio();
  for (let k = 1; k <= MAX; k++) { let o = new p5.Oscillator(F0 * k, 'sine'); o.amp(0); o.start(); oscs.push(o); }
  on = true;
}"""

# (c) a step sequencer: the grid is the score
SEQ_HEAD = """// a step sequencer: the grid is the score. 16 steps x 6 rows; the rule reads it left to right, forever
const STEPS = 16, ROWS = ['kick', 'snare', 'hat', 'bass C2', 'C4', 'E4'];
const HZ = [0, 0, 0, 65.41, 261.63, 329.63];           // the pitched rows, in Hz
const X0 = 140, Y0 = 90, CS = 50;                      // where the grid sits, and the cell size
let grid, step = -1, nextAt = 0, bpm = 120, on = false, moved = false;
let kick, kickEnv, snare, snareEnv, hat, hatEnv, voices = [], envs = [];

function setup() {
  createCanvas(1000, 600); frameRate(60);
  grid = ROWS.map(() => Array(STEPS).fill(false));
  seed();
}
function seed() {                                      // a pattern to start from: a rule you can hear
  for (let s of [0, 4, 8, 12]) grid[0][s] = true;
  for (let s of [4, 12]) grid[1][s] = true;
  for (let s = 0; s < STEPS; s += 2) grid[2][s] = true;
  for (let s of [0, 7, 10]) grid[3][s] = true;
  for (let s of [0, 3, 6, 11]) grid[4][s] = true;
  for (let s of [2, 9, 14]) grid[5][s] = true;
}
"""

SEQ_STEP = """function draw() {                    // the clock
  if (moved) bpm = round(map(mouseY, 0, height, 180, 60));
  let dur = 60000 / bpm / 4;         // a 16th note, in ms
  if (millis() >= nextAt) {          // time for the next step
    step = (step + 1) % STEPS;    // left to right, again
    nextAt = max(nextAt + dur, millis() - 100);
    for (let r = 0; r < 6; r++)   // every row: on this step?
      if (grid[r][step]) play(r);    // then this sound
  }
  picture();
}"""

SEQ_REST = """
function play(r) {                                     // the sounds: an envelope on a noise or an oscillator
  if (!on) return;
  if (r == 0) { kick.freq(150); kick.freq(45, 0.12); kickEnv.play(kick); }
  else if (r == 1) { snareEnv.play(snare); }
  else if (r == 2) { hatEnv.play(hat); }
  else { envs[r - 3].play(voices[r - 3]); }
}

function picture() {
  background(255);
  textFont('JetBrains Mono'); noStroke(); textAlign(LEFT, BASELINE);
  fill(237, 109, 36); textSize(16); text('THE GRID IS THE SCORE · 16 STEPS × 6 SOUNDS', X0, 40);
  fill(0, 11, 28); textSize(40); textAlign(RIGHT, BASELINE); text(bpm + ' BPM', width - 40, 52);
  for (let r = 0; r < 6; r++) {
    fill(0, 11, 28); textSize(16); textAlign(RIGHT, CENTER); text(ROWS[r], X0 - 14, Y0 + r * CS + CS / 2);
    for (let s = 0; s < STEPS; s++) {
      let x = X0 + s * CS, y = Y0 + r * CS, onCell = grid[r][s];
      stroke(s == step ? color(0, 11, 28) : color(225)); strokeWeight(s == step ? 3 : 1);
      fill(onCell ? (r < 3 ? color(237, 109, 36) : color(100, 194, 195)) : (s == step ? color(244) : color(255)));
      rect(x + 3, y + 3, CS - 6, CS - 6, 4);
    }
  }
  noStroke(); fill(90); textSize(14); textAlign(LEFT, BASELINE);
  for (let b = 0; b < 4; b++) text('beat ' + (b + 1), X0 + b * 4 * CS + 4, Y0 + 6 * CS + 24);
  fill(0, 11, 28); textSize(16);
  text('a step = 60 / ' + bpm + ' / 4 s = ' + round(60000 / bpm / 4) + ' ms · a bar = ' + nf(16 * 60 / bpm / 4, 1, 2) + ' s', X0, Y0 + 6 * CS + 64);
  fill(90); textSize(14);
  text(on ? 'click a cell to toggle it · mouse y = tempo · C clears the grid' : 'click to start the sound · then click cells · mouse y = tempo · C clears', X0, Y0 + 6 * CS + 92);
}

function mouseMoved() { moved = true; }
function mousePressed() {
  if (!on) { userStartAudio(); build(); on = true; return; }   // the first click only starts the sound
  let s = floor((mouseX - X0) / CS), r = floor((mouseY - Y0) / CS);
  if (s >= 0 && s < STEPS && r >= 0 && r < 6) grid[r][s] = !grid[r][s];
}
function keyPressed() { if (key == 'c' || key == 'C') { for (let g of grid) g.fill(false); return false; } }

function build() {                                     // the instruments, made once
  kick = new p5.Oscillator(150, 'sine'); kick.amp(0); kick.start();
  kickEnv = new p5.Envelope(0.001, 0.18, 0, 0.05); kickEnv.setRange(0.9, 0);
  snare = new p5.Noise('white'); snare.amp(0); snare.start();
  snareEnv = new p5.Envelope(0.001, 0.12, 0, 0.05); snareEnv.setRange(0.5, 0);
  hat = new p5.Noise('white'); hat.amp(0); hat.start();
  hatEnv = new p5.Envelope(0.001, 0.035, 0, 0.02); hatEnv.setRange(0.18, 0);
  for (let i = 3; i < 6; i++) {
    let o = new p5.Oscillator(HZ[i], i == 3 ? 'square' : 'triangle'); o.amp(0); o.start(); voices.push(o);
    let e = new p5.Envelope(0.005, 0.12, 0.25, 0.15); e.setRange(i == 3 ? 0.18 : 0.28, 0); envs.push(e);
  }
}"""

SEQ_CODE = SEQ_HEAD + '\n' + SEQ_STEP + '\n' + SEQ_REST

# (d) a Markov melody: eight pitches, a hand-written table — the Illiac Suite's fourth experiment in a page
MARKOV_TABLE = """const NOTES = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5'];
const TABLE = [        // row = the last note, column = the next
  [20, 40, 20,  5, 10,  2,  1,  2],   // after C4: mostly D4
  [15, 15, 40, 15, 10,  3,  1,  1],   // after D4: mostly E4
  [10, 20, 15, 30, 15,  6,  2,  2],
  [ 5, 10, 30, 10, 30, 10,  3,  2],
  [10,  4, 15, 20, 10, 25,  8,  8],
  [ 2,  3,  8, 12, 30, 10, 25, 10],
  [ 2,  2,  4,  5, 15, 20, 12, 40],   // after B4: pull to C5
  [25,  4,  5,  3, 20, 10, 25,  8],   // after C5: back down
];"""

MARKOV_STEP = """function nextNote(last, temp) {  // one die, thrown on one row
  let w = TABLE[last].map(p => pow(p, 1 / temp));  // T sharpens
  let sum = w.reduce((a, b) => a + b), r = random(sum);
  for (let i = 0; i < 8; i++) { r -= w[i]; if (r < 0) return i; }
  return 7;
}"""

MARKOV_CODE = """// a Markov melody: eight pitches and a hand-written table of what follows what
""" + MARKOV_TABLE + """
const HZ = [261.6, 293.7, 329.6, 349.2, 392.0, 440.0, 493.9, 523.3];
let last = 0, from = -1, melody = [], temp = 1, nextAt = 0, osc, env, on = false, moved = false;

function setup() {
  createCanvas(800, 600); randomSeed(1957); frameRate(30);
  for (let i = 0; i < 12; i++) { from = last; last = nextNote(last, 1); melody.push(last); }   // a silent start
}

""" + MARKOV_STEP + """

function draw() {
  if (moved) temp = mouseX < width / 2 ? pow(10, map(mouseX, 0, width / 2, -1, 0))     // left half: 0.1 → 1
                                       : pow(3, map(mouseX, width / 2, width, 0, 1));   // right half: 1 → 3
  if (millis() >= nextAt) {                            // every 320 ms: one more note
    let n = nextNote(last, temp); from = last; last = n;
    melody.push(n); if (melody.length > 22) melody.shift();
    nextAt = millis() + 320;
    if (on) { osc.freq(HZ[n]); env.play(osc); }
  }
  background(255); matrix(); strip(); labels();
}

function matrix() {                                    // the table, as darkness; the transition just taken, in orange
  const X = 70, Y = 90, S = 42;
  textFont('JetBrains Mono'); noStroke(); textSize(13); fill(90);
  textAlign(CENTER, BASELINE); for (let j = 0; j < 8; j++) text(NOTES[j], X + j * S + S / 2, Y - 8);
  textAlign(RIGHT, CENTER); for (let i = 0; i < 8; i++) text(NOTES[i], X - 8, Y + i * S + S / 2);
  for (let i = 0; i < 8; i++) for (let j = 0; j < 8; j++) {
    let p = pow(TABLE[i][j], 1 / temp), sum = TABLE[i].reduce((a, b) => a + pow(b, 1 / temp), 0), v = p / sum;
    noStroke(); fill(244 - min(1, v * 2.2) * 244, 244 - min(1, v * 2.2) * 233, 242 - min(1, v * 2.2) * 214);
    rect(X + j * S, Y + i * S, S - 1, S - 1);
    fill(v > 0.2 ? 255 : 60); textSize(11); textAlign(CENTER, CENTER); text(round(v * 100), X + j * S + S / 2, Y + i * S + S / 2);
  }
  if (from >= 0) { noFill(); stroke(237, 109, 36); strokeWeight(3); rect(X + last * S - 1, Y + from * S - 1, S + 1, S + 1); }
  noStroke(); fill(237, 109, 36); textSize(13); textAlign(LEFT, BASELINE);
  text('NEXT NOTE →', X, Y - 30); text('↓ LAST', X - 62, Y - 30);
}

function strip() {                                     // the melody so far, as a piano roll
  const X = 450, Y = 90, S = 42, CW = 14;
  for (let i = 0; i < 8; i++) { noStroke(); fill(i % 2 ? 244 : 255); rect(X, Y + (7 - i) * S, 22 * CW, S - 1); }
  for (let k = 0; k < melody.length; k++) {
    let n = melody[k], lastOne = k == melody.length - 1;
    fill(lastOne ? color(237, 109, 36) : color(0, 11, 28)); rect(X + k * CW + 1, Y + (7 - n) * S + 6, CW - 2, S - 12);
  }
  fill(237, 109, 36); textSize(13); textAlign(LEFT, BASELINE); text('THE MELODY · our table, their idea', X, Y - 30);
  fill(90); textAlign(LEFT, CENTER); for (let i = 0; i < 8; i++) text(NOTES[i], X + 22 * CW + 8, Y + (7 - i) * S + S / 2);
}

function labels() {
  noStroke(); fill(0, 11, 28); textSize(16); textAlign(LEFT, BASELINE);
  text('temperature ' + nf(temp, 1, 1) + (temp < 0.5 ? ' · the likeliest note, almost always' : temp < 1.5 ? ' · the table as written' : ' · the table flattened: almost any note'), 70, 452);
  fill(90); textSize(14);
  text('mouse x = temperature · T → 0: a rule · T → 3: a die', 70, 482);
  text('orange = the transition just taken · ' + (on ? 'playing · click = new dice' : 'click to hear it'), 70, 508);
  text('Hiller & Isaacson 1957, experiment 4: the next note depends on the last.', 70, 536);
}

function mouseMoved() { moved = true; }
function mousePressed() {
  if (!on) {
    userStartAudio();
    osc = new p5.Oscillator(HZ[0], 'triangle'); osc.amp(0); osc.start();
    env = new p5.Envelope(0.01, 0.28, 0.15, 0.15); env.setRange(0.3, 0);
    on = true; return;
  }
  randomSeed(millis()); melody = []; last = 0; from = -1;            // new dice, same table
}"""

# Appended to every sound sketch's page (not shown on the code panels): when the audio worklets cannot load — a deck
# opened from a file:// URL, or the headless snapshot — p5.sound would wait forever and setup() would never run.
# The guard turns that failure into a warning, so the picture always draws; only the microphone needs a worklet.
SOUND_GUARD = """(function () {   // keep drawing when p5.sound's worklets cannot load (file:// decks, snapshots)
  if (!self.AudioWorklet || !AudioWorklet.prototype.addModule) return;
  const orig = AudioWorklet.prototype.addModule;
  AudioWorklet.prototype.addModule = function (u, o) {
    return orig.call(this, u, o).catch(function (e) { console.warn('p5.sound worklet skipped: ' + e); });
  };
})();"""

# ───────────────────────── the panels (specs, templates) ─────────────────────────
SOUND_SPEC = [
    'THE SOUND SPEC', ' ',
    'PURPOSE: what the sound is for, for whom',
    'THE MOMENT: when it plays, where, how often',
    'LENGTH: [seconds], then silence',
    'TEMPO: [BPM], or "no pulse"',
    'MOOD: [three words]',
    'TIMBRE: [instruments or sounds];',
    '        nothing electric / nothing acoustic',
    'STRUCTURE: [first this, then this, then stop]',
    'LIKE / NOT LIKE: [a reference], not [another]',
    'MUST NOT: no voice, no words, no reverb tail',
    'DELIVERABLE: one file, [seconds], tool named',
]

PROMPT_FOR_LM = [
    'TO THE LANGUAGE MODEL', ' ',
    'Here is a sound spec for a product:',
    '[paste the spec]', ' ',
    'Write a prompt for a text-to-music model',
    'in under 60 words: genre, tempo, mood,',
    'instruments, structure, length, and what',
    'to leave out. No lyrics. No artist names.',
    'Then, in one sentence: the rule the',
    'sound follows.', ' ',
    'THEN: paste the prompt into the music',
    'model. Generate twice. Listen to both.',
    'Three lines: what did it decide that',
    'the spec did not say?',
]

SPEC_EXAMPLE = [
    'THE SPEC · AN EXAMPLE', ' ',
    'PURPOSE: the rider knows the bike is theirs,',
    '  without looking down',
    'THE MOMENT: the lock clicks open, 08:10,',
    '  a busy street, once per ride',
    'LENGTH: 3 s, then silence',
    'TEMPO: 120 BPM, in time with the bell',
    'MOOD: light, outdoors, a small win',
    'TIMBRE: a marimba and a soft bell,',
    '  nothing electric',
    'STRUCTURE: two rising notes, one chord, stop',
    'LIKE: a bicycle bell. NOT LIKE: a slot machine',
    'MUST NOT: no voice, no words, no reverb tail',
    'DELIVERABLE: one WAV, 3 s, tool + plan named',
]

def hands_up(text, choices, eyebrow_text, notes):
    """A chapter quick check answered by a show of hands: the question layout, no ClassPoint button."""
    s = question('multiple_choice', text, choices, eyebrow_text=eyebrow_text, notes=notes)
    s.cp = None
    return s


S = []  # the slides, in order

# ───────────────────────── 00 · title ─────────────────────────
S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 06 · LECTURE + WORKSHOP',
               'Sound machines.',
               'Week 6 — what a machine hears, and thirty seconds for a product.',
               notes='Join code on screen from 30 minutes before. Headphones or earbuds out: the second half makes sound. Laptops out from the start; the TAs have paired people without a laptop with people who have one. The sketches in this deck make sound in the html deck only, after a click.'))

S.append(agenda('SD2112 · WEEK 06', [
    'Last week, in your words', 'What a machine hears', 'Rules that play', 'Models that listen',
    'Voices, and who owns a sound', 'Sound for a product', 'Activity: thirty seconds for a product', 'Mock quiz, reflection, Challenge 5',
], notes='Eight stops. The first four are the lecture: what sound is to a machine, then the two machines again — a sequencer and a Markov chain on one side, a diffusion model over pictures of sound and a language model over pieces of sound on the other. Break. Then voices and the lawsuits, the sound spec, the activity, and eight mock-quiz questions spread through the second half, because the real one is next week.'))

# ───────────────────────── 01 · last week, in your words ─────────────────────────
S.append(section('01', 'Last week, in your words', 'the video · challenge 4 · the map',
                 notes='Ten minutes of recap from what you gave us: the homework video, the Challenge 4 vote, and where we are. Module 2 closes today.'))

S.append(question('short_answer', 'AltexSoft: one thing you understood, one you did not.',
                  hint='Two short lines. "Understood: … Not yet: …". The video was How AI Sound and Music Generation Works; the second line writes today\'s lecture.',
                  eyebrow_text='01 · HOMEWORK · SHORT ANSWER',
                  notes='ClassPoint short answer, two minutes. Read six aloud, sorted. What people understood is usually "a spectrogram is a picture"; what they did not is usually how the picture becomes sound again, or what a token of audio is. Say which chapter answers each: chapter two for the picture, chapter four for the tokens. Keep the screenshot: the mid-term draws on this video.'))

S.append(cards('01 · WEEK 5 · IN THREE LINES', 'The machine that draws from noise.', [
    ('DIFFUSION', 'Noise, denoised, steered by words.', 'A picture is made by removing noise step by step, and the prompt steers every step. Today the same machine draws a picture of sound.'),
    ('CLIP', 'Words and pictures in one space.', 'A caption and its image land near each other. Today a caption and its sound do the same: a different sense, the same trick.'),
    ('MEDIATION', 'The thing in between is never neutral.', 'Ihde and Verbeek: a tool shapes what you perceive and do. A sound is the most invisible mediation a product has. Nobody reads it; everybody hears it.'),
], notes='Three lines from last week, because today stands on them. Diffusion comes back as road one of machine B for sound. CLIP comes back as the thing that lets a text prompt steer a music model. Mediation comes back at the end: a notification sound decides what a hundred million people do with their hands, and nobody calls that design.'))

S.append(cards('01 · CHALLENGE 4 · FOUR ENTRIES · BY BRIEF', 'A layout you could not design.', [
    ('ENTRY A', 'The brief', '"a poster for a night market, only type, the grid decided by the model, one colour I chose"'),
    ('ENTRY B', 'The brief', '"a menu for a noodle shop, twelve items, the hierarchy generated, then I moved one thing"'),
    ('ENTRY C', 'The brief', '"a magazine spread from a photo of a stairwell: the model set the columns, I set the margins"'),
    ('ENTRY D', 'The brief', '"a bus timetable that reads at a glance: three iterations, the third one is mine"'),
], text_size=22, notes='Replace these four with the real ones: the four best Challenge 4 entries from Blackboard, anonymised, the layout on screen from the Blackboard page and the brief on the card. Read each brief before showing its layout; ask the room to guess what the model decided that the designer did not. That question is the whole of the second half, for sound.'))

S.append(question('multiple_choice', 'Challenge 4: which entry gets the star?', [
    'Entry A', 'Entry B', 'Entry C', 'Entry D',
], eyebrow_text='01 · CHALLENGE 4 · AWARDS · MULTIPLE CHOICE',
    notes='ClassPoint vote, one minute. No correct answer: the room decides, the winner gets a participation star and thirty seconds to say what the model decided that they kept. Note the split for the awards list. Challenge 5 is briefed at the end of today; it is voted on next week, before the quiz.'))

S.append(journey('01 · THE SEMESTER', 'Where we are', JOURNEY, here=(1, 2),
                 notes='The last of the three tool weeks: language, images, sound. Next week is the mid-term: the quiz on weeks 1 to 6 and the playlist, your pitches, and teams. The reflection is due next week too; there is a draft check with the TAs today. Then module 3: the model inside the product.'))

# ───────────────────────── 02 · what a machine hears ─────────────────────────
S.append(section('02', 'What a machine hears', 'a waveform · a spectrogram · a score of numbers', bg=INK,
                 notes='Chapter two: three ways to write sound down, and the one a model looks at. Everything in the tools later depends on which of the three the machine was shown.'))

S.append(figure_slide('02 · A WAVEFORM', 'Sound is pressure over time. A waveform is the drawing.', F.w06_waveform(),
                      body=['Air pushes on your eardrum, more and less, hundreds of times a second. Draw the pushing against time and you have a waveform: loudness is the height, pitch is how often it repeats. A computer keeps only dots: 44,100 of them a second on a CD.'],
                      caption='A 220 Hz tone with four harmonics, computed, not recorded. You hear from about 20 Hz to 20 kHz; A above middle C is 440 Hz (ISO 16, 1975). CD audio: 44,100 samples a second.',
                      notes='Start from the body: pressure on the eardrum, that is all sound is. The drawing is the pressure against time. Two facts to keep: pitch is how often the wave repeats — 220 times a second here — and a computer only keeps dots, 44,100 a second, each one a number. A second of sound is 44,100 numbers; a three-minute song is eight million. That is why nobody trains a music model on the dots directly; the next slide is the trick.'))

S.append(figure_slide('02 · A SPECTROGRAM', 'A spectrogram is a picture of sound.', F.w06_spectrogram_how(),
                      body=['Cut the wave into short slices. Fourier, 1822: any wave is a sum of sines, so each slice becomes a list of frequencies and how loud each one is. Stand the lists side by side and you have a picture: time across, frequency up, loudness as darkness.'],
                      caption='Three things instead of two. The first bar is the pitch; the bars above it are the timbre — what makes a flute and a violin on the same note different pictures.',
                      notes='This is the slide the homework video was about. Walk it left to right: a slice, its recipe of sines, the recipe as one column, many columns as a picture. Say the three axes out loud: time, frequency, loudness — the quick check at the end of the chapter asks for them. The design point: once sound is a picture, every image trick from last week applies to it. Chapter four does exactly that.'))

S.append(sketch_slide('02 · LIVE · YOUR VOICE AS A PICTURE', 'Speak. Whistle. Clap. Watch.',
                      live('w06-spectrogram', SPECTRO_CODE, 1400, 500, hint='click to start the microphone · speak, whistle, clap · mouse y reads the frequency', extra=SOUND_GUARD, sound=True),
                      body=['The microphone, drawn as a scrolling spectrogram: a whistle is one thin line, a vowel is a stack of lines, a clap is a vertical stripe. If the microphone is refused or stays silent, a built-in sweep takes over and the mouse sets its pitch.'],
                      caption='p5.js with p5.sound: p5.AudioIn into p5.FFT, 1024 bins, redrawn thirty times a second on a log-frequency axis from 50 Hz to 8 kHz. Before the click it shows a computed tone, so the still is never empty.',
                      notes='Html deck only; click the sketch once to start audio and allow the microphone. Whistle first — one line, and you can read its frequency with the mouse. Then say "aaa" and "eee": the stack of harmonics changes shape with the vowel; that shape is what a voice clone learns. Then clap: a vertical stripe, all frequencies at once. If the room\'s PC has no microphone, the sweep runs and the mouse plays it like a theremin. The microphone works only when the deck is served over http(s) — the course site, or a local server; a deck opened from a file shows the sweep. Two minutes; the pptx shows a still.'))

S.append(sketch_slide('02 · LIVE · TIMBRE', 'An instrument is which harmonics, and how loud.',
                      live('w06-additive', ADD_CODE, 1400, 500, hint='mouse x = how many harmonics · mouse y = how bright · click to hear', extra=SOUND_GUARD, sound=True),
                      body=['One sine is the purest tone and the dullest. Add its multiples — 440, 660, 880 Hz — with a rule for how fast they fade, and the same pitch turns from a flute into a reed into a buzz. The recipe is the timbre. When a spec says "marimba, nothing electric", this is the thing it is asking for.'],
                      caption='Additive synthesis: sixteen sine oscillators, one per harmonic, started once; the mouse only changes their volumes. Fourier\'s sum, run backwards.',
                      notes='One minute of playing. Left to right: one sine, then more; up and down: how fast the harmonics fade. Ask the room to name the sound at each end — flute, then oboe-ish, then a buzz. The lesson for the spec: "instrument" is a recipe of harmonics over time, and a music model has learned thousands of such recipes from examples; you name one with a word. Cut if behind.'))

S.append(figure_slide('02 · MIDI · 1983', 'A note is four numbers.', F.w06_midi(),
                      body=['MIDI carries no sound. It carries a score: which key, when it went down, when it came up, how hard. Pitch 0 to 127, middle C at 60; velocity 0 to 127. A synthesiser turns the numbers into sound, and any synthesiser will do. Melody, harmony and rhythm all fit in these four numbers.'],
                      caption='The MIDI 1.0 specification, 1983, agreed between synthesiser makers so that any keyboard could drive any box. A piano roll is the drawing of it. A language model can write MIDI; a sequencer obeys it exactly.',
                      notes='The rule side of music has had a file format for forty years. Four numbers per note, no sound inside — the same score on a piano patch and a drum patch is the same file. This is what the sequencer after the break is: a very small MIDI file you can see. Say it with week 2: a MIDI file is a spec; the synthesiser is the executor.'))

S.append(cards('02 · FOUR WORDS', 'Melody, harmony, rhythm, timbre.', [
    ('MELODY', 'One note after another.', 'A sequence of pitches. The Markov chain in chapter three writes exactly this: the next note from the last one.'),
    ('HARMONY', 'Notes at the same time.', 'A stack: a chord is three pitches with one onset. Counterpoint is the rulebook for stacks that move — the Illiac\'s rules.'),
    ('RHYTHM', 'When, and how often.', 'A grid of onsets against a pulse: tempo in beats per minute, steps of a beat. The sequencer\'s whole job.'),
    ('TIMBRE', 'Which sound.', 'The recipe of harmonics and how it changes over the note. The hardest one to write as a rule, and the first thing a model learns from examples.'),
], text_size=22, notes='The vocabulary for the spec, in four words, each tied to a machine you will see today. Three of them are easy to write as rules — a sequence, a stack, a grid — and that is why rule-based music is sixty years old. Timbre is the one that resisted rules and fell to examples. When you write the spec later, notice which lines are which.'))

S.append(hands_up('A spectrogram shows three things. Which three?', [
    'Time, frequency, loudness', 'Pitch, key, tempo', 'Left, right, centre', 'Bass, mid, treble',
], eyebrow_text='02 · QUICK CHECK · HANDS UP',
    notes='A show of hands, thirty seconds: A, B, C, D. Correct: A. Time across, frequency up, loudness as darkness. B is music theory, not a picture; D is three bands of frequency with no time axis. Say why it matters: three things is what makes it an image, and an image is what last week\'s machine eats.'))

# ───────────────────────── 03 · rules that play ─────────────────────────
S.append(section('03', 'Rules that play', 'machine A · a sequencer · counterpoint · a Markov chain · 1957', bg=VIOLETS[0],
                 notes='Chapter three: music from rules, live. A grid you can hear, then the first computer-composed score and its two moves — generate and test, and a table of what follows what.'))

S.append(sketch_slide('03 · LIVE · A STEP SEQUENCER', 'The grid is the score.',
                      live('w06-sequencer', SEQ_CODE, 1000, 600, hint='click to start · click a cell to toggle · mouse y = tempo · C clears', extra=SOUND_GUARD, sound=True),
                      body=['Sixteen steps, six sounds. The playhead reads the grid left to right, forever; every filled cell is a rule: on this step, this sound. The mouse changes one number, the tempo. Nothing here learned anything, and it will play the same bar until the sun goes out.'],
                      caption='Kick, snare and hat are envelopes on a sine and on white noise; the three pitched rows are oscillators at C2, C4 and E4. A step is 60 ÷ BPM ÷ 4 seconds. Press C to clear and write your own.',
                      notes='Html deck only; one click starts the sound. Let the seed pattern play for a bar, then toggle cells while it runs: the room hears the rule change the moment you click. Drag the mouse down: slower; up: faster. Press C and build a beat from nothing in twenty seconds — kick on 1, 5, 9, 13, hat on the evens. That is machine A for music: exact, explainable, and you can point at the cell that decided. This sketch comes back in the activity as the rule-based twist.'))

S.append(code_slide('03 · THE SEQUENCER · THE RULE', 'Sixteen steps, read left to right, forever.', SEQ_STEP, F.w06_grid_score(),
                    caption='The clock in eleven lines: a step lasts 60 ÷ BPM ÷ 4 seconds; when it is time, advance one step and play every row that has a cell on. The grid is the whole score; the loop is the whole musician.',
                    code_size=20,
                    notes='Read it top to bottom, like the week-2 sketches. The tempo is one number from the mouse; the duration of a step is arithmetic; the if is the clock; the for over rows is the rule applied. Compare with 10 PRINT: a loop and a lookup. Ask where chance enters — nowhere. That is the point, and the difference from the next slide.'))

S.append(video('03 · HILLER & ISAACSON · ILLIAC I · 1956 – 57', 'A computer writes a string quartet: propose, test, keep.', 'n0njBFLQSk8',
               ['The Illiac Suite, University of Illinois: the ILLIAC generates random notes and keeps the ones that pass the rules of counterpoint. Four experiments, four movements.',
                '- Generate and test: chance proposes, the rules decide. The oldest move in symbolic AI, in music.',
                '- The fourth experiment replaces the rules with a table: the next note depends on the last. Week 2 met it with Nake\'s signs; week 4 with tokens. On the playlist since week 2.'],
               thumb='yt/n0njBFLQSk8.jpg',
               notes='Play a minute of the first movement if there is time: it sounds like Renaissance polyphony because the rules are Renaissance rules. First performed in 1956, published in 1957, and generally called the first score composed by a computer. Then the structure: experiments one and two are rules; three is rhythm and dynamics; four is a Markov chain. The next two slides open experiments one and four.'))

S.append(figure_slide('03 · THE ILLIAC SUITE · TWO MOVES', 'Propose, test, keep — or a table instead.', F.w06_generate_test(),
                      body=['Left, experiments one and two: a random number proposes a pitch; the rules of strict counterpoint accept or reject it; the melody grows one accepted note at a time. Right, experiment four: no rulebook, only a table of how likely each next interval is, given the last. Simpler intervals more likely than bigger ones.'],
                      caption='Our reading of Hiller and Isaacson\'s experiments; the rules on the left are a few of the classical ones, the table on the right uses our numbers. What they share: the design is in the rules and the table; chance only proposes.',
                      notes='Two machines that are both machine A. The generate-and-test loop is what Cage did with coins and the I Ching, mechanised: every note is legal because it passed. The table is subtler: nothing is illegal, some things are likely, and the texture of the music lives in the numbers. Ask the room which one they could explain to a client — both, line by line. Then the live version of the table.'))

S.append(content('03 · LIVE · EXPERIMENT 4 IN A PAGE', 'The next note depends on the last one.',
                 ['Eight pitches, and an eight-by-eight table we wrote by hand: after C, mostly D; after B, a pull to C. A die is thrown on one row of the table for every note. The orange cell is the transition just taken.',
                  '- **Mouse x is the temperature.** Low: the likeliest note almost always — a rule. High: the table flattened — a die.',
                  '- Click to hear it; click again for new dice with the same table.',
                  'This is Nake\'s Walk-Through-Raster in sound, and week 4\'s next-token machine with a vocabulary of eight.'],
                 sketch=live('w06-markov-melody', MARKOV_CODE, 800, 600, hint='mouse x = temperature · click to hear · click again = new dice', extra=SOUND_GUARD, sound=True),
                 caption='A first-order Markov chain over eight pitches. The table is the aesthetic: change a row and the melody changes character; change the temperature and it changes discipline.',
                 body_size=28,
                 notes='Html deck only; click to hear it. Move the mouse to the far left: the melody becomes a loop, the likeliest path through the table, and the room can predict the next note. Far right: almost any note, no character. The middle is the table as written. Point at the orange cell moving: that is the whole machine, one lookup per note. Say the week-4 sentence: a language model is this table with fifty thousand rows and a very long memory. Then the code.'))

S.append(code_slide('03 · THE MARKOV STEP', 'A table, a die, a temperature.', MARKOV_TABLE + '\n\n' + MARKOV_STEP,
                    caption='Eight rows, eight columns, five lines of loop. Raising every number to 1 ÷ T is the temperature: below 1 the big numbers win; above 1 they even out.',
                    code_size=19, sketch=live('w06-markov-melody-2', MARKOV_CODE, 800, 600, hint='mouse x = temperature · click to hear · click again = new dice', extra=SOUND_GUARD, sound=True),
                    notes='The table first: each row sums to about a hundred, each row is one note\'s habits. Then nextNote: raise to a power, add them up, throw one die, walk down the row until the die is spent. Ask: where is the design? In the table. Where is chance? One line. Where would a model be? It would fill the table from a million melodies instead of us writing it — machine B is a Markov chain that learned its table. Cut if behind; the previous slide carries it.'))

S.append(video('03 · STANFORD LAPTOP ORCHESTRA · BING CONCERT HALL · 10 JUNE 2023', 'The dawn of computer music, replayed by a laptop orchestra.', 'Ih9lHXMlrtE',
               ['The Dawn of Computer Music, by Terry Feng, Soohyun Kim and Yikai Li: two movements — Strauss\'s sunrise fanfare synthesised by invisible instruments, then a sound collage of space in the manner of musique concrète.',
                '- The history it plays with: 1957, Max Mathews and Newman Guttman at Bell Labs make an IBM 704 play seventeen seconds of sound with MUSIC I. 1961, a Bell Labs computer sings Daisy Bell; Arthur C. Clarke hears it and gives it to HAL in 2001.',
                '- Rules that play, seventy years on: a laptop is an instrument when someone writes the rule.'],
               thumb='yt/Ih9lHXMlrtE.jpg', body_size=26,
               notes='Optional; cut if behind. The piece is on the playlist because it stages the history in eight minutes: the fanfare everyone knows from 2001, played by code, then the tape-music tradition of the 1950s done live. Mathews\' seventeen seconds in 1957 — Guttman\'s The Silver Scale — are the same year as the Illiac Suite: sound from rules and notes from rules were born together. Ask who has heard a computer sing Daisy Bell; half the room has, through HAL. (The year is 1961 in most accounts, 1960 in Guinness\'s; do not make a quiz question of it.)'))

S.append(hands_up('In the Illiac Suite\'s first experiments, where does chance enter?', [
    'Which note is proposed; the rules decide whether it stays', 'Which rules apply to each note', 'The tempo of the movement', 'The choice of instruments',
], eyebrow_text='03 · QUICK CHECK · HANDS UP',
    notes='A show of hands, thirty seconds. Correct: A. The same question as Schotter in week 2 — where, exactly, is the die thrown — and the same shape of answer: chance proposes, the rule decides. In experiment four the rule becomes a table, but the die still only ever picks from the table.'))

# ───────────────────────── 04 · models that listen ─────────────────────────
S.append(section('04', 'Models that listen', 'machine B · a picture of sound · a language of sound · the products', bg=INK,
                 notes='Chapter four: show the machine examples instead. Two roads, both built from things you already met — last week\'s diffusion and week 4\'s next-token machine — and then the three products the room will use.'))

S.append(figure_slide('04 · TWO ROADS', 'A picture of sound, or a language of sound.', F.w06_two_roads(),
                      body=['Road one: turn sound into a spectrogram and treat it as an image; a diffusion model denoises a new one, steered by words; the inverse Fourier transform plays the picture. Road two: a codec turns sound into a few tokens per frame; a next-token model writes new tokens; the codec plays them back.'],
                      caption='Riffusion, 15 December 2022, is road one. Jukebox (April 2020), MusicLM (January 2023) and MusicGen (June 2023) are road two, and most likely so are the products of 2024–26, which do not publish what is inside. Nobody wrote a rule about music in either road.',
                      notes='The whole chapter in one figure. Road one is last week: the picture of sound is just another picture, and a diffusion model does not know the difference. Road two is week 4: tokens, a table, a die, a temperature — except the tokens come from a codec instead of a tokenizer, and mean fractions of a second instead of pieces of words. Say the spine: in neither road did anyone write a rule of counterpoint. The rules are in the examples.'))

S.append(content('04 · ROAD 1 · RIFFUSION · 15 DECEMBER 2022', 'Draw the spectrogram. Then play the drawing.',
                 ['Seth Forsgren and Hayk Martiros fine-tuned Stable Diffusion 1.5 on spectrograms of music tagged with genres and instruments — "blues guitar", "jazz piano", "afrobeat".',
                  '- Prompt in, spectrogram image out, inverse Fourier transform, five seconds of sound. The model never heard anything. It saw pictures.',
                  '- Everything from week 5 applies: the prompt pulls to the middle of the tags; a reference image steers; the picture can be interpolated between two prompts, and the sound morphs with it.',
                  'A hobby project that became a company. The idea is the lesson: once sound is an image, machine B is already built.'],
                 body_size=30,
                 notes='The cleanest example in the course of one machine re-used for another medium. Ask what "typical" means here: the middle of every spectrogram tagged "blues guitar". Ask what the edge is: a sound nobody tagged. The week-1 cups, for sound. Cut to one sentence if behind: the picture of sound is a picture.'))

S.append(cards('04 · ROAD 2 · A LANGUAGE OF SOUND', 'A codec turns sound into pieces a language model can predict.', [
    ('JUKEBOX · APRIL 2020', 'OpenAI: raw audio, 1.2 million songs.', 'Sound compressed into codes, a transformer writing codes, a decoder playing them back — with rudimentary singing. Slow, rough, and the proof that road two works.'),
    ('MUSICLM · JANUARY 2023', 'Google: text to music through SoundStream tokens.', 'A neural codec gives the tokens; a text model trained on captions gives the steering. Thirty seconds of coherent music from a sentence.'),
    ('MUSICGEN · JUNE 2023', 'Meta: open weights, EnCodec tokens.', 'One transformer over the codec\'s codes; a melody can be given as a reference. Runs on a laptop; the free demo on Hugging Face is one of today\'s tools.'),
    ('PRODUCTS · 2024 – 26', 'Suno, Udio, and the rest.', 'Full songs with lyrics and vocals from a prompt. What is inside is not published in detail; what they were trained on is what the lawsuits after the break are about.'),
], text_size=21, notes='Four steps of road two. The mechanism is the week-4 lecture with a different tokenizer: a codec that turns each fraction of a second into a few symbols from a fixed vocabulary, then a transformer predicting the next symbol, then the codec run backwards. The last card is honest: the companies do not publish their architectures, so we say what they do, not how. What they trained on is a court question now.'))

S.append(video('04 · ALTEXSOFT · THE HOMEWORK', 'How AI sound and music generation works.', 'bp7Qb8QY1Pw',
               ['The video you watched: waveforms and spectrograms as the two representations; models that learn patterns from large sets of them; a latent space you sample from, and a decoder that turns the sample back into a spectrogram or a wave.',
                '- The vocabulary it gives you — waveform, spectrogram, latent space, decoder — is the vocabulary of the quiz.',
                '- Rewatch the spectrogram minute if your "not yet" line was about it.'],
               thumb='yt/bp7Qb8QY1Pw.jpg',
               notes='Do not replay it; point at the three ideas and connect them to the two roads: the spectrogram is road one\'s image, the latent space is where both roads sample, the decoder is the inverse Fourier or the codec. Then ask the "not yet" lines from the start of class again — most are answered by now.'))

S.append(cards('04 · THREE PRODUCTS · SEPTEMBER 2026', 'Suno, AIVA, Udio: what they are, what you own.', [
    ('SUNO · CAMBRIDGE, MA · 2022', 'A full song from a prompt.',
     ['Lyrics, vocals, instruments; v5.5 since March 2026. Free plan: outputs for personal, non-commercial use only. Paid plans: Suno assigns you its rights in the output — and its terms say it makes no promise that any copyright exists in it at all.',
      'Terms effective 3 September 2026. Licensed models replacing the current ones are due in 2026, after the Warner deal.']),
    ('AIVA · LUXEMBOURG · 2016', 'A composer, on paper.',
     ['Classical and cinematic pieces, MIDI export. Registered with SACEM in 2016–17 as the first "virtual composer" a rights society recognised.',
      'Free (€0) and Standard (€11 a month, billed yearly): copyright stays with AIVA. Pro (€33 a month, billed yearly): "copyright owned by you", full monetisation.']),
    ('UDIO · NEW YORK · 2024', 'A walled garden since October 2025.',
     ['Songs from a prompt, like Suno. After settling with Universal, downloads were switched off on 30 October 2025; a 48-hour window reopened them in early November. The licensed platform with UMG and Warner is due in 2026.',
      'What you make there stays there. Read that before you build a challenge on it.']),
], text_size=20, head_size=32, notes='Three products, three different answers to "what do I own". Read the Suno line twice: paid users get whatever rights Suno has, and Suno says it does not know whether that is anything. AIVA sells the copyright on the Pro plan and keeps it on the others. Udio keeps the file. For Challenge 5 the rule is simple: name the tool and the plan you used; the terms are part of the process note. Prices and terms as read on 5 September 2026 — check before you quote them.'))

S.append(hands_up('Which of these is machine B — examples, not rules?', [
    'A step sequencer playing a grid', 'A Markov table you wrote by hand', 'Suno writing a song from a prompt', 'A metronome at 120 BPM',
], eyebrow_text='04 · QUICK CHECK · HANDS UP',
    notes='A show of hands, thirty seconds. Correct: C. The other three are rules you could write on a napkin, including the Markov table — it becomes machine B only when the numbers are learned from data instead of written by you. That sentence is the reflection\'s argument in one line.'))

S.append(statement('Break. Fifteen minutes.', eyebrow_text='AFTER THE BREAK · VOICES · THE LAWSUITS · A SOUND FOR A PRODUCT · THE MOCK QUIZ', size=120, bg=PAPER,
                   notes='1:18. Headphones, laptops charged, genai.polyu.edu.hk open, and the music model Nicolò tested open in a second tab. The TAs help anyone whose login fails now, not during the activity.'))

# ───────────────────────── 05 · voices, and who owns a sound ─────────────────────────
S.append(section('05', 'Voices, and who owns a sound', 'voice cloning · three cases · two years of lawsuits · the terms', bg=PINKS[0],
                 notes='Chapter five, after the break: the part of sound that is about people. A voice is the most personal sound there is, and it is a few seconds of data. Then what the courts have said so far.'))

S.append(content('05 · VOICE CLONING', 'A voice is a small vector. A few seconds is enough.',
                 ['A modern text-to-speech system writes a spectrogram from text and a vocoder plays the picture. The voice — the stack of harmonics you saw when you said "aaa" — is a handful of numbers the model learned from a short recording.',
                  '- Give it a new handful, from a few seconds of someone else, and the same text comes out in their voice. That is cloning: the same machine, a different vector.',
                  '- Nothing here is a rule about that person. It is the middle of their examples, which is why it sounds right and says things they never said.',
                  'Who owns the vector? Not a copyright question — a voice is not a work. A likeness question, a consent question, and in Hong Kong a largely unanswered one.'],
                 body_size=30,
                 notes='Connect to the spectrogram sketch: the shape of the harmonic stack when they said "aaa" is what the model captures. The consequence is the three cases on the next slide. The law line is deliberately careful: copyright protects works, not voices; the cases so far are about likeness, consent and platform rules, and the answers differ by country. If a student asks about Hong Kong specifically, say that there is no dedicated rule and that this is a design decision they will have to make for themselves in week 8.'))

S.append(cards('05 · THREE CASES', 'Whose voice is it?', [
    ('HEART ON MY SLEEVE · APRIL 2023', 'A hit by nobody, in two famous voices.',
     'Ghostwriter977 released a song on 4 April 2023 with AI vocals made to sound like Drake and The Weeknd. Millions of plays in days; Universal had it taken down from the streaming services. Later re-cut without the AI voices to try for a Grammy.'),
    ('SKY · MAY 2024', 'A voice that sounded like an actor who had said no.',
     'Scarlett Johansson said she had declined OpenAI\'s request to voice ChatGPT; a voice called Sky sounded like her anyway. OpenAI said Sky was another actor, cast before any outreach, and paused it on 19 May 2024.'),
    ('THE VELVET SUNDOWN · 2025', 'A band with a million monthly listeners, and no members.',
     'A 1960s-style rock act climbed Spotify\'s playlists until listeners could find no trace of the people. In July 2025 the bio changed: "a synthetic music project guided by human creative direction", composed and voiced with AI.'),
], text_size=22, notes='Three cases, three questions. The first is about a voice as a likeness: the takedown was not a copyright judgment, it was a platform acting on a label\'s request. The second is about consent even when the voice is technically someone else\'s. The third is about disclosure: nothing was stolen, nobody was told. Ask the room which of the three bothers them most; the split is the mediation brief they will write in week 11.'))

S.append(timeline('05 · TWO YEARS OF LAWSUITS', 'Sued, settled, licensed — and still in court.', [
    ('JUN 2024', 'The majors sue', '24 June: UMG, Sony and Warner, with the RIAA, sue Suno (Boston) and Udio (New York) over training.'),
    ('OCT 2025', 'UMG settles with Udio', '29 October: a licensed platform for 2026, trained on authorised music; artists opt in. The next day Udio switches downloads off.'),
    ('NOV 2025', 'Warner settles with Udio', '19 November: the same shape, a licensed creation service for 2026, across recordings and publishing.'),
    ('NOV 2025', 'Warner settles with Suno', '25 November: licensed models to replace the current ones in 2026; downloads only on paid plans, with caps.'),
    ('JUL 2026', 'Sony sues Udio again', '20 July: a second New York complaint over 30,117 recordings. Sony is the one major still fighting both companies.'),
    ('JUL 2026', 'GEMA beats Suno in Munich', '31 July: the German society wins on training and on outputs; Suno may appeal.'),
    ('AUG 2026', 'UMG and Sony amend', '25 August: the Massachusetts case against Suno adds "stream ripping" from YouTube. Fair use is still open.'),
    ('2026 →', 'The licensed products', 'New models promised this year. Whether the output is yours is a question of the terms, not the law.'),
], notes='Two years in eight steps, verified on 5 September 2026; add anything that happened since. The shape to teach: sue, settle, license — two of the three majors made deals with both companies; the third is still fighting both, and a German court said no to Suno\'s training. Nothing here is final, and none of it is a rule you can build on: what you can build on is the terms of the product in front of you. Do not read every step; pick the first, the second and the last.'))

S.append(cards('05 · WHERE IT STANDS · 5 SEPTEMBER 2026', 'Settled with two majors. Fighting the third. Lost once in Munich.', [
    ('SETTLED', 'Universal and Warner.',
     'Both have deals with Udio; Warner has one with Suno. Licensed platforms and models due in 2026, with opt-in and payment for artists. Figures not disclosed by the parties.'),
    ('IN COURT', 'Sony, and the German society.',
     'Sony against Udio (New York, two cases) and, with Universal, against Suno (Massachusetts). GEMA won against Suno on 31 July 2026; Suno says it may appeal. Fair use in the US is undecided.'),
    ('WHAT YOU OWN', 'Read the plan, not the law.',
     'Suno free: non-commercial. Suno paid: whatever rights Suno has, no promise there are any. AIVA Pro: the copyright. Udio: no downloads. Terms change; note the date.'),
    ('CHALLENGE 5', 'Name the tool and the plan.',
     'Your process note says which model, which plan, and what its terms let you do with the sound. A sound you cannot download or reuse is evidence for the reflection, not a deliverable for a client.'),
], text_size=21, notes='The take-away card is the third: for a designer the live question is the terms of service, because that is what decides whether the sound you made for a client is yours to hand over. Say the date again — these change monthly. Then the mock quiz starts: three questions now, two in the next chapter, three at the end. Same format as next week.'))

S.append(question('multiple_choice', 'Photoshop has three fills: Auto Levels, Content-Aware Fill, Generative Fill. Which one learned from examples?', [
    'Auto Levels', 'Content-Aware Fill', 'Generative Fill', 'All three',
], eyebrow_text='05 · MOCK QUIZ · 1 OF 8 · MULTIPLE CHOICE',
    notes='Mock quiz, question 1 of 8, week 1. Correct: C. Auto Levels is a rule on the histogram; Content-Aware Fill is PatchMatch, clever rules with no training; Generative Fill is a diffusion model trained on Adobe Stock. The real quiz is in this format: one idea per question, four choices, one right.'))

S.append(question('multiple_choice', 'In a p5.js sketch, randomSeed(1) means…', [
    'No randomness at all', 'The same "random" numbers every run, on any machine', 'One random number between 0 and 1', 'A random number of points',
], eyebrow_text='05 · MOCK QUIZ · 2 OF 8 · MULTIPLE CHOICE',
    notes='Question 2 of 8, week 2. Correct: B. The seed loads the die: the rule stays the rule, chance stays inside it, and the picture repeats exactly. A is wrong because random() is still called; C describes random() with no arguments.'))

S.append(question('multiple_choice', 'AlphaGo\'s move 37 against Lee Sedol (2016) mattered because…', [
    'It broke a rule of Go', 'It was a move no human would play, and it won', 'Lee Sedol played it', 'It was copied from a database of games',
], eyebrow_text='05 · MOCK QUIZ · 3 OF 8 · MULTIPLE CHOICE',
    notes='Question 3 of 8, week 3 and the playlist film. Correct: B. The commentators called it a mistake; it was not, and no human game contained it — AlphaGo learned it playing itself. A is wrong: it was legal. D is the Lovelace objection, and the whole point is that it does not apply.'))

# ───────────────────────── 06 · sound for a product ─────────────────────────
S.append(section('06', 'Sound for a product', 'sonic identity · the sound spec · what the model decides', bg=VIOLETS[0],
                 notes='Chapter six: the design brief for the second half. Five sounds everyone knows, the anatomy of a sound spec, the template, and the four questions to ask of every sound a model gives you.'))

S.append(cards('06 · FIVE SOUNDS YOU KNOW', 'Sonic identity: a rule, a brief, a few seconds.', [
    ('THX · 1983', 'Deep Note.',
     'James A. Moorer at Lucasfilm: a synthesised crescendo that glides from a narrow band around 200–400 Hz to three octaves wide. Premiered before Return of the Jedi. A rule, played.'),
    ('INTEL · 1994', 'The bong.',
     'Walter Werzowa: five notes, about three seconds, debuted in 1995. Intel\'s own count: five notes and twenty sounds built from them.'),
    ('WINDOWS 95 · 1995', 'The startup chime.',
     'Brian Eno, from a brief that asked for "inspiring, universal, blah-blah, da-da-da, optimistic, futuristic, sentimental, emotional" — and three and a quarter seconds. He delivered about six.'),
    ('NETFLIX · 2015', 'Ta-dum.',
     'Lon Bender: a wedding ring knocked on a nightstand, and a guitar chord played backwards. Two notes that a hundred million people hear every night.'),
    ('MASTERCARD · 2019', 'A sound architecture.',
     'Launched 8 February 2019: a melody for ads, a chime for the moment you pay, and regional versions. A design system, for the ear.'),
], text_size=19, head_size=28, notes='Five briefs, five answers, none longer than a breath. Point at what each spec must have contained: a length (Eno\'s three and a quarter seconds), a moment (the payment chime, the startup), a feeling in words, a must-not. Hum the Intel one; the room finishes it. That recognition is the deliverable of sonic identity, and it is exactly what a model cannot know it has achieved. Then the anatomy.'))

S.append(figure_slide('06 · THE SOUND SPEC', 'A sound spec is a brief for a machine that plays.', F.w06_sound_spec(),
                      body=['The week-2 spec and the week-4 brief, now audible. Half the lines are rules a sequencer obeys exactly — length, tempo, structure, must-nots. The other half are examples a model interprets — mood, timbre, like and not like. A good spec has both, and knows which is which.'],
                      caption='A made-up product; the headings are the point. Purpose first, always: what the sound is for and for whom. The must-nots matter more for sound than for pictures — a model that adds a voice has ruined a notification.',
                      notes='Read one line from each column aloud and ask which machine could execute it. "3 seconds, 120 BPM, two notes then a chord" — the sequencer, exactly. "Light, outdoors, a small win" — only a model, from its middle. That split is the reflection\'s argument again, and it tells them what to expect in the rounds: the rule lines will come back exactly, the example lines will come back typical.'))

S.append(two_col('06 · THE TEMPLATE', 'A language model writes the prompt. A music model plays it.',
                 ['Fill the spec. Paste it into a language model on **genai.polyu.edu.hk**; ask for a prompt for a text-to-music model: under sixty words, no lyrics, no artist names.',
                  '- Two machines in a row: the language model translates your spec into the music model\'s dialect; the music model answers from its middle.',
                  '- Ask for the rule back: "in one sentence, the rule the sound follows." If it does not match the spec, the prompt does not either.',
                  'When the sound drifts, fix the spec — not the prompt, not the sound.'],
                 SOUND_SPEC, right_size=22, left_size=26,
                 notes='The template is on the course site and on Blackboard. The pipeline is the week-2 pipeline with one more machine: spec → language model → prompt → music model → sound. Each arrow loses something; the "rule back" check catches the first loss before you spend a generation on it. Tell them the tool and the plan now: Nicolò has tested one music model from the classroom network; use that one, so the middle is the same middle for everyone.'))

S.append(cards('06 · WHAT THE MODEL DECIDES', 'Four questions for every sound.', [
    ('DID IT DO WHAT I SAID?', 'Tick the rule lines.', 'Length, tempo, no voice, the structure. A dropped one is a dropped constraint: restate it. Models are bad at exact lengths; count the seconds.'),
    ('WHAT DID IT DECIDE?', 'Find the middle.', 'A key, a fade at the end, a reverb, the corporate ukulele. Every choice you did not brief came from the typical example. Circle them.'),
    ('WHAT DID IT INVENT?', 'Find the extra.', 'A voice, a lyric, a second section, a drum fill you never asked for. The must-not lines exist for this.'),
    ('WOULD I SHIP IT?', 'The product test.', 'On the device, in the moment, a hundred times a day. If not: which line of the spec fixes it? Fix the line, run again.'),
], text_size=22, notes='The week-4 compare questions, for the ear. The second is the hard one: the middle of "app sound" is a specific, recognisable ukulele-and-claps, and the room will hear it in round two and laugh. The fourth question is what makes this design rather than generation: a sound a hundred times a day is a mediation, and the person who chose it is responsible for it.'))

S.append(question('multiple_choice', 'In a language model, a token is…', [
    'Always one word', 'A piece of text the model reads as a number', 'One letter', 'A sentence',
], eyebrow_text='06 · MOCK QUIZ · 4 OF 8 · MULTIPLE CHOICE',
    notes='Question 4 of 8, week 4. Correct: B. Pieces, not words: "unbelievable" is three tokens, a Chinese character can be one token or several, and the model never sees letters — which is why it cannot count them. Today the same idea with a codec: a token of sound is a fraction of a second.'))

S.append(question('multiple_choice', 'A diffusion model makes an image by…', [
    'Searching the web for the closest picture', 'Removing noise step by step, steered by the prompt', 'Copying the nearest training image', 'Drawing vector shapes from a rule',
], eyebrow_text='06 · MOCK QUIZ · 5 OF 8 · MULTIPLE CHOICE',
    notes='Question 5 of 8, week 5 and the playlist. Correct: B. Start from noise, remove a little at every step, let the words steer each step. C is the common misconception and worth a sentence: the model holds the middle of millions of examples, not the examples. Road one of today\'s lecture is B applied to a spectrogram.'))

# ───────────────────────── 07 · activity: thirty seconds for a product ─────────────────────────
S.append(section('07', 'Thirty seconds for a product.', f'35 minutes · a product · a music model · {GENAI}', bg=YELLOWS[0],
                 notes='The activity. A sound spec alone; generate, listen and write what the model decided in pairs; the same brief as a rule in fours, with the sequencer. Each round ends in ClassPoint; the last capture is an image with the spec as the caption. Nicolò keeps time; Amber, WU Zhao and MA Jie walk with the four questions. Headphones on; one laptop per pair.'))

S.append(content('07 · THE TOOLS', 'One music model for the room. And a fallback that is a rule.',
                 [f'**The language model:** any model on **{GENAI}**, to write the spec with you and translate it into a prompt.',
                  '**The music model:** the one Nicolò tested from the classroom network this morning — its name and its link are on Blackboard. Same model for everyone, so the middle is the same middle.',
                  '**The fallback, and round 4 for everyone:** the step sequencer from chapter three, on its own page on the course site — the link is on Blackboard. It runs on a phone. The spec is what you submit; the sound is evidence.',
                  '- Phones: the spec, the language model and the sequencer all work in a browser. Pair with a laptop for the music model.'],
                 body_size=28,
                 notes='Say which music model it is today; it changes term by term and the free tiers change monthly. The candidates Nicolò tries in the morning: Suno\'s free plan (personal, non-commercial), the MusicGen demo on Hugging Face, Stable Audio\'s free tier — whichever answers from the classroom network. If none answers — it has happened — the workshop is the spec plus the sequencer, and the debrief is the same. The sequencer link on Blackboard is the sketch\'s own page on the course site (week06/sketches/w06-sequencer.html, p5.js 1.11 with p5.sound 1.0 built in), not the p5.js editor: the editor\'s default has been p5.js 2.x since August 2026, and this p5.sound code needs 1.x. The point of the exercise is the spec and the comparison, not the file.'))

S.append(activity('1 — ALONE · THE SPEC', 5, 'Write the spec.',
                  ['Pick a product you know and a moment in it: a lock opening, a payment going through, an app starting, a timer ending.',
                   'Fill the template. **Numbers where you can**: seconds, BPM. Words where you must: mood, timbre, like, not like. One must-not at least.',
                   'The words are the deliverable. Ask a language model to check it if you like; do not let it write the mood for you.'],
                  panel=SOUND_SPEC, panel_size=22, bg=YELLOWS[0],
                  notes='Five minutes, silent. Watch for specs with no purpose line and no must-not — both come back to bite in round two. Watch for "epic" and "cinematic": the middle of every music model. Push for a moment: a sound without a moment is a song, not a product sound.'))

S.append(question('short_answer', 'Everyone: the product, the moment, the length.',
                  hint='One line, like "a bike-share app · the lock clicks open · 3 s". We put all of them on the wall.',
                  eyebrow_text='07 · CAPTURE 1 · SHORT ANSWER · EVERYONE',
                  notes='ClassPoint short answer, everyone, two minutes. The wall: a hundred products and moments. Read five aloud: the lengths cluster at three seconds and thirty; the moments are payments, unlocks and alarms. Point at one with a purpose you can hear in the line, and one without. Screenshot it.'))

S.append(activity('2 — IN PAIRS · THE MODEL', 10, 'Generate. Listen. Write what it decided.',
                  ['Pick the better of your two specs. Paste it into a language model with the instruction on the right; paste the prompt it writes into the music model. **Generate twice.**',
                   'Listen to both with the four questions. Tick the rule lines. Circle the middle. Box what it invented.',
                   '**Three lines: what did the model decide that the spec did not say?** Then fix one line of the spec and run once more.'],
                  panel=PROMPT_FOR_LM, panel_size=21, bg=YELLOWS[1],
                  notes='Ten minutes, one laptop per pair, headphones shared. Expect the four failures: the length ignored, a fade the spec never asked for, a voice appearing, the ukulele. The three lines are the work; every pair must write them before the fix. If the music model queues or fails, skip to round 4 and do the sequencer now — the three lines then describe what the sequencer could not do.'))

S.append(question('short_answer', 'Pairs: the spec in one line, the link, and one thing the model decided.',
                  hint='"3 s · 120 BPM · marimba, no voice · [link] · it added a reverb tail". One per pair.',
                  eyebrow_text='07 · CAPTURE 2 · SHORT ANSWER · ONE PER PAIR',
                  notes='ClassPoint short answer, one per pair, about 55 answers, two minutes. Put the wall up and read the "it decided" halves in a row: reverb, a fade, a voice, a key change, a second instrument. The list is the model\'s middle for "product sound", and nobody typed it. Keep the links: they are the start of Challenge 5.'))

S.append(activity('4 — TWO PAIRS · THE RULE', 10, 'The same brief, as a rule.',
                  ['Join the pair behind you. Take the better spec. Build it in the sequencer: **the spec\'s tempo, sixteen steps, three sounds at most.** Press C first.',
                   'Play both back to back: the model\'s and the grid\'s. **Which one is the product\'s?** All four have to agree, and say why in one sentence.',
                   'One scribe screenshots the grid — or the model\'s waveform — and uploads it with the spec as the caption.'],
                  sketch=live('w06-sequencer-act', SEQ_CODE, 1000, 600, hint='click to start · click a cell to toggle · mouse y = tempo · C clears', extra=SOUND_GUARD, sound=True),
                  bg=YELLOWS[2],
                  notes='Ten minutes in fours. The sequencer obeys the rule lines exactly and has no idea what "light, outdoors" means; the model had the mood and ignored the tempo. Four people arguing about which is the product\'s sound are doing the design. Expect a split: the grid wins for notifications and unlocks, the model for anything longer than five seconds. The sketch runs here in the html deck; the link on Blackboard opens the same sketch on its own page on the course site, on any device.'))

S.append(question('image_upload', 'Scribes only. The grid or the spectrogram, and the spec that made it.',
                  hint='One image per four: a screenshot of the sequencer grid, or of the model\'s waveform. Caption: the spec, word for word.',
                  eyebrow_text='07 · CAPTURE 3 · IMAGE UPLOAD · ONE PER FOUR',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': True},
                  notes='Scribes only, about 28 images, caption required. Put the wall on screen. Read two captions aloud and ask the room whether the picture is a grid or a waveform before showing it — a spec with numbers usually produced a grid. Download the submissions: they are the seed of Challenge 5 and evidence for the reflection.'))

S.append(content('07 · WHAT JUST HAPPENED', 'You wrote the spec. Two machines played it.',
                 ['The spec: half rules, half examples, and you could say which half was which. That is the reflection\'s argument, in your own product.',
                  'The model: it did what you said where you said it in numbers, and the middle where you said it in words. The list of what it decided is the same list for a hundred pairs.',
                  'The grid: exact, explainable, deaf to mood. You could point at the cell that decided, and you could not make it feel like a morning.',
                  '**The machine played every note. You wrote the spec. That was the design.**'],
                 body_size=32,
                 notes='Mirror of the whole class, and of weeks 1, 2 and 4: the cup, the spec, the brief, the sound. Say the last line slowly; it is the week-2 line with one word changed, for the third time. Then the sentence for the reflection: a sound has a rule side and an example side, and the designer is the one who decides which lines are which.'))

# ───────────────────────── 08 · the quiz, the reflection, the challenge ─────────────────────────
S.append(section('08', 'The quiz, the reflection, the challenge', 'three questions · the draft check · challenge 5 · week 7', bg=INK,
                 notes='Chapter eight: the last three mock questions, how the real quiz works, what a good reflection draft has, Challenge 5, and the homework. Twelve minutes.'))

S.append(question('multiple_choice', 'The Illiac Suite\'s fourth experiment (1957) chose notes with…', [
    'A coin toss for every note', 'A Markov chain: the next note depends on the last', 'A human composer correcting the machine', 'A microphone listening to the quartet',
], eyebrow_text='08 · MOCK QUIZ · 6 OF 8 · MULTIPLE CHOICE',
    notes='Question 6 of 8, today and the playlist. Correct: B. A is experiments one and two with the rules removed — not what they did; C is what happened to the third movement, which was adjusted by hand, but not the fourth. The live version was the orange cell moving across the table.'))

S.append(question('multiple_choice', 'Riffusion (December 2022) made music by…', [
    'Training a model on MIDI files', 'Generating spectrogram images with a diffusion model, then playing them', 'Recording musicians and mixing the takes', 'Applying the rules of counterpoint'],
    eyebrow_text='08 · MOCK QUIZ · 7 OF 8 · MULTIPLE CHOICE',
    notes='Question 7 of 8, today. Correct: B. Road one: Stable Diffusion fine-tuned on spectrograms, the picture played back with the inverse Fourier transform. A is road two\'s symbolic cousin, D is the Illiac. If the room gets this, the two roads landed.'))

S.append(question('multiple_choice', '"Designing things is designing human existence." Who wrote it?', [
    'Alan Turing, 1950', 'Ada Lovelace, 1843', 'Peter-Paul Verbeek, 2015', 'Sol LeWitt, 1967',
], eyebrow_text='08 · MOCK QUIZ · 8 OF 8 · MULTIPLE CHOICE',
    notes='Question 8 of 8, weeks 1 and 5, the core reading. Correct: C. Verbeek, Beyond Interaction, 2015 — the mediation reading. Lovelace wrote that the Engine cannot originate; LeWitt that the idea becomes a machine that makes the art; Turing asked whether machines can think. Four sentences, four weeks: know who said which.'))

S.append(content('08 · THE MID-TERM · WEEK 7 · 10%', 'Multiple choice. Weeks 1 to 6, and the playlist.',
                 ['In class next week, before the pitches. Questions in the shape you just saw: one idea, four choices, one right answer. Weeks 1 to 6 and the videos on the playlist, in course order.',
                  '- Revise from the decks: the PDFs are on the course site, one per week; the quick checks in each deck are the model of the questions.',
                  '- The playlist: 3Blue1Brown, the diffusion and CLIP videos, AltexSoft, AlphaGo, the Illiac Suite, Cage, Tinguely, Kaprow.',
                  '- The two machines are the spine of every question: which one is it, where does chance enter, what did it learn from.',
                  'Eight today, in this room: that is the practice. The scores are not graded.'],
                 body_size=30,
                 notes='Say clearly what is and is not examined: the decks and the playlist, nothing from outside them. The eight mock questions are not graded; the real one is ten percent. The revision advice is concrete: the quick checks in each deck, and the two machines as the question behind every question.'))

S.append(cards('08 · REFLECTION · DUE WEEK 7 · 20%', 'What a good draft has. Check it with a TA today.', [
    ('CONCEPTS · 30%', 'Both machines, accurately.', 'Rule-based and adaptive, explained in your own tools: which of your instruments are rules, which learned, and what each did to your process.'),
    ('ARGUMENT · 30%', 'A stance.', 'Where AI belongs in your creative process, and where it does not — and why. One claim, defended, not a list of pros and cons.'),
    ('EVIDENCE · 20%', 'Three experiments, with images.', 'At least three of your challenges from weeks 2 to 6, with the spec or prompt, the output, and what you changed. The walls from class count.'),
    ('CLARITY · 10%', 'About 1000 words, in order.', 'A structure a stranger can follow. A missing process note costs a band: say how you used AI to write it.'),
    ('ORIGINALITY · 10%', 'Something only you could say.', 'A cup, a spec, a brief, a layout, a sound: what surprised you, and what you did about it. Invented citations fail the assignment.'),
], text_size=20, head_size=28, notes='The rubric from the syllabus, with what a good draft has under each criterion. The TAs run the draft check after class today and before class next week: bring a draft, any length, and the three experiments you intend to use. The evidence card is where most drafts are thin: three experiments means three specs or prompts, three outputs and three edits — the walls from every class are on Blackboard.'))

S.append(cards('08 · CHALLENGE 5 · DUE BEFORE WEEK 7', 'Thirty seconds of sound.', [
    ('THE SPEC', 'Words first, numbers where you can.', 'A product, a moment, a purpose; length, tempo, mood, timbre, must-nots. Start from today\'s; it is the caption and the evidence.'),
    ('THE SOUND', 'A model, a rule, or both.', 'Up to thirty seconds: generated, sequenced, or a model\'s take edited by you. Say which. A link or a file on Blackboard, plus a screenshot of the spectrogram or the grid.'),
    ('THE TERMS', 'Name the tool and the plan.', 'Which model, which plan, what its terms let you do with the output. Three lines on what the model decided that you kept, or undid.'),
    ('THE VOTE', 'Next week, before the quiz.', 'The room listens to four and votes; winners get a star. The TAs help 30 minutes before and after class. The fifth and last piece of evidence for the reflection.'),
], notes='Three things on Blackboard before next class: the spec, the sound with a screenshot, and the terms-and-decisions note. The vote is first thing next week, before the quiz, so submissions close the night before. This is the last challenge: after next week the making moves into the group project.'))

S.append(content('08 · BEFORE WEEK 7', 'The reflection, the revision, the sound — and a pitch.',
                 ['**The individual reflection**, about 1000 words with three experiments, on Blackboard before class. Draft check with the TAs today after class and next week before it.',
                  '**Revise weeks 1 to 6** from the PDFs on the course site and the playlist. The quick checks are the model of the quiz.',
                  '**Challenge 5** on Blackboard: the spec, the sound, the terms.',
                  '**A pitch idea, one sentence:** a product or service in which a model decides something for each person. Next week you say it to the room in sixty seconds, and teams of four or five form around the ideas people want to build.',
                  f'[{SITE}]({"https://" + SITE}) · [{PLAYLIST.replace("https://", "")}]({PLAYLIST})'],
                 body_size=30,
                 notes='Four things, one of them new: the pitch. One sentence is enough — the product, who it is for, what the model decides. Next week the pitches take the middle hour, and teams form around them. Say the order of next week: the Challenge 5 vote, the quiz, the pitches, the teams.'))

S.append(end('See you next week. Mid-term: quiz, pitches, teams.',
             'Bring your sound, your reflection draft, and one sentence of a pitch.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Next week: the Challenge 5 vote, the mid-term quiz, your pitches, and teams of four or five. Homework in one line: the reflection, the revision, the sound, the sentence. The TAs stay for 30 minutes for the draft check.'))

DECK = dict(title='SD2112 · AI in Design · Week 06', slides=finalize(S, FOOTER), pdf='SD2112-week06.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week06', FOOTER, do_pptx=not only_html, do_html=True, do_png=not only_html, do_pdf=not only_html)
    for k, v in out.items():
        if k == 'warnings':
            print('\n'.join(v) if v else 'no text overflow warnings')
        elif k == 'png':
            print(f'png: {len(v)} previews')
        else:
            print(f'{k}: {v}')

# Sources (consulted 5 September 2026)
# Videos (titles verified with the YouTube oEmbed endpoint):
#   https://www.youtube.com/watch?v=bp7Qb8QY1Pw  AltexSoft, "How AI Sound and Music Generation Works"
#   https://www.youtube.com/watch?v=Ih9lHXMlrtE  "Dawn of Computer Music (2023) | Stanford Laptop Orchestra"
#   https://www.youtube.com/watch?v=n0njBFLQSk8  "Lejaren Hiller - Illiac Suite for String Quartet [1/4]"
#   https://slork.stanford.edu/events/notes/2023-slork-spring.pdf  (programme note: The Dawn of Computer Music, Feng, Kim, Li; 10 June 2023, Bing Concert Hall)
#   https://www.altexsoft.com/blog/sound-music-voice-generation/  (the article behind the video)
# Sound basics:
#   https://www.iso.org/standard/3601.html  (ISO 16:1975, A4 = 440 Hz)
#   https://en.wikipedia.org/wiki/A440_(pitch_standard)
#   https://www.open.edu/openlearn/science-maths-technology/engineering-technology/sound-music-technology-an-introduction/content-section-9.1  (20 Hz – 20 kHz)
#   https://www.recordingblogs.com/wiki/sampling-rate  (44,100 Hz)
#   https://www.britannica.com/biography/Joseph-Baron-Fourier  (Théorie analytique de la chaleur, 1822)
#   https://www.mixonline.com/technology/1983-dave-smith-sequential-circuits-midi-specification-383642
#   https://en.wikipedia.org/wiki/MIDI  (note on/off, 0–127, middle C = 60)
# Illiac Suite and early computer music:
#   https://en.wikipedia.org/wiki/Illiac_Suite  (four experiments; the fourth: Markov chains)
#   https://distributedmuseum.illinois.edu/exhibit/illiac-suite/  (premiere August 1956; composed by the end of 1956)
#   https://sandred.com/texts/Revisiting_the_Illiac_Suite.pdf  (screening rules; probability tables with simpler intervals more likely)
#   https://www.computerhistory.org/revolution/computer-graphics-music-and-art/15/222  (Max Mathews, MUSIC, 1957, IBM 704)
#   https://120years.net/music-n-max-mathews-usa-1957/  (Mathews and Newman Guttman, 1957: 17 seconds, "The Silver Scale")
#   https://www.guinnessworldrecords.com/world-records/454935-first-song-performed-using-computer-speech-synthesis  (Daisy Bell: Guinness says 1960 on an IBM 704, Lochbaum, Kelly, Mathews)
#   https://en.wikipedia.org/wiki/Daisy_Bell  (1961 on an IBM 7090, Kelly, Lochbaum, Mathews; Clarke, 2001: A Space Odyssey — the slide keeps 1961)
# Machine B for audio:
#   https://en.wikipedia.org/wiki/Riffusion  and  https://techcrunch.com/2022/12/15/try-riffusion-an-ai-model-that-composes-music-by-visualizing-it/
#   https://huggingface.co/riffusion/riffusion-model-v1  (fine-tuned from Stable Diffusion v1.5)
#   https://openai.com/index/jukebox/  and  https://siliconangle.com/2020/04/30/openai-debuts-jukebox-machine-learning-framework-creates-music/
#   https://www.deeplearning.ai/the-batch/google-introduces-an-ai-that-generates-music-from-text  (MusicLM, January 2023, SoundStream tokens)
#   https://www.engadget.com/metas-open-source-musicgen-ai-uses-text-to-create-song-genre-mashups-114030499.html  (MusicGen, June 2023, EnCodec)
#   https://huggingface.co/spaces/facebook/MusicGen  (the free demo)
#   https://stableaudio.com/pricing  (Stable Audio free tier)
# Products and terms:
#   https://suno.com/terms-of-service  (revised 10 August 2026, effective 3 September 2026: non-commercial on free; assignment of Suno's rights to paid subscribers; no warranty that copyright vests)
#   https://en.wikipedia.org/wiki/Suno_(platform)  (Cambridge MA, founders, v5.5 March 2026)
#   https://www.aiva.ai/pricing  (Free €0 / Standard €11 / Pro €33 a month, billed annually; copyright AIVA vs "owned by you")
#   https://en.wikipedia.org/wiki/AIVA  (February 2016, Luxembourg, SACEM)
# Voices:
#   https://en.wikipedia.org/wiki/Heart_on_My_Sleeve_(Ghostwriter977_song)  and  https://edition.cnn.com/2023/04/19/tech/heart-on-sleeve-ai-drake-weeknd
#   https://openai.com/index/how-the-voices-for-chatgpt-were-chosen/  and  https://variety.com/2024/digital/news/scarlett-johansson-responds-shocked-angered-openai-chatgpt-her-1236011135/
#   https://www.rollingstone.com/music/music-features/ai-band-the-velvet-sundown-confirm-ai-1235379354/
# Lawsuits:
#   https://variety.com/2024/music/news/record-labels-sue-ai-music-services-suno-and-udio-copyright-infringement-1236045366/  (24 June 2024)
#   https://www.musicbusinessworldwide.com/universal-music-settles-udio-lawsuit-strikes-deal-for-licensed-ai-music-platform/  (29 October 2025)
#   https://www.prnewswire.com/news-releases/universal-music-group-and-udio-announce-udios-first-strategic-agreements-for-new-licensed-ai-music-creation-platform-302599129.html
#   https://www.billboard.com/pro/udio-deal-backlash-ai-users-download-ai-songs-48-hours/  (downloads off 30 October; 48-hour window)
#   https://techcrunch.com/2025/11/19/warner-music-settles-copyright-lawsuit-with-udio-signs-deal-for-ai-music-platform/  (19 November 2025)
#   https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/  (25 November 2025)
#   https://www.musicbusinessworldwide.com/sony-music-files-new-lawsuit-against-ai-platform-udio-asserting-over-30000-sound-recordings-a-judge-barred-it-from-adding-to-its-original-case/  (20 July 2026)
#   https://www.musicweek.com/publishing/read/gema-wins-court-ruling-on-breach-of-copyright-by-ai-music-firm-suno/094644  (31 July 2026, Munich)
#   https://completemusicupdate.com/universal-and-sony-file-amended-suno-lawsuit-after-judge-gives-all-clear-to-add-stream-ripping-claims/  (25 August 2026)
# Sonic identity:
#   https://www.thx.com/deepnote/  and  https://en.wikipedia.org/wiki/Deep_Note  (1983, James A. Moorer)
#   https://timeline.intel.com/1995/the-intel-bong  (composed 1994, debuted 1995, three seconds, five notes)
#   https://www.intel.com/content/www/us/en/support/articles/000015030/programs.html
#   https://www.musicradar.com/artists/producers-engineers/the-thing-from-the-agency-said-we-want-a-piece-of-music-that-is-inspiring-universal-blah-blah-da-da-da-and-at-the-bottom-it-said-and-it-must-be-3-and-1-4-seconds-long-brian-enos-windows-95-start-up-sound-added-to-the-us-library-of-congress  (the brief quoted whole; about six seconds delivered)
#   https://github.com/processing/p5.js/issues/8870  and  https://github.com/processing/p5.js-web-editor/issues/3513  (p5.js 2.x the editor's default since 31 July / August 2026; the 1.x p5.sound throws under 2.x — why the sequencer link is the site's own page)
#   https://www.hollywoodreporter.com/news/general-news/netflixs-signature-sound-was-a-goats-bleat-1305916/  (Lon Bender, 2015)
#   https://www.mastercard.com/news/europe/en-uk/newsroom/press-releases/en-gb/2019/february/sound-on-mastercard-debuts-sonic-brand/  (8 February 2019)
