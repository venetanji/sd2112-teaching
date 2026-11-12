"""Week-owned bridge: selective learning, mediation and reflective use."""
from deckgen.layouts import content, cards, two_col, section

MITCHELL = 'https://www.cs.cmu.edu/~tom/pubs/NeedForBias_1980.pdf'
VERBEEK = 'https://doi.org/10.1145/2751314'
EEDE = 'https://doi.org/10.1007/s10699-010-9190-y'


def bias_distinction():
    return cards('BIAS / ONE WORD, DIFFERENT CLAIMS', 'Learning is selective. Is it unfair?', [
        ('INDUCTIVE BIAS', 'Assumptions enable learning.', 'A model needs a basis for generalizing beyond the examples it has seen.'),
        ('LEARNED PATTERN', 'A regularity is not a verdict.', 'Selected data and objectives shape what is learned. A repeated pattern is not automatically an error.'),
        ('HARMFUL BIAS', 'Consequences need scrutiny.', 'A pattern can stereotype, exclude or burden people. Who is affected, in which task, and with what evidence?'),
    ], text_size=30, notes='About two minutes within 25-45. Treat everything a network learns is bias as a provocation, not a technical definition. Distinguish inductive bias, learned regularity and social unfairness. Statistical bias is another sense: a systematic deviation relative to a specified target or estimator, not a synonym for all three. Mitchell (1980), The Need for Biases in Learning Generalizations, sections 1-4 and conclusion, defines the basis for preferring generalizations beyond consistency with examples. Application to neural architecture, representation, objective and optimization is our extension. Necessary selectivity does not excuse preventable discrimination. A model is not a complete or neutral picture of humanity. The source is linked on the reference shelf.')


def mediation_slides():
    return [
        section('03 / 45-60 / TECHNOLOGICAL MEDIATION', 'Not just a mirror.',
            'How a technology shapes what we notice, judge and do.', bg='#246E70',
            notes='Ten-second transition inside the fifteen-minute philosophy block. The previous audit showed unequal errors, not their complete cause. Now ask a different question: how does an apparently useful tool organize the relation between a person and the world? Bridge the established Heidegger, Ihde and Verbeek course material to Van Den Eede on transparency. This is a philosophical framework and design interpretation, not another causal experiment or proof that reflective use improves fairness.'),
        content('FROM LEARNING TO MEDIATION', 'Whose humanity does AI reflect?', [
            'Data contains traces of people - not all people equally.',
            'Collection, labels and objectives select what counts.',
            'Outputs can reproduce, transform or amplify those patterns.',
            'Our responses can become the next inputs. The mirror acts back.',
        ], body_size=36, notes='About two minutes. Preserve reflection of humanity as a provocation, but reject merely as a complete account. Training can also use synthetic data, simulations and physical measurements; even human-created corpora do not represent humanity equally. Institutions and designers select representations, labels, objectives, interface defaults and deployment contexts. A model learns transformations, not a census of human values. The final sentence is an instructor metaphor for mediation and possible feedback, not a claim that every system retrains online or increases harm. The next empirical block provides bounded evidence that some interactions change people. In Lion\'s storefront study, section 5.3, a repeated dark centre prompted reflection on how shops had been selected and photographed; a situated example of learned regularity, not by itself proof of discrimination.'),
        cards('RECALL / HEIDEGGER -> IHDE -> VERBEEK', 'Using a tool also shapes our experience.', [
            ('HEIDEGGER', 'The tool can recede.', 'In absorbed use, attention goes to the task rather than the equipment that makes it possible.'),
            ('IHDE', 'Experience is mediated.', 'A technology can amplify some aspects of the world while reducing others.'),
            ('VERBEEK', 'Actions are mediated too.', 'Design helps shape what we notice, choose and take responsibility for.'),
        ], text_size=31, notes='About three minutes; a teaching bridge, not identical theories. Heidegger: ready-to-hand equipment can withdraw from focal attention in absorbed practical involvement; breakdown can bring it to attention, but deliberate reflection need not require failure. Do not conflate this with later enframing or attribute the transparency vocabulary as his literal terminology. Underlying source: Being and Time sections 15-16, interpretation checked through Van Den Eede section 2.1, printed pp.142-144. Ihde: amplification/reduction and human-technology-world relations; established course framework checked through Van Den Eede pp.148-150 and Verbeek pp.28-29. Neither original book was newly read. Verbeek p.31 connects mediation to design and responsibility, not determinism. Use the fictional ranked-workshop example: order makes some opportunities visible while others go unencountered.'),
        two_col('INTRODUCING / YONI VAN DEN EEDE / 2011',
            'Transparent in which sense?', [
                'IN USE: does the tool recede while I focus on the task?',
                'A smooth feed can make its selection easy to overlook.',
                'Unnoticed does not mean neutral.',
            ], ['IN REFLECTION: can I notice how the relation is shaped?',
                'Question the choices, social context and effects behind the interface.',
                'Model explainability is one resource, not the whole context.',
                'Double vision: use the tool and examine its mediation.'],
            right_font='body', left_size=34, right_size=32,
            notes='About four minutes. Yoni Van Den Eede, In Between Us: On the Transparency and Opacity of Technological Mediation, Foundations of Science 16 (2011), 139-159; published online 2010. Section 2.4 pp.148-150 explains relations/degrees of transparency; section 3 pp.154-156 distinguishes use/context and what becomes focal or invisible. Referents matter: do not translate contextual transparency directly into visible model internals or a single transparency slider. His closing remarks p.157 propose double vision and self-reflexivity. The two on-slide questions paraphrase this tension; they are not quotations or a validated UI metric. Explainability can support reflection but does not disclose the whole social context or establish trustworthiness. Making mediation noticeable can interrupt fluent use. Do not present the historical course\'s rule/data notation or transparent alterity as his own category.'),
        cards('REFLECTIVE USE / SAME SYSTEM, A DIFFERENT RELATION', 'Pause. Compare. Choose differently.', [
            ('ABSORBED USE', 'Accept the top result.', 'The ranked list can feel like the available world. Its selection stays in the background.'),
            ('REFLECTIVE USE', 'Notice the selection.', 'Ask why it appears, compare an alternative, and check whose needs are missing.'),
            ('CHANGED INTERACTION', 'Act on the difference.', 'Correct a constraint, change the ordering, browse beyond it or refuse the suggestion.'),
        ], text_size=31, notes='About five minutes including a short spoken comparison, within 45-60. Instructor design synthesis informed by Van Den Eede pp.154-157 and Verbeek p.31, not a validated intervention from either paper. In a fictional workshop finder, a person notices that prior clicks stand in for suitability, compares browse-all, and edits an access constraint. This can change attention, interpretation and action without retraining the model. Reflection is insufficient if the product offers no meaningful response or accessible alternative. More information or friction is not automatically better; it can overwhelm people or shift responsibility onto those already disadvantaged. Ask what changed in the relation and what did not. Next ask when interactions can change later human judgement.'),
    ]


def philosophy_reference():
    return content('NON-ASSIGNED / REFERENCE SHELF / LEARNING + MEDIATION', 'Read the distinctions in context.', [
        f'[Mitchell (1980) / The Need for Biases in Learning Generalizations]({MITCHELL})',
        'Heidegger: Being and Time, sections 15-16. Ihde: Technology and the Lifeworld (1990).',
        f'[Verbeek (2015) / Beyond Interaction]({VERBEEK})',
        f'[Van Den Eede (2011) / In Between Us]({EEDE})',
    ], body_size=32, notes='Non-assigned reference shelf; no extra lecture minutes or homework. Mitchell (1980): main argument read; inductive bias does not mean every learned weight is prejudice. Heidegger and Ihde are recalled through the established course framework and the mediation articles, not claimed as fresh full-book reads. Verbeek: Interactions 22(3), 26-31, especially pp.28-29 and 31. Van Den Eede: Foundations of Science 16, 139-159, especially pp.148-150 and 154-157, online publication 2010/issue 2011. Source access is recorded in the evidence ledger. The fictional workshop example is an instructor application, not an empirical intervention from these texts.')
