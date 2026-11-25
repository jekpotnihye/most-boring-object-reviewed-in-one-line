# Build notes — The Most Boring Object, Reviewed in One Line

Competition: The Most Boring Object, Reviewed in One Line
(`u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3`), $2 pool,
no entry fee (entryFeeUsd null, entryFeesUsd "0.00"), deadline
2026-11-26T17:25:00Z (27 Nov 2026, 00:25 WIB). Blind rounds: nothing is
judged on submit; rounds judge the field, the last at the deadline.

## The brief, in criterion order

From RULES.txt / competition.yaml, read first (judge brief published
in full). The judge is a comedy editor picking the review that is
funnier and truer about its boring object, weighing most important
first, lexicographically — the first criterion where two entries
differ decides unless a later one differs by much more:

1. Is a one-line review of a boring everyday object, funny and true:
   loses to any review on the subject.
2. Makes the judge laugh at a real, recognisable detail of the object
   rather than at a joke that would fit anything.
3. Is true: the observation matches how the object actually behaves,
   so the laugh arrives with recognition.
4. Stays inside one line and 200 characters, with every word earning
   its place.
5. Lands fast: the turn comes early and the last words sharpen it
   instead of trailing off.

"The best of these make the object's own dullness the joke. Length
for its own sake does not count." Gate: `/output/entry.txt` is UTF-8
text of 1 to 200 characters, not only whitespace. Ties break to the
smaller text (fewer bytes), then the earlier receipt — so short wins
ties. Competitor patterns applied: twist/sharpening in the last
word(s), go short (the cap is a ceiling), fresh/specific/true over
polished/generic, never reproduce house anchor texts (none were seen;
all lines here are original).

## Drafts considered and polish rounds

Four versions were built and run, each verified byte-for-byte. The
object had to be named in the line, the detail had to be true of that
object alone, and the last word had to sharpen the joke.

### v1 — Tea towel, first draft (103 chars)

> Five stars. This tea towel dries nothing, stays damp, and gets used as an oven glove anyway. Essential.

On-subject and true (tea towels famously stay damp and get grabbed
for hot pans), but wordy: "and gets used as ... anyway" spends words
without adding a detail, and "Essential." lands softly after it.

### Polish 1 — Paperclip angle (100 chars)

> Five stars. Held two pages together for a year, then got bent straight to open a SIM tray. Promoted.

A different boring object, with a very specific true detail: a
paperclip really does get straightened to eject a SIM tray, and
"Promoted." is a sharp last word. Rejected: the object is never
named — the reader must infer "paperclip" from the SIM detail — so
criterion 1 (a review *of* a boring object) is weaker than in the
versions that name their object outright.

### Polish 2 — Doorstop angle (105 chars)

> Five stars. This doorstop holds the door, gets kicked daily, and has never once asked for a raise. Loyal.

Names its object and "gets kicked daily" is a true, recognisable
detail. Rejected: it is the longest of the candidates, and the
"never asked for a raise / Loyal" payoff is an anthropomorphic
underappreciated-worker joke that would fit almost anything, which
criterion 2 punishes. The dullness is described, not made the joke.

### Polish 3 — Tea towel, tightened (94 chars) — FINAL

> Five stars: this tea towel dries nothing, stays damp, doubles as an oven glove. Indispensable.

Cut "and gets used as ... anyway" to "doubles as", dropped the
sentence break after "stars" for a colon so the review reads as one
rating followed by its evidence, and swapped "Essential." for
"Indispensable." — a longer, more absolute last word that sharpens
the irony: an object that fails its own job is declared
indispensable. Two true, object-specific details (dries nothing /
stays damp; grabbed as an oven glove), the turn comes early ("dries
nothing" contradicts the five stars at once), and the last word
lands the joke. Shortest of the strong candidates (94 vs 100/103/105).

### Polish 3b — "yet" variant, tried and rejected (98 chars)

> Five stars: this tea towel dries nothing, stays damp, yet doubles as an oven glove. Indispensable.

"Yet" adds 4 characters and no meaning: the bare list already carries
the irony, and the extra word slows the landing. The plain form from
Polish 3 stands as the final entry.

## Final entry

> Five stars: this tea towel dries nothing, stays damp, doubles as an oven glove. Indispensable.

94 characters. It is a review (five stars, named object), it is true
about tea towels, its laugh comes from two details no other object
shares, and its dullness — an object bad at its one job that nobody
would throw away — is the joke itself.

## Verification

`main.py` (Python standard library only) writes exactly the line above
to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default `/output`), with no
trailing newline. Verified 25 Nov 2026, runs with
`MAKEFUN_OUTPUT_DIR=output`:

- v1: 103 chars, sha256
  `5c1fdc50ad2fabf7329756a7b2c5f5c8516b8919704d65fd10cce5c4f6b6f89f`
- Polish 1 (paperclip): 100 chars, sha256
  `73836cf1a34f492e243fa2e16540393bd59b30109d490b7191b8f98f3016a8ff`
- Polish 2 (doorstop): 105 chars, sha256
  `8690fa0e15ec49ad216608aa6a5009f2d59d337c422cc38d1a151000e0aac130`
- Polish 3 (final): 94 chars, sha256
  `f1ef28ed9a2a74bafd3b2d3853d08d2595ece1316e56f14c417f137c17874ee3`
- Polish 3b ("yet"): 98 chars, sha256
  `158efed86729669a554b39285dd72d35b38ecfa18bc8142afdd4554e14e7ace0`
- Final re-run (after restoring Polish 3): 94 chars, same sha256
  `f1ef28ed9a2a74bafd3b2d3853d08d2595ece1316e56f14c417f137c17874ee3`;
  a second run to a different output directory produced byte-identical
  output (`cmp` clean).

Final gate check: 94 characters, 94 bytes, UTF-8 decodes cleanly, 0
newlines, not whitespace-only — inside the 1–200 character gate.
