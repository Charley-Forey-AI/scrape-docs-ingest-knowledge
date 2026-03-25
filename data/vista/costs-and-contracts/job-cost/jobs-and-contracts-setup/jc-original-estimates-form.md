---
title: "JC Original Estimates Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-original-estimates-form"
---

# JC Original Estimates Form

Use this form to create original estimates for each phase on a job.
You can access this form from the main menu or by double-clicking a cost type on the Estimates grid in JC Jobs.
As you enter estimates for each cost type on a phase, the Job Total and Phase Total fields (above the tabs) provide a running total of the estimated costs.
Once you set up estimated units for a phase, you can post progress to the phase so that a percent complete can be determined and used for suggested billing information and meaningful job cost reports.

## Initialize Cost Types

If you are adding phases to a job using this program, you will also need to add the cost types for each phase; they are not added automatically. You can initialize cost types either using the Initialize button or by selecting File > Initialize Cost Types. Initialization adds all cost types for the phase as defined in JC Phases. The unit of measure and bill flag for each cost type defaults from JC Phases, and the Hours, Units, Unit Cost, and Cost values are set to 0.00. You can enter estimate information as necessary.

## Entering Units for Lump Sum Phase/Cost Types

In most cases, Vista restricts the entry of units when the unit of measure is LS (lump sum). However, if you will be updating progress using JC Progress Entry, it is recommended that you enter units (1 or 100) for phase/cost type estimates where the unit of measure is LS. This will allow for entering percent complete for progress on the job. Many Job Cost reports use this information for monitoring progress and projecting final costs.

## Source

The display-only Source field shows the source/status for each phase/cost type estimate set up for the job. This field corresponds to the Update field PM Project Phases. The system updates these fields automatically each time you enter and save a phase/cost type combination in either form.
Note: When entering phases/cost types in this form, the source/status will always be J-Entered in Job Cost. The other three source/status options are for phases/cost types entered in Project Management.

The following table shows the source/status options used in this form versus the corresponding options used in the Update field in PM Project Phases.
JC Original EstimatesPM Project Phases
J-Entered in Job CostJ-Job Cost
Y-Entered in Project Management and yet to be interfaced to Job CostY-Ready to Update
N-Entered in Project Management and flagged not to be interfaced to Job CostN-Not ready to Update
I-Interfaced from Project ManagementI-Interfaced

[Add a New Phase to a Job](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/add-a-new-phase-to-a-job)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
