"""SD2112 Week 5: image generation as a designed, iterative process."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import build_all, PAPER, INK, VIOLET, ORANGE, TEALS  # noqa: E402
from deckgen.layouts import (title, end, agenda, section, statement, content, cards,
                             question, activity, two_col, figure_slide, finalize)  # noqa: E402
from course import SITE, PLAYLIST, JOURNEY, footer  # noqa: E402
import week05_figures as F  # noqa: E402

FOOTER = footer(5)
S = []

S.append(title('POLYU SCHOOL OF DESIGN · SD2112 · WEEK 05 · LECTURE + WORKSHOP',
               'Images, intentions, iterations.',
               'You bring the idea. The model brings possibilities.',
               notes='Open with the students’ own image ideas. The lecture makes the visual-model sequence legible: image-only GANs, CLIP’s shared image/text representation, diffusion, then an agent that can use image-understanding and image-generation tools. The workshop applies that sequence to student-owned intent. Confirm the actual authorized image service before class; do not imply a direct API is available if it is not.'))

S.append(agenda('SD2112 · WEEK 05', [
    'Start with an image you want to make',
    'From image-only GANs to CLIP and diffusion',
    'Use image understanding and generation through an agent',
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
                 'What changed when images learned language?',
                 'from examples · to alignment · to denoising', bg=VIOLET,
                 notes='Frame this as a change in how visual models can be conditioned, not as a claim that one architecture simply replaced another. Keep the technical account at the level needed to understand the image-generation tools students will meet.'))

S.append(content('GANs · 2014 · GENERATIVE ADVERSARIAL NETWORKS',
                 'GANs learn a visual distribution—not a description.', [
                     'A generator turns random input into candidate images.',
                     'A discriminator learns to distinguish generated images from examples.',
                     'In this early image-generation story, there is no caption telling the GAN what to draw.',
                 ], image='edmond-de-belamy.jpg', fit='contain', body_size=28,
                 caption='Obvious, Portrait of Edmond de Belamy (2018), made with a GAN; the historical example shown in the 2025 Week 5 deck.',
                 notes='Use the portrait as a concrete artifact, not as evidence that all GANs are unconditional: conditional GAN variants exist. The teaching contrast is with the text-conditioned image-generation interfaces students use today. The original 2025 Week 5 deck shows generated sample grids and a generator/discriminator schematic on pp. 45–46, then this portrait on p. 47.'))

S.append(figure_slide('GANs · TWO MODELS IN COMPETITION',
                      'One learns to make. The other learns to catch.', F.gan_adversaries(),
                      caption='A simplified training picture. Classic image GANs learn from image examples; text is not the instruction channel here.',
                      notes='Walk left to right: training examples and random latent input; the generator makes a candidate; the discriminator compares it with real examples; their competition improves both. This is a teaching schematic, not a literal network diagram for every GAN variant. The original 2025 slide used a generator/discriminator flow beside grids of generated digits, faces and animals.'))

S.append(figure_slide('CLIP · CONTRASTIVE LANGUAGE–IMAGE PRETRAINING',
                      'CLIP brings words and images into a shared space.', F.clip_shared_space(),
                      caption='Paired text and image representations are trained to align; CLIP is not itself the image generator.',
                      notes='Explain the two encoders and paired examples: matching captions and pictures are trained to have similar representations, while non-matching pairs are pushed apart. Treat the 2D points as a conceptual projection, not CLIP’s literal high-dimensional space. This updates the 2025 deck’s helpful caption/image pairing and similarity-matrix visuals on pp. 48–50.'))

S.append(figure_slide('TEXT-TO-IMAGE · A GENERATIVE SYSTEM',
                      'A prompt guides an iterative image-generation pipeline.', F.text_conditioning(),
                      caption='In latent diffusion, text conditions iterative denoising; a VAE decoder turns the final latent into pixels.',
                      notes='Walk from prompt to text encoder to contextual text features. Separately sample initial latent noise; the denoising model updates that latent over many steps, using the text features as a condition, and the VAE decoder returns pixels. This is a high-level latent-diffusion workflow, not a literal network graph: exact text encoders, denoisers, step counts and VAE configurations vary by model. The 2025 Week 5 PDF page 54 shows a comparable text encoder, random-noise input, iterative diffusion model and VAE decoder; its CLIP label is model-specific, not universal.'))

S.append(figure_slide('LATENT DIFFUSION · VARIATIONAL AUTOENCODER',
                      'A VAE moves between pixels and a compact latent.', F.vae_latent(),
                      caption='The encoder predicts a latent distribution; sample z at the narrow bottleneck, then decode back to image space.',
                      notes='Follow the hourglass: image x enters the encoder, which predicts a distribution over z (shown with its mean and log-variance); sample z, then the expanding decoder predicts reconstruction x-hat. This is the standard VAE shape shown in the 2025 Week 5 PDF page 53. Do not imply that text-to-image sampling needs a source image: in latent diffusion, noise is denoised in latent space and the VAE decoder maps the final latent to pixels.'))

S.append(figure_slide('DIFFUSION · TRAINING AND GENERATION',
                      'Generation reverses the gradual noising process.', F.diffusion_denoising(),
                      caption='Training adds noise to examples; generation iteratively removes it from a noisy latent.',
                      notes='Contrast the directions: forward noising is used to train the denoiser; generation runs the learned process in reverse, updating a noisy latent over many steps. The sketches show only a few qualitative snapshots, not literal saved outputs or measured noise levels. Encoded text can condition the reverse updates. A VAE decoder then maps the final latent to pixels in latent-diffusion systems. The 2025 deck introduces this forward/reverse relationship on p. 51 and connects the text encoder, denoiser and VAE on p. 54.'))

S.append(figure_slide('AGENTS · IMAGE UNDERSTANDING + GENERATION AS TOOLS',
                      'The agent can look, make, and look again.', F.agent_image_tools(),
                      caption='The student supplies the intent and decides whether the result is worth keeping.',
                      notes='Bridge from model capability to interaction. An agent can inspect an image with a vision tool, draft or revise a prompt, call an image-generation/editing tool, and inspect the result. The agent coordinates tools; it does not own the design intention or decide what counts as success. Tool availability and actual course platform are still subject to the pre-class check.'))

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
                 notes='Before class, confirm the authorized student-facing image-generation API, its account requirements, supported inputs and rate limits. The syllabus names PolyU GenAI with Flux and Qwen, but does not establish a direct API endpoint or student API credentials. If only the approved platform UI is available, use it and describe the activity accurately; do not invent an API route or ask students to expose credentials.'))

S.append(two_col('03 · A FIRST GENERATION', 'Make a first image, not a final answer.',
                 [
                     'Use your approved image-generation API or course platform.',
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
