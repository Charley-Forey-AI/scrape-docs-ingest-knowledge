---
title: "PR Leave Code Reset Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form"
---

# PR Leave Code Reset Form

Use the PR Leave Code Reset form to reset the Accrual Limits and/or the Available Balance limits for a specific, or all, leave codes.
 Access the PR Leave Code Reset form via PR Leave Entry by selecting File > Leave Code Reset.
 You can reset leave codes for a specific frequency or all frequencies, and for a specific employee or all employees.
Resets are typically performed at the end of the frequency period specified by the limit. You can only perform a reset when open, or unprocessed, PR Leave Entry batches do not exist for the current PR Company. For more information on how limits and frequencies function, see [About Leave Code Settings](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/about-leave-code-settings).
Once entries are generated, a confirmation message displays and prompts you to post the batch. If you select Yes, the PR Batch Process form displays and you can proceed with posting the batch. If you select No, you are returned to the PR Leave Code Reset form. You can either continue adding entries to the batch until you are ready to post or you can close the form and open PR Leave Entry to review the entries and post your batch.
The Reset Date determines when the new frequency period begins. The Reset Date can be any valid date, but it should be greater than the date in the Last Date Reset field for the applicable limit in PR Employee Leave. The system ignores all leave history posted on or before this date when updating current balances and available amounts. In addition, this date updates to the Last Date Reset fields in PR Employee Leave, regardless of whether there was any balance reset for the employee.
Once the reset is run, the applicable Accrual Limit fields only reflect accrual amounts that occur after the reset date that you specify here. Available Balances show the balance of accruals and usage that occur after the reset date. Any remaining balances will not exceed set accrual limits and/or balance limits.
Note: The system sets all negative leave balances to 0.00 during the reset process.
For instructions on how to reset leave code limits, see [Reset Leave Code Limits](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits).
If you've already reset your limits and need to add hours to employee leave balances, see [Update Fixed Amount Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-fixed-amount-accruals) (if you grant fixed amounts) or [Update Usage and Rate-Based Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-usage-and-rate-based-accruals) (if your employees accrue leave hours at a rate).

## Deleting Reset Transactions

If you have run a previous batch of transactions for this date and need to reverse them, select the Delete Any Reset Transactions checkbox. The reset process pulls the previously reset transactions into the new PR Leave Entry batch. You can post and process the batch from this form, or you can review and post the transactions from PR Leave Entry.

Note: The system skips inactive employees and inactive leave codes during resets and reset reversals.

Related information

- [Reset Leave Code Limits](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits)

- [PR Leave Entry Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form)

- [PR Employee Leave Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form)
