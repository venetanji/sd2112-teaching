"""SD2112 Week 5: one identity, made with rules, learned images and both."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import build_all, PAPER, INK, VIOLET, ORANGE, TEALS  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, content, cards,
                             question, activity, two_col, figure_slide, finalize, T, Rect)  # noqa: E402
from deckgen.core import Image, Figure  # noqa: E402
from course import SITE, PLAYLIST, JOURNEY, footer  # noqa: E402
import week05_figures as F  # noqa: E402
import week05_mediation_figures as M  # noqa: E402
import week05_history as H  # noqa: E402
import week05_case as C  # noqa: E402

FOOTER = footer(5)
S = []
ASSETS = Path(__file__).resolve().parent / 'assets'


def photographic_frame():
    slide = content('PHOTOGRAPHY · THE IMAGE IS A CHOICE',
                    'Photography is not a neutral window.', [], bg=PAPER, title_size=64,
                    notes='Source: Giovanni Lion, Concept Formation in Computational Creativity, Chapter 5 opening and sections 5.1 and 5.3: https://giovannilion.link/thesis/5-study-images.html#scope-1 . The left image is the study photograph in Figure 5.1 (Miller and Lion, 2022); the right is a teaching crop of that SAME file, not another exposure or a generated variant. Photography records light from a scene, but viewpoint, framing, exposure, timing and selection mediate that record. A generated image need not document any photographed event. Ask what the tighter frame makes salient and what it excludes; do not call photography false or erase the distinction between capture and synthesis. Keep this photographic example to about 90 seconds.')
    slide.els = slide.els[:2]
    slide.els += [
        Image(120, 330, 780, 545, str(ASSETS / 'week05-thesis-storefront.jpg'), 'contain'),
        Image(1020, 330, 780, 545, str(ASSETS / 'week05-thesis-storefront-crop.jpg'), 'contain'),
        T(120, 890, 780, 40, 'STUDY PHOTOGRAPH · SHAM SHUI PO', 'monomed', 24, '#246E70'),
        T(1020, 890, 780, 40, 'TEACHING CROP · SAME PHOTOGRAPH', 'monomed', 24, '#246E70'),
        T(120, 946, 1680, 45, 'What did the frame make you notice—and what disappeared?', 'xbold', 35, INK),
    ]
    return slide


def flusser_apparatus():
    slide = content('FLUSSER · PHOTOGRAPHY AND PROGRAMMED POSSIBILITIES',
                    'Flusser: the camera is part of an apparatus.', [], bg=PAPER, title_size=64,
                    notes='Source: Lion thesis Chapter 5.1, applying Vilem Flusser, Towards a Philosophy of Photography (English edition cited as 2000), and Chapter 5.3: https://giovannilion.link/thesis/5-study-images.html#method-1 . Flusser is a media philosopher whose apparatus argument Lion brings into a postphenomenological analysis; do not present him as the founder of Ihde\'s school. A program structures possibilities, not merely literal camera firmware. The wider apparatus includes production, distribution and cultural conventions; photographers can explore and challenge its possibilities rather than only repeat defaults. The photograph shown is one example from the study, NOT the sole training image. These two actual first-iteration FastGAN outputs are from thesis Figure 5.3; their native resolution is 128 x 128, not a slide-export fault. Across the curated dataset, habitual framing and shop selection produced a repeated dark centre, which appeared in generated outputs and prompted reflection. This is the researchers\' case, not a finding asserted by Flusser or a controlled experiment isolating one cause. Spend about two minutes; keep the detailed dataset/training procedure out of the lecture.')
    slide.els = slide.els[:2]
    slide.els += [
        T(120, 348, 780, 80, 'More than a camera.', 'xbold', 46, INK),
        T(120, 446, 780, 145, 'Optics, settings and formats.\nDistribution and conventions.\nA field of programmed possibilities.', 'body', 33, INK, lh=1.25),
        T(120, 655, 780, 145, 'In the study, a habitual dark centre\nechoed in the generated shops.\nThe outputs exposed a framing habit.', 'body', 33, INK, lh=1.25),
        T(970, 338, 400, 45, 'CURATED PHOTOGRAPHS', 'monomed', 24, '#246E70'),
        Image(970, 405, 390, 300, str(ASSETS / 'week05-thesis-storefront.jpg'), 'contain'),
        T(970, 733, 390, 90, 'One study photograph,\nfrom a larger dataset.', 'body', 27, INK, lh=1.2),
        T(1430, 338, 370, 45, 'FASTGAN SAMPLES', 'monomed', 24, '#246E70'),
        Image(1460, 405, 220, 220, str(ASSETS / 'week05-thesis-fastgan-1.jpg'), 'contain'),
        Image(1460, 650, 220, 220, str(ASSETS / 'week05-thesis-fastgan-2.jpg'), 'contain'),
        T(1400, 885, 400, 40, 'NATIVE 128 PX · THESIS FIG. 5.3', 'mono', 20, '#246E70'),
        T(120, 946, 1680, 45, 'Are you exploring possibilities—or repeating the apparatus’s defaults?', 'xbold', 35, INK),
    ]
    return slide


def machine_mediation():
    slide = content('GIO’S COURSE EXTENSION · MACHINE A / MACHINE B / A+B',
                    'Same request. Different machines.', [], bg=PAPER, title_size=64,
                    notes='Source: Lion thesis Chapter 3.1 and Chapter 6.1: https://giovannilion.link/thesis/3-methodology.html#sec:technological-mediation ; https://giovannilion.link/thesis/6-study-text-to-image.html#scope-2 . Also the 2025 Week 5 PDF pages 42-43. Use ONLY the established course A/B/A+B labels on slides, not the thesis notation. This comparison applies Lion\'s extension of the mediation framework; A/B are not Ihde\'s original categories. Left: an illustrative execution of two explicit circle calls matching the 2025 teaching code, not an image-model result. Right: the actual four historical Stable Diffusion samples in thesis Figure 6.1 for the prompt two circles. They show that exact count was not reliably enforced in that example; do not generalize to every current model, every seed or all prompts. Code can include randomness, learned systems can be repeatable, and neither is fully transparent just because we know the label. In the workshop, Machine B can write the code that Machine A executes. A+B allocates coded geometry and generated appearance; it does not automatically improve the result. Ask which choices students make and which the system makes possible or likely. This is a spoken question within the five-slide bridge, not another ClassPoint activity.')
    slide.els = slide.els[:2]
    svg, png = M.two_circle_rules()
    slide.els += [
        T(120, 312, 1680, 60, 'THE REQUEST: “TWO CIRCLES”', 'xbold', 38, INK),
        T(120, 399, 780, 42, 'MACHINE A · EXPLICIT INSTRUCTIONS', 'monomed', 24, '#246E70'),
        T(1020, 399, 780, 42, 'MACHINE B · LEARNED INTERPRETATION', 'monomed', 24, '#246E70'),
        Rect(120, 456, 780, 385, '#FFFFFF'),
        Figure(253, 456, 514, 385, svg, png, name='two-circle-rules'),
        Image(1218, 456, 385, 385, str(ASSETS / 'week05-thesis-two-circles.jpg'), 'contain'),
        T(120, 860, 780, 76, 'circle(200, 300, 150);\ncircle(400, 200, 250);', 'mono', 27, INK, lh=1.2),
        T(1020, 860, 780, 76, 'Historical Stable Diffusion samples.\nAppearance suggested; count not enforced.', 'body', 27, INK, lh=1.2),
        T(120, 947, 1680, 45, 'A+B: code sets the boundary; generated pixels supply the surface.', 'xbold', 34, INK),
    ]
    return slide


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
    """A post-break showcase connects the theory to the shared identity brief."""
    slide = content('AFTER THE BREAK · EASEL CLIENT · LOGO DEMO',
                    'One mark. Three routes.', [], bg=PAPER, title_size=64,
                    notes='Post-break logo/Easel demo, after all the theory and before installation and the brief: show one prepared identity as coded HTML/SVG/Canvas graphics, a generated image and a combination. These are routes to compare, not a claim that a hybrid is best. Easel Client UI name is Easel Studio: https://github.com/venetanji/easel-client. The agent writes code; the browser executes it. Media models generate pixels through separate tools. Apply the Machine A/B distinction just taught, rather than giving a long feature tour. Show already saved outputs; do not let an asynchronous image/video job delay the demo. Follow with the actual course-mark still and chat/video iterations. Keep the combined demo to around ten minutes. Installation and provider checks come next, outside the 40-minute activity; do not display credentials.')
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

S.append(agenda('SD2112 · WEEK 05', [
    'Images and technology: perception, mediation, photography',
    'Machine A: rules, Bense, Nake and computer art',
    'Machine B: learned images and text-to-image',
    'Agents: coordinating Machine A + Machine B',
    'After the break: logo demo, setup and brief',
    'Activated: Machine A, Machine B, Machine A+B',
    'Compare the routes; develop your reflection',
], notes='Start with roughly one hour of theory. Break, the logo/Easel demo, installation and the brief precede the 40-minute making block. Protect 10 + 10 + 15 + 5 minutes; do not add a separate prompt-writing or 35-minute iteration exercise.'))

S.append(section('00 · IMAGES AND TECHNOLOGY', 'Images and technology.',
                 'Perception → mediation → apparatus → photography', bg=INK,
                 notes='Introduce images broadly before specializing in photography or generated images. Start with Heidegger and Ihde, then Flusser and the photographic case. This divider is a transition within the existing lecture budget, not an extra teaching block.'))
S.append(figure_slide('HEIDEGGER · EQUIPMENT AND TECHNOLOGICAL REVEALING',
                      'Heidegger: a tool is more than an object.', M.tool_encounter(), bg=PAPER,
                      caption='A way of revealing—not a synonym for photographic framing.',
                      notes='Keep two accounts distinct: Being and Time (1927) examines equipment in practical involvement (ready-to-hand) and objects considered in inspection (present-at-hand); breakdown may interrupt use but does not simply define presence-at-hand. The Question Concerning Technology (1954) examines modern technology as enframing, a mode of revealing that orders things as resources or standing-reserve. Enframing is not a photographic crop, nor merely a property of a device. These are introductory distinctions, not identical to Ihde\'s categories. Lion thesis Chapter 2 and Chapter 3.1 situate the phenomenological background; sources: https://plato.stanford.edu/entries/heidegger/ and https://giovannilion.link/thesis/3-methodology.html#sec:technological-mediation . Spend around two minutes; avoid a history-of-philosophy detour.'))
S.append(figure_slide('IHDE · POSTPHENOMENOLOGY AND TECHNOLOGICAL MEDIATION',
                      'Ihde: technology mediates our world.', M.mediation_relations(), bg=PAPER,
                      caption='Same camera. Different relations—depending on how you use it.',
                      notes='Source: Don Ihde, Technology and the Lifeworld (1990), as discussed in Lion thesis Chapter 3.1: https://giovannilion.link/thesis/3-methodology.html#sec:technological-mediation . The four relations are embodiment, hermeneutic, alterity and background. Use two situated examples: looking through a viewfinder towards a scene; interpreting a photograph as a representation. Neither permanently classifies all photography. Interacting with a camera menu or an agent may foreground the tool as quasi-other; background systems shape the situation without focal attention. Technologies amplify and reduce aspects of perception and action, rather than being neutral pipes between a fully fixed person and world. The diagram is a simplified relational schema, not a signal-processing pipeline. Postphenomenology inherits and revises phenomenological questions; do not collapse Ihde with Heidegger, or call Flusser its founder. Spend around two minutes.'))
S.append(flusser_apparatus())
S.append(photographic_frame())
S.append(machine_mediation())
S.append(cards('THE DESIGNER’S JOB · AFTER THE THEORY', 'The model does not supply your reason for making the image.', [
    ('INTENT', 'What should the image do?', 'Name the subject, audience, feeling, use and visual choices that matter to you.'),
    ('PROMPT', 'Make the intent legible.', 'An agent can ask questions, expose ambiguity and help you write a clearer specification.'),
    ('JUDGEMENT', 'Decide what happens next.', 'You select, critique, revise or reject the result. The model does not own that decision.'),
], text_size=23,
notes='After the philosophical and photographic examples, return to the designer\'s reason for making an image. Position the language agent as a prompt clarifier, not an autonomous creative director. Students remain the source of the idea and the judge of the output.'))

S.append(section('01 · MACHINE A · PROCEDURAL IMAGES', 'Machine A: images from rules.',
                 'Procedures · Bense · Nake · the computer-art debate', bg='#246E70',
                 notes='Name the first image-making route before the five history slides. Machine A executes explicit instructions; rules may include controlled randomness. Keep this divider within the existing six-minute history block.'))
S.extend(H.slides())

S.append(section('02 · MACHINE B · LEARNED IMAGES',
                 'Machine B: images from learned patterns.',
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

S.append(question('short_answer', 'When would a convincing image still fail your intention?',
                  hint='Name a convincing result you would reject. What in your brief would it fail?',
                  eyebrow_text='REFLECTION SEED 1 · INTENT AND APPEARANCE',
                  notes='Allow roughly three minutes within the lecture, not an extra quiz. Reflection seed: distinguish visual plausibility, matching words and serving a purpose. Use evidence from a previous experiment or a specific example just shown; state which requirement matters and why. CLIP alignment is not image generation or a guarantee of exact count, identity or meaning. Connect Bense/Nake\'s critique of novelty to a present design decision without equating the historical systems. There is no preferred pro- or anti-AI answer. These ClassPoint responses can become starting claims for the Week 7 reflection, not finished paragraphs or new assessment requirements.'))

S.append(figure_slide('MACHINE A+B · AGENTS COORDINATE TOOLS',
                      'The agent can look, make, and look again.', F.agent_image_tools(),
                      caption='The student supplies the intent and decides whether the result is worth keeping.',
                      notes='Bridge from model capability to interaction. An agent can inspect an image with a vision tool, draft or revise a prompt, call an image-generation/editing tool, and inspect the result. The agent coordinates tools; it does not own the design intention or decide what counts as success. Easel Client is the lecturer demo. Student tool access and the installed app configuration still require a pre-class check.'))

S.append(cards('FROM WEEK 2 + WEEK 4 · NAME THE MACHINES',
               'Same intent. Different kinds of control.', [
    ('MACHINE A', 'Rules execute.', 'Code sets the shapes, layout and parameters. Change a rule; inspect its effect.'),
    ('MACHINE B', 'Learned patterns propose.', 'An image model interprets the brief. You judge its appearance and assumptions.'),
    ('A + B', 'Divide the decisions.', 'Keep geometry in code; use generated pixels for material, texture or atmosphere.'),
], text_size=24,
notes='Machine B writes the code; Machine A executes it. This is the Week 2 distinction, not a claim that the coding agent is a symbolic model. All three routes may use a learned agent; the distinction concerns how the visual artifact is produced. A programmed sketch can include controlled randomness, so do not equate Machine A with no variation. Rendering a generated texture on a surface is not a generated 3D model.'))

S.append(section('BREAK', 'After the break: make it yours.',
                 'Logo demo → install Easel → set one brief → make A, B and A+B', bg=INK,
                 notes='Natural break after about one hour of theory. On return, show the logo/Easel demo and actual chat/video iterations, then walk through installation and the shared brief before starting the activity clock. The lecturer may use remaining scheduled class time for setup or individual help; do not inflate the 40-minute activity to fill the three-hour booking.'))

S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 05 · DEMO + WORKSHOP',
               'Images, intentions, iterations.',
               'You bring the idea. The model brings possibilities.',
               notes='This title begins the post-break demo and workshop, after all the theory. Demonstrate Easel with the course mark and real logo/video iterations, then walk through installation and one shared personal-mark brief. The 40-minute activity clock starts only once setup and the brief are complete. Students make A, B and A+B studies of the same identity; do not imply student credentials or endpoint access are already established.'))

S.append(easel_demo())
S.append(logo_exploration())
S.append(video_discussion())
S.extend(C.slides())

S.append(content('AFTER THE BREAK · EASEL SETUP', 'Install. Open. Check.', [
    '[Download Easel Studio for your OS](https://github.com/venetanji/easel-client/releases).',
    'Open Easel Studio. Create one project for your personal mark.',
    'Use the course-approved configuration; test a canvas and one image call.',
    'If setup fails: [PolyU GenAI](https://genai.polyu.edu.hk/) for images; Open Design or your working harness.',
    'Keep the same brief. Pair or use the prepared fallback if needed.',
], body_size=29,
notes='Installation and access checks are outside the 40-minute activity. Current verified release on 2 October: https://github.com/venetanji/easel-client/releases/tag/v0.0.4. Packaged Windows x64 EXE/ZIP, macOS ARM64 DMG/ZIP and Linux x86_64 AppImage/DEB are listed; no Intel Mac installer was listed on 2 October. Check current releases, actual classroom OS/architecture and permitted installation before class. Release installers do not require the Node.js development workflow. Do not bypass OS or institutional security controls. Student accounts, endpoints and quotas must be course-approved; do not ask for keys in a chat or screenshot. Test HTML/SVG/Canvas, image generation and saved-image reuse. For optional Three.js, verify the bundled offline kit under Settings > Kits and in project settings; no CDN or external URL imports. If installation fails, students can use an already working, permitted Open Design setup or another harness; PolyU GenAI is an image-generation fallback, not a promised code/project or API replacement. Keep the same brief and record which tool supplied each part. Do not require a new account or unverified provider. If no device works, use a TA-prepared browser example and supplied texture; label supplied assets as fallback rather than student-generated evidence.'))

S.append(content('THE SHARED BRIEF · BEFORE THE TIMER',
                 'Make a mark that represents you.', [
    'Choose a name, nickname, invented character or personal symbol.',
    'Write one sentence: what should this identity communicate?',
    'Choose two things that must remain recognizable across all three routes.',
    'Keep the same brief. A fictional identity is fine; no portrait is required.',
], body_size=32,
notes='Briefing precedes the making timer. Ask for two observable invariants, for example a crescent silhouette and a detached dot, not a demand that every pixel match. Use this same brief in A, B and A+B. No real name, photograph or personal data is required. This is a rapid identity study, not a commercial trademark or a finished branding project.'))

S.append(question('short_answer', 'What should your mark never lose—even when a model reinterprets it?',
                  hint='Name a feature and why it matters to your intent—not only how it looks.',
                  eyebrow_text='REFLECTION SEED 2 · YOUR SHARED BRIEF',
                  notes='A reflexive moment within the post-break brief before the making timer. Reflection seed: choose a boundary between a deliberate invariant and an interpretation you can delegate. Give evidence by identifying an observable feature and explaining its significance to the chosen identity. Students may use a fictional identity; no personal photograph or private details are required. Keep one sentence of intent and two recognizable features across A, B and A+B. Answers are provisional: later outputs may challenge the student\'s priorities, but any change to the brief must be acknowledged rather than retroactively called success.'))

S.append(activity('WORKSHOP · ONE BRIEF · THREE QUICK STUDIES', 40,
                  'One identity. Three ways of making it.', [
    'A · 10 min: code a mark; change one parameter.',
    'B · 10 min: generate an interpretation; inspect one model choice.',
    'A+B · 15 min: combine generated pixels with the coded form.',
    'Compare · 5 min: review your iterations; upload the final A+B image.',
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
    'One final image submission.',
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
    'Ask the agent to generate images from the same identity brief.',
    'Explore one material, texture or atmosphere; keep one candidate.',
    'Identify one visible choice the model added or changed.',
    'Save the image, prompt and model name if available.',
], panel=[
    'ASK THE AGENT',
    'Use my shared identity brief.',
    'Call the image-generation tool.',
    'Keep the two key features.',
    'Explore material and atmosphere.',
    'Do not depend on exact lettering.',
    '',
    'Save the returned image asset.',
    'Keep it for A+B.',
], panel_size=24, bg=PAPER,
notes='Ten minutes includes image-generation waits and inspecting the candidates. Ask the Easel agent to call the image-generation tool, not merely write a prompt or draw SVG in place of generated pixels. Use the verified course image route. Exact generated lettering is not a requirement; if it fails, that is evidence about control rather than a reason to spend the activity chasing it. Save the returned image assets for the third exercise; there is no intermediate ClassPoint submission. Keep a private observation about one model choice for the reflection process record. Submit a generation job once; do not duplicate a pending job. If the call is unavailable or slow, use a supplied image and explicitly record its source.'))

S.append(activity('A+B · MACHINE A + MACHINE B', 15,
                  'Keep the form. Borrow the surface.', [
    'Give the agent your A code and saved B assets as image inputs.',
    'Clip the image, or a cropped region, inside your coded silhouette.',
    'Refine your final version: code controls form; pixels supply the surface.',
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

S.append(question('image_upload', 'Upload your final A+B image.',
                  hint='One image of your third exercise: export the result or take a screenshot.\nSubmit the final version, not a comparison sheet of all three.',
                  eyebrow_text='COMPARE · 5 MIN · FINAL IMAGE SUBMISSION',
                  cp={'type': 'image_upload', 'hide_names': False, 'caption_required': False},
                  notes='One required classroom image submission per student, after all three exercises, within the final five minutes of the protected 40-minute activity. Upload an exported image or screenshot of the final third-exercise A+B result, not the B-only candidate and not a required A/B/A+B comparison collage. No written answer or caption is required here. Review the iterations against the brief before selecting the final version; retain code, prompts, inputs and private observations for the existing reflection. An honest partial result or labeled fallback is acceptable. This classroom capture does not change the separate Challenge 4 or Week 7 assessment brief.'))

S.append(content('OPTIONAL EXTRA · VIDEO SUBMISSION', 'Optional: animate your final version.', [
    'Ask the Easel agent to animate your final version.',
    'Record the animated canvas, or use video generation if available.',
    'Upload a playable clip in the optional video activity, or skip this.',
    'Your final image completes the workshop.',
], body_size=32,
notes='Optional extra submission, only after the required final image. Ask the Easel agent to animate the final composition, reusing its saved assets. The Easel README documents record_canvas_video for a visible canvas, producing silent video; it does not record a DOM-only composition or add audio. generate_video is another option only if the permitted video endpoint is configured and working. Verify the installed classroom version and recording route before class; do not promise image-to-video reference support, a built-in DOM/HTML-to-video exporter or guaranteed generation completion. Skip this if there is no time, access or playable result; it is not an extra timed exercise, an assessment requirement or an extension to the 40-minute activity. Do not wait for a pending video before submitting the required image, and do not duplicate pending generation jobs. PRE-CLASS MANUAL SETUP: deckgen v0.11.2 does not support native video_upload activities in HTML or PPTX. On slide 44, use the ClassPoint add-in to add a Video Upload activity manually, then test it on the classroom computer. Run it only for volunteers, without a mandatory caption or additional written response. This source intentionally has no CP metadata or fake generated video button.'))

S.append(cards('CHALLENGE 4 · BRING TO WEEK 6',
               'Three routes. One comparison layout.', [
    ('YOUR IDENTITY', 'Keep the shared brief.', 'One sentence of intent, two recognizable features, and the A / B / A+B views.'),
    ('YOUR PROCESS', 'Keep the evidence.', 'Code, image prompt, model/tool details and one deliberate change with its effect.'),
    ('YOUR JUDGEMENT', 'Explain the trade-off.', 'What did rules enforce? What did the model invent? Was the hybrid worth it?'),
], text_size=23,
notes='Use these studies in a side-by-side comparison layout, then make and critique one deliberate revision before Week 6. This connects the new personal-mark activity to the syllabus Challenge 4 wording: a layout you could not design, generated, iterated and critiqued. Do not silently change assessment weighting, deadline or submission destination. Record supplied fallback images honestly. A comparison can use the code-based layout and generated media, not a claim that the image model generated the whole page.'))

S.append(content('KEEP A PROCESS RECORD · WEEK 7 REFLECTION', 'Turn a result into an argument.', [
    'Return to a ClassPoint question: make a claim about your creative process.',
    'Support it with a decision and evidence: images, code, prompts or revisions.',
    'Compare A and B. What did each make possible, difficult or likely?',
    'About 1000 words; three of your own experiments with images; an AI-writing process note.',
], body_size=30,
notes='Remind the existing syllabus reflection brief, not a new requirement: about 1000 words on the role of AI in your creative process, particularly Machine A versus Machine B, at least three of your own weekly-challenge experiments from weeks 2–6 with images, and a short note on how AI was used in writing. Submitted in Week 7 via Canvas. The two ClassPoint questions about intention and identity, plus private observations about model choices and relocated control, are optional avenues for an evidence-led argument, not compulsory essay sections. The final image and optional video are classroom captures, not additional essay requirements. Retain the brief, code/parameter change, prompt/asset and hybrid choices; identify supplied fallbacks honestly. Do not expose credentials or personal identifiers. A rejected hybrid or service failure can be useful evidence without a fabricated output.'))

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
