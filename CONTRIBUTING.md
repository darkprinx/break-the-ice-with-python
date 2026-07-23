# Contributing

Thanks for wanting to add a solution or fix something! This repo gets a lot of
first-time contributions, so here's a quick guide to keep things smooth for
everyone.

## Finding the right file

Every question lives in a `Status/Day_XX.md` file (Day 1–9 are named
`Day 1.md`, `Day 2.md`, ... with a space; Day 10 onward are named
`Day_10.md`, `Day_11.md`, ... with an underscore — that's just a historical
inconsistency, not a mistake). The [README's Practice Status
table](README.md) maps question numbers to the day file that contains them.

Most days also have a matching notebook in `notebooks/Day_XX.ipynb` with the
same content in Jupyter form. If you're adding a solution, please add it to
**both** the `Status/*.md` file and the matching notebook where one exists,
so they don't drift apart.

## Adding an alternate solution

Find the question's section in the day file, and add a new fenced code block
right after the existing solutions for that question (before the `---`
separator), following the pattern already used in the file:

```python
'''Solution by: your-github-username
'''
<your code>
```

A few things that keep solutions easy to read and merge cleanly:

- **Close every code fence.** An unclosed ` ```python ` block swallows
  everything after it in the file — including the day-navigation links at
  the bottom — into a code block. Before opening a PR, preview the rendered
  Markdown (or just double check your diff has a closing ` ``` ` for every
  opening one) to make sure the fence balances.
- **Only put code inside the fence.** Markdown headings, `---` separators,
  or prose don't belong inside a ` ```python ` block — they'll render as
  literal text and can make the block invalid Python.
- **Make sure the code actually runs as pasted.** Watch out for stray
  leading whitespace (accidental indentation from your editor) and remember
  to print/return the result — a solution that computes an answer but never
  prints it won't show anything when someone runs it.
- **Add alongside, don't replace**, unless you're specifically fixing a bug
  in an existing solution. If you *are* fixing a bug, please explain what
  was wrong in the PR description.
- **Keep notebook diffs small.** Jupyter tends to rewrite `execution_count`,
  cell outputs, and kernel metadata (Python version, `display_name`) on
  every save even when you didn't touch that cell. Where you can, avoid
  committing metadata/version bumps that aren't related to your change —
  they make diffs noisier and unrelated to review.
- **One topic per PR.** A PR that touches a single question (or a single
  day) is much easier to review and merge than one that reshapes many days
  at once. If you have several unrelated additions, separate PRs are
  welcome.

## Reporting a bug in an existing solution

Please open an issue (or better, a PR with the fix) that includes:

- Which day/question is affected
- What input you tested with
- What output you got vs. what you expected

## Submitting a PR

1. Fork the repo and create a branch for your change.
2. Make your edit(s) following the guidelines above.
3. Open a PR describing what you added or fixed.

If you don't have push access to create a branch on your own fork for some
reason, opening an issue with your solution pasted in is a fine fallback —
a maintainer can fold it in.

## Code style

This is a beginner-friendly exercise repo, not a production codebase — clear
and correct beats clever. There's no enforced linter; just try to match the
style of the surrounding solutions in the file you're editing.
