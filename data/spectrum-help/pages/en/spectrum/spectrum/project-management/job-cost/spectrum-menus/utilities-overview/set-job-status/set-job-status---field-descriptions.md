---
title: "Set Job Status - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/utilities-overview/set-job-status/set-job-status---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/utilities-overview/set-job-status/set-job-status---field-descriptions"
---

# Set Job Status - Field Descriptions

Use the table below for reference when completing fields on this screen.
Fields
Descriptions

Job Description Last cost date Last bill date Current status
The job number, detailed job description, date of the last cost item, date of the last bill, and current job status display.
Click to sort the records on the screen in ascending job number order. Click again to set the order to descending.

New status Complete date
The new status and complete date defaults display in these columns.
If the 'New Status' option in the Build Job Status window was set to 'Complete', the stored complete date will display in this column.
If Equipment Tracking is being used, you cannot set the status to 'complete' if there is any chargeable equipment currently 'issued' to the Job (or Phase).
If the selected job is a sub-job and the status is Complete, disallow the status to be changed if the master job status is also Complete. If the selected job is a master job, the status cannot be changed to Complete is any of its sub-jobs are set to Active or Inactive. All sub-jobs must be completed before closing the master job.

Disallow revenue entry?
If the current status is 'Complete,' select this checkbox to specify that revenue entries are disallowed. When this option is selected, Spectrum will validate whether users are authorized to record revenue transactions for the job in Accounts Receivable.

Customer
The customer name displays in this field.
