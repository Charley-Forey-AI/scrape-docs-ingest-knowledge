---
title: "Close a Pay Period | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/close-a-pay-period"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods/close-a-pay-period"
---

# Close a Pay Period

You can close a pay period using the PR Pay Period Control form.

Before you close a pay period, make sure it is fully processed; that is, all time has been posted, deductions and liabilities calculated, accumulations updated, and checks printed. Once closed, you cannot enter or change any timecard entries, reprocess a payroll, or print checks.

1. Open the PR Pay Period Control form.

1.  Specify the pay period to close using the PR Group and Pay Period Ending Date fields.

1. Click Change Status.A message displays indicating the Pay Period has just been closed and asking if you want to run the Ledger Update.

1. Select YES.The PR Ledger Update form displays.Note: If you select NO (that is, you elect to not run the Ledger Update), the screen displays a message asking if you want to run Leave Entry for accrual/usage updates. It is recommended that you select YES. If you select NO, the pay period's final leave update will be considered complete; however, this may result in discrepancies with your leave totals.

1. Tab through the PR Group and Pay Period Ending Date fields to accept the defaulted values.This also enables the Available Updates checkboxes.

1. In the Available Updates section, select the General Ledger / Cash Mgmt / Accumulations checkbox. This auto-selects the other applicable update checkboxes.

1. Click Validate.A message displays indicating that you have successfully completed the ledger update validation.Note: If errors are encountered during validation, a message displays indicating there are errors and the Error audit report is enabled. You must correct the errors before proceeding.

1. Click Close.

1. Preview and/or print the applicable distribution (audit) reports.

1. In the Posting Date field, accept the default (today's date) or enter a new posting date. You may 'back date' the batch if desired.

1. Click Post.

1. Close the PR Ledger Update form.A message displays asking if you want to run Leave Entry for accrual/usage updates.

1. Select YES.The Batch Selection form displays.Note: If you changed timecards that affect leave entry (that is, the timecards are associated with a leave entry earn code), you should always answer YES. Answering NO can cause errors later due to unbalanced or negative leave.

1.  Create a new batch using the same month as the pay period you closed. If it is a split-month pay period, use the same month as the timecard batch month.The PR Leave Entry form displays.

1. Select File > Leave Accrual Usage/Init....The PR Auto Leave Accrual/Usage form displays.

1.  In the Usage and Rate Based Accruals section, select the Use Pay Period earnings to update Leave usage and rate based accruals checkbox.The PR Group and Beginning/Ending PR Ending Date fields are enabled.

1. Enter the payroll group and pay period ending dates, using the values specified for the pay period in PR Pay Period Control. Make sure you enter the same value in both the beginning and ending PR Ending Date fields.

1. Click Update.

1. Close the PR Auto Leave Accrual / Usage form.The PR Leave Entry form displays all entries added to the batch (both deleted and added).

1. Select File > Batch Process, and then validate and process the batch.

The system sets the pay period status to Closed, selects the applicable Final Updates checkboxes, and enters a date in the Date Closed field.Important: If you elected to close the pay period without running the Ledger Update, the Final Updates checkboxes are left unselected and you will be unable to close the month.
