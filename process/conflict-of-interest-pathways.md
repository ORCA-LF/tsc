# ORCA — Conflict of Interest: Development Pathways

This document is a companion to [Conflict of Interest Guidance for Research Projects](./conflict-of-interest-guidance.md) and describes the two development pathways available to research projects hosted on ORCA.

## 1. Guiding principle: developer choice

ORCA recognizes that the right balance between openness and confidentiality depends on the project, the venue, and the authors' goals. Accordingly, **the choice of development pathway belongs to the project's developers**, not the Foundation. ORCA's role is to make the trade-offs of each pathway clear, to provide guidance that protects both the developer's publication and the integrity of the Foundation's decisions, and to handle conflicts consistently when they arise.

Foundation acceptance of a project is a governance and maturity decision. It is **not** an academic publication and does not by itself constitute prior or concurrent publication of an associated paper. This separation holds regardless of which pathway a developer chooses.

## 2. The two development pathways

### 2.1 The Closed Pathway — Closed development until paper acceptance

The project is developed privately and is opened (repositories made public, announcement, promotion) only after the paper has been accepted or the venue's review is complete.

**What it protects.** Strong protection of double-anonymous review: there is no public artifact to de-anonymize the authors, and no Foundation announcement that could compromise the submission.

**Trade-offs.** Defers the open-source benefits ORCA exists to enable — public collaboration, external contribution, early adoption, and community building. Some venues now run *artifact evaluation* and expect public artifacts, so a fully closed approach may need to be reconciled with the target venue's artifact track.

**Developer obligations under this pathway.**
- Disclose to the TSC at intake that development is proceeding privately pending a submission, including the target venue and expected notification window.
- Coordinate the timing of opening/announcing the project with the venue's notification schedule.
- Confirm the closed-then-open plan is compatible with the venue's publication and anonymity rules.

### 2.2 The Open Pathway — Open development from the beginning

The project is public from the start, with development, repositories, and history visible throughout — including while the paper is under review.

**What it protects.** Fully realizes ORCA's open-source mission: open collaboration, transparency, external contribution, and early adoption from day one.

**Trade-offs.** Creates real COI and anonymity exposure. Authors should not self identify as maintainers fo the project or similar as this may de-anonymize a paper under double-anonymous review and risk desk rejection. Instead authors should talk about contributing work to an ORCA project. It also means anyone who has seen the project (including ORCA reviewers) may be able to identify the authors — which has downstream consequences for who may review the paper at its venue (see [Conflict of Interest Guidance for Research Projects, §5](./conflict-of-interest-guidance.md#5-area-of-concern-2--handling-coi-when-it-happens)).

**Developer obligations under this pathway.**
- Disclose at intake that an associated paper is or will be under submission, with venue and review window.
- Confirm that open development is compatible with the target venue's anonymity and dual-submission rules *before* relying on it. However, note that this is allowed under ACM, IEEE, and USENIX Guidelines, so should be applicable to most computer science academic venues.
- Optionally request a **quiet period**: ORCA withholds author-identifying promotion (blog posts, press, social) until after notification, even while the code stays public. ORCA grants this by default on request where a double-anonymous venue is involved.

### 2.3 Neither pathway is mandated

Per the consensus, ORCA presents both pathways with their trade-offs and lets the developer choose.
