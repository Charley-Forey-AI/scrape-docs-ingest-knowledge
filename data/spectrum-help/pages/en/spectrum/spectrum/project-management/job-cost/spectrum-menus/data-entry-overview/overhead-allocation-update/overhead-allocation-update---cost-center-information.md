---
title: "Overhead Allocation Update - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/overhead-allocation-update/overhead-allocation-update---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/overhead-allocation-update/overhead-allocation-update---cost-center-information"
---

# Overhead Allocation Update - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, the Overhead Allocation Update starting screen includes a selection for a Cost group.
When you specify a cost center on the Overhead Allocation Update starting screen, Spectrum verifies that you have permission to access that cost center before proceeding.
When performing the Overhead Allocation Update, Spectrum will create overhead transaction entries for the job only if you have permission to access the job. During the update, Spectrum compares the cost center assigned to the job with cost centers in your associated scheme; if the cost center is not included, then overhead entries for that job will not be created.
When your scheme includes override settings for job entries in Cost Center Scheme Maintenance, this update will validate the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with job override cost centers in your assigned scheme; if the cost center is not included, then the transaction entry line will not be created.
Spectrum updates from all phases of authorized jobs, regardless of cost center, if any, specified for the phase. Likewise, job cost overhead transactions are created for the phase specified in Overhead Allocation Maintenance to receive the charges, without regard for cost center set up for that phase.
The cost center assigned to overhead transactions created during this update is determined by the cost center stored in Job Cost history of each basic cost transaction. The cost center from the history file is assigned to both the Debit and Credit cost center fields.
