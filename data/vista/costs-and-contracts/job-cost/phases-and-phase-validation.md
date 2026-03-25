---
title: "Phases and Phase Validation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation"
---

# Phases and Phase Validation

An important concept of the Job Cost module, and one that affects other modules as well, is your phase setup and the validation of phases at posting time.

All phase codes that your company will use on jobs must be set up in the JC Phases form. Estimated and actual costs for your jobs are processed and tracked by these phase codes.
You are not required to set up every phase code you will use in its entirety. For example, if you use an eleven-character multi-part phase code in which the first eight characters represent common work activities, followed by a dash and two characters that are reserved for change orders, you need only define the eight-character phases in JC Phases. You set this up by entering 8 in the Number of Valid Characters in Phase Code field in the JC Company Parameters form.
For less restrictive phase validation, specify fewer characters. Validating even the first two characters allows adding nearly any phase to the job dynamically, provided JC Phases contains at least one phase with those characters.
For example, say you set up the following phases in JC Phases:
01–001
01–002
You then post to a job and need to add phase ‘01-100’. Since the validation process confirms the existence of at least one phase in the phase master containing the characters “01”, the entry is allowed.
Note: If you are using the 'locked phases' feature, the 'number of characters' validation will only apply to phases being added to a job via JC Job Phases, JC Original Estimates, JC Change Orders, PM Project Phases, or PM Change Orders. When posting to a job, only phases assigned specifically to that job may be entered.

[Validation when Phases are not Locked](/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation/validation-when-phases-are-not-locked)
[Validation for Locked-Phase Jobs](/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation/validation-for-locked-phase-jobs)
