---
title: "Build Projected Cost Transaction File - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file/build-projected-cost-transaction-file---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file/build-projected-cost-transaction-file---cost-center-information"
---

# Build Projected Cost Transaction File - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, when building jobs Spectrum will create projected cost transaction entries for the job only if you have permission to access the job information. During the update, Spectrum compares the cost center assigned to the job with cost centers in your assigned scheme; if the cost center is not included, then entries for that job are not created. When your scheme includes override settings for job entries in Cost Center Scheme Maintenance, this update will validate the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost centers list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with job override cost centers in your assigned scheme; if the cost center is not included, then the transaction entry line will not be created. Spectrum builds all phases of authorized jobs regardless of cost center, if any, specified for the phase. When the Clear file for batch checkbox is selected, all selected jobs will be cleared regardless of cost center assignment.
