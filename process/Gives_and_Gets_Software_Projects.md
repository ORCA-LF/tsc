# "Gives and Gets" for ORCA Software Projects

_v1.0 approved and merged by the TSC on XXX_

Projects are initiatives that are hosted, managed and supported by ORCA aimed at making isolation and compartmentalization approaches usable in real software stack.  In exchange for meeting certain requirements, the Software Projects are eligible to receive an assortment of benefits and have access to the capabilities of the Alliance's resources.  The specific requirements and benefits (aka "Gives and Gets") for each level of project maturity are documented below. Based on the specific type of work the Project is focused on (e.g., software, specification, or documentation development) the requirements and benefits may slightly differ as applicable.

Also note that benefits may actually vary based on resources and funds availability, or lack thereof.

## Voting on Project Acceptance and Removal

Decisions to accept a project into ORCA at any level, or to archive, demote, or remove a project from ORCA stewardship, are made by a vote of the TSC and require the approval of at least two-thirds (2/3) of the votes cast.

- Voting members who are absent, do not cast a vote, or are recused due to a conflict of interest with the project under consideration are not counted toward the total against which the two-thirds threshold is calculated.
- A vote is valid only if a quorum participates: at least a majority (more than half) of the TSC's eligible voting members must cast a vote. Members recused for a conflict of interest are excluded from both the quorum count and the threshold calculation. If quorum is not met, the decision does not carry and may be reconsidered at a subsequent meeting.

## Sandbox Level Gives & Gets

### Gives/Requirements
* [PR filed](https://github.com/ORCA-LF/tsc/pulls) to enter the sandbox stage.
* Project must be aligned with the [ORCA mission](https://docs.google.com/document/d/1r8CyeJBo9hHDggBvjk4o9GmKI2xNit-0wwjmwDnXyWk/edit?tab=t.0#heading=h.iubcu7w2p6mf) and either be a novel approach for existing areas or address an unfulfilled need. It is preferred that extensions of existing ORCA projects collaborate with the existing project rather than seek a new project.
* Project must have and maintain a history of producing public software releases, including a software pipeline that others are able to build.  Adequate tests and getting started instructions must exist to enable execution and use of the platform in reasonable environments by interested parties. Developers are responsible for responding in an appropriate way to issues on their tracker. There must be a reasonable balance of stability and a cadence of fixes.
* Project agrees to follow the [Secure Software Development Guiding Principles](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/SecureSoftwareGuidingPrinciples.md) and the [Open Source Consumption Manifesto](https://github.com/ossf/wg-endusers/tree/main/MANIFESTO).
* Project must provide an accurate, up-to-date, and factual description of the capabilities and limitations of their project for use in ORCA webpages and other materials.  This must be approved by the project’s TSC sponsor or delegate.
* If contributing an existing Project to the ORCA, the contribution must undergo license and IP due diligence by the Linux Foundation (LF).
* Project must provide quarterly updates to the TSC on technical vision and progress on vision.
* Project must have a plan for deployment in practice or evidence of practical experimentation.
* Project will have a [SECURITY.md](https://github.com/ORCA-LF/tsc/blob/main/process/SECURITY.md) that describes how the Project manages vulnerabilities.
* The Project team must give a presentation on the project at a public TSC meeting or ORCA Tech Talk
* A project must continually meet all requirements.  Any project which fails to meet the requirements above, may be archived, demoted, or removed from ORCA stewardship at the discretion of the TSC.

### Gets/Benefits
* Project can get assistance with Architecture & Roadmap Alignment.
* Project receives guidance on technical direction from the TSC.
* Project may request basic infrastructure support from the ORCA (e.g., mailing list and github repo).
* Projects may say they are, "A sandbox project in the ORCA" or "An experimental project in the ORCA".
* Project receives communication & collaboration support through ORCA mailing list, ORCA Slack channel, ORCA GitHub, ORCA Calendaring / Recording through Linux Foundation,  ORCA Social Media & External Engagement Support, etc. 
* Project receives best-effort ORCA staff support.
* Project receives consideration as in-scope for any submission to an ORCA-managed conference or event.
* With additional TSC approval, may fundraise for dedicated project funds, with assistance and coordination by the ORCA TSC.  This includes items like a letter of support for a grant supporting a project, acting as a partner for calls that require such support, etc. 
* Project receives Governance & Administration Support - Project Charter Development & Review, Project Technical Steering Committee Setup, Project IP & License Review, Project Operations & Maintenance, Technical Support.

## Incubating Level Gives & Gets

### Gives/Requirements
* All requirements of Sandbox must be fulfilled.
* [PR filed](https://github.com/ORCA-LF/tsc/pulls) to promote Project to Incubating stage.
* Project must have documented, initial group governance.
* Project maintains a diversified contributor base (i.e. not a single-vendor project) with an active flow of contributions, and documents the current list of maintainers.
* Project must have a minimum of three maintainers with a minimum of two different organization affiliations.
* Project has had public meetings at least 5 times within the last calendar quarter.  In most cases, this should occur after a project was admitted to Sandbox, but this may be waived by the TSC for projects with a mature and diverse public community. It is recommended that projects have monthly, public community meetings.
* Project must have defined a contributor guide, which makes it clear how and when contributors should be given increasing responsibilities towards maintainership of the project. (Example guides: [Sigstore](https://github.com/sigstore/community/blob/main/CONTRIBUTING.md), [AllStar](https://github.com/ossf/allstar/blob/main/contributor-ladder.md))
* Project should be able to show adoption (ideally by multiple parties) and adoption's value to the open source community and/or end users (may include adoption of beta/early versions) with the intent to showcase wide adoption by the project's consumers.
* The software project's source code:
	* Implements, practices, and refines mature software development and release practices such as following a version schema.
	* Follows security best practices (as recommended by the OpenSSF and others), including passing the OpenSSF Baseline criteria, secret scanning, and code scanning.
	* Maintains a point of contact for vulnerability reports in the [SECURITY.md](https://github.com/ORCA-LF/tsc/blob/main/process/SECURITY.md).
	* Begins to establish the appropriate governance that enables its sustainment for potential graduation.


### Gets/Benefits
Projects are eligible to receive all Gets from Sandbox plus:
* May request custom ORCA Logo for the project.
* May use the ORCA logo to promote their project (in accordance with the trademark guidelines). Projects may be referred to as an "ORCA Project" or "ORCA $ProjectName."
* May post project updates and tutorials to the ORCA blog.
* Receives higher priority for ORCA staff support than Sandbox, less than Graduated.
* May request swag bearing custom ORCA Logo (funds permitting).

## Graduated Level Gives & Gets

### Gives/Requirements
* All requirements of incubating must be fulfilled.
* [PR filed](https://github.com/ORCA-LF/tsc/pulls) to promote Project to graduated stage.
* Project must have documented governance and be able to demonstrate that governance in action.
* Project has a defined and documented roadmap and annual goals.
* Project has met at least 4 times over a period of at least 2 months since becoming Incubating.
* Project must have a minimum of five maintainers from a minimum of three different organization affiliations.
* Project that develops code should do the following:
	* Implements, practices, and refines mature software development and release practices, such as adherence to semantic versioning, and having a declared policy for stable releases and backported fixes.
	* Must be able to show a consistent release cadence.
	* Maintains a point of contact for vulnerability reports and follows coordinated vulnerability disclosure practices.
	* Should harden its build systems in accordance with the SLSA Framework.
* Project must have completed a self assessment.  In addition, the project must complete a joint assessment and/or a security audit through a third party and address audit findings and recommendations.

### Gets/Benefits
Project are eligible to receive all Gets from Incubating plus:
* Receives consideration as in-scope for any submission to an ORCA-managed conference or event.  This includes consideration for booth space at the conference and/or the ORCA booth.
* Receives advanced infrastructure support from the ORCA subject to available funding (e.g., cloud hosting, to be determined by project leads and ORCA TSC).
* May post project updates and tutorials to the ORCA blog.
* May request ORCA budget for project improvements such as security audits (subject to availability of funds).
* May use the ORCA logo to promote their project (in accordance with the trademark guidelines). Projects may be referred to as an "ORCA Project" or "ORCA $ProjectName."
* Highest priority for ORCA staff support.
