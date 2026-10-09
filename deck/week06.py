"""Week 6: sound and music with explicit rules, learned patterns and both."""
from pathlib import Path
import base64
import sys
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import attach_reports, INK, PAPER, TEALS, VIOLETS, YELLOWS
from deckgen.layouts import (title, end, agenda, section, statement, content, cards,
                             question, activity, two_col, figure_slide, code_slide,
                             live, finalize)
from course import SITE, footer
import week06_figures as F

FOOTER = footer(6)
EASEL = 'https://github.com/venetanji/easel-client/releases'
STRUDEL = 'https://strudel.cc/workshop/getting-started/'
SUNO = 'https://suno.com/'
S = []
ANALYSIS_CODE = (Path(__file__).parent / 'week06_analysis.js').read_text()

# The lecture instrument uses bundled p5 for drawing and native Web Audio.
# It stays silent until a real click and closes its audio context on Stop.
SEQ_CODE = """const W = 1000, H = 600;
const pitches = [261.63, 329.63, 392, 493.88];
let grid = [[1,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0],
            [0,1,0,1,0,1,0,1],[0,0,0,1,0,0,0,1]];
let ctx = null, running = false, starting = false, generation = 0, bpm = 100, step = -1;
let nextTime = 0, timer = null;
function setup() { createCanvas(W,H); textFont('monospace'); }
function draw() {
  background(255); noStroke(); fill(0,11,28); textSize(25);
  text('A written score: click cells to change the rule',40,42);
  textSize(18);
  for(let c=0;c<8;c++) text(c+1,95+c*110,105);
  for(let r=0;r<4;r++) text(['C4','E4','G4','B4'][r],15,160+r*80);
  for(let r=0;r<4;r++) for(let c=0;c<8;c++) {
    fill(grid[r][c] ? '#246E70' : '#EAF2F2');
    rect(60+c*110,120+r*80,96,65,5);
    if(c===step && running) { noFill(); stroke('#ED6D24');
      strokeWeight(4); rect(60+c*110,120+r*80,96,65,5); noStroke(); }
  }
  fill('#000B1C'); rect(60,470,170,55,5);
  fill(255); text(running?'STOP':'PLAY',100,507);
  fill('#000B1C'); text(bpm+' BPM',285,507);
  text('click here: slower     faster',460,507);
  textSize(18); text('Quiet start. Escape stops. No microphone or recording.',60,566);
}
function schedule() {
  if(!running || !ctx) return;
  while(nextTime < ctx.currentTime + 0.12) {
    step=(step+1)%8;
    for(let r=0;r<4;r++) if(grid[r][step]) {
      const o=ctx.createOscillator(),g=ctx.createGain();
      o.type='sine'; o.frequency.value=pitches[r];
      g.gain.setValueAtTime(0,nextTime);
      g.gain.linearRampToValueAtTime(0.035,nextTime+0.01);
      g.gain.exponentialRampToValueAtTime(0.0001,nextTime+0.22);
      o.connect(g);g.connect(ctx.destination);o.start(nextTime);o.stop(nextTime+0.24);
    }
    nextTime+=60/bpm/2;
  }
}
function stopAudio() {
  generation++; running=false; starting=false; clearInterval(timer);timer=null;
  if(ctx) {ctx.close();ctx=null;} step=-1;
}
async function mousePressed() {
  if(mouseY>=120 && mouseY<440 && mouseX>=60 && mouseX<940) {
    const r=floor((mouseY-120)/80),c=floor((mouseX-60)/110);
    if(r<4 && c<8) grid[r][c]=1-grid[r][c];return;
  }
  if(mouseY>=470 && mouseY<=525) {
    if(mouseX>=60 && mouseX<230) {
      if(running || starting) {stopAudio();return;}
      starting=true; const token=++generation;
      try {
        ctx=new (window.AudioContext || window.webkitAudioContext)();
        const local=ctx; await local.resume();
        if(generation!==token || ctx!==local || local.state==='closed') return;
        running=true;nextTime=ctx.currentTime+0.03;
        schedule();timer=setInterval(schedule,25);
      } catch(error) {
        if(generation===token) stopAudio();
        console.error('Audio could not start',error);
      } finally {if(generation===token) starting=false;}
    } else if(mouseX>=460 && mouseX<950) bpm=constrain(bpm+(mouseX<700?-10:10),40,180);
  }
}
function keyPressed() { if(keyCode===27) stopAudio(); }
window.addEventListener('keydown',e=>{
  if(e.key==='Escape') {stopAudio();e.preventDefault();e.stopImmediatePropagation();}
},true);
document.addEventListener('visibilitychange',()=>{if(document.hidden) stopAudio();});
window.addEventListener('pagehide',stopAudio);
window.addEventListener('message',e=>{
  if(e.source===window.parent && e.data==='slide:stop') stopAudio();
});
"""

# The online editor parses double-quoted mini-notation; single quotes are literals.
RHYTHM_CODE = 'note("c2 ~ c2 ~").s(\'sine\').decay(0.08).sustain(0).gain(0.25)'
BASS_CODE = 'note("c2 c2 g2 c2").s(\'triangle\').gain(0.18)'
HARMONY_CODE = 'note("[c3,e3,g3]").s(\'sine\').gain(0.12)'
MELODY_CODE = 'note("c4 e4 g4 b4").s(\'sine\').gain(0.22)'
PARTS = [('rhythm', RHYTHM_CODE), ('bass', BASS_CODE),
         ('harmony', HARMONY_CODE), ('melody', MELODY_CODE)]


def starter_code(count=4):
    declarations = '\n'.join(f'const {name} =\n  ' + code.replace('.s(', '\n  .s(').replace('.gain(', '\n  .gain(') + ';' for name, code in PARTS[:count])
    return ('// Online Strudel editor: native synths only\nsetcpm(100/4); // 100 beats per minute\n'
            + declarations + '\nstack(' + ', '.join(name for name, _ in PARTS[:count]) + ')')


def editor_link(code):
    return 'https://strudel.cc/#' + quote(base64.b64encode(code.encode()).decode(), safe='')


STR_CODE = starter_code()


S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 06',
               'Sound machines.', 'Music with rules. Music with learned patterns. Music with both.',
               notes='Theory first, then break, instructor demo, brief and making. Headphones ready; start quiet. The 2025 Week 6 PDF pages 25–50 and PR #3 are starting sources, not an unchanged script.'))
S.append(agenda('SOUND AND MUSIC · THE ROADMAP', [
    'Sound, music and listening', 'Machine A · compose the procedure',
    'Machine B · generate from patterns', 'Agents · coordinate A+B',
    'Break, then play and export', 'Your demo becomes the reference',
    'Listen, decide, submit', 'Challenge 5 · reflection · Week 7',
]))
S.append(statement('A sound changes\nwhat you notice\nand what you do.',
                   eyebrow_text='LISTENING IS A DESIGN RELATION', bg=PAPER, size=104,
                   notes='Connect to Ihde and Verbeek from Week 5 without re-teaching their philosophy. A notification directs attention; a cue can support action or interrupt it. The same recording on headphones, a phone speaker and a public installation is not the same listening situation. This is our application of mediation, not a quotation. Ask students to imagine hearing their cue repeatedly.'))
S.append(figure_slide('SOUND · TIME DOMAIN', 'A waveform shows change over time.', F.w06_analysis_still(),
    sketch=live('w06-live-analysis', ANALYSIS_CODE, 1200, 700,
                hint='Click Play · change pitch and waveform · watch frequency through time'),
    caption='Click Play in HTML · one quiet sound, waveform, spectrum and waterfall · no microphone.',
    notes='Airborne sound is a longitudinal pressure wave; the drawn waveform is pressure or signal amplitude against time, not air moving up and down. Frequency relates to pitch for periodic sounds, but a complex sound has many frequencies. Source: 2025 Week 6 PDF25–30; Open University Sound, music and technology.'))
S.append(cards('DIGITAL AUDIO · TWO DIFFERENT CHOICES', 'Samples in time. Values in each sample.', [
    ('SAMPLE RATE', 'How often we measure.', '44,100 samples per second is one common rate. A higher rate is not automatically a better composition.'),
    ('BIT DEPTH', 'How finely we store values.', 'PCM bit depth sets quantization precision and affects available dynamic range. It is not the number of samples.'),
    ('RECONSTRUCTION', 'Numbers become sound.', 'A playback system reconstructs a signal, moves a speaker and changes air pressure. A file alone is not a listening experience.'),
], text_size=27, notes='Source: 2025 PDF29. Nyquist limit is half the sample rate for band-limited signals; anti-alias filtering matters. Do not demonstrate extremes of loudness or hearing thresholds.'))
S.append(content('SOUND · FREQUENCY DOMAIN', 'One moment. Many frequencies.', [
    'The spectrum measures frequency components in a short window.',
    'FFT computes a discrete Fourier transform efficiently.',
    'Change sine to sawtooth in the live sketch: harmonics appear.',
    'Older spectra recede in the waterfall. Window size trades time and frequency resolution.',
], body_size=29, figure=F.w06_analysis_still('w06-spectrum-still'),
    sketch=live('w06-frequency-analysis', ANALYSIS_CODE, 1200, 700,
                hint='Play · SINE / TRIANGLE / SAWTOOTH · change pitch · Escape stops'),
    caption='Frequency × time × relative level · analysis, not an equalizer effect.',
    notes='The native Web Audio AnalyserNode measures the actual audible signal using a 2048-sample FFT and Blackman window, with smoothing disabled. Displayed log-spaced frequency bins repeat where FFT resolution is coarse. Waterfall rows are captured roughly every 60 ms, not one independent FFT hop per sample. Height displays -100 to -20 dBFS; it is not loudness. 220 Hz sine is the default; the PDF/PPTX illustration is explicitly not a measured capture. No microphone or p5.sound dependency. Stop on Escape and navigation.'))
S.append(figure_slide('SOUND · A PICTURE THROUGH TIME', 'A spectrogram keeps the changing spectrum.', F.w06_spectrogram_how(),
    caption='Time × frequency · colour encodes magnitude or energy, not human loudness directly.',
    notes='Source: 2025 PDF33 and original PR #3 computed figure. Explain short windows in sequence. Horizontal harmonic bands and transient stripes help compare tone and attack. A magnitude spectrogram omits phase; converting a generated image back to audio requires reconstruction, not simply playing pixels.'))
S.append(content('LISTENING · THE BODY IS NOT A NEUTRAL METER', 'Equal amplitude does not mean equal loudness.', [
    'Our sensitivity changes with frequency and listening level.',
    'A sound’s meaning also depends on context, repetition and expectation.',
    'Design for the listener and the device—not only the waveform.',
    'Start quietly. Use headphones. Never test your hearing by raising the volume.',
], body_size=34, notes='2025 PDF34–35 shows equal-loudness contours, not one universal hearing threshold. Individual hearing varies. No loud sweep or student microphone collection is needed.'))
for number, (layer, description) in enumerate([
    ('Rhythm', 'Place attacks and rests.'),
    ('Bass', 'Anchor the pulse and pitch.'),
    ('Harmony', 'Let notes sound together.'),
    ('Melody', 'Make a phrase through time.'),
], 1):
    part_name, part_code = PARTS[number - 1]
    code = ('setcpm(100/4); // shared 100 BPM\n\n'
            + f'const {part_name} =\n  ' + part_code.replace('.s(', '\n  .s(').replace('.gain(', '\n  .gain(')
            + f';\n\n{part_name}')
    S.append(code_slide('MUSIC · ONE ROLE AT A TIME', layer + ': ' + description, code,
        F.w06_layer(layer), code_size=27, lang='js', edit=False,
        caption='[Open ' + layer.lower() + ' + earlier layers in Strudel](' + editor_link(starter_code(number)) + ')',
        notes='The left panel isolates this role; the editor link combines it with earlier roles in one 100 BPM starter. Native oscillators, no external sample packs. Rhythm alternates a short C2 sine attack with a rest; bass has four triangle notes C2 C2 G2 C2; harmony sustains C3 E3 G3 together for one cycle; melody plays C4 E4 G4 B4. One cycle is four beats, 2.4 seconds at 100 BPM. These are useful roles, not universal rules of music. Timbre and articulation affect every layer. The online Strudel REPL is separate from Easel app.js: do not paste top-level REPL code into createPattern unchanged. Human presses Play.'))
S.append(figure_slide('REPRESENTATIONS · MIDI', 'MIDI describes events. It contains no sound.', F.w06_midi(),
    caption='A score is not a recording · the instrument or synthesizer supplies the sound.',
    notes='2025 PDF42. Simplified note view: pitch, onset, duration and velocity. MIDI itself carries messages including note-on/off, controllers and more; time and duration belong to sequencing/file context. Velocity is not always literal loudness. Do not equate MIDI with compressed audio.'))

S.append(section('01 · MACHINE A', 'Compose the procedure.', 'SYNTHESIS · SEQUENCING · RULES · CHANCE', bg='#246E70'))
S.append(content('HILLER AND ISAACSON · 1956–57', 'The Illiac Suite: a program writes a score.', [
    'Explicit constraints and probability generate material for a string quartet.',
    'Generate → test → keep: chance proposes notes; written constraints select them.',
    'Other experiments explore probability tables and Markov processes.',
    '[Read the Illinois museum account](https://distributedmuseum.illinois.edu/exhibit/illiac-suite/)',
], body_size=34, notes='PR #3 history retained. The Illinois museum records the first three movements performed on 9 August 1956 and four movements completed by the end of 1956; the score is commonly dated 1957. Avoid an absolute first-ever claim. The computer produced score data, not a virtual-string recording.'))
S.append(figure_slide('MACHINE A · TWO WRITTEN PROCEDURES', 'Chance can be part of a rule.', F.w06_generate_test(),
    caption='Illustrative constraints and probability table · not a transcription of the historical program.',
    notes='The handwritten table is A because we set its values. A learned probability table would have a different provenance; that does not make every learned music model a small Markov chain. Random proposal plus filtering remains an explicit procedure.'))
S.append(content('MACHINE A · SYNTHESIS', 'Compose the sound as well as the notes.', [
    'An oscillator supplies a signal. An envelope shapes its attack and decay.',
    'Combining and shaping signals creates timbre.',
    'Sine, triangle, square and sawtooth are useful starting sounds.',
    'A rule-based composition can be expressive: people design the rules and choose how to perform them.',
], body_size=34, notes='2025 PDF43. Do not teach that only B can create mood or that A is inherently unmusical. Additive, subtractive and other synthesis methods are examples; the Strudel starter deliberately uses a supported native oscillator.'))
S.append(figure_slide('MACHINE A · LIVE IN THE HTML DECK', 'The grid is a score you can change.', F.w06_written_score(),
    sketch=live('w06-written-score', SEQ_CODE, 1000, 600,
                hint='Play starts quietly · click cells · adjust BPM · Stop or Escape'),
    caption='Lecture instrument: four sine voices · eight steps · click Play for sound.',
    notes='This course-owned lecture instrument illustrates a written sequencer; it is not Easel or Strudel. Native Web Audio, no microphone and no external samples. Click Play, change a cell, then tempo; stop before navigation. PDF/PPTX show the illustrative grid still, not a live audio file.'))
S.append(code_slide('MACHINE A · STRUDEL', 'Four parts. One editable starter.', STR_CODE,
    F.w06_layer('Melody', 'w06-combined-starter'), code_size=23, lang='js', edit=False,
    caption='[Open the complete starter in Strudel](' + editor_link(STR_CODE) + ')',
    notes='This is runnable online-editor code, not a historical Illiac Suite reconstruction or the Easel template wrapper. Click the link, press Play yourself, change one note and one sound, then Stop. setcpm sets cycles per minute: 100/4 means 100 BPM for a four-beat cycle. Each role is an independent pattern passed to stack. The figure is a labelled melody-part illustration, not a complete four-part piano roll. Practical exporting and Easel reference upload start after the break. Gio owns testing/fixing the classroom integration; this source revision does not modify Strudel, Easel or shared Deckgen.'))
S.append(cards('MACHINE A · WHERE DID THE CHOICE GO?', 'Fixed rules. Variable outcomes.', [
    ('FIX', 'What must repeat?', 'A note pattern, entry point or duration can be specified explicitly.'),
    ('VARY', 'Where may chance enter?', 'Choose the possible notes, their probabilities or a permitted timing variation.'),
    ('LISTEN', 'What serves the brief?', 'Predictability is not automatically boring; randomness is not automatically creative.'),
], text_size=28, notes='Refer back to Week2 chance and seeds. A written probability rule can produce varied outputs; a learned model can also be run repeatably. The distinction is explicit design versus learned parameters, not deterministic versus random.'))
S.append(section('02 · MACHINE B', 'Generate from patterns.', 'EXAMPLES · REPRESENTATIONS · LEARNED POSSIBILITIES', bg=INK))
S.append(figure_slide('MACHINE B · TWO DOCUMENTED APPROACHES', 'A picture of sound. Or tokens of sound.', F.w06_two_roads(),
    caption='Historical Riffusion v1 and MusicGen illustrate mechanisms—not Suno’s unpublished internals.',
    notes='Use the documented models as conceptual bridges to Weeks4–5. Diffusion over spectrograms is one route; autoregressive codec-token generation is another. Other audio systems use different architectures including diffusion over latent audio. This is not an exhaustive taxonomy.'))
S.append(content('RIFFUSION V1 · 2022', 'Generate a spectrogram, then reconstruct audio.', [
    'Stable Diffusion 1.5 was fine-tuned on spectrogram images with text descriptions.',
    'A prompt conditions a new magnitude-spectrogram image.',
    'A reconstruction stage estimates phase and converts it back to audio.',
    '[Read the original Riffusion model card](https://huggingface.co/riffusion/riffusion-model-v1)',
], body_size=29, image=str(Path(__file__).parent / 'assets/week06/riffusion-v1-interface.png'), fit='contain', caption='Original Riffusion interface · Forsgren & Martiros, 2022 · MIT', notes='Do not confuse historical modelv1 with current commercial offerings. The original converter uses magnitude representations and phase estimation; an arbitrary picture is not directly a playable waveform. Sources: modelcard and github.com/riffusion/riffusion spectrogram_converter.py.'))
S.append(content('MUSICGEN · 2023', 'Predict learned codes. Decode them into sound.', [
    'A neural audio codec represents short segments using discrete codes.',
    'A transformer predicts code sequences conditioned on a description.',
    'The codec decoder reconstructs the audio waveform.',
    '[Read MusicGen’s documented mechanism](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)',
], body_size=29, figure=F.w06_musicgen(), notes='Official AudioCraft docs: 32 kHz EnCodec tokenizer, four codebooks at 50 Hz; delayed codebooks permit 50 autoregressive steps per second. Tokens are not necessarily notes, words or instruments. Do not equate the transformer with a handwritten eight-note Markov table or promise ordinary-laptop inference.'))
S.append(content('MACHINE B · SUNO', 'Your demo can guide a new musical proposal.', [
    'Supply your own exported demo as audio reference; describe the transformation.',
    'Listen to the actual result: arrangement, pacing, timbre, voices and surprises.',
    'Keep a candidate because it serves the brief—not because it arrived first.',
    '[Suno](https://suno.com/) · generate through the configured Easel integration in the workshop.',
], body_size=29, image=str(Path(__file__).parent / 'assets/week06/suno-public-interface.png'), fit='contain', caption='Public Suno landing page · 9 Oct 2026 · not the Easel interface.', notes='Gio confirms a Thursday Easel release with proper Suno support. Verify the generation tool and model ID, bounded request, job receipt and completion, saved output and import. Exact tool arguments are not invented here. Audio-upload/reference is the intended exercise; Gio tests the actual Easel operation and provider access. Do not promise exact BPM, duration, stems or precise preservation of the motif. No paid music generation was used to prepare this draft.'))
S.append(cards('MACHINE B · LISTEN TO THE UNSPECIFIED CHOICES', 'The model fills gaps. You decide what stays.', [
    ('REQUESTED', 'What did you ask for?', 'A listener, a moment, a mood, some instruments and constraints.'),
    ('PROPOSED', 'What arrived anyway?', 'A key, an extra instrument, an ending, a voice or a familiar stylistic convention.'),
    ('SELECTED', 'What did you keep?', 'Accept, reject or revise for a reason. Record the choice, not only the prompt.'),
], text_size=28, notes='Learned regularities can make familiar choices likely, but output is not simply a statistical average or nearest training example. A candidate may violate even numeric constraints. Compare actual results rather than claiming that the model obeyed the numbers.'))
S.append(cards('AUTHORSHIP · YOUR ORIGINAL INPUT', 'Your original demo is still your work.', [
    ('INPUT', 'Keep your creation history.', 'Suno consumer terms say you retain your rights in your original demo. Exporting a file does not establish rights in borrowed loops or voices.'),
    ('PERMISSION', 'Uploading grants a licence.', 'Suno receives a broad licence to use uploaded material, including service/model improvement. Ownership is not confidentiality.'),
    ('CONSENT', 'Clear all contributions.', 'Use original or appropriately licensed notes, audio and lyrics. Obtain the necessary consent for collaborators and voices; attribution alone is not permission.'),
], text_size=25, notes='Current Suno consumer terms checked 9 Oct 2026: Submissions remain yours as between Suno and you, but the licence is worldwide, non-exclusive, royalty-free, perpetual and irrevocable. These consumer terms do not establish the Easel integration contract. Avoid personal or confidential recordings. Primary source: https://suno.com/terms-of-service . Hong Kong legal copyright and musical-work/sound-recording rights may differ.'))
S.append(content('RIGHTS · GENERATED OUTPUT', 'Permission is not a copyright guarantee.', [
    'Free/Basic consumer generations: personal, non-commercial use.',
    'Pro/Premier: assigned Suno rights, subject to current terms; commercial use requires an approved download.',
    'Paying later does not automatically license older free-plan songs. Copyright protection is not guaranteed.',
    '[Read the Suno terms](https://suno.com/terms-of-service). Check the Easel/provider agreement—not just a consumer plan.',
], body_size=31, notes='Terms revised 10 Aug 2026, effective 3 Sep 2026, checked 9 Oct 2026. Approved-download limits and channels apply; recording/stream ripping is not a substitute. Collaborative Remixes have specific non-commercial restrictions even on paid plans; do not confuse them with every own-demo transformation. Suno assigns rights it owns, not guaranteed statutory copyright or uniqueness. Help articles may use simplified/older wording. Hong Kong computer-generated-work rules differ from US rules; the necessary arranger and originality are fact-specific. Do not offer a legal opinion. Easel credits do not prove a personal Pro account or commercial entitlement. Sources: terms; help.suno.com/en/articles/2425729; Hong Kong IPD 8 July 2024 consultation PDF pp10,16–17.'))

S.append(section('03 · AGENTS · A+B', 'Coordinate both machines.', 'THE AGENT IS NOT A THIRD MAGIC MUSIC MODEL', bg='#246E70'))
S.append(cards('AGENT HARNESS · PROPOSAL / EXECUTION / APPROVAL', 'The agent helps. You choose the reference.', [
    ('MAKE', 'Write or play a demo.', 'You and an agent can write Strudel notes; the runtime plays explicit rules. GarageBand or another tool is also fine.'),
    ('TRANSFORM', 'Give B your exported audio.', 'The agent supplies your rights-cleared demo to the supported Suno reference operation, tracks the job and saves its output.'),
    ('DECIDE', 'Listen against your intent.', 'You decide what the model preserved or changed. The agent can help save or trim, but cannot guarantee identity, rights or quality.'),
], text_size=26, notes='A learned agent can propose A code; the sound-producing runtime executes explicit instructions. A reference is actual audio, not merely a text description. This exercise uses an A-made demo to condition B generation, not unrelated A/B clips spliced into prescribed seconds. Keep learned proposal, software/tool execution and human approval distinct. Reference upload through the classroom Easel integration requires the instructor test; this deck build does not verify it.'))
S.append(two_col('A+B · A DEMO BECOMES A REFERENCE', 'Keep an intention. Let the arrangement change.', [
    'Make a short motif or demo with notes, pulse and a chosen sound.',
    'Export an audio file. MIDI or a screenshot alone is not the audio reference.',
    'Use that file through Easel to guide Suno, with a clear transformation brief.',
    'Listen: what stayed recognizable, what changed, and what serves the listener?',
], ['YOUR DEMO', 'Strudel / GarageBand / other tool', '', 'EXPORTED AUDIO', 'rights-cleared reference input', '', 'SUNO TRANSFORMATION', 'listen / choose / revise / save'],
    right_size=25, left_size=31,
    notes='No compulsory 4/12/16-second timeline, intro/excerpt/outro or stems. A+B here is reference-conditioned generation: A provides authored material; B proposes a new arrangement. Cover/re-arrangement or Extend depends on the actual classroom operation Gio demonstrates. Do not equate upload with guaranteed musical fidelity. Preserve both the original audio and provenance, but collect only one final playable output. The final cue remains up to 30 seconds; trimming is allowed using tested tools.'))
S.append(statement('Break.\nTen minutes.', eyebrow_text='AFTER THE BREAK · DEMO → BRIEF → MAKING', bg=PAPER,
    notes='1:00–1:10. This is the end of the theory lecture. TAs check headphones, Easel launch and access; do not start a generation job for every student during the break.'))
S.append(title('SD2112 · WEEK 06 · EASEL WORKSHOP', 'Your demo.\nA new arrangement.',
    'Make a motif. Export it. Use it as the reference. Listen.', size=128,
    notes='Practical chapter starts after all theory. Instructor demo 1:10–1:20; setup and brief 1:20–1:35; making 1:35–2:15; flexible feedback 2:15–3:00.'))
S.append(content('INSTRUCTOR DEMO · AFTER THE BREAK', 'Play → export → reference → listen.', [
    'Make a simple demo in Strudel or GarageBand. Change notes, rhythm or timbre.',
    'Export audio and replay that file—not only the editor preview.',
    'Give Easel the exported demo; use the supported Suno reference workflow.',
    'Hear the saved transformation. What recognisable feature survived?',
], body_size=32, notes='Ten minutes after the break, not a student export task during the theory lecture. Gio is fixing/testing the local Strudel/Easel integration; do not modify it as part of course-source work. Prepare the original demo, a completed reference-conditioned output and a labelled licensed fallback. Show the real supported operation; do not invent tool arguments, upload limits or pretend a pending job finished. Avoid duplicate submissions and paid generation during deck preparation.'))
S.append(content('SETUP · CLASSROOM RELEASE', 'Choose a demo tool. Check the reference route.', [
    '[Download Easel](https://github.com/venetanji/easel-client/releases). Use the classroom version Gio identifies.',
    '[Open the Strudel starter](' + editor_link(STR_CODE) + '), or use GarageBand or another available music tool.',
    'Check Play/Stop, quiet headphones and export to an audio format the reference tool accepts.',
    'Confirm Easel/Suno reference access. Pair up or use the labelled fallback if needed.',
], body_size=30, notes='Before class Gio verifies/fixes the actual reference upload, generation and saved-output path. This deck does not assert a published release contains the necessary features, consumer upload limits or entitlement. Do not paste credentials into prompts, code or submissions. Online Strudel is a separate editor; export through the demonstrated supported route. Pairing and fallback must preserve honest attribution.'))
S.append(content('SHARED BRIEF · A SONIC IDENTITY', 'Make a sound for one identity and moment.', [
    'Use your previous mark/product—or invent an identity. No personal recording needed.',
    'Choose a listener and a moment: opening, arriving, completing, waiting.',
    'Name one recognizable musical feature and one thing the sound must not do.',
    'Make a short result, up to 30 seconds. Let your demo guide the generated version.',
], body_size=33, notes='Fictional identities are allowed. Connect the Week 5 mark to Week 6 sound and the existing product-sound brief. Students need neither last week’s image as input nor a video render. A full song or lyrics are not required.'))
S.append(two_col('THE SOUND SPEC · YOUR DECISIONS', 'Be precise about intent. Honest about control.', [
    'Numbers can be enforced in code—but a model may only approximate a numeric request.',
    'Mood can be composed with rules or proposed by a learned model.',
    'Judge on the intended device and in the intended moment.',
    'Keep code, prompt, saved assets and one deliberate revision as process evidence.',
], ['LISTENER / IDENTITY', 'WHEN IT PLAYS', 'DESIRED EFFECT', 'LENGTH / PULSE',
    'TIMBRE / MUSICAL FEATURE', 'MUST NOT', 'WHAT I WILL LISTEN FOR'],
    right_size=26, left_size=31,
    notes='Correct the old PR #3 overstatement: B has no exact-constraint guarantee. This is a private working brief, not another required capture. Mood is not exclusive to B and timbre is not inherently beyond rules.'))
S.append(cards('MAKING · 40 MINUTES · HEADPHONES ON', 'Demo → exported reference → transformation → save.', [
    ('15 MIN', 'Make and export.', 'Build a small demo you can explain.'),
    ('15 MIN', 'Transform from audio.', 'Supply that demo to Suno through Easel.'),
    ('5 MIN', 'Listen and revise.', 'Keep or change a deliberate musical choice.'),
    ('5 MIN', 'Check and save.', 'One final playable result; no intermediate submissions.'),
], text_size=25, notes='Protect 15 + 15 + 5 + 5 = 40 minutes, 1:35–2:15. The student may explore the starter after the break; setup, access and brief are outside making time. If B queues, use the instructor fallback and label it honestly. No requirement to pay or repeat pending requests.'))
S.append(activity('1 · MACHINE A · YOUR DEMO', 15, 'Make and export a demo you can explain.', [
    'Use Strudel, GarageBand or another available tool to make a short original demo.',
    'Choose notes, rhythm and sound. Change one thing; listen to the difference.',
    'Export an audio file using the demonstrated route. Keep your code or project.',
    'Replay the exported file. This is the reference—not a MIDI file or screenshot.',
], panel=['YOUR INPUT', 'A small motif is enough.', 'Use material you have rights to upload.',
          'Make one deliberate change.', 'Export actual audio.', 'No compulsory intermediate submission.'], panel_size=24, bg=TEALS[4],
    notes='Fifteen minutes. Gio owns the local Strudel/Easel export test and integration fixes. The online starter uses native synths; it is not a promise of Easel export compatibility. GarageBand built-in material/loops still require checking the applicable permissions for provider upload/model use; prefer self-authored synth notes. Preserve the original audio and creation history. Export limits/file type must come from the actual tested classroom tool, not guessed consumer limits.'))
S.append(activity('2 · MACHINE B · USE THE REFERENCE', 15, 'Transform your demo—not an unrelated prompt.', [
    'Give Easel your exported audio as the Suno reference input.',
    'Ask for a new arrangement for the same identity and moment. Name what should remain recognisable.',
    'Use the supported reference operation Gio demonstrates. Track the pending job; do not duplicate it.',
    'Listen to a completed output and save it. Label any supplied fallback honestly.',
], panel=['ASK THE AGENT', 'Use this exported demo as reference.', 'Keep the intent and motif recognisable.',
          'Describe the desired transformation.', 'Save the completed output.', 'Do not invent a successful upload.'], panel_size=24, bg=YELLOWS[1],
    notes='Fifteen minutes. Reference-conditioned generation is the intended route, subject to the instructor test Gio performs of the local integration. Cover/re-arrangement or Extend depends on actual support; do not invent operation names or arguments. A textual description alone is not evidence that audio was attached. No precise BPM, duration, stems or motif fidelity guarantee. Consumer Suno terms do not establish the Easel/provider agreement. If upload fails, clearly label the fallback; do not silently substitute text-only generation and call it reference-conditioned.'))
S.append(activity('3 · A+B · LISTEN AND REVISE', 5, 'What did the reference actually change?', [
    'Replay your original demo, then the completed transformation. Stop competing players.',
    'Identify one preserved feature and one changed or missing feature.',
    'Keep the result, or make one supported edit or revision for your listener.',
    'Check the final cue is up to 30 seconds. Trim with a tested tool if needed.',
], panel=['YOUR DECISION', 'Listen for the intended motif.', 'Do not claim fidelity from the prompt.',
          'Keep one reason for your revision.', 'No compulsory A/B spliced timeline.', 'Do not regenerate by default.'], panel_size=24, bg=TEALS[4],
    notes='Five minutes. A+B is an authored demo conditioning a learned arrangement, not a fixed intro/excerpt/outro recipe. Compare actual sound and cite evidence; an honest missing motif matters. If no completed output exists, use the labelled fallback rather than fabricate a comparison. Retain process evidence privately; only one final result is collected.'))
S.append(activity('4 · LISTEN AND SAVE', 5, 'Check the final result—not just the preview.', [
    'Stop other players. Replay the arrangement at a quiet level.',
    'Save/export using the classroom release’s tested route.',
    'Reopen the saved result and check that it plays with sound.',
    'Submit that one final result. Keep iterations for your own process record.',
], bg=YELLOWS[0], notes='Final five minutes of the protected making block. Slide 41 collection is not a second timed exercise. Accept the actual verified format, including WebM with sound, rather than promising an MP3/WAV master. A failed job is not a finished asset; an honest partial or labelled fallback is acceptable.'))
S.append(content('ONE FINAL SUBMISSION · CANVAS', 'Submit your final playable result.', [
    'One saved file, or a working share link, in the classroom Canvas activity.',
    'Submit your chosen final cue—not separate demo, generation and comparison uploads.',
    'Check that it plays with sound. If export is WebM with audio, submit that file.',
    'Keep your brief, code, prompt and iterations for your process record.',
], body_size=33,
    notes='Exactly one required final classroom capture after three approaches. No compulsory caption, essay or intermediate captures. The instructor creates and tests the classroom Canvas activity; no specific private URL is invented. Pinned deckgen v0.11.2 has no native ClassPoint audio-upload generator; cp=None is intentional. Keep student files and private activity URLs out of the public repo. Challenge 5 and reflection assessment remain unchanged.'))
S.append(content('DEBRIEF · WHICH CHOICES BECAME YOURS?', 'A result is not the whole creative process.', [
    'What did your written pattern make possible—or rule out?',
    'What did the music model propose that you did not request?',
    'What stayed recognisable when your exported demo became the reference?',
    'Did the transformation help this listener? “Not this time” is a useful answer.',
], body_size=33, notes='Spoken/private questions, not extra ClassPoint buttons. Use flexible feedback time 2:15–3:00. Invite process discussion, not rankings of polish. A labelled failure or fallback can be evidence; it does not prove behavior of an untested model.'))
S.append(question('short_answer', 'What made this sound yours: the demo, the prompt, or the listening decision?',
    hint='Use one audible change from your demo and final result. Explain your contribution and its limits.',
    eyebrow_text='REFLECTION · AFTER LISTENING',
    notes='First of two deep short answers, after making. Use actual listening evidence, not an imagined output. A labelled fallback or failed attempt is valid process evidence if described honestly. Connect an argument about authorship, delegated choices and control to the existing reflection; no new assessed submission or required essay section.'))
S.append(question('short_answer', 'Which choice would you reclaim from the model—and why does it matter to your listener?',
    hint='Name a concrete change, the evidence you heard, and whether you would act in code, reference, prompt or editing.',
    eyebrow_text='REFLECTION · CONTROL AND RESPONSIBILITY',
    notes='Second and last ClassPoint short answer. Ask for evidence and interpretation, not A-good/B-bad or a popularity vote. Ground the answer in the demo/reference transformation or honestly labelled fallback. Develop the existing Week 7 reflection without extra grading or compulsory essay sections.'))
S.append(cards('WEEK 7 · MOCK QUIZ PRACTICE · NOT GRADED', 'Explain the difference before choosing an answer.', [
    ('1 REPRESENTATION', 'MIDI or audio?', 'Which contains instrument events rather than a recorded waveform? Explain what supplies the sound.'),
    ('2 PROCEDURE', 'Random means learned?', 'A written probability table selects notes. Is chance alone evidence that the system learned?'),
    ('3 GENERATION', 'Codes or literal notes?', 'MusicGen predicts codec tokens. Must one token correspond to one musical note?'),
], text_size=27, notes='Practice after making; no extra ClassPoint attention checks. Answers: MIDI carries event messages and a synth supplies sound; chance alone is not learning, the handwritten table is A; codec tokens are audio representations, not one token per note. Real Week 7 quiz remains multiple choice on Weeks 1–6 and the playlist, worth 10%.'))
S.append(cards('CHALLENGE 5 · BRING TO WEEK 7', 'Thirty seconds of sound.', [
    ('INTENT', 'For someone, at a moment.', 'A product or identity, a purpose and a short brief. Up to 30 seconds of sound.'),
    ('PROCESS', 'A, B or both.', 'Keep the sound, a grid/timeline/spectrogram image and one deliberate revision. Name the tool/model and route used.'),
    ('JUDGEMENT', 'Say what mattered.', 'What did you keep or change—and why? Note supplied assets and the terms that apply. Submit via Canvas.'),
], text_size=27, notes='Existing syllabus Challenge 5: thirty seconds of sound, before Week 7. The final classroom arrangement can be a starting point, not duplicated intermediate assessment. No new weight or deadline. Check current tool terms rather than copy stale pricing or litigation claims.'))
S.append(content('INDIVIDUAL REFLECTION · WEEK 7 · 20%', 'Turn listening into an evidence-led argument.', [
    'About 1000 words on AI in your creative process, especially Machine A and Machine B.',
    'At least three of your own weekly-challenge experiments from Weeks 2–6, with images.',
    'Use a concrete choice, output and revision to support a claim—not a list of tools.',
    'End with a short AI-writing process note. Submit on Canvas in Week 7.',
], body_size=30, notes='Existing reflection brief and 20% weighting, unchanged rubric and deadline. The two post-making ClassPoint answers are optional starting points for arguments, not compulsory essay sections. For music, grid/timeline/spectrogram images can support listening evidence. TA draft checks in flexible feedback and before/after class. Week 7 quiz, pitches and team formation remain unchanged.'))
S.append(end('Rules. Patterns.\nYour listening.', 'Next week: quiz, pitches, teams—and your reflection.', 'SD2112 · WEEK 06 · '+SITE,
    notes='Close with the designer’s responsibility for intent, selection, arrangement and listening context. No automatic production publication.'))

attach_reports(S, Path(__file__).resolve().parent / 'week06-reports.json')
DECK = dict(title='SD2112 · AI in Design · Week 06', slides=finalize(S, FOOTER), pdf='SD2112-week06.pdf')

# Sources: 2025 Week6 PDF25–50 and MasterPDF45; PR #3 week06 source and figures.
# Additional primary/source links are on the corresponding slides and in notes.
