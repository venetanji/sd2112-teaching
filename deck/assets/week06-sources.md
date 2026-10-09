# Week 6 figure sources

## Adapted course source

- Original course-refresh PR 3: `tools/figures_week06.py` on
  `claude/sd2112-course-refresh-hwww8e`, retrieved with the authenticated GitHub
  contents API at commit `83733ca09969da3439c251260a45549a16f12e71`.
  Source: https://github.com/venetanji/sd2112-teaching/blob/83733ca09969da3439c251260a45549a16f12e71/tools/figures_week06.py
- The course-owned adaptation is `deck/week06_figures.py`; the Canvas import is
  now `deckgen.figures`, not the old local `figures` module.
- Retained/adapted computed examples: additive harmonic waveform, analytic
  rising/falling harmonic magnitude image, MIDI note list, six-row step grid,
  seeded illustrative accepted/rejected melody and shared-bike sound brief.
  These are teaching illustrations, not recordings, actual model states or
  historical Illiac Suite scores. The spectrogram illustration is analytic,
  not an STFT computed from the adjacent stationary waveform; the three panels
  explain the representation, not one measured signal's numerical conversion.
- The lecture sequencer still is a separate course-owned four-voice/eight-step
  score matching its live seed, sine pitches and 100 BPM eighth-note timing.
  The Strudel still depicts the actual four-note sine pattern, not PR 3's
  unrelated six-row/16-step drum score, which remains available as provenance.

## Scientific and historical boundaries

- Waveform amplitude and spectral magnitude are signal quantities, not direct
  measurements of perceptual loudness. The two signed waveform directions are
  not "louder" and "quieter". The computed tone's fundamental is 220 Hz; pitch
  perception is not asserted to be universally identical to the first peak.
- A MIDI piano roll is a view of timed events. Note-on/note-off timing gives
  duration; velocity is a parameter whose sonic effect depends on the chosen
  instrument. MIDI is not sampled sound.
  MIDI Association overview: https://midi.org/about-midi-part-1-overview
- Historic Riffusion v1, not subsequent Riffusion products: Stable Diffusion
  generated spectrogram images; the documented conversion used magnitude
  spectrograms and Griffin-Lim phase reconstruction. An isolated inverse
  Fourier transform does not reconstruct phase omitted by a magnitude image.
  Original repository: https://github.com/riffusion/riffusion
  Conversion implementation: https://github.com/riffusion/riffusion/blob/main/riffusion/spectrogram_converter.py
- MusicGen is a documented example of learned prediction over EnCodec audio
  tokens, followed by codec decoding. Its architecture is not a claim about
  proprietary Suno internals or all audio models.
  Paper: https://arxiv.org/abs/2306.05284
  Implementation: https://github.com/facebookresearch/audiocraft/blob/main/docs/MUSICGEN.md
- Generate-and-test is inspired by Hiller and Isaacson's *Illiac Suite* (1957),
  described in *Experimental Music* (1959). The simplified range/leap checks
  and displayed melody are illustrative, not a reconstruction of a specific
  experiment. The three-state transition table is handwritten for this course;
  it is Machine A, not evidence of learning. Neither MusicGen nor GPT is
  presented as a first-order Markov lookup table.

## October 2026 interactive revision

- `deck/week06_analysis.js` is a course-owned p5/native Web Audio instrument,
  not a microphone stream or an equalizer. A quiet oscillator feeds the audible
  output and a 2048-point `AnalyserNode` FFT (Blackman window, no smoothing).
  Display: waveform, log-frequency spectrum, and perspective waterfall of
  roughly 60 ms analysis observations; relative dBFS is not perceived loudness.
  The static twin is a labelled analytic illustration of the default 220 Hz
  sine, not a recorded measurement or the initial silent browser state.
  API: https://webaudio.github.io/web-audio-api/#AnalyserNode
- Four native-synth Strudel roles share `setcpm(100/4)`: rhythm uses short C2
  attacks/rests, bass C2 C2 G2 C2, harmony simultaneous C3 E3 G3, and melody
  C4 E4 G4 B4. Each online editor link includes that part and earlier parts;
  the complete starter stacks all four. These are modern teaching examples,
  not the historical Illiac Suite. The still beside the combined code depicts
  its melody part, not all voices. Online REPL code is not the Easel wrapper.
  The public editor requires double quotes for parsed mini-notation; single
  quotes leave multi-note text literal. Compiler/query checks on 9 October
  confirmed 2 rhythm attacks, 4 bass notes, 3 simultaneous harmony notes and
  4 melody notes in one cycle. Seed links use percent-encoded UTF-8 Base64
  fragments, matching the official Share format.
- Historical Riffusion UI screenshot, unmodified, from creator repository:
  https://github.com/riffusion/riffusion-app-hobby/blob/f961d034997adcf830c9f206fe8997ed4c0b1247/public/about/web_app_screenshot.png
  Commit dated 29 November 2022; Hayk Martiros and Seth Forsgren. MIT notice
  retained in `week06/RIFFUSION-LICENSE.txt`; repository licence retrieved from
  https://github.com/riffusion/riffusion-app-hobby/blob/main/LICENSE .
- Suno public logged-out landing-page screenshot, checked 9 October 2026:
  https://suno.com/ . Used for attributed classroom product identification,
  not evidence of an Easel interface, audio upload success or generated music.
  Suno retains its trademarks and website rights; this is not MIT-licensed.
- Suno consumer rights checked 9 October 2026 against controlling terms:
  https://suno.com/terms-of-service (revised 10 August; effective 3 September
  2026). Original submissions retain their ownership, with a broad provider
  licence; Basic output is personal/non-commercial, paid output rights remain
  subject to the terms including permitted downloads. No guaranteed statutory
  copyright or uniqueness; consumer plans do not establish Easel/API rights.
  No automatic retroactive free-song upgrade:
  https://help.suno.com/en/articles/2425729
  Own rough-demo/audio uploads and reference influence:
  https://help.suno.com/en/articles/6141569
  https://help.suno.com/en/articles/6141377
  These consumer interfaces/limits do not prove Easel support. Gio owns the
  local integration and classroom save/upload/generate/reopen smoke test.
- Hong Kong copyright uncertainty, not a US-law shortcut: official IPD
  consultation, 8 July 2024, PDF pages 10 and 16–17, discusses arrangements
  necessary for computer-generated works and fact-specific originality/authorship:
  https://www.ipd.gov.hk/filemanager/ipd/en/share/consultation-papers/Eng-Copyright-and-AI-Consultation-Paper-20240708.pdf
  This dated consultation is not a legal opinion or proof of every later change.
