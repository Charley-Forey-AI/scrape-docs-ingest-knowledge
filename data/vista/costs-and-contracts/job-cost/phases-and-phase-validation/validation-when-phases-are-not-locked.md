---
title: "Validation when Phases are not Locked | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation/validation-when-phases-are-not-locked"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/phases-and-phase-validation/validation-when-phases-are-not-locked"
---

# Validation when Phases are not Locked

If you do not lock job phases, you can post to any phase code that is set up in JC Phases.
To explain the validation process for phases that are not locked, we will assume an eleven-character multi-part phase code in which the first eight characters represent common work activities, followed by a dash and two characters that are reserved for change orders:

If you do not select the Phases on this job are locked checkbox for the job in JC Jobs, operators can post to any phase code that is set up exactly in JC Phases, or any code longer than eight characters where the first eight are defined in the JC Phases form. In either case, the cost type used must be set up for the phase in JC Phases. Pressing F4 in a Phase field shows you a list of valid phases (those set up in JC Phases)
If you enter a phase code that has not previously been used on a selected job, the system automatically sets up that phase on that job, using the phase description and unit of measure from the Phases form. How the billing flag is set depends on whether the phase/cost type unit of measure matches that of the contract item. The contract item to which the phase code is linked depends on whether the validated phase has already been set up on the job. The following examples illustrate how the Bill flag and Contract Item are set when you add new phases to a job:
Phase Code
UM
Bill Flag
Contract Item
UM

Set up in JC Phases:

12000– 40–

Y

12000– 50–

N

Already added to Job:

12000– 40–
SF
Y
23
SF

When you add this phase and UM:

12000– 40– 11
SF
Y
23
SF

12000– 40– 12
CY
C
23
SF

12000– 50– 10
LF
N
1
LS

How the bill flags were set for examples shown above:The unit of measure assigned to contract item 23 is SF, and phase 12000-40- is flagged as billable. When 12000-40-11 was entered, it was validated against the JC Phases entry for 12000-40-, so the bill flag was set to Y as well. However, when 12000-40-12 was added with a different unit of measure, the bill flag was set to C. In the third example, the Bill flag for the new entry was set to N because the Bill flag for phase 12000-50-was set to N in JC Phases.How the contract items were set for these examples:When the two entries starting with 12000-40-were added, the system was able to find that phase already on that job in its validated form, so it used the contract item link from that entry. In the last example, no previous entry for 12000-50- was found, so the system used the first contract item on the job.
Note: You can override any information set up automatically using JC Job Phases.
