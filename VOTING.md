# ORCA Project Application Voting

How the TSC votes on project applications. Votes are held with
[GitVote](https://github.com/cncf/gitvote) on the application issue.

> Placeholder handles below are from the example roster. Regenerate the
> command table with `python3 generate_gitvote_config.py --table` after any
> roster change and paste the result in.

## For the vote chair

### 1. Collect conflict-of-interest declarations

**Before** opening the vote. Once a vote is created, GitVote locks in the
configuration as it existed at that moment — the binding voter list cannot be
changed afterward. Hence, record the conflicts as a comment on the application issue before the voting starts.

### 2. Open the vote with the matching command

Post the command on a line by itself as a comment on the application issue.
GitVote only reads commands in newly created comments — editing a comment to
add the command does nothing.

| Conflicted members | Command | Binding voters |
| --- | --- | --- |
| none | `/vote` | 5 |
| balexios | `/vote-recusedBalexios` | 4 |
| cherishlxy | `/vote-recusedCherishlxy` | 4 |
| deadly-platypus | `/vote-recusedDeadlyplatypus` | 4 |
| gricart | `/vote-recusedGricart` | 4 |
| JustinCappos | `/vote-recusedJustinCappos` | 4 |
| balexios, cherishlxy | `/vote-recusedBalexiosCherishlxy` | 3 |
| balexios, deadly-platypus | `/vote-recusedBalexiosDeadlyplatypus` | 3 |
| balexios, gricart | `/vote-recusedBalexiosGricart` | 3 |
| balexios, JustinCappos | `/vote-recusedBalexiosJustinCappos` | 3 |
| cherishlxy, deadly-platypus | `/vote-recusedCherishlxyDeadlyplatypus` | 3 |
| cherishlxy, gricart | `/vote-recusedCherishlxyGricart` | 3 |
| cherishlxy, JustinCappos | `/vote-recusedCherishlxyJustinCappos` | 3 |
| deadly-platypus, gricart | `/vote-recusedDeadlyplatypusGricart` | 3 |
| deadly-platypus, JustinCappos | `/vote-recusedDeadlyplatypusJustinCappos` | 3 |
| gricart, JustinCappos | `/vote-recusedGricartJustinCappos` | 3 |



Names in the command are alphabetical: `/vote-recused-balexios-cherishlxy` exists,
`/vote-recused-cherishlxy-balexios` does not.

**Three or more conflicted members:** no profile exists. This would leave
fewer than three binding voters, so the vote cannot proceed as normal.

### 3. Verify the bot comment

GitVote replies with the vote details. Confirm the binding voter list matches
the intended one before letting voting proceed. If it is wrong, close the vote
with `/cancel-vote` and start again.

## For everyone voting

React to the **GitVote bot comment**, not the application issue:

| In favor | Against |
| --- | --- |
| 👍 | 👎 |

Reacting with both voids your vote.

### Not voting counts as a vote against

Only 👍 advances an application. A binding voter who does not react has the same effect on the outcome as one who reacts 👎. The threshold is a percentage of *all binding voters*, not of votes cast.

### About the 👀 reaction

The GitVote bot's own comment will offer 👀 as an "abstain" option. Under ORCA's
rule it has exactly the same effect on the result as 👎 or as silence. GitVote records and reports it separately, but it changes nothing.

Ignore it. If you have read an application and do not support it, react 👎.

**Non-binding votes are welcome.** ORCA members and the wider community are
encouraged to react to show support. These are recorded and reported
separately and do not affect the outcome.

**Recused members must not react at all.** GitVote has no concept of recusal —
it would count a recused member's reaction toward the non-binding tally, which
publicly signals a position on an application you are conflicted on. Abstain by
not reacting.

**Voting is public.** GitHub reactions are attributed to your account and
anyone can see who reacted. There is no secret ballot. The full history is
published at `gitvote.com/audit/OWNER/REPO`.

## Thresholds

A vote passes when in-favor reactions reach **66.66%** of binding voters. The
percentage is calculated against the number of *allowed voters*, not the number
who actually voted — so a binding voter who never reacts effectively counts
against passage. Recused members are excluded from the denominator entirely.

Votes stay open for **2 weeks** with a status check every 5 days.

---

## Maintaining the roster

`tsc.yml` is the single source of truth. `.gitvote.yml` is generated from it —
**never edit `.gitvote.yml` by hand.**

When TSC membership changes:

```bash
# 1. Edit the members list (GitHub handles, not display names)
vim tsc.yml

# 2. Regenerate
python3 -m pip install pyyaml     # first time only
python3 generate_gitvote_config.py

# 3. Commit both files together
git add tsc.yml .gitvote.yml
git commit -m "Update TSC roster for <year>"

# 4. Update the command table in this file
python3 generate_gitvote_config.py --table
```

CI runs `generate_gitvote_config.py --check` on any PR touching these files and
fails if `.gitvote.yml` is out of date.

### Settings

Adjust in the `settings:` block of `tsc.yml`, then regenerate:

- `pass_threshold` — 51 for strict majority, 66 for two-thirds. Both behave
  correctly at every roster size.
- `max_recusals` — how many simultaneous conflicts get a profile. Raising this
  grows the file combinatorially.
- `min_binding_voters` — refuses to generate a profile leaving fewer binding
  voters than this.

### Handle changes

If a member changes their GitHub handle, the config silently stops matching
them: they become a non-binding voter while still counting in the denominator,
making the vote harder to pass. Re-verify handles whenever membership rotates.
