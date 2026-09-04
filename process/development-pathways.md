# ORCA — Development Pathways

This document is meant to help academics working on open source to understand how to balance academic and open source project philosophies.  While there are many different ways to work inside a project, this document describes two reasonable but fundamentally opposed development pathways to best contrast the differences.  However, ORCA does not mandate any particular style of interaction as we first describe.

## 1. Guiding principle: developer choice

ORCA recognizes that the right balance between openness and confidentiality depends on the project, the venue where the research paper is submitted, and the authors' goals. Accordingly, **the choice of development pathway belongs to the project's developers and the academics working with them**, not ORCA Foundation. ORCA's role is to make the trade-offs of each pathway clear, to provide guidance that protects the academic publication, the open source project's ability to maintain production software, and the integrity of the Foundation's decisions.

## 2. Two diverse development pathways

### 2.1 The Closed Pathway — Closed development until paper acceptance

The project is developed privately and is opened (repositories made public, announcement, promotion) only after the paper has been accepted or the venue's review is complete.

**What it protects.** Strong protection of double-anonymous review: there is no public artifact to de-anonymize the authors, no code is available for other researchers to examine, and no Foundation announcement that could compromise the submission.

**Negative ramifications.** The project cannot benefit from the academic work until the paper is accepted.  This means that the open source project will have its main codebase move ahead without the project's fork, possibly through multiple submission cycles.  As a result, integrating the code base will be much more problematic and time consuming.  This can create contention between the maintainers / adopters and the academic contributors. This also means that the work is not visible to adopters so the paper will be unlikely to contain any operational experience or use information. Also, some venues now run *artifact evaluation* and expect public artifacts, so a fully closed approach may need to be reconciled with the target venue's artifact track.

**Academic obligations under this pathway.**
- If you are submitting a project for intake into ORCA, please disclose to the TSC that development is proceeding privately pending a submission, including the target venue and expected notification window.  You may be asked to allow the TSC access to evaluate the implementation
- Coordinate the timing of opening/announcing the project with the venue's notification schedule.
- Confirm the closed-then-open plan is compatible with the venue's publication and anonymity rules.

**Summary.**
This pathway is a positive for academic reviewers who treat novelty as the main goal and place little value on practical impact and for venues that do not do any sort of artifact evaluation.  This pathway also causing friction with the open source project and reduced the potential for practical impact.  

### 2.2 The Open Pathway — Open development from the beginning

The project is public from the start, with development, repositories, and history visible throughout — including while the paper is under review.

**What it protects.** Fully realizes ORCA's open-source mission: open collaboration, transparency, external contribution, and early adoption from day one.  Merging in changes is obviously much easier, since this is done as the developed functionality is useful to the open source project.  Research advances are used in practice and submitted papers can contain operational experience since code will be used in practice.  Evaluation results can therefore be more realistic and case studies can be included.  The problems the work solves are also easier to motivate with real world examples.  

**Negative ramifications.** There is the potential for this to deanonymize the project.  Authors should not self identify as maintainers of the project or similar as this may de-anonymize a paper under double-anonymous review and risk desk rejection. In practice, mentioning the contribution process as though you are an external contributor (instead of a maintainer, if applicable) is sufficient.  In some cases, reviewers may have experience with the project and may feel like it is more known which may impact a reviewer's perception of novelty.  

**Developer obligations under this pathway.**
- Confirm that open development is compatible with the target venue's anonymity and dual-submission rules *before* relying on it. However, note that this is allowed under ACM, IEEE, and USENIX Guidelines, so should be applicable to most computer science academic venues.
- Optionally request a **quiet period**: ORCA and the project maintainers may be asked to withhold author-identifying promotion (blog posts, press, social) until after notification, even while the code stays public.

**Summary.**
This pathway is a positive for academic reviewers that value practical impact, real world deployments / experiences, and for venues that emphasize artifact evaluation.  This pathway also enables researchers to work closely with the open source project and increases the potential for practical impact.  
  
### 3 Conclusion

If you have questions about either pathway or other aspects not covered here, please mention them in the #orca-tsc channel in the ORCA slack or speak to a TSC member.
