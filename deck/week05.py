"""SD2112 Week 5: one identity, made with rules, learned images and both."""
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
    """A short opening showcase; installation and student making happen after the break."""
    slide = content('OPENING SHOWCASE · EASEL CLIENT · 5 MIN',
                    'One mark. Three routes.', [], bg=PAPER, title_size=64,
                    notes='Five-minute opening showcase, before the lecture: show one prepared identity as coded HTML/SVG/Canvas graphics, a generated image and a combination. These are routes to compare, not a claim that a hybrid is best. Easel Client UI name is Easel Studio: https://github.com/venetanji/easel-client. The agent writes code; the browser executes it. Media models generate pixels through separate tools. Explain the Machine A/B distinction during the lecture, not a long feature tour here. Show already saved outputs; do not let an asynchronous image/video job delay the opening. Video generation remains a documented capability and the real logo-video iterations are discussed later. Installation and provider checks happen after the break; do not display credentials.')
    slide.els = slide.els[:2]
    rows = [
        (330, 'A', 'Code the form.', 'HTML / SVG / Canvas: shapes and parameters.'),
        (515, 'B', 'Generate an interpretation.', 'An image model proposes appearance and material.'),
        (700, 'A+B', 'Combine the two.', 'Generated pixels inside a coded shape or surface.'),
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
                       notes='Open with a five-minute Easel showcase, then roughly 55 minutes of lecture. Keep the image-model theory and real logo/video discussion. After the break, walk through installation and one shared personal-mark brief. The 40-minute activity clock starts only once setup and the brief are complete. Students make A, B and A+B studies of the same identity; do not imply student credentials or endpoint access are already established.'))

S.append(easel_demo())

S.append(agenda('SD2112 · WEEK 05', [
    'One personal identity: code, generate, combine',
    'GANs generate; CLIP aligns; diffusion and flow models generate',
    'Agents, tools and our logo/video iterations',
    'After the break: install Easel and set the brief',
    '40 minutes: Machine A, Machine B, Machine A+B',
    'Compare the routes; keep evidence for Week 6',
], notes='The opening showcase plus lecture takes roughly an hour. Break, installation and the brief come before the 40-minute making block. Protect 10 + 10 + 15 + 5 minutes; do not add a separate prompt-writing or 35-minute iteration exercise.'))

S.append(question('short_answer', 'What could stand for you without being a portrait?',
                  hint='A name, nickname, character or symbol—and one quality it should communicate.',
                  eyebrow_text='00 · START WITH YOUR IDENTITY',
                  notes='Take a few short responses within the lecture, not a separate making exercise. Students can use a fictional identity or non-identifying nickname. No photograph or personal details are required. The final brief is written after the break.'))

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

S.append(video_discussion())

S.append(cards('FROM WEEK 2 + WEEK 4 · NAME THE MACHINES',
               'Same intent. Different kinds of control.', [
    ('MACHINE A', 'Rules execute.', 'Code sets the shapes, layout and parameters. Change a rule; inspect its effect.'),
    ('MACHINE B', 'Learned patterns propose.', 'An image model interprets the brief. You judge its appearance and assumptions.'),
    ('A + B', 'Divide the decisions.', 'Keep geometry in code; use generated pixels for material, texture or atmosphere.'),
], text_size=24,
notes='Machine B writes the code; Machine A executes it. This is the Week 2 distinction, not a claim that the coding agent is a symbolic model. All three routes may use a learned agent; the distinction concerns how the visual artifact is produced. A programmed sketch can include controlled randomness, so do not equate Machine A with no variation. Rendering a generated texture on a surface is not a generated 3D model.'))

S.append(section('BREAK', 'After the break: make it yours.',
                 'Install Easel → set one brief → make A, B and A+B', bg=INK,
                 notes='Break after about one hour including the opening showcase. On return, walk through installation and the shared brief before starting the activity clock. The lecturer may use remaining scheduled class time for setup or individual help; do not inflate the 40-minute activity to fill the three-hour booking.'))

S.append(content('AFTER THE BREAK · EASEL SETUP', 'Install. Open. Check.', [
    'Download the package for your OS from github.com/venetanji/easel-client/releases.',
    'Open Easel Studio. Create one project for your personal mark.',
    'Use the course-approved configuration; test a canvas and one image call.',
    'If setup fails, pair on a working device. Keep your own brief and decisions.',
], body_size=29,
notes='Installation and access checks are outside the 40-minute activity. Current verified release: https://github.com/venetanji/easel-client/releases/tag/v0.0.1. Packaged Windows x64 EXE/ZIP, macOS ARM64 DMG/ZIP and Linux x86_64 AppImage/DEB are listed; no Intel Mac installer was listed on 1 October. Check current releases, actual classroom OS/architecture and permitted installation before class. Release installers do not require the Node.js development workflow. Do not bypass OS or institutional security controls. Student accounts, endpoints and quotas must be course-approved; do not ask for keys in a chat or screenshot. Test HTML/SVG/Canvas, image generation and saved-image reuse. For optional Three.js, verify the bundled offline kit under Settings > Kits and in project settings; no CDN or external URL imports. If no device works, use a TA-prepared browser example and supplied texture; label supplied assets as fallback rather than student-generated evidence.'))

S.append(content('THE SHARED BRIEF · BEFORE THE TIMER',
                 'Make a mark that represents you.', [
    'Choose a name, nickname, invented character or personal symbol.',
    'Write one sentence: what should this identity communicate?',
    'Choose two things that must remain recognizable across all three routes.',
    'Keep the same brief. A fictional identity is fine; no portrait is required.',
], body_size=32,
notes='Briefing precedes the making timer. Ask for two observable invariants, for example a crescent silhouette and a detached dot, not a demand that every pixel match. Use this same brief in A, B and A+B. No real name, photograph or personal data is required. This is a rapid identity study, not a commercial trademark or a finished branding project.'))

S.append(activity('WORKSHOP · ONE BRIEF · THREE QUICK STUDIES', 40,
                  'One identity. Three ways of making it.', [
    'A · 10 min: code a mark; change one parameter.',
    'B · 10 min: generate an interpretation; inspect one model choice.',
    'A+B · 15 min: combine generated pixels with the coded form.',
    'Compare · 5 min: show all three and explain the trade-off.',
], panel=[
    'SAME IDENTITY',
    'One sentence of intent.',
    'Two recognizable features.',
    '',
    'THREE ROUTES',
    'A: rules',
    'B: learned images',
    'A+B: rules + generated pixels',
    '',
    'Quick studies, not finished logos.',
], panel_size=25, bg=PAPER,
notes='This overview announces the entire block, not an additional 40-minute exercise. Start the 40-minute clock only after installation, tool checks and the brief. The following steps divide it: 10 + 10 + 15 + 5 = 40. Students may share a device but retain individual authorship. Build one modest artifact per route. Iteration happens within the steps, not a separate prompt-writing or repeated-generation block. If a media job is slow, submit it once, work on the code while it waits, and label any supplied fallback texture.'))

S.append(activity('A · MACHINE A · RULES MAKE THE PICTURE', 10,
                  'Code the mark.', [
    'Ask the agent for a simple SVG or Canvas mark from your shared brief.',
    'Expose two parameters: spacing, stroke width, scale or colour.',
    'Change one value. Check what changes and what stays fixed.',
    'Save the code and one view of the mark.',
], panel=[
    'ASK THE CODING AGENT',
    'Use my shared identity brief.',
    'Make HTML with SVG or Canvas.',
    'No image-generation call here.',
    'Expose two simple controls.',
    'Preserve my two key features.',
    '',
    'Machine B writes the code;',
    'Machine A executes it.',
], panel_size=24, bg=TEALS[4],
notes='Ten minutes includes the deliberate parameter change. The coding agent is Machine B; the resulting explicit rules and browser execution are Machine A. Code is not the same as sampled image pixels. Keep the mark simple enough to edit: initials, a few geometric shapes or a symbol. Do not require students to read every line, but ask them to locate the parameter they changed. If randomness is used, a fixed seed supports comparison. Save this source for the hybrid step.'))

S.append(activity('B · MACHINE B · PATTERNS PROPOSE THE PICTURE', 10,
                  'Generate an interpretation.', [
    'Give the image model the same identity brief and two key features.',
    'Explore one material, texture or atmosphere; keep one candidate.',
    'Identify one visible choice the model added or changed.',
    'Save the image, prompt and model name if available.',
], panel=[
    'ASK THE IMAGE TOOL',
    'Use my shared identity brief.',
    'Interpret it as an image.',
    'Keep the two key features.',
    'Explore material and atmosphere.',
    'Do not depend on exact lettering.',
    '',
    'Save the returned image asset.',
    'Keep it for A+B.',
], panel_size=24, bg=PAPER,
notes='Ten minutes includes generation waits and the short observation question that follows. Use the verified course image route. Exact generated lettering is not a requirement; if it fails, that is evidence about control rather than a reason to spend the activity chasing it. A saved image can be reused or a visible material region cropped for the hybrid. Submit once; do not duplicate a pending job. If the call is unavailable or slow, use a supplied image and explicitly record its source.'))

S.append(question('short_answer', 'What did the model decide that you did not specify?',
                  hint='Point to one visible choice in B. Would you keep it for A+B?',
                  eyebrow_text='B · OBSERVE BEFORE COMBINING',
                  notes='A brief check within the B ten-minute allocation, not extra activity time. Ask for an observable choice tied to the shared brief; material, framing, shape, text or atmosphere. A model contribution is not automatically a mistake.'))

S.append(activity('A+B · MACHINE A + MACHINE B', 15,
                  'Keep the form. Borrow the surface.', [
    'Reuse the A code and the image saved from B.',
    'Clip the image, or a cropped region, inside your coded silhouette.',
    'Let code control the boundary and placement; pixels supply the surface.',
    'Three.js is optional: use a texture on a coded surface or mark.',
], panel=[
    'ASK THE CODING AGENT',
    'Keep my A silhouette and controls.',
    'Use the saved B image as a texture.',
    'Use SVG clipping or Canvas masking.',
    'Let me change crop, scale or offset.',
    'Reuse the asset; do not regenerate.',
    '',
    'Optional: bundled Three.js kit.',
    'No external CDN imports.',
], panel_size=24, bg=TEALS[4],
notes='Fifteen minutes. SVG image clipping or Canvas drawImage plus a mask is the baseline. Explicitly request the saved project asset, not a guessed path or a remote URL. The original B image may include a mark; choose a material region and crop it deliberately if reusing the whole image duplicates the shape. This operation reuses pixels; it is not a new generative-model call or a generated 3D model. Three.js is optional only when its offline kit is enabled and WebGL works. A texture on a coded plane or an extruded mark is sufficient; do not add a 3D modeling tutorial. Code fixes boundaries, transforms and interaction; a supplied fallback texture must be labeled. The hybrid is not automatically better.'))

S.append(question('short_answer', 'What did combining the machines buy you?',
                  hint='Show A / B / A+B. Where did rules help—and where did generation help?',
                  eyebrow_text='COMPARE · 5 MIN',
                  notes='The final five minutes of the 40-minute activity. Place the three views side by side in an HTML comparison or a simple contact sheet. Name one enforced decision, one delegated decision and one trade-off. The hybrid may be worse; ask for evidence, not a favourite-image vote. A partial study with an honest explanation is more useful than an unsupported claim of control.'))

S.append(cards('CHALLENGE 4 · BRING TO WEEK 6',
               'Three routes. One comparison layout.', [
    ('YOUR IDENTITY', 'Keep the shared brief.', 'One sentence of intent, two recognizable features, and the A / B / A+B views.'),
    ('YOUR PROCESS', 'Keep the evidence.', 'Code, image prompt, model/tool details and one deliberate change with its effect.'),
    ('YOUR JUDGEMENT', 'Explain the trade-off.', 'What did rules enforce? What did the model invent? Was the hybrid worth it?'),
], text_size=23,
notes='Use these studies in a side-by-side comparison layout, then make and critique one deliberate revision before Week 6. This connects the new personal-mark activity to the syllabus Challenge 4 wording: a layout you could not design, generated, iterated and critiqued. Do not silently change assessment weighting, deadline or submission destination. Record supplied fallback images honestly. A comparison can use the code-based layout and generated media, not a claim that the image model generated the whole page.'))

S.append(content('KEEP A PROCESS RECORD', 'Show who decided what.', [
    'Keep your shared brief and the three views: A, B and A+B.',
    'Retain the A code and parameter change; the B prompt and returned asset.',
    'Record the hybrid crop, mask or texture choices, plus one success or miss.',
    'Name tools and supplied assets honestly. Keep credentials out of the record.',
], body_size=30,
notes='This record supplies evidence for the Week 7 Machine A/B reflection. Follow course privacy rules and the confirmed submission route. Do not expose keys, account tokens or real personal identifiers. Students can explain a rejected hybrid or a service failure without fabricating an output.'))

S.append(end('Rules. Patterns. Your decisions.',
             'You chose what each machine could decide—and what it could not.',
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
