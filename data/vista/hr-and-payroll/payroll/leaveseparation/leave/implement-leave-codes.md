---
title: "Implement Leave Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes"
---

# Implement Leave Codes

If you plan to set accrual and available balance limits for leave codes, and you are implementing a new Vista™ system, you must enter any balance forwards from your legacy system prior to setting limits.
The system uses the last reset date to determine the start date for the limit frequency. If you create leave codes with limits, prior to entering balance forwards, the system applies the balances to the limit and leave accrual will not calculate correctly.
Note: The last reset date for a frequency does not appear on PR Leave Codes, as it is a setup form. The last reset date for a frequency is associated with each employee and displays on the PR Leave Entry form, along with the PR Employee Leave form.
The following instructions provide an overview of the process of creating leave codes with limits, and entering balance forwards on a new Vista system. For additional information on any of the forms mentioned, refer to Related Topics below.

1. In PR Leave Codes, create a leave code, but do not specify accrual limits, available balance limits, or accrual and usage information.Note: When you create a new leave code, the Active checkbox is automatically selected. Leave selected to enable assigning the leave code to any new or existing employees (manually or via initialization).

1. Assign the leave code to applicable employees. You can initialize multiple employees by selecting Initialize Employees or you can assign employees manually using the Employee Leave tab on PR Leave Codes. Note: If you select Initialize Employees, the system displays the PR Employee Leave Initialization form. Use this form to initialize employees by group. For more information, see [Initialize a Leave Code for Multiple Employees](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/initialize-a-leave-code-for-multiple-employees).

1. In PR Leave Entry, enter any leave balance forwards and process/post the batch.

1. Run the PR Employee Leave Balance & Accumulation report to verify that you have entered the balance forward information correctly.

1. In PR Leave Codes, enter the Accrual Limit and Available Balance Limit information for the leave code.

1. In PR Employee Leave, if applicable, enter Accrual Limit or Available Balance Limit overrides for specific employees.

1. In PR Leave Code Reset, reset the accrual accumulator limits. Note: Do not run PR Leave Code Reset for available balances at this time, or you will delete all the balance forward information that you previously entered and you will have to restart the process.

Once you run the reset, you can process leave normally throughout the year or at whatever frequency limits you specify. For more information, see [About Processing Employee Leave](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/about-processing-employee-leave).

Related information

- [PR Leave Codes Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form)

- [PR Leave Entry Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form)

- [PR Employee Leave Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form)

- [PR Employee Leave Initialization Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-employee-leave-initialization-form)

- [PR Leave Code Reset Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form)
