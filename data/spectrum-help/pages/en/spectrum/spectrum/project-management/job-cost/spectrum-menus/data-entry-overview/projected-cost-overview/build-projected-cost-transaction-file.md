---
title: "Build Projected Cost Transaction File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/build-projected-cost-transaction-file"
---

# Build Projected Cost Transaction File

Use the Build Projected Cost Transaction File screen to build a transaction file for use in entering projected cost transactions. Typically the same selections will be specified on this page that were specified on the Projected Cost Worksheet. It is recommended that one job be processed at a time (build, enter, update). This reduces the risk of inadvertently updating projections for jobs that were not intended; it will also increase software performance speed.
The transaction file is built from estimate and projected cost information in Job Phases. Actual costs-to-date through the specified year and period will be included in the transaction file.
You can select transactions by group summary, as needed. If major or minor grouping is selected at the time of the build, the projected entry page will show only the major or minor group totals for entry.
When entering a percent complete, cost to complete, or final projection for the group, Spectrum will automatically allocate this percentage complete to all the detail phases of this group. The worksheet and projected reports also display the group summary information.
Note: This page checks the current batch for any projected
 cost history records that come after the date in the Through period end date field. If any
 dates are found, the following message displays: "Projections have already been posted for
 a subsequent date. These projections will be treated as a 'correction' to the previous
 projection, but will not affect the current projections." During the update, the adjustment
 will be based on the projection history file, as of the batch through date instead of the
 current projection from the phase file. If any projection history records exist for the
 same phase with a transaction date later than the current batch date, then a matching
 record will be created to balance the current transaction. The date of the matching record
 will be the same as the next projection history transaction for the phase. The current
 projection for the phase will remain unchanged.
