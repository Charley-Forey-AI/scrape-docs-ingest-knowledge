---
title: "Reset Leave Code Limits | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/reset-leave-code-limits"
---

# Reset Leave Code Limits

Use the PR Leave Code Reset form to reset limits (accrual accumulator or available balance) specified for a leave code.
The following instructions explain how to reset leave code limits. For further information, refer to [PR Leave Code Reset](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form).

1. To reset accrual limits for the specified leave code(s), select the Reset Accrual Amounts to 0.00 hours for the next frequency period checkbox.

1. To reset available balance limits for the specified leave code(s, select the Reset Available Balances to Carryover Limit checkbox.

1.  In the Reset Date field, enter the reset date to use. This date determines the start of the new frequency period for the reset limits.

1. Select the appropriate radio button from the Leave Code section of the form.

-  All - Reset limits for all leave codes

-  Leave Code - Reset limits for a specific leave code

1. If you selected the Leave Code option, enter the leave code in the Leave Code field or press F4 to select from a list of valid leave codes. Leave code must be set as Active in PR Leave Codes. Note: Leave code must be set as Active in both PR Leave Codes and PR Employee Leave.


1. Select the appropriate radio button from the Frequency section of the form.

- All - Reset limits for all frequencies associated with the leave code limits

-  Frequency - Reset limits for a specific frequency associated with the leave code limits

1. If you selected the Frequency option, enter a frequency code in the Frequency field or press F4 for a list of valid frequency codes.

1. Select the appropriate radio button from the Employee section of the form.

- All - Reset limits for the specified leave code(s) for all employees

-  Employee - Reset limits for the specified leave code(s) for a selected employee

1. If you selected the Employee option, enter the employee for which to update leave code limits in the Employee field or press F4 for a list of valid employees codes. Employee must be set as Active in PR Employees.

1.

1. Click Update. The system updates PR Leave Entry with all transactions and displays a confirmation message.Note: The system skips inactive employees and inactive leave codes during the reset process.

1. Click Close.

1. Select File > Process Batch. The PR Batch Process form displays.

1. [Process the batch](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form).

Add hours to employee leave balances (if applicable). For more information, see [Update Fixed Amount Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-fixed-amount-accruals) (if you grant fixed amounts) or [Update Usage and Rate-Based Accruals](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/update-usage-and-rate-based-accruals) (if your employees accrue leave hours at a rate).

Related information

- [PR Leave Code Reset Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form)

- [PR Leave Entry Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form)

- [About Processing Employee Leave](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave)
