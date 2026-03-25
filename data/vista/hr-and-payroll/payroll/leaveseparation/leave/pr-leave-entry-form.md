---
title: "PR Leave Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form"
---

# PR Leave Entry Form

Use the PR Leave Entry form to enter leave accrual and usage entries.
 If you prefer to generate leave/accrual entries automatically, use the PR Automatic Leave Accrual/Usage form. You can then use this form to review and edit the generated entries. However, edits are limited to the amount and description for each entry; you cannot edit the employee, leave code, date, or type. If needed, you can delete an entry and manually enter a new one, but the new entry will not have a PR group, pay period ending date, or sequence #. You may also rerun the PR Automatic Leave Accrual/Usage form as needed to correct errors.
Note: Please be aware that these are batch entries; therefore, you must post the batch before the updated information is reflected in PR Employee Leave or any Leave Tracking reports.
Whether entering entries manually or reviewing auto generated entries, the informational display above the grid provides information about each employee's leave values. For each of the Accrual Accumulators and the Available Balance, the display shows the Adjustment, Current, and Limit values, as well as the Reset Frequency and Last Reset date.
If you are adding entries manually, the Adjustment values remain blank until the entry is accepted, then populate based on the entry type.
Note: In order to post leave accrual and usage entries, the specified leave code must
 have an assigned limit greater than 0.00 in PR Leave Codes. Additionally, the
 leave code must be flagged as Active in PR Leave Codes and PR Employee Leave. If
 you enter an inactive leave code manually, the system displays an error and will
 not allow the entry. If you generated leave entries in PR Auto Leave
 Accrual/Usage, the system automatically skips inactive leave
 codes.

## Reopening and Closing a Pay Period

On occasion, you may need to reopen a pay period to make changes, such as to void and re-issue a check. When you close the pay period, if you changed any timecards that affect leave entry (that is, the timecards are associated with a leave entry earn code), it is strongly recommended that you run the leave entry process after you have run AP Ledger Update. This ensures that you not encounter errors later due to unbalanced or negative leave. For more information, see [About Closing/Opening Pay Periods](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-closingopening-pay-periods).

## Reset and Reset Reversal Transactions

If you have run the PR Leave Code Reset form, you can review the reset transactions in this form. Reset transactions are assigned a Type of R (Reset) and a description that identifies the type of reset (e.g. '**Reset Accrual/Avail Bal). Some editing may be done to these transactions, though you cannot edit the Type or Amount. You also have the option to delete those transactions that you do not want processed.
You can also review reset reversal transactions in this form. Reset reversals are 'reset' transactions that have been pulled back into a batch and marked for deletion using the PR Leave Code Reset form. When reviewing these transactions in this form, note that they are highlighted in red and flagged as Delete. In addition, each transaction is flagged with transaction type of R (Reset) and has a description matching the original reset transaction. These transactions cannot be edited, though you can delete transactions you do not want processed.
For both reset and reset reversal transactions, note that the Accrual Limit #1 Adjust, Accrual Limit #2 Adjust, and Avail Bal Adjust columns in the grid display a value (these columns do not display values for Usage and Accrual entries). These values are identical to the Adjustment values shown in the informational display above the grid, except that they are the reverse of the values above the grid. For example, if the values in the grid are negative, the values above the grid are positive and vice-versa. The grid shows the original reset entry that you are backing out, whereas the informational display shows the values you are adding back in.

Related information

- [PR Employee Leave Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form)

- [PR Leave Code Reset Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form)

- [PR Leave Codes Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form)

- [PR Add Leave Trans to Batch Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-add-leave-trans-to-batch-form)
