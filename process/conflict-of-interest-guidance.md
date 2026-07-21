# ORCA — Conflict of Interest Guidance for Research Projects

## 1. Purpose

ORCA hosts projects that are frequently tied to ongoing academic research, where an associated paper may be under peer review at a venue such as ACM, IEEE, or USENIX. This creates a tension between two cultures: open-source development is public by default, while academic peer review is confidential and often anonymous. This document records the consensus reached by the TSC on how ORCA should approach conflicts of interest (COI) for such projects.

## 2. Guiding principle: developer choice

ORCA recognizes that the right balance between openness and confidentiality depends on the project, the venue, and the authors' goals. Accordingly, **the choice of development pathway belongs to the project's developers**, not the Foundation. ORCA's role is to make the trade-offs of each pathway clear, to provide guidance that protects both the developer's publication and the integrity of the Foundation's decisions, and to handle conflicts consistently when they arise.

Foundation acceptance of a project is a governance and maturity decision. It is **not** an academic publication and does not by itself constitute prior or concurrent publication of an associated paper. This separation holds regardless of which pathway a developer chooses.

## 3. The two development pathways

ORCA offers developers a choice between a Closed Pathway (private development until paper acceptance) and an Open Pathway (public development from the start), each with its own protections, trade-offs, and developer obligations. See [Conflict of Interest: Development Pathways](./conflict-of-interest-pathways.md) for the full description of both pathways, and confirmation that neither is mandated.

## 4. Area of concern 1 — Avoiding COI in the first place

Measures that reduce the chance a conflict ever materializes:

- **Disclosure at intake (both pathways).** Every research project discloses, at submission to ORCA, whether a paper is under or headed to review, the venue, the review window, and the review model (single-anonymous / double-anonymous / open). This lets the TSC sequence public steps and assign reviewers cleanly.
- **Confidentiality of evaluation materials.** TSC deliberations on a project with a paper under submission are confidential until the project is public.
- **Timing controls.** For closed pathway, coordinate opening with notification; for open pathway, offer the quiet period to protect anonymity without abandoning openness.
- **Author responsibility for venue compatibility.** Venue rules differ and change between editions; the developer confirms compatibility and flags conflicts to the TSC before public steps are taken.
- **Clean reviewer assignment.** When assigning the TSC member(s) who will shepherd a project, ORCA proactively avoids assigning anyone with a conflict (see §5.2), rather than discovering it later.

## 5. Area of concern 2 — Handling COI when it happens

### 5.1 General standard

A conflict exists where a member's objective judgment is — or would be perceived by a reasonable observer to be — compromised by a relationship to the work or its authors. This covers conflicts that are *actual, perceived, or potential*. Members err toward declaring. Self-assessment ("I can be objective") is not a sufficient safeguard; **disclosure and recusal are the operative controls.**

### 5.2 Within the TSC (the Foundation's decision on a project)

- **Affirmative duty to disclose.** Every TSC member assesses and discloses any conflict with a project before its review. The duty is per-project and recurs for each project — a member clean on one may be conflicted on another. Members may keep standing disclosures of affiliations and funding on file so only project-specific conflicts need fresh declaration.
- **Abstain and cite.** A conflicted member abstains from the vote and explicitly states the conflict.
- **Reassign the sponsor.** If the member who would shepherd the project is conflicted, an unconflicted TSC member is assigned as sponsor instead.
- **Quorum from the clean members.** Decisions proceed by majority of non-conflicted members; the TSC confirms a non-conflicted quorum under ORCA's bylaws.
- **Document.** Each recusal is recorded in the minutes, naming the member and the nature of the conflict.

### 5.3 Cross-venue case (TSC member who is also a paper reviewer / PC member)

A particularly important case for ORCA: a TSC member may also sit on the program committee of the venue where a project's paper is submitted. Such a member is **conflicted as a reviewer of that paper** and should declare the conflict to the program chairs and recuse. Three independent grounds support this:

1. **De-anonymization** — having evaluated the ORCA project, the member can identify the authors (USENIX lists exactly this: anyone who can identify the authors from previous exposure to the work).
2. **Institutional stake** — ORCA has an interest in an admitted project's success, creating at least a perceived conflict.
3. **Non-public information** — the member may hold information other reviewers lack.

The program chairs make the final determination on the recusal; the member does not self-judge it as acceptable. **Symmetrically**, a TSC member who is a reviewer or PC member for a project's paper is also conflicted in ORCA's decision on that project and recuses under §5.2. This keeps the two review systems from contaminating each other in either direction.


## 6. References

These sources informed the COI standards and the foundation-governance mechanics above. Conference URLs are edition-specific and revised each cycle; verify against the current edition and record an access date when adopting. For CNCF, prefer the primary GitHub repositories over third-party summaries.

- **ACM Conflict of Interest Policy** — https://www.acm.org/publications/policies/conflict-of-interest — "reasonable observer" standard; PC member as covered evaluator; recusal from deliberation.
- **ACM Peer Review Policy** — https://www.acm.org/publications/policies/peer-review — review free of personal/professional conflicts; reviewer confidentiality.
- **IEEE Submission and Peer Review Policies** — https://journals.ieeeauthorcenter.ieee.org/become-an-ieee-journal-author/publishing-ethics/guidelines-and-policies/submission-and-peer-review-policies/ — reviewers/editors recuse; conflicts actual, perceived, or potential.
- **USENIX Security Call for Papers (current edition)** — https://www.usenix.org/conference/usenixsecurity26/call-for-papers — conflict includes anyone who can identify the authors from prior exposure; chairs may strike illegitimate conflicts.
- **USENIX Security Submission Policies (prior edition)** — https://www.usenix.org/conference/usenixsecurity24/submission-policies-and-instructions — conflicted PC members excluded from evaluation and discussion by default.
- **CNCF TOC process** — https://github.com/cncf/toc — sponsored Due Diligence, public comment, TOC vote; abstain-and-cite; reassign unconflicted sponsor.
- **CNCF Code of Conduct incident-resolution procedures** — https://github.com/cncf/foundation/blob/main/code-of-conduct/coc-incident-resolution-procedures.md — soft-conflict (no vote, may discuss); non-conflicted quorum and majority.
- **CNCF project lifecycle / Due Diligence** — https://contribute.cncf.io/projects/lifecycle/ — TOC Due Diligence and moving-levels process.
- **OpenSSF project lifecycle** — https://github.com/ossf/tac/blob/main/process/project-lifecycle.md — TAC approves projects and progression; Working Groups recommend to the TAC; LF license/IP due diligence.

