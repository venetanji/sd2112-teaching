"""Week 12 course recap, closing discussion, ESFQ, and fair setup."""
from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from deckgen import INK, TEAL
from deckgen.layouts import T, cards, content, finalize, palette, statement, title, two_col
from course import SITE, footer
import week01
import week02
import week03
import week04
import week05
import week06
import week08
import week09
import week11
from week09_mediation import EEDE, MITCHELL, VERBEEK


def source(week, slide, label):
    return f'[{label}](https://{SITE}/week{week:02d}/#/{slide - 1})'


def paper(authors, title, url):
    return f'{authors} / [{title}]({url})'


def recap(original, number, notes, *, heading=None, eyebrow=None, labels=None):
    slide = deepcopy(original.DECK['slides'][number - 1])
    slide.els = [el for el in slide.els if not el.name.startswith('chrome-')]
    slide.notes = notes
    if eyebrow:
        slide.els[0].paras[0].runs[0].text = eyebrow
    if heading:
        slide.title = heading
        slide.els[1].paras[0].runs[0].text = heading
    if labels:
        for element in slide.els:
            for paragraph in getattr(element, 'paras', []):
                for run in paragraph.runs:
                    run.text = labels.get(run.text, run.text)
    week = int(original.__name__[-2:])
    in_band = getattr(slide, 'caption_band', False)
    text_color, _, muted = palette(INK if in_band else slide.bg)
    links = source(week, number, f'Week {week} / Original slide')
    slide.els.append(T(1260, 970 if in_band else 999, 450, 34, links, 'monomed', 23,
                       TEAL if text_color == INK else muted))
    return slide


board_path = Path(__file__).with_name('week12-poster-fair-link.txt')
if board_path.is_file():
    board = f'[Open the Excalidraw room]({board_path.read_text().strip()})'
else:
    board = 'Open the Excalidraw room link shared in class.'

S = [
    title('POLYU SCHOOL OF DESIGN / SD2112 / WEEK 12',
          'Can a machine\noriginate a design?', 'Course recap and discussion / ESFQ at 12:30',
          notes='11:30. Put the opening course question back on screen. Ask students to hold their first answer in mind, then name one thing they would now add. Weeks 1-3 gave us concepts, mediation and AI paradigms. Weeks 4-6 used AI for language, visual work and audio. In the second half we asked what happens when people use products with AI inside. Stop for ESFQ at 12:30.',
          size=125),
    recap(week01, 24,
          '11:30-11:35 / Opening. Read the first sentence of Note G. Lovelace was writing about the Analytical Engine. What would count as originating? Hold that question for the closing discussion.'),
    recap(week01, 27,
          'Introduce the distinction with chairs. Machine A follows rules a person specifies. Machine B learns a pattern from examples. A handwritten rule may use chance. A learned model can be controlled by rules around it. The distinction is where the rule for the task came from.',
          eyebrow='WEEKS 1-3 / CONCEPTS, MEDIATION AND AI PARADIGMS'),
    recap(week05, 7,
          'Return to the two circles example from the 2025 recap, page 9. Here the code fixes the count. The historical Stable Diffusion outputs show that an instruction in a prompt may only guide the result. Ask what each route leaves to the system.'),

    recap(week03, 35,
          '11:35-11:41 / Rules and the plotter. Put the two theories of concepts beside the two approaches to AI, as in the 2025 recap. Briefly distinguish definitions from typical examples. First follow the rules line into art, then return to examples and learning.'),
    recap(week02, 24,
          'The wall drawing begins as an instruction that other people can execute. LeWitt is a bridge from a written score to a computer program. What can the executor decide?'),
    recap(week02, 31,
          'Georg Nees, Schotter. Follow the image from perfect grid to gravel. A plotter draws the marks. In this reconstruction the human wrote the grid, the possible rotation and displacement, and how variation grows down the page. Name the rule and the source of variation.'),
    recap(week02, 33,
          'Frieder Nake, Walk-Through-Raster. The program ran in ALGOL on a Zuse Graphomat Z64 plotter. Compare the four prints. Look for a repeated structure and one mark that varies. The program specifies a family of images.'),
    recap(week02, 34,
          'Point to the empty cell and the cap below it. Nake carries one bit of state from the cell above. Rules and chance can work together, yet the program is explicit.'),
    recap(week03, 8,
          '11:41-11:47 / Concepts and learning. The classical theory defines a concept by necessary and jointly sufficient features. A candidate must satisfy every condition. Ask whether we can write comparable conditions for a chair or a game.',
          heading='Classical theory of concepts'),
    recap(week03, 20,
          'Remember the fruit exercise. We recognize less typical fruit without writing a complete definition. Prototype theory explains typicality through similarity to representative features. Connect this to learning from examples as an analogy.',
          heading='Prototype theory'),
    recap(week03, 26,
          'A neuron takes a weighted sum, adds a bias and produces an output. In the perceptron exercise, examples with labels told us when to nudge the weights. The person chooses the inputs and learning setup, while the weights are learned.'),
    recap(week03, 32,
          'Hinton, Rumelhart and Williams helped popularize backpropagation in 1986. Show the portrait briefly. The problem was how to learn the weights across several layers, where each layer can learn features useful to the next.'),
    recap(week03, 34,
          'Trace the diagram from input to guess, then from error back through the layers. Backpropagation computes how changing each weight would affect the error. Training adjusts the weights and repeats this across examples.'),
    recap(week03, 42,
          'The same arithmetic happens across many pixels or activations. Graphics chips from gaming can run many such operations in parallel, making large neural-network training more practical.'),
    recap(week03, 44,
          'AlexNet in 2012 connects data, learning and GPUs. Follow the diagram from pixels through learned features to classes. Classifying an image and generating a new image are different tasks.'),
    recap(week05, 4,
          'Close the foundations with mediation: technology changes what a person notices and can do. Use the camera to show two relations to the same world. Carry that question into our own use of tools and later into products other people use.'),

    recap(week01, 40,
          '11:47 / Introduce the two roles before the media recap. Use a team making a poster with AI as the first example, and a product using AI to decide what a person sees as the second. Start with the creative tools from Weeks 4-6. Return to the product distinction after audio.',
          eyebrow='WEEKS 4-6 / LANGUAGE, VISUAL AND AUDIO',
          labels={'WEEKS 1 – 6 · THE PROCESS': 'WEEKS 4-6 / THE CREATIVE PROCESS',
                  'WEEKS 8 – 12 · THE PRODUCT': 'WEEKS 8-11 / THE PRODUCT'}),
    recap(week04, 12,
          '11:47-11:51 / Language. Start with ELIZA as a rule-based comparison. Its reply can sound apt because a written pattern matches and is transformed. Then ask how learning from text changes what can be handled.'),
    recap(week04, 16,
          'Follow a token in the transformer diagram. A language model uses context to predict a distribution for the next token, then repeats. Training from examples makes the language flexible. A fluent continuation still needs checking against evidence.'),
    recap(week04, 24,
          'The 2025 recap puts hallucination and retrieval together. An embedding can retrieve relevant passages. The model then writes with that material in context. Verify whether the cited source actually supports the answer.'),
    recap(week04, 28,
          'When text becomes an interface for actions, the model can propose a tool call. The harness determines available tools and executes permitted calls. This is Machine B inside a system that also contains Machine A. Save the permission question for the discussion.'),
    recap(week05, 18,
          '11:51-11:54 / Images and video. CLIP places related text and images near one another in a learned space. It gives us a way to compare or condition across media. The generator is a separate component.'),
    recap(week05, 23,
          'Trace the classic latent diffusion diagram from noise to image. The denoising steps are guided by the prompt and the learned model, then a decoder produces pixels. Different seeds and references can change the result.'),
    recap(week05, 33,
          'These are saved still-image iterations of the course mark. Point to the shape that carries through and the setting and contrast that change. Then ask what has to carry across shots when the image becomes a video.'),
    recap(week05, 34,
          'For the course-mark video, the V8 render put flames inside the letter and along its edge. The team asked for a front-facing burn from the top down, replacing that transition and preserving the adjacent shots. The revision was delivered for review. Video introduces continuity and timing decisions across frames.'),
    recap(week06, 20,
          '11:54-11:57 / Music and sound. Take a four-bar groove. The composer fixes the tempo and bass pattern, defines where a drum fill can vary and listens for whether it supports the phrase. These are illustrative choices, using the same idea of explicit rules and bounded chance as the plotter.',
          heading='Musical choices in a sequencer',
          eyebrow='WEEKS 4-6 / MUSIC / MACHINE A',
          labels={
              'What must repeat?': 'Tempo and bass',
              'A note pattern, entry point or duration can be specified explicitly.':
                  'Set 100 BPM and repeat the same four-bar bass pattern.',
              'Where may chance enter?': 'Drum fills',
              'Choose the possible notes, their probabilities or a permitted timing variation.':
                  'At the end of each phrase, choose one of three fills or leave a rest.',
              'What serves the brief?': 'Groove and space',
              'Predictability is not automatically boring; randomness is not automatically creative.':
                  'Listen back. Does the fill lift the next phrase or crowd it?',
          }),
    recap(week06, 22,
          'Compare a spectrogram image with audio tokens. The representation shapes what can be learned. Contrast both with a step sequencer where you can read the rule or edit the notes directly.'),
    recap(week06, 25,
          'The audio reference workflow takes a demo the designer made and proposes a new arrangement. Listen for what stays, what changes and who decides which version to release. The examples of language, image, video and music all bring us from making a candidate to judging it.'),

    recap(week08, 20,
          '11:57-12:00 / AI inside products. Switch from the designer using a creative tool to a person who encounters AI inside an experience. In this study, choices of who to talk to and ratings of how a reply felt came apart. Feeling heard here describes a response to this task. Ask what else we would need to measure to assess care quality or lasting benefit.',
          eyebrow='WEEKS 8-11 / AI INSIDE PRODUCTS / R8'),
    recap(week08, 12,
          'Calibrated trust. Can someone understand the boundary, disagree and act? Treat a claim about trust as a specific question about evidence and control. What can people check before relying on the answer?'),
    recap(week09, 16,
          '12:00-12:03 / Feedback, harm and design process. Trace exposure, choice, signal and the next feed. The product chooses what becomes visible. Later data includes responses to what it already showed.'),
    recap(week09, 20,
          'Gender Shades: look past the aggregate. Error differed across groups and systems in this evaluation. Ask whose errors our projects could be averaging away.'),
    content('WEEK 10 / DESIGN PROCESS', 'The Double Diamond', [
        'Discover and Define: understand the people and decide which problem the AI would address.',
        'Develop and Deliver: compare interactions, test with people, and revise when the evidence changes.',
        source(8, 56, 'Week 8 / AI in the design process'),
    ], image='week12/design-council-double-diamond.png', fit='contain', body_size=34,
        caption='[Design Council, The Double Diamond](https://www.designcouncil.org.uk/our-resources/the-double-diamond/). [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).',
        notes='Recall the Week 10 guest session and the design-process material in the 2025 recap, page 36. Follow the two moments of opening possibilities and narrowing choices. The official Design Council diagram is reused unchanged from the Week 10 draft. The AI questions are our application of the framework.'),
    recap(week11, 11,
          '12:03-12:07 / Curation, agency and ownership. Individuals in the writing experiment got better ratings with AI ideas, yet their stories also became more similar. This is one bounded task. Ask which outputs and sources get selected and what becomes less visible.'),
    content('COURSE RECAP / RECOMMENDERS, BIAS AND MEDIATION', 'Week 9 papers', [
        paper('Covington, Adams & Sargin (2016)', 'Deep Neural Networks for YouTube Recommendations', week09.REFS['R1'][1]),
        paper('Gauthier et al. (2026)', "The Political Effects of X's Feed Algorithm", week09.REFS['R2'][1]),
        paper('Glickman & Sharot (2025)', 'How human-AI feedback loops alter human perceptual, emotional and social judgements', week09.REFS['R3'][1]),
        paper('Buolamwini & Gebru (2018)', 'Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification', week09.REFS['R4'][1]),
        paper('Gebru et al. (2021)', 'Datasheets for Datasets', week09.REFS['R5'][1]),
        paper('Mitchell (1980)', 'The Need for Biases in Learning Generalizations', MITCHELL),
        paper('Verbeek (2015)', 'Beyond Interaction: A Short Introduction to Mediation Theory', VERBEEK),
        paper('Van Den Eede (2011)', 'In Between Us: On the Transparency and Opacity of Technological Mediation', EEDE),
    ], body_size=30,
        notes='Brief reference within the recap, with links for later use. These papers come from the Week 9 teaching route and its theory discussion.'),
    content('COURSE RECAP / CURATION, AUTHORSHIP AND RESPONSIBILITY', 'Week 11 papers', [
        paper('Verbeek (2015)', 'Beyond Interaction: A Short Introduction to Mediation Theory', week11.REFS['V'][1]),
        paper('Doshi & Hauser (2024)', 'Generative AI Enhances Individual Creativity but Reduces the Collective Diversity of Novel Content', week11.REFS['D'][1]),
        paper('Gebru et al. (2021)', 'Datasheets for Datasets', week11.REFS['G'][1]),
        paper('Naqvi, He & Kaur (2025)', 'Catalyst for Creativity or a Hollow Trend?: A Cross-Level Perspective on The Role of Generative AI in Design', week11.REFS['N'][1]),
        paper('Joshi & Vogel (2026)', 'Interaction Techniques that Encourage Longer Prompts Can Improve Psychological Ownership when Writing with AI', week11.REFS['J'][1]),
        paper('U.S. Copyright Office (2025 report)', 'Copyright and Artificial Intelligence, Part 2: Copyrightability', week11.REFS['U'][1]),
    ], body_size=30,
        notes='Brief reference within the recap. Verbeek and Gebru recur from Week 9. The U.S. Copyright Office entry is the policy report discussed in the lesson.'),
    recap(week11, 15,
          'Follow the contribution map across generation, selection, revision and approval. Ask who decides at each point and who responds when the finished work causes a problem.'),
    recap(week11, 16,
          'Feeling that something is yours, contributing work, having permission and holding a legal right are separate questions. Use them to open the ethical discussion. Ask what the team would credit, what it should clear first, and who is answerable for release.'),
    cards('12:07-12:13 / THE DESIGNER\'S ROLE', 'Designers as curators', [
        ('OUTPUTS', 'What makes the cut?',
         'Choose what fits the brief. Be able to explain why you kept, edited or rejected a result.'),
        ('TRAINING DATA', 'Whose work shapes it?',
         'Look at whose work and whose perspective the examples represent. Check permissions and gaps.'),
        ('HUMAN OVERSIGHT', 'Who has the last word?',
         'Decide where an agent can act and when a person must review, intervene or stop it.'),
    ], text_size=34,
        notes='Adapted from the 2025 Week 12 recap, pp. 60-63. Discuss how curation happens before generation, at selection and at release. Ask each pair which of the three choices they would need to defend on their own project. Earlier example: https://' + SITE + '/week11/#/8'),
    two_col('12:13-12:19 / PROMPTS, RULES AND ACTIONS', 'Language as an interface', [
        'A phrase can specify a rule, as in a geometry instruction.',
        'A description can steer a model toward a range of possible stories or images.',
        'A music brief can do both. Fix the tempo and leave the arrangement open.',
    ], [
        'When the prompt can trigger an action, what is left implicit?',
        'What should the interface show before a person lets the agent act?',
        source(4, 28, 'Week 4 / The model requests, the harness executes'),
    ], left_size=34, right_size=33, right_font='body',
        notes='Adapted from the 2025 Week 12 recap, pp. 55-59. Ask whether using language to reach a concept, a picture or an action changes what we think to ask for. Ihde treats language as bound up with how people interpret and make meaning. Use the two circles or music example to show that the same wording can specify a rule or invite an interpretation, depending on the system.'),
    content('12:19-12:25 / CONTRIBUTION AND CREDIT', 'Fractional authorship', [
        'A team makes a poster with AI. Who shaped the idea, made the source material, selected the image, or edited the final composition?',
        'Credit each contribution you can identify and describe what the model did. What should you disclose if the origins of training material are unclear?',
        'Ask separately who gave permission to use the material and who holds rights in the finished work.',
        source(11, 15, 'Week 11 / Trace four different decisions'),
    ], body_size=38,
        notes='Adapted from the authorship and ownership questions in the 2025 Week 12 recap, pp. 64-66. Fractional authorship is a discussion lens for creative contributions at different stages. It does not assign percentages, establish who owns copyright or grant permission. Ask students to describe a fair credit line for their chosen workflow.'),
    content('12:25-12:27 / SYNTHESIS', 'What answer would you give Lovelace now?', [
        'One responsibility you will carry into your work.',
        'One skill you will keep practising.',
        'One question you still want to answer.',
    ], body_size=44,
        notes='Invite short spoken answers. Return to what was specified, what was learned and who decided. Use two minutes, then advance to the AMA. The archive slide is available if you need to jump back to an example.'),
    two_col('COURSE ARCHIVE', 'Earlier slides', [
        source(1, 24, 'Week 1 / Lovelace and the opening question'),
        source(2, 55, 'Week 2 / Rules and specifications'),
        source(3, 20, 'Week 3 / Learning from examples'),
        source(4, 13, 'Week 4 / Language models'),
        source(5, 4, 'Week 5 / Technological mediation'),
    ], [
        source(6, 22, 'Week 6 / Sound and representations'),
        source(7, 11, 'Week 7 / Midterm recap'),
        source(8, 56, 'Week 8 / AI in the design process'),
        source(9, 16, 'Week 9 / Recommendation and feedback'),
        source(11, 16, 'Week 11 / Credit and responsibility'),
    ], left_size=34, right_size=33, right_font='body',
        notes='Optional reference slide. Links open the exact slide in the published earlier deck.'),
    content('12:27-12:30 / ASK ME ANYTHING', 'Course AMA', [
        'Submit a short question about the course in ClassPoint.',
        'A confusing concept, a case we discussed, or an ethical question you are still thinking about.',
    ], body_size=40, cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
        notes='Open the ClassPoint short-answer activity. Spoken questions are welcome. Use the preceding archive slide if an earlier diagram helps answer one. Close submissions and stop at 12:30 for ESFQ.'),
    statement('ESFQ', '12:30 / STUDENT FEEDBACK',
              notes='12:30 HKT. Pause teaching. Leave this slide up for the whole ESFQ. Move to the board only once ESFQ finishes.'),
    content('AFTER ESFQ / POSTER FAIR', 'Claim your poster-fair space', [
        board,
        'One editor per group finds the exact group name and adds the project title.',
        'Add a draft poster or placeholder. Landscape and portrait both work.',
        'Add viewing links for the video and mediation brief when available.',
        'Ask another group to find your space and open the links. Submit the final work in Canvas.',
    ], body_size=38,
        notes='Begin after ESFQ. The board has 26 named spaces. Demonstrate zoom, pan and locating a group. For a PDF poster, put an image preview on the board and link to a full-resolution copy students can view. Check permissions from another group’s account. Keep the room edit link in the class channel. A final poster is not required for this setup.'),
    content('GROUP PROJECT / ASK ME ANYTHING', 'Group project AMA', [
        'Submit a short question about your group project in ClassPoint.',
        'Ask about your design or evidence, the poster, video, mediation brief, Excalidraw, or Canvas.',
    ], body_size=40, cp={'type': 'short_answer', 'hide_names': False, 'multiple': True},
        notes='Open the ClassPoint short-answer activity once groups have tried their spaces. Spoken questions are welcome. Clarify requirements using the current project brief and Canvas. Close submissions once the AMA finishes.'),
]

DECK = dict(title='SD2112 / AI in Design / Week 12', slides=finalize(S, footer(12)),
            pdf='SD2112-week12.pdf', presenter_start_slide=1)
