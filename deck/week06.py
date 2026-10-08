"""Week 6: sound and music with explicit rules, learned patterns and both."""
from pathlib import Path
import sys

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

# The lecture instrument uses bundled p5 for drawing and native Web Audio.
# It stays silent until a real click and closes its audio context on Stop.
SEQ_CODE = """const W = 1000, H = 600;
const pitches = [261.63, 329.63, 392, 493.88];
let grid = [[1,0,0,0,1,0,0,0],[0,0,1,0,0,0,1,0],
            [0,1,0,1,0,1,0,1],[0,0,0,1,0,0,0,1]];
let ctx = null, running = false, bpm = 100, step = -1;
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
  running=false; clearInterval(timer);timer=null;
  if(ctx) {ctx.close();ctx=null;} step=-1;
}
async function mousePressed() {
  if(mouseY>=120 && mouseY<440 && mouseX>=60 && mouseX<940) {
    const r=floor((mouseY-120)/80),c=floor((mouseX-60)/110);
    if(r<4 && c<8) grid[r][c]=1-grid[r][c];return;
  }
  if(mouseY>=470 && mouseY<=525) {
    if(mouseX<230) {
      if(running) {stopAudio();return;}
      ctx=new (window.AudioContext || window.webkitAudioContext)();
      await ctx.resume();running=true;nextTime=ctx.currentTime+0.03;
      schedule();timer=setInterval(schedule,25);
    } else if(mouseX>=460 && mouseX<950) bpm=constrain(bpm+(mouseX<700?-10:10),40,180);
  }
}
function keyPressed() { if(keyCode===27) stopAudio(); }
document.addEventListener('visibilitychange',()=>{if(document.hidden) stopAudio();});
window.addEventListener('pagehide',stopAudio);
window.addEventListener('message',e=>{
  if(e.source===window.parent && e.data==='slide:stop') stopAudio();
});
"""

STR_CODE = """// In the Easel Strudel template's app.js
// Keep its existing controls and Play / Stop.
function createPattern(params) {
  return window.strudel
    .note('c4 e4 g4 b4')
    .s('sine')
    .gain(0.3)
    .attack(0.01)
    .release(0.05);
}
// Human presses Play; code defines the notes.
// Change one note, then one sound. Listen.
"""

S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 06',
               'Sound machines.', 'Music with rules. Music with learned patterns. Music with both.',
               notes='Theory first, then break, instructor demo, brief and making. Headphones ready; start quiet. The 2025 Week 6 PDF pages 25–50 and PR #3 are starting sources, not an unchanged script.'))
S.append(agenda('SOUND AND MUSIC · THE ROADMAP', [
    'Sound, music and listening', 'Machine A · compose the procedure',
    'Machine B · generate from patterns', 'Agents · coordinate A+B',
    'Break, then an Easel demo', 'One brief · three approaches',
    'Listen, decide, submit', 'Challenge 5 · reflection · Week 7',
]))
S.append(statement('A sound changes\nwhat you notice\nand what you do.',
                   eyebrow_text='LISTENING IS A DESIGN RELATION', bg=PAPER, size=104,
                   notes='Connect to Ihde and Verbeek from Week 5 without re-teaching their philosophy. A notification directs attention; a cue can support action or interrupt it. The same recording on headphones, a phone speaker and a public installation is not the same listening situation. This is our application of mediation, not a quotation. Ask students to imagine hearing their cue repeatedly.'))
S.append(figure_slide('SOUND · TIME DOMAIN', 'A waveform shows change over time.', F.w06_waveform(),
    caption='Illustrative computed signal · amplitude is not the same as perceived loudness.',
    notes='Airborne sound is a longitudinal pressure wave; the drawn waveform is pressure or signal amplitude against time, not air moving up and down. Frequency relates to pitch for periodic sounds, but a complex sound has many frequencies. Source: 2025 Week 6 PDF25–30; Open University Sound, music and technology.'))
S.append(cards('DIGITAL AUDIO · TWO DIFFERENT CHOICES', 'Samples in time. Values in each sample.', [
    ('SAMPLE RATE', 'How often we measure.', '44,100 samples per second is one common rate. A higher rate is not automatically a better composition.'),
    ('BIT DEPTH', 'How finely we store values.', 'PCM bit depth sets quantization precision and affects available dynamic range. It is not the number of samples.'),
    ('RECONSTRUCTION', 'Numbers become sound.', 'A playback system reconstructs a signal, moves a speaker and changes air pressure. A file alone is not a listening experience.'),
], text_size=27, notes='Source: 2025 PDF29. Nyquist limit is half the sample rate for band-limited signals; anti-alias filtering matters. Do not demonstrate extremes of loudness or hearing thresholds.'))
S.append(content('SOUND · FREQUENCY DOMAIN', 'What frequencies are inside this moment?', [
    'A spectrum describes frequency components in a selected time window.',
    'An FFT is an efficient algorithm for computing a discrete Fourier transform.',
    'A pure tone and a rich tone can share a fundamental, but have different spectra.',
    'Window size trades time resolution against frequency resolution.',
], body_size=34, notes='Correct the 2025 slide31 spelling to Fourier. FFT is an algorithm, not another kind of sound. Do not claim every finite or nonperiodic signal is exactly a short list of sines.'))
S.append(figure_slide('SOUND · A PICTURE THROUGH TIME', 'A spectrogram keeps the changing spectrum.', F.w06_spectrogram_how(),
    caption='Time × frequency · colour encodes magnitude or energy, not human loudness directly.',
    notes='Source: 2025 PDF33 and original PR #3 computed figure. Explain short windows in sequence. Horizontal harmonic bands and transient stripes help compare tone and attack. A magnitude spectrogram omits phase; converting a generated image back to audio requires reconstruction, not simply playing pixels.'))
S.append(content('LISTENING · THE BODY IS NOT A NEUTRAL METER', 'Equal amplitude does not mean equal loudness.', [
    'Our sensitivity changes with frequency and listening level.',
    'A sound’s meaning also depends on context, repetition and expectation.',
    'Design for the listener and the device—not only the waveform.',
    'Start quietly. Use headphones. Never test your hearing by raising the volume.',
], body_size=34, notes='2025 PDF34–35 shows equal-loudness contours, not one universal hearing threshold. Individual hearing varies. No loud sweep or student microphone collection is needed.'))
S.append(cards('MUSIC · RELATIONS WE CAN COMPOSE', 'Rhythm, bass, harmony, melody, timbre.', [
    ('TIME', 'Rhythm and pulse.', 'Onsets, rests, accents and duration. Tempo alone does not define a rhythm.'),
    ('PITCH', 'Melody and harmony.', 'Notes through time; notes sounding together. Bass often anchors rhythm and harmony, but need not always play the root.'),
    ('SOUND', 'Timbre and articulation.', 'The spectrum and its evolution, attack and decay, texture and expression. The same notes can feel very different.'),
], text_size=28, notes='2025 PDF36–40. These are useful components, not a universal definition of music. Music can be noisy, unpitched or without a steady pulse; meaning and cultural conventions matter.'))
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
S.append(code_slide('MACHINE A · STRUDEL', 'A pattern you can read, revise and hear.', STR_CODE,
    F.w06_strudel_pattern(), code_size=25, lang='js', edit=False,
    caption='Easel template example · four notes on a native synth · human presses Play.',
    notes='Target the upcoming Thursday Easel release containing PR #13. createPattern is in the template app.js; this is not the full strudel.cc REPL. Keep the template controls; tempo uses its existing parameter plumbing. Supported starter methods note/s/gain/attack/release. Do not promise sample packs, imported Suno-as-sample, effects or export of unsupported methods. Official tutorial: '+STRUDEL))
S.append(cards('MACHINE A · WHERE DID THE CHOICE GO?', 'Fixed rules. Variable outcomes.', [
    ('FIX', 'What must repeat?', 'A note pattern, entry point or duration can be specified explicitly.'),
    ('VARY', 'Where may chance enter?', 'Choose the possible notes, their probabilities or a permitted timing variation.'),
    ('LISTEN', 'What serves the brief?', 'Predictability is not automatically boring; randomness is not automatically creative.'),
], text_size=28, notes='Refer back to Week2 chance and seeds. A written probability rule can produce varied outputs; a learned model can also be run repeatably. The distinction is explicit design versus learned parameters, not deterministic versus random.'))
S.append(question('short_answer', 'Which musical choice would you fix—and which would you leave open?',
    hint='Choose a listener and moment. Give one fixed constraint, one open choice, and a reason.',
    eyebrow_text='REFLECTION MOMENT · MACHINE A',
    notes='Two minutes. One of only two ClassPoint short answers. Read contrasting reasons, not correct/incorrect choices. Connect to the existing reflection: a claim about control needs a concrete decision and evidence. These answers are possible starting points, not new compulsory essay sections or extra assessment.'))

S.append(section('02 · MACHINE B', 'Generate from patterns.', 'EXAMPLES · REPRESENTATIONS · LEARNED POSSIBILITIES', bg=INK))
S.append(figure_slide('MACHINE B · TWO DOCUMENTED APPROACHES', 'A picture of sound. Or tokens of sound.', F.w06_two_roads(),
    caption='Historical Riffusion v1 and MusicGen illustrate mechanisms—not Suno’s unpublished internals.',
    notes='Use the documented models as conceptual bridges to Weeks4–5. Diffusion over spectrograms is one route; autoregressive codec-token generation is another. Other audio systems use different architectures including diffusion over latent audio. This is not an exhaustive taxonomy.'))
S.append(content('RIFFUSION V1 · 2022', 'Generate a spectrogram, then reconstruct audio.', [
    'Stable Diffusion 1.5 was fine-tuned on spectrogram images with text descriptions.',
    'A prompt conditions a new magnitude-spectrogram image.',
    'A reconstruction stage estimates phase and converts it back to audio.',
    '[Read the original Riffusion model card](https://huggingface.co/riffusion/riffusion-model-v1)',
], body_size=33, notes='Do not confuse historical modelv1 with current commercial offerings. The original converter uses magnitude representations and phase estimation; an arbitrary picture is not directly a playable waveform. Sources: modelcard and github.com/riffusion/riffusion spectrogram_converter.py.'))
S.append(content('MUSICGEN · 2023', 'Predict learned codes. Decode them into sound.', [
    'A neural audio codec represents short segments using discrete codes.',
    'A transformer predicts code sequences conditioned on a description.',
    'The codec decoder reconstructs the audio waveform.',
    '[Read MusicGen’s documented mechanism](https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md)',
], body_size=34, notes='Official AudioCraft docs: 32 kHz EnCodec tokenizer, four codebooks at 50 Hz; delayed codebooks permit 50 autoregressive steps per second. Tokens are not necessarily notes, words or instruments. Do not equate the transformer with a handwritten eight-note Markov table or promise ordinary-laptop inference.'))
S.append(content('MACHINE B · SUNO', 'A prompt proposes music—not a finished decision.', [
    'Describe purpose, mood, instrumentation and what to avoid.',
    'Listen to the actual result: arrangement, pacing, timbre, voices and surprises.',
    'Keep a candidate because it serves the brief—not because it arrived first.',
    '[Suno](https://suno.com/) · generate through the configured Easel integration in the workshop.',
], body_size=34, notes='Gio confirms a Thursday Easel release with proper Suno support. Verify the generation tool and model ID, bounded request, job receipt and completion, saved output and import. Exact tool arguments are not invented here. Do not promise exact BPM, duration, stems, extensions or audio-reference support. No paid music generation was used to prepare this draft.'))
S.append(cards('MACHINE B · LISTEN TO THE UNSPECIFIED CHOICES', 'The model fills gaps. You decide what stays.', [
    ('REQUESTED', 'What did you ask for?', 'A listener, a moment, a mood, some instruments and constraints.'),
    ('PROPOSED', 'What arrived anyway?', 'A key, an extra instrument, an ending, a voice or a familiar stylistic convention.'),
    ('SELECTED', 'What did you keep?', 'Accept, reject or revise for a reason. Record the choice, not only the prompt.'),
], text_size=28, notes='Learned regularities can make familiar choices likely, but output is not simply a statistical average or nearest training example. A candidate may violate even numeric constraints. Compare actual results rather than claiming that the model obeyed the numbers.'))
S.append(content('AUTHORSHIP · CONSENT · REUSE', 'A usable file is not permission to use it.', [
    'Do not imitate a real person’s voice without informed permission.',
    'Name the tool and model; check the current provider terms and your plan.',
    'Ownership, reuse permission and legal copyright protection are different questions.',
    '[Read current Suno terms](https://suno.com/terms-of-service) before reusing an output.',
], body_size=34, notes='Keep a concise design responsibility discussion rather than copying PR #3’s dated litigation timeline. No blanket claim about Hong Kong law, guaranteed copyright or a particular account tier. API-provider terms can differ from consumer subscriptions; verify the actual classroom provider. Fictional identity/instrumental baseline avoids voice-cloning tasks.'))
S.append(question('short_answer', 'Which choice in generated music would you accept—and which would you challenge?',
    hint='Use an output you have heard, or a clearly labelled expectation. Explain why, for your listener.',
    eyebrow_text='REFLECTION MOMENT · MACHINE B',
    notes='Two minutes; second and last ClassPoint short answer. Invite rejection as well as acceptance. No fabricated listening evidence: before the live demo, an expectation must be labelled as such. Later students can revisit with actual output. Connect to the existing reflection’s argument and evidence, not an extra required written submission.'))

S.append(section('03 · AGENTS · A+B', 'Coordinate both machines.', 'THE AGENT IS NOT A THIRD MAGIC MUSIC MODEL', bg='#246E70'))
S.append(cards('AGENT HARNESS · SAME INTENT, DIFFERENT OPERATIONS', 'Brief → tools → saved material → revision.', [
    ('WRITE', 'B can propose A’s code.', 'The agent writes a Strudel pattern. The runtime executes explicit instructions.'),
    ('GENERATE', 'B proposes an audio asset.', 'The agent requests music, tracks the job and retains an actual saved result.'),
    ('ARRANGE', 'A makes choices executable.', 'Code or timeline operations place, trim and fade the selected assets. You listen and revise.'),
], text_size=27, notes='Connect Week 4 agents and Week 5 saved-image inputs. A learned language model can propose code executed by A. The agent coordinates tools within their actual constraints. A finished file is not evidence that the brief was satisfied. Reuse completed jobs; never resubmit merely because a request is pending.'))
S.append(two_col('A+B · ALLOCATE CONTROL', 'Compose the boundary between the two.', [
    'Use a written pattern for a recognizable motif.',
    'Use generated audio for material you select by listening.',
    'Arrange saved files; choose entries, cuts, levels and transitions.',
    'The hybrid is not automatically better. Test it against the same brief.',
], [
    'ILLUSTRATIVE ARRANGEMENT', '', '0–4 s    A motif', '4–12 s   selected B excerpt',
    '12–16 s  A return / ending', '', 'Trim tails. Set quiet levels.',
    'Do not assume stems or beat matching.',
], right_size=27, left_size=32,
    notes='The 16-second arrangement is an example within Challenge 5’s up-to-30-second limit. Reuse exported A and saved/imported B on explicit tracks. Tracks are not separated stems. Suno-as-Strudel-sample import is not verified. A’s tempo does not retime B or synchronize its beat. Current timeline export is WebM/Opus, not a guaranteed WAV/MP3 master; verify Thursday’s build. Source: 2025 Master PDF page 45, qualified as Gio’s course application.'))
S.append(statement('Break.\nTen minutes.', eyebrow_text='AFTER THE BREAK · DEMO → BRIEF → MAKING', bg=PAPER,
    notes='1:00–1:10. This is the end of the theory lecture. TAs check headphones, Easel launch and access; do not start a generation job for every student during the break.'))
S.append(title('SD2112 · WEEK 06 · EASEL WORKSHOP', 'One brief.\nThree approaches.',
    'A written loop. A generated candidate. A deliberate combination.', size=128,
    notes='Practical chapter starts after all theory. Instructor demo 1:10–1:20; setup and brief 1:20–1:35; making 1:35–2:15; flexible feedback 2:15–3:00.'))
S.append(content('INSTRUCTOR DEMO · EASEL', 'Watch the choices—not only the tools.', [
    'A: play a Strudel pattern. Change one note, then the sound. Save the loop.',
    'B: request music for the same intent. Listen and retain one completed result.',
    'A+B: arrange those saved assets; make one deliberate cut or transition.',
    'Replay. What improved—and what did the revision lose?',
], body_size=32, notes='Ten minutes after the break. Demonstrate the actual Thursday build. Prepare one A example and a permitted saved B backup. A paid Suno smoke test needs authorization. Show pending jobs honestly; use the backup rather than wait or duplicate a request. Stop one player before starting another. B may be longer than requested: trim a selected excerpt rather than claiming exact-duration generation.'))
S.append(content('SETUP · CLASSROOM RELEASE', 'Open Easel. Check that sound works.', [
    '[Download the classroom Easel release](https://github.com/venetanji/easel-client/releases). Use the version Gio identifies for this workshop.',
    '[Strudel getting started](https://strudel.cc/workshop/getting-started/) · [Suno](https://suno.com/) · class links on Canvas.',
    'Open the Strudel template. Press Play yourself; check Stop and quiet headphone output.',
    'Pair up if needed. If generation queues, use the supplied, labelled B asset.',
], body_size=30, notes='Target Thursday’s upcoming release; do not fix a version number before publication. Before class, verify PR #13, Suno support, class-material links, saving, import, export and reopening. Full strudel.cc is a separate online-editor fallback, not an embedded Easel REPL. PolyU GenAI is not a guaranteed music/API replacement. Name supplied B assets honestly. Never paste credentials into code, prompts or Canvas.'))
S.append(content('SHARED BRIEF · A SONIC IDENTITY', 'Make a sound for one identity and moment.', [
    'Use your previous mark/product—or invent an identity. No personal recording needed.',
    'Choose a listener and a moment: opening, arriving, completing, waiting.',
    'Name one recognizable musical feature and one thing the sound must not do.',
    'Make a short result, up to 30 seconds. Keep the same intent across A, B and A+B.',
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
S.append(cards('MAKING · 40 MINUTES · HEADPHONES ON', 'A → B → A+B → listen and save.', [
    ('10 MIN', 'Write a loop.', 'A pattern you can revise deliberately.'),
    ('10 MIN', 'Select music.', 'B proposes; your listening decides.'),
    ('15 MIN', 'Arrange both.', 'Reuse saved assets. Do not regenerate by default.'),
    ('5 MIN', 'Listen. Save.', 'One final playable result; no intermediate uploads.'),
], text_size=26, notes='Protect the 40 minutes: 10 + 10 + 15 + 5. Start at 1:35 and finish at 2:15. TAs help throughout; do not shrink making to squeeze in quiz practice or legal news.'))
S.append(activity('1 · MACHINE A', 10, 'Make a pattern you can explain.', [
    'Ask the agent for a small Strudel synth loop for your brief.',
    'Keep Play/Stop and the template’s controls.',
    'Change one note pattern, then one timbre or envelope choice. Listen after each change.',
    'Save the code and export a supported loop to Media.',
], panel=['ASK THE AGENT', 'Use the Strudel sound template.', 'Use native synths; no remote samples.',
          'Keep it simple and exportable.', 'Explain which line changes the notes.',
          'Do not start audio automatically.'], panel_size=24, bg=TEALS[4],
    notes='Ten minutes. Use native synths and supported export methods: note, s, gain, attack, release. Verify the release. PR #13 WAV export supports 1–16 four-beat cycles, at most 30 seconds including a 0.5-second tail. Adjust cycles and tempo. Simplify unsupported methods before export. LLM-written code is B proposing an A procedure; students listen and select. No intermediate upload.'))
S.append(activity('2 · MACHINE B', 10, 'Generate. Listen. Choose.', [
    'Ask the Easel agent to generate music for the same identity and moment.',
    'Specify mood, instrumentation and must-nots; an instrumental cue is a useful starting point.',
    'Listen to a completed candidate. Choose what serves the brief and name one surprise privately.',
    'Save the audio asset. If it queues, use the supplied B file and label it honestly.',
], panel=['ASK THE AGENT', 'Use the configured Suno integration.', 'Keep the same sonic intent.',
          'Save one completed candidate.', 'Keep the job receipt while pending.',
          'Never duplicate pending jobs.'], panel_size=24, bg=YELLOWS[1],
    notes='Ten minutes; target Thursday’s release. Do not guarantee an instrumental flag, exact duration, stems, extensions or reference input before API verification. Use one bounded request within the classroom quota, not three compulsory generations. While pending, finish A or use supplied B without claiming personal model generation. No intermediate upload.'))
S.append(activity('3 · MACHINE A+B', 15, 'Arrange the material you already made.', [
    'Give the agent your saved A loop and selected B asset.',
    'Build a short arrangement: A intro → B excerpt → A outro is one option.',
    'Choose entries, trims, levels and fades. Avoid competing players and sudden loudness.',
    'Revise one transition; listen again. Keep the version that serves the brief.',
], panel=['ASK THE AGENT', 'Reuse these saved assets.', 'Place and trim them on the timeline.',
          'Keep playback quiet.', 'Do not assume separated stems.', 'Do not regenerate B by default.'],
    panel_size=24, bg=TEALS[4],
    notes='Fifteen minutes. Arrange saved assets; do not assume Suno imports into a Strudel sampler. Treat B as a full mix unless actual stems are provided. No assumed automatic tempo matching or speed change. Trim A’s export tail where appropriate. Export may be WebM with sound; verify any audio-only route in Thursday’s release. The hybrid need not improve A or B: retain honest observations.'))
S.append(activity('4 · LISTEN AND SAVE', 5, 'Check the final result—not just the preview.', [
    'Stop other players. Replay the arrangement at a quiet level.',
    'Save/export using the classroom release’s tested route.',
    'Reopen the saved result and check that it plays with sound.',
    'Submit that one final result. Keep iterations for your own process record.',
], bg=YELLOWS[0], notes='Final five minutes of the protected making block. Slide 41 collection is not a second timed exercise. Accept the actual verified format, including WebM with sound, rather than promising an MP3/WAV master. A failed job is not a finished asset; an honest partial or labelled fallback is acceptable.'))
S.append(content('ONE FINAL SUBMISSION · CANVAS', 'Submit your final playable result.', [
    'One saved file, or a working share link, in the classroom Canvas activity.',
    'Submit the final arrangement—not three separate uploads or a comparison collage.',
    'Check that it plays with sound. If export is WebM with audio, submit that file.',
    'Keep your brief, code, prompt and iterations for your process record.',
], body_size=33,
    notes='Exactly one required final classroom capture after three approaches. No compulsory caption, essay or intermediate captures. The instructor creates and tests the classroom Canvas activity; no specific private URL is invented. Pinned deckgen v0.11.2 has no native ClassPoint audio-upload generator; cp=None is intentional. Keep student files and private activity URLs out of the public repo. Challenge 5 and reflection assessment remain unchanged.'))
S.append(content('DEBRIEF · WHICH CHOICES BECAME YOURS?', 'A result is not the whole creative process.', [
    'What did your written pattern make possible—or rule out?',
    'What did the music model propose that you did not request?',
    'What changed when you selected, trimmed and arranged the material?',
    'Did combining A and B help this listener? “Not this time” is a useful answer.',
], body_size=33, notes='Spoken/private questions, not extra ClassPoint buttons. Use flexible feedback time 2:15–3:00. Invite process discussion, not rankings of polish. A labelled failure or fallback can be evidence; it does not prove behavior of an untested model.'))
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
], body_size=30, notes='Existing reflection brief and 20% weighting, unchanged rubric and deadline. The two ClassPoint answers are optional starting points for arguments, not compulsory essay sections. For music, grid/timeline/spectrogram images can support listening evidence. TA draft checks in flexible feedback and before/after class. Week 7 quiz, pitches and team formation remain unchanged.'))
S.append(end('Rules. Patterns.\nYour listening.', 'Next week: quiz, pitches, teams—and your reflection.', 'SD2112 · WEEK 06 · '+SITE,
    notes='Close with the designer’s responsibility for intent, selection, arrangement and listening context. No automatic production publication.'))

attach_reports(S, Path(__file__).resolve().parent / 'week06-reports.json')
DECK = dict(title='SD2112 · AI in Design · Week 06', slides=finalize(S, FOOTER), pdf='SD2112-week06.pdf')

# Sources: 2025 Week6 PDF25–50 and MasterPDF45; PR #3 week06 source and figures.
# Additional primary/source links are on the corresponding slides and in notes.
