---
title: "PR TimeCard Compliance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-compliance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-compliance-form"
---

# PR TimeCard Compliance Form

Use the PR Timecard Compliance Form to review timecards that do not meet compliance rules and then either correct the violations or accept them.
This form displays once you select File > Process Batch from PR Timecard Entry. However, it will only display if all three of the following conditions are met:

- You selected the Enable Timecard Compliance checkbox in PR Company Parameters (Info tab)

- The Severity Level for the violated rule(s) is Allowed With Warning or Not Allowed

- Discrepancies were found in the timecard batch (based on employee history, enabled rules, and/or compliance settings).

The grid displays all violated rules in the timecard batch that are flagged as Allowed With Warning or Not Allowed. Information shown includes (but is not limited to) the batch sequence, reason, employee, date, timecard type, department, earn code, hours, and rate.
Violated rules are color-coded. Red means that the severity level for that rule is set to Not Allowed, so you must either delete the record from the list or correct the timecard before you can post the batch. Yellow means that the severity level for that rule is set to Allowed With Warning. This means that you can either accept the discrepancy, correct it, or delete the record from the list before you can post the batch.
Note: If you delete a record from the violated rules grid, that record is deleted from the timecard batch the same as if you deleted it from the timecard entry grid. If you still need to post those hours, you'll need to create a new timecard batch and re-enter the line.

## Accepting Discrepancies

For rules flagged as Allow With Warning (yellow highlight), you have the option to accept the discrepancy without correcting it. You can do this by either selecting the Accept checkbox for individual entries or by selecting the Accept All button. However, you can only accept items highlighted in yellow.
 Once you have accepted applicable violations, select Submit to update the timecard batch. The PR Batch Process form displays and you can validate and post your batch.
Note: If you have a mix of red and yellow highlighted lines, you must either correct the red highlighted lines or delete them from the list before you can submit the entries. The Submit button is disabled until all entries are accepted, corrected, or deleted.

 After you post the timecard batch, any discrepancies that you accepted are displayed on the Compliance tab in PR Pay Period Control, providing you an audit record of who accepted violations without correcting them.

## Correcting Discrepancies

You can correct the discrepancies found during timecard validation in one of two ways:

- Directly in the grid in this form

- Using the PR Timecard Entry form

If you elect to make changes in PR Timecard Entry, you can close this form, which automatically returns you to your timecard batch in PR Timecard Entry. Once you make corrections, select File > Process Batch and if no further discrepancies are found, the PR Batch Process form displays and you can validate and post your batch.
If you elect to make changes directly in the PR Timecard Compliance grid, just edit the highlighted value for each rule violation, and then select Submit. The timecard batch is updated accordingly and the PR Batch Process form displays. You can then validation and post your batch.
