# Combining weekly teaching drafts

Weekly PRs are deliberately independent. An individually green or mergeable PR
is not proof that the complete sequence is integrated. This document does not
authorize merging or publication.

When integration is explicitly approved:

1. Preserve the union of all accepted weekly entry points in `deckgen.toml`.
   Do not resolve the shared `course.decks` line with an entire “ours” or “theirs”
   replacement. Include separately accepted earlier weeks, including Week 7.
2. Preserve all accepted navigation links and site cards where the course uses
   them. Do not register a week whose source has not been brought into the branch.
3. Run `python scripts/check_deck_registration.py`. It rejects missing sources,
   duplicate entries and weekly source files lost from the registration list.
4. Run `python -m unittest discover -s tests -v`, plus
   `python tests/exercises.test.py` when that file exists.
5. Run an unfiltered `deckgen build` with the pinned requirements and a supported
   Chromium setup. Inspect the full combined site, PDF and both PPTX exports,
   student/staff boundaries, navigation, notes, fonts and actual classroom tools.

PR CI runs the full repository suite and builds affected registered weeks with
HTML, PDF, plain/ClassPoint PPTX and preview artifacts. It follows local Python
imports for changed deck helpers; shared assets/site/toolchain changes or an
unknown-only change fall back to all registered decks. All entry-point
registrations are validated on every run. The selected list is retained in the
artifact. This does not claim exhaustive dynamic-import analysis or replace the
unfiltered integration build above.

The workflow is read-only (`contents: read`), has no deployment or publishing
step, and does not request secrets. Ubuntu 24.04, Python 3.12, Node 22 and
Playwright 1.56.1 avoid the unsupported Ubuntu 26.04 browser setup. The existing
Deckgen version remains pinned by `requirements.txt`.

A successful build checks export generation and slide counts; it does not prove
visual quality, source accuracy, classroom PowerPoint/ClassPoint compatibility,
physical room access, or assessment-platform readiness.
