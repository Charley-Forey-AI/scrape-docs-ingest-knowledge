---
title: "Delete a Leave Code Reset | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits/delete-a-leave-code-reset"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits/delete-a-leave-code-reset"
---

# Delete a Leave Code Reset

You can delete previously posted leave code reset transactions that were posted in error.
When deleting previously posted leave code reset transactions, you must use the same batch month and reset date. The reset process pulls
 the previously reset transactions into a new batch and flags all of the
 transactions for deletion.
 The following instructions explain how to delete a leave code reset.

1. Launch the PR Leave Code Reset form and create a new batch using the same month as the original leave reset transactions.

1. Select the Reset Accrual Amounts to 0.00 hours for the next frequency period checkbox or the Reduce Available Balances to Carryover Limit checkbox, depending on which option you selected when you ran the original reset. If you selected both checkboxes in the original run, then select both here.

1. In the Reset Date field, enter the same date used for the original reset transactions.

1. Select the Delete any reset transactions currently posted to this date checkbox.

1. Click Update. The system adds all of the previously posted reset transactions into a leave batch and displays a confirmation message, prompting you to post the batch.

1. At the prompt, do one of the following:If you elect to post the batch now, select File > Process Batch. 

- If you are ready to post the batch, select Yes. The PR Batch Process form displays and you can proceed with posting the batch.

- If you want to review the leave entries before posting the batch, select No to the prompt. You are returned to the PR Leave Code Reset form. You can then exit the form and review the entries in PR Leave Entry.

When you post the batch, the system removes all transactions from the Leave History
 table, sets the Last Date Reset field in PR Employee Leave to the previous last reset date for that code/employee, and sets the
 Accrual Limits and Available Balance Limits to the previous
 values.
