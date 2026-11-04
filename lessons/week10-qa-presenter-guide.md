# Week 10: audience Q&A for the four TAs

Separate four-slide deck: Nicolò Azzolin, Amber, WU Zhao and MA Jie, one native
ClassPoint Short Answer collection each. File order is **not an agreed speaking
order**. Move the relevant Q&A slide after each actual presentation, or switch to
it in this separate deck. No presentation topics, allocations or extra time are
assigned here.

## Participation contract

Audience participation is optional and not graded. One question per response;
multiple submissions are enabled so a person can ask another question. Names are
not hidden by the generated activity: do not promise anonymity. Keep questions
about the presentation, not private information. Read/moderate responses before
projecting them; select relevant questions without awarding stars or grades.

## Before class: PowerPoint and add-in smoke test

1. Use the **`week10_qa-classpoint.pptx`** export, not the plain PowerPoint, PDF or
   HTML. Open in the classroom's supported desktop PowerPoint with ClassPoint
   installed and signed in; confirm the course's Inter/JetBrains Mono fonts.
2. Start Slide Show and the actual ClassPoint presenter session. Display or
   announce its **current live class code**. Do not invent a code, reuse a code
   from an earlier class, or treat any static image as a running session.
3. Scan a slide's QR on a second device. It opens the generic student join page
   at **https://www.classpoint.app/**; enter the live code from step 2 and join.
   The same generic QR is intentionally on all four slides. It neither embeds a
   session code nor starts an activity. The printed URL is the fallback.
4. On each TA's slide, click the real **Short Answer** ClassPoint button in Slide
   Show, check its speaker label, and send two harmless test questions from the
   second device. Confirm both reach the correct collection, multiple responses
   work, names behave as expected, and there is no quiz/grading requirement.
   Native metadata has quiz mode off, no grading instructions, multiple answers
   on and hidden names off. Do not enable scoring or award stars manually.
5. Close collection before moving to the next speaker. Use ClassPoint's supported
   fresh-run/reset workflow to remove the test responses before students join;
   verify the audience starts with empty collections. If the add-in/session is
   unavailable, take spoken questions instead: the generic QR, plain PPTX, HTML
   and PDF cannot collect answers by themselves.

The pinned Deckgen v0.11.2 source was inspected at both native boundaries:
`classpoint.activity()` emits ShortAnswerActivity / ActivityType 1, and the native
builder attaches `ACTIVITYMODEL` tags to `btnInknoeActivityCp2` picture buttons.
Its ait4x master/template adds course chrome and layouts, **not a dynamic join QR
or live code**. ClassPoint itself may expose session joining controls at runtime;
verify them on the actual classroom installation. No actual presenter session or
end-to-end audience submission was available during source QA.

## Generic QR provenance

Verified 4 November 2026: `https://www.classpoint.app/` returned HTTP 200 with the
title **ClassPoint App | Join class**. The official join-page search result says
students join using a class code. The locally generated, course-owned PNG has a
four-module quiet zone and was independently decoded with ZXing-C++ to that exact
HTTPS URL. It contains no fabricated live session or activity identifier. This is
a generic page check, not proof that a future presenter session is running.

## After class: reports and reordering

`deck/week10_qa.py` calls `attach_reports(S, REPORTS)` **before** `finalize`, with
its own future `deck/week10_qa-reports.json` (not Week 10's other activity map).
Missing/empty reports are a safe pre-class no-op. Do not create report links or
publish responses until actual activities exist and their content has been
reviewed. Standard public report links can expose participant names and answers.
Withhold any private/sensitive, hidden-name or unrun collection with an explicit
`activity: null` placeholder and its exact question title, rather than dropping it.
No responses, real activity IDs or student fixtures are supplied by this deck.

The mapping is positional. If you reorder the exported slides, reconcile the
actual runs back to the four exact **Questions for [TA name]** titles in source
order before attaching reports, or reorder the source and report map together.
Never attach chronological exports blindly after a speaking-order change. Count
and question-text drift must fail, including null/unrun entries. Native button
tags follow their actual slide relationships; tag numbers are not slide numbers.

## Local verification

Run `.venv/bin/python -m unittest discover -s tests -p test_week10_qa.py -v`.
The tests build throwaway native PowerPoints from the pinned generator and inspect
button/tag relationships, DTO settings, plain-export absence of activity tags,
QR placement/linking, HTML badges and synthetic report-loader drift. They do not
contact participant reports or substitute for the classroom smoke test.
