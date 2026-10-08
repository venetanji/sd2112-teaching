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
