"""SD2112 Week 5: image generation as a designed, iterative process."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import build_all, PAPER, INK, VIOLET, ORANGE, TEALS  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, content, cards,
                             question, activity, two_col, figure_slide, finalize, T, Rect)  # noqa: E402
from deckgen.core import Image  # noqa: E402
from course import SITE, PLAYLIST, JOURNEY, footer  # noqa: E402
import week05_figures as F  # noqa: E402

FOOTER = footer(5)
S = []
ASSETS = Path(__file__).resolve().parent / 'assets'


def logo_exploration():
    """Use an actual group co-creation to test what an image model preserves."""
    slide = content('IMAGE GENERATION · A COURSE EXAMPLE',
                    'What changed when we remade our course mark?', [],
                    bg=PAPER, title_size=62,
                    notes='This is a real SD2112 group co-creation, not a finalized course logo. The clean a-plus-dot mark was the source; the forest/wall version is an exploratory AI-edited variant from the group. Compare the letterform, dot, colour, material and implied space. The model can propose material and setting, but it also changes a solid dot into a chalk ring: ask whether that breaks the brief or creates a better one. Be candid that this variant was selected and further edited by people, not generated in a single perfect prompt. Ask what should be fixed in the next iteration. Source images: SD2112 group logo exploration, September 2026, shared with the teaching team.')
    slide.els = slide.els[:2]
    slide.els += [
        Rect(220, 322, 630, 570, '#FFFFFF'),
        Image(250, 326, 570, 555, str(ASSETS / 'week05-logo-original.png'), 'contain'),
        Rect(1060, 322, 630, 570, INK),
        Image(1090, 326, 570, 555, str(ASSETS / 'week05-logo-forest-exploration.jpg'), 'contain'),
        T(220, 910, 650, 46, 'SOURCE MARK · THE SHAPE TO KEEP', 'monomed', 24, INK),
        T(1060, 910, 660, 46, 'EXPLORATION · MATERIAL + SETTING', 'monomed', 24, INK),
    ]
    return slide


def lantern_example():
    """Let the real output carry the slide; separate brief, observation and judgement."""
    slide = content('GENERATED EXAMPLE · EASEL / FLUX2-9B',
                    'The model gives you a candidate—not a decision.', [],
                    title_size=62, bg=PAPER,
                    notes='Course-generated still: Easel Flux2-9B, 28 September 2026. The on-slide intent is an illustrative summary, not the verbatim generation prompt. Ask students to point at observable choices: the dense foliage, lantern geometry and dramatic lighting. These were not all specified by the brief. The sample is one generated candidate, not evidence of a controlled A/B experiment or a perfect prompt. Flux is a flow-matching model family; the next slides teach classic latent diffusion as a conceptual foundation, not this exact model architecture.')
    slide.els = slide.els[:2]
    slide.els += [
        Image(1015, 318, 755, 620, str(ASSETS / 'week05-lantern-easel.jpg'), 'contain'),
        T(120, 340, 820, 45, 'INTENT', 'monomed', 25, VIOLET),
        T(120, 400, 780, 116, 'One paper lantern\nin a night garden.', 'xbold', 46, INK, lh=1.1),
        T(120, 560, 820, 45, 'OBSERVATION', 'monomed', 25, '#246E70'),
        T(120, 615, 800, 110, 'Dense leaves. Warm light.\nA very particular lantern shape.', 'body', 34, INK, lh=1.2),
        T(120, 770, 820, 45, 'DECISION', 'monomed', 25, VIOLET),
        T(120, 825, 800, 110, 'Which choices serve the intent?\nWhich would you change?', 'body', 34, INK, lh=1.2),
        T(1030, 950, 740, 35, 'COURSE-GENERATED STILL · 28 SEP 2026', 'mono', 20, '#5C6470'),
    ]
    return slide


def easel_demo():
    """Three concrete outputs, with generation and code authoring kept distinct."""
    slide = content('LIVE DEMO · EASEL CLIENT',
                    'One agent. Three kinds of making.', [], bg=PAPER, title_size=64,
                    notes='Gio will demo Easel Client (repository UI name: Easel Studio): https://github.com/venetanji/easel-client. Source capabilities checked 1 October 2026. Image generation/editing, generate_video, HTML project source edits and live captures are documented. Media support depends on the configured provider/model. HTML is code authored by the agent and rendered by the browser; it is not a diffusion image. Start one short video job without resubmitting while it is pending, then use the wait to build the HTML comparison. Accepted generation may continue after Stop. Test the installed app and configured models before class; repository support is not a guarantee of classroom access. Do not show credentials.')
    slide.els = slide.els[:2]
    rows = [
        (330, 'IMAGE', 'Make a candidate.', 'Call a media model; inspect the result.'),
        (515, 'VIDEO', 'Make change over time.', 'Call a video model; check motion and continuity.'),
        (700, 'HTML', 'Make something you can use.', 'The agent writes code; the browser renders it.'),
    ]
    for y, label, heading, detail in rows:
        slide.els += [
            Rect(120, y + 150, 1680, 2, '#D5DCDA'),
            T(120, y + 16, 240, 70, label, 'xbold', 49, '#246E70'),
            T(425, y + 4, 1300, 70, heading, 'xbold', 44, INK),
            T(425, y + 82, 1300, 65, detail, 'body', 32, INK),
        ]
    slide.els.append(T(120, 914, 1680, 60, 'Easel Client connects the tools. You set the brief and judge what returns.',
                       'body', 32, INK))
    return slide


def video_discussion():
    slide = content('CASE DISCUSSION · OUR CHAT + VIDEO ITERATIONS',
                    'What stayed wrong after a better prompt?', [], bg=INK, title_size=64,
                    notes='Gio will show the actual chat and multiple iterations from the SD2112 logo-video experiment in the other session. Switch to that chat and play selected real versions side by side or in sequence. This slide is a discussion guide, not an embedded recording or a claim that the final sequence succeeded. The documented intended sequence was nature/leaves, origami paper, electronic circuits/optic fibres, then the upper-right dot reveal. Earlier versions had unwanted jumps and unstable letterforms; exact duration, sound and final-frame constraints changed with the brief. Ask which revision changed the prompt, which changed the reference or pipeline, and what the resulting video actually shows. If a clip is unavailable, discuss the saved chat without fabricating a result. Keep media generations out of this preparation pass: no new video render is requested.')
    slide.els = slide.els[:2]
    for y, label, heading, detail in [
        (340, 'BRIEF', 'What must survive?', 'The mark, the ordered transformations, the final reveal.'),
        (525, 'EVIDENCE', 'What actually changed?', 'Motion, continuity, shape—and the constraints we lost.'),
        (710, 'NEXT MOVE', 'Prompt, reference, or workflow?', 'Choose the intervention that addresses the visible failure.'),
    ]:
        slide.els += [
            T(120, y + 15, 275, 60, label, 'monomed', 28, TEALS[4]),
            T(425, y, 1300, 75, heading, 'xbold', 47, '#FFFFFF'),
            T(425, y + 86, 1300, 65, detail, 'body', 31, '#D3E7E8'),
        ]
    slide.els.append(T(120, 927, 1680, 55, 'Watch the versions. Do not confuse a confident explanation with a better result.',
                       'body', 30, '#FFFFFF'))
    return slide


def modern_models():
    slide = content('TODAY’S MODELS · SAME MAP, DIFFERENT TRAINING',
                    'The diagram is a map—not every model’s blueprint.', [],
                    title_size=62, bg=PAPER,
                    notes='Noise prediction describes a classic DDPM-style objective, not all diffusion objectives. Flow matching learns a vector field or velocity along a path between noise and data; it is not simply predicting the noise just added. Flux and Qwen Image are transformer-based flow-matching families, not the exact CLIP/U-Net pipeline in the historical 2025 slide. Check the demonstrated model/version in Easel: app name, agent model and media model are different things. Sources: https://github.com/black-forest-labs/flux (Flux Kontext flow-matching paper reference); https://github.com/QwenLM/Qwen-Image; https://github.com/huggingface/diffusers/blob/main/src/diffusers/pipelines/qwenimage/pipeline_qwenimage.py (FlowMatchEulerDiscreteScheduler).')
    slide.els = slide.els[:2]
    for x, label, heading, body in [
        (120, 'CLASSIC DIFFUSION', 'Predict the noise.', 'Learn from known added noise\nat different noise levels.'),
        (1000, 'FLOW MATCHING', 'Learn a direction.', 'Learn a direction along a path\nfrom noise towards data.'),
    ]:
        slide.els += [
            T(x, 350, 780, 50, label, 'monomed', 27, '#246E70'),
            T(x, 432, 780, 92, heading, 'xbold', 52, INK),
            T(x, 555, 780, 145, body, 'body', 36, INK, lh=1.25),
        ]
    slide.els += [
        Rect(120, 750, 1680, 3, '#D5DCDA'),
        T(120, 794, 1680, 76, 'Text condition → latent updates → decoding', 'xbold', 43, INK),
        T(120, 903, 1680, 65, 'Flux and Qwen Image use flow matching. Check the model—not just the app name.',
          'body', 30, INK),
    ]
    return slide

S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 05 · LECTURE + WORKSHOP',
               'Images, intentions, iterations.',
               'You bring the idea. The model brings possibilities.',
               notes='Open with the students’ own image ideas. The lecture makes the visual-model sequence legible: image-only GANs, CLIP’s shared image/text representation, diffusion, then an agent that can use image-understanding and image-generation tools. The workshop applies that sequence to student-owned intent. Confirm the actual authorized image service before class; do not imply a direct API is available if it is not.'))

S.append(agenda('SD2112 · WEEK 05', [
    'Start with an image you want to make',
    'GANs generate; CLIP aligns; diffusion and flow models generate',
    'Easel Client: images, video and HTML through an agent',
    'Clarify the intent; do not outsource it',
    'Generate, critique, and change one thing at a time',
    'Bring a deliberate iteration to Week 6',
], notes='Give the image-model sequence a clear visual explanation before moving into the agent-supported making exercise. Protect the extended time for making, looking, discussing and iterating.'))

S.append(question('short_answer', 'What image have you wanted to make but not yet managed to make?',
                  hint='Name the subject and one visual quality you care about.',
                  eyebrow_text='00 · START WITH YOUR IDEA',
                  notes='Give students a minute to write privately, then take a few examples. Invite specific personal visual intentions, not personal data or sensitive images. They may work from an imagined image; no upload is required.'))

S.append(cards('00 · THE DESIGNER’S JOB', 'The model does not supply your reason for making the image.', [
    ('INTENT', 'What should the image do?', 'Name the subject, audience, feeling, use and visual choices that matter to you.'),
    ('PROMPT', 'Make the intent legible.', 'An agent can ask questions, expose ambiguity and help you write a clearer specification.'),
    ('JUDGEMENT', 'Decide what happens next.', 'You select, critique, revise or reject the result. The model does not own that decision.'),
], text_size=23,
notes='Position the language agent as a prompt clarifier, not an autonomous creative director. Students remain the source of the idea and the judge of the output.'))

S.append(section('IMAGE MODELS · A SHORT LINEAGE',
                 'How did words begin to guide image generation?',
                 'GANs synthesize · CLIP aligns · diffusion / flow models generate', bg=VIOLET,
                 notes='Frame this as a change in how visual models can be conditioned, not as a claim that one architecture simply replaced another. Keep the technical account at the level needed to understand the image-generation tools students will meet.'))

S.append(content('GANs · 2014 · GENERATIVE ADVERSARIAL NETWORKS',
                 'GANs learn a visual distribution—not a description.', [
                     'A generator turns random input into candidate images.',
                     'A discriminator learns to distinguish generated images from examples.',
                     'Classic image GANs: no text prompt telling the model what to draw.',
                 ], image='edmond-de-belamy.jpg', fit='contain', body_size=28,
                 caption='Obvious, Portrait of Edmond de Belamy (2018), made with a GAN; the historical example shown in the 2025 Week 5 deck.',
                 notes='Use the portrait as a concrete artifact, not as evidence that all GANs are unconditional: conditional GAN variants exist. The teaching contrast is with the text-conditioned image-generation interfaces students use today. The original 2025 Week 5 deck shows generated sample grids and a generator/discriminator schematic on pp. 45–46, then this portrait on p. 47.'))

S.append(figure_slide('GANs · TWO MODELS IN COMPETITION',
                      'One learns to make. The other learns to catch.', F.gan_adversaries(),
                      caption='A simplified training picture. Classic image GANs learn from image examples; text is not the instruction channel here.',
                      notes='Walk left to right: training examples and random latent input; the generator makes a candidate; the discriminator compares it with real examples; their competition improves both. This is a teaching schematic, not a literal network diagram for every GAN variant. The original 2025 slide used a generator/discriminator flow beside grids of generated digits, faces and animals.'))

S.append(figure_slide('CLIP · CONTRASTIVE LANGUAGE–IMAGE PRETRAINING',
                      'CLIP brings words and images into a shared space.', F.clip_shared_space(),
                      caption='Matching pairs move closer; mismatched pairs move apart. CLIP does not generate an image.',
                      notes='Explain the two encoders and paired examples: matching captions and pictures are trained to have similar representations, while non-matching pairs are pushed apart. Treat the 2D points as a conceptual projection, not CLIP’s literal high-dimensional space. This updates the 2025 deck’s helpful caption/image pairing and similarity-matrix visuals on pp. 48–50.'))

S.append(figure_slide('TEXT-TO-IMAGE · A GENERATIVE SYSTEM',
                      'A prompt guides an iterative image-generation pipeline.', F.text_conditioning(),
                      caption='Text is a condition, noise is the starting state, and the decoder returns pixels. Classic latent-diffusion schematic.',
                      notes='Walk from prompt to text encoder to contextual text features. Separately sample initial latent noise; the denoising model updates that latent over many steps, using the text features as a condition, and the VAE decoder returns pixels. This is a high-level latent-diffusion workflow, not a literal network graph: exact text encoders, denoisers, step counts and VAE configurations vary by model. The 2025 Week 5 PDF page 54 shows a comparable text encoder, random-noise input, iterative diffusion model and VAE decoder; its CLIP label is model-specific, not universal.'))

S.append(lantern_example())

S.append(figure_slide('LATENT DIFFUSION · VARIATIONAL AUTOENCODER',
                      'A VAE moves between pixels and a compact latent.', F.vae_latent(),
                      caption='This image-to-image reconstruction illustrates VAE training; generation begins from latent noise.',
                      notes='Follow the hourglass: image x enters the encoder, which predicts a distribution over z (shown with its mean and log-variance); sample z, then the expanding decoder predicts reconstruction x-hat. This is the standard VAE shape shown in the 2025 Week 5 PDF page 53. Do not imply that text-to-image sampling needs a source image: in latent diffusion, noise is denoised in latent space and the VAE decoder maps the final latent to pixels.'))

S.append(figure_slide('CLASSIC LATENT DIFFUSION · TRAINING',
                      'Training teaches a denoiser to remove noise.', F.diffusion_training(),
                      caption='Compare predicted noise with known added noise; use that error to update the denoiser, not the latent.',
                      notes='Read the top preparation row, then the learning row. Encode an example image with a VAE; combine its latent with known sampled noise at a chosen noise level t. Feed the noisy latent and noise level to the denoiser, compare its noise prediction with the saved target, and update denoiser weights using the error. Repeat on many examples and noise levels. Text conditioning and scheduler details are omitted for clarity. zt means a sampled training noise level, not always the fully noised endpoint zT. The VAE is usually trained separately; this flow does not jointly train every module. This is the classic noise-prediction objective, not a universal account of Flux or Qwen Image. The 2025 deck illustrates forward noising on PDF p. 51 and the VAE on p. 53.'))

S.append(figure_slide('CLASSIC LATENT DIFFUSION · GENERATION',
                      'Generation turns new noise into an image.', F.diffusion_generation(),
                      caption='The loop changes the latent, not the trained weights. Decode the final latent after the last update.',
                      notes='Follow this flow left to right, contrasting it with the preceding training slide. The denoiser starts from new latent noise; text features can guide each update through many steps. A VAE decoder maps the final clean latent to a viewable image. The lantern is a different illustrative output from the chair used as the preceding training example; do not suggest the model copied that chair. Colored tiles symbolize latent data, not saved image frames. The 2025 deck illustrates reverse denoising on p. 51 and a text-conditioned latent-diffusion workflow on p. 54.'))

S.append(modern_models())

S.append(question('short_answer', "If CLIP can match the words 'a chair' to a picture, why can't CLIP draw that chair?",
                  hint='What can your tool show or control? What would require evidence?',
                  eyebrow_text='IMAGE MODELS · DEEP QUESTION',
                  notes='Allow three minutes. A strong answer separates CLIP-like alignment from generation: the text encoder produces a condition; iterative denoising builds a latent; the VAE decoder maps the final latent to pixels. CLIP itself is not the drawing system. In some pipelines the conditioning encoder is not CLIP-derived. Probe what a student can actually inspect or control in the approved image tool, and what would need vendor documentation or another source as evidence; do not assume the controls exist. Then bridge to tools an agent might call.'))

S.append(figure_slide('AGENTS · IMAGE UNDERSTANDING + GENERATION AS TOOLS',
                      'The agent can look, make, and look again.', F.agent_image_tools(),
                      caption='The student supplies the intent and decides whether the result is worth keeping.',
                      notes='Bridge from model capability to interaction. An agent can inspect an image with a vision tool, draft or revise a prompt, call an image-generation/editing tool, and inspect the result. The agent coordinates tools; it does not own the design intention or decide what counts as success. Easel Client is the lecturer demo. Student tool access and the installed app configuration still require a pre-class check.'))

S.append(logo_exploration())

S.append(easel_demo())

S.append(video_discussion())

S.append(section('DEMO · WATCH THE HANDOFFS',
                 'What can the agent change?',
                 'Images. Video. HTML. What must you still decide?', bg=INK,
                   notes='Live demo prompt suggestion, not a recorded result: make a lantern image, request one short video from an available supported route, then ask the agent to build an HTML comparison with the returned assets. Do not imply the selected video model supports image conditioning until checked. While a video job waits, inspect the image or work on the HTML; do not resubmit accepted jobs. Show one critique and one revision, the tool/model names and the saved chat. Ask the audience to identify a model choice, an agent/tool choice and a human decision. HTML interaction and sampled video frames do not establish smooth playback or sound: play and test the actual output.'))

S.append(section('01', 'A picture is not a prompt',
                 'intent first · words second · output third', bg=VIOLET,
                 notes='Use an example volunteered by the class. Do not replace it with a generic prompt exercise.'))

S.append(content('01 · MAKE THE VISUAL INTENT CONCRETE',
                 'What must the image communicate?', [
                     'Subject and action: what is happening, and to whom?',
                     'Point of view and composition: where is the viewer, and what is in frame?',
                     'Light, colour, material and atmosphere: what should it feel like?',
                     'Use and constraints: where will it appear, what must remain legible, and what should be absent?',
                 ], body_size=29,
                 notes='Do not prescribe one aesthetic. Ask students which of these dimensions matter for their own image and which they want to leave open. They can name intentional uncertainty too.'))

S.append(activity('02 · PAIRS · CLARIFY THE IDEA · 12 MIN', 12,
                  'Ask an agent to help sharpen your prompt.', [
                      'Describe your own image idea in plain language; say what matters most to you.',
                      'Ask the agent to ask up to five clarifying questions before it rewrites anything.',
                      'Answer, skip or reject its assumptions. Keep your original idea visible.',
                      'Ask for one concise prompt and a short list of unresolved choices.',
                  ], panel=[
                      'PROMPT-CLARIFIER STARTER',
                      'Do not invent my image idea.',
                      'Ask questions first.',
                      'Preserve my intent and words.',
                      'Flag assumptions; offer options.',
                      'Wait for my approval before rewriting.',
                  ], panel_size=20, bg=PAPER,
                  notes='Twelve minutes. One person owns the image idea; their partner helps inspect the revised prompt. The language agent may clarify, but the student chooses which suggestions to keep. If no language-model access is available, partners interview each other using the same questions.'))

S.append(content('02 · PROMPT AS A WORKING SPECIFICATION',
                 'Keep the choices that matter; leave room where you want surprise.', [
                     'Intent: subject, purpose and intended viewer.',
                     'Visual controls: composition, viewpoint, light, palette, material or style—only where useful.',
                     'Constraints: aspect ratio, text or no text, exclusions and practical limits.',
                     'Open choices: name what the model may interpret, rather than pretending to control everything.',
                 ], body_size=27,
                 notes='This is not a magic-word recipe. More detail is not automatically better: specify what matters to this image, and deliberately leave some dimensions open.'))

S.append(section('03', 'Call the image model',
                 'one prompt · one first result · record what you actually used', bg=INK,
                 notes='Gio demos Easel Client for agent-directed image, video and HTML making. Student use is a separate access decision: confirm the authorized student-facing image service, accounts, quotas and inputs. The syllabus names PolyU GenAI with Flux and Qwen, but does not establish student API credentials or Easel access. Use the approved platform UI or fallback where necessary; do not ask students to expose credentials.'))

S.append(two_col('03 · A FIRST GENERATION', 'Make a first image, not a final answer.',
                 [
                     'Demo: Easel Client. Your task: the course-approved image service.',
                     'Submit the prompt you approved with the agent.',
                     'Record the model, tool, settings and date if shown.',
                     'Save the output and prompt together.',
                 ], [
                     'Do not paste API keys into a chat or shared prompt.',
                     'Use only images you may upload; an image reference is optional.',
                     'If the service is unavailable, work from the prompt and critique a sample provided by the teaching team.',
                     'One image is enough to begin critique.',
                 ], left_size=28, right_size=24,
                 notes='Live tool details remain subject to a pre-class API/access check. No API keys or personal identifiers should appear in submitted screenshots. Provide a no-login fallback if access or quotas fail.'))

S.append(question('short_answer', 'What did the model decide that you did not specify?',
                  hint='Point to one visible choice: framing, detail, colour, text, material, or something else.',
                  eyebrow_text='04 · LOOK BEFORE YOU PROMPT AGAIN',
                  notes='Ask students to identify an observable choice, not just say good/bad. Separate what the prompt specified, what the output shows and what the viewer infers.'))

S.append(cards('04 · CRITIQUE THE RESULT', 'Use evidence from the image and your intent.', [
    ('INTENT', 'What did you want it to do?', 'Which part of the brief mattered most?'),
    ('OUTPUT', 'What is actually visible?', 'Where did the result meet, miss or reinterpret the intent?'),
    ('DECISION', 'What was left to the model?', 'Name one useful surprise and one assumption or failure to address.'),
], text_size=23,
notes='The model’s unasked-for choices are not automatically errors. Students decide whether to keep, alter or reject them in light of their purpose.'))

S.append(activity('05 · SOLO → PAIRS · ITERATE DELIBERATELY · 35 MIN', 35,
                  'Change one thing. Compare. Decide.', [
                      'Choose one critique point and write the change you intend to test.',
                      'Revise one prompt dimension; keep the rest stable where possible.',
                      'Generate a new image. Compare it with the previous version against your stated intent.',
                      'Repeat once if time allows. Keep both outputs, prompts and the reason for each change.',
                  ], panel=[
                      'ITERATION LOG',
                      'Version / model / settings',
                      'What I changed — one thing',
                      'What I expected to change',
                      'What actually changed',
                      'Keep · revise · reject? Why?',
                  ], panel_size=20, bg=TEALS[4],
                  notes='Thirty-five minutes includes generation waits and comparison. Students may change composition, palette, subject detail or another dimension, but should make one deliberate change per round so they can interpret the result. A seed or reference may help hold other variables steady only if the chosen API exposes it; do not promise controls the service lacks. In pairs, each student remains author of their own idea.'))

S.append(content('05 · COMPARE, DO NOT JUST POLL FOR A FAVOURITE',
                 'Which version better serves the intent—and why?', [
                     'Compare the images side by side against the original brief.',
                     'Name what changed and what stayed stubbornly the same.',
                     'Did the agent’s rewrite help, flatten, or redirect your idea?',
                     'Choose: keep, revise again or reject. Explain the choice in your own terms.',
                 ], body_size=28,
                 notes='Invite two examples with contrasting decisions. Do not frame iteration count or polish as success; an informed rejection is a valid design outcome.'))

S.append(question('short_answer', 'What did you keep, change or reject—and what evidence led you there?',
                  hint='Name one prompt choice and one visible effect in the image.',
                  eyebrow_text='06 · SHARE THE DESIGN DECISION',
                  notes='Use responses to make authorship explicit: image generation is part of the process, and deciding what counts as success remains design work.'))

S.append(cards('06 · CHALLENGE 4 · BRING TO WEEK 6',
               'A deliberate image iteration, with its evidence.', [
    ('YOUR IDEA', 'Start with your intent.', 'Keep your initial image idea and the prompt you approved.'),
    ('YOUR PROCESS', 'Show the changes.', 'Name the model/tool and retain two or more versions with the prompts or settings you used.'),
    ('YOUR CRITIQUE', 'Explain one decision.', 'Identify something the model decided, then say whether you kept, changed or rejected it and why.'),
], text_size=22,
notes='The syllabus calls Challenge 4 “a layout you could not design, generated, iterated and critiqued.” Keep that challenge framing while making clear the student owns the image idea and the iteration decisions. Submit via the course platform specified by the teaching team; do not invent a due date beyond Week 6.'))

S.append(two_col('06 · KEEP A PROCESS RECORD', 'A useful record makes your choices visible.',
                 [
                     'Your original idea and intended audience or use.',
                     'The first prompt and the agent’s proposed rewrite; mark what you accepted or refused.',
                     'The first output and the model/service details available to you.',
                 ], [
                     'Each iteration prompt and image in order.',
                     'One critique tied to visible evidence.',
                     'A short process note: what you decided, and why.',
                 ], left_size=25, right_size=25,
                 notes='This process record can contribute evidence to the Week 7 reflection. Follow the course platform’s normal submission and privacy rules; do not include API keys, account tokens or personal information.'))

S.append(end('The model made an image.',
             'You decided what the image was for—and what to do next.',
             f'{SITE} · {PLAYLIST.replace("https://", "")}',
             notes='Close with the course question: the image model produces possibilities from learned patterns, but the designer defines the intention, judges the result and takes responsibility for the iteration.'))

DECK = dict(title='SD2112 · AI in Design · Week 05', slides=finalize(S, FOOTER), pdf='SD2112-week05.pdf')

if __name__ == '__main__':
    only_html = '--html' in sys.argv
    out = build_all(DECK, 'week05', FOOTER, do_pptx=not only_html, do_html=True,
                    do_png=not only_html, do_pdf=not only_html)
    for key, value in out.items():
        if key == 'warnings':
            print('\n'.join(value) if value else 'no text overflow warnings')
        elif key == 'png':
            print(f'png: {len(value)} previews')
        else:
            print(f'{key}: {value}')
