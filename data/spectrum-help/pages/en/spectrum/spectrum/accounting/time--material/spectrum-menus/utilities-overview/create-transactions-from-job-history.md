---
title: "Create Transactions From Job History | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/utilities-overview/create-transactions-from-job-history"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/utilities-overview/create-transactions-from-job-history"
---

# Create Transactions From Job History

Use this feature to generate billing transactions from Job Cost history for the selected job. This update creates billing transactions for all selected cost history. These transactions are created based on current Time + Material or Cost-plus settings.
If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.
Important: If a new job is set up with an incorrect price
 type, specifically when T+M or cost plus jobs are initially set up as fixed or unit price
 jobs, the billing details are not accumulated in the Time + Material module as job costs
 are incurred. To prevent potential double-billing, delete any T+M transactions that already
 exist for this job before proceeding.
Note: Transactions for all selected phases are built during
 this update regardless of the current phase status (Active, Inactive, or Complete).Fields
Descriptions

Job
Enter or search for the job you want to generate
 billing transactions for. The job name displays to the right.

From transaction date To transaction date
Enter the beginning and end transaction dates. Click
 the arrow to view the Search Calendar window.
