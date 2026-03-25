---
title: "Create a Fixed Amount Leave Code | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/create-a-fixed-amount-leave-code"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/create-a-fixed-amount-leave-code"
---

# Create a Fixed Amount Leave Code

The following describes how to create fixed amount leave codes.

1. Select Payroll > Programs > PR Leave Codes.

1. In the Leave Code and Description fields, enter an ID and description for the code, respectively.

1. The Active checkbox is automatically selected when adding a new code. You can deselect this checkbox if needed; however, you must set the code to Active prior to assigning it to employees in PR Employee Leave.

1. In the UM field, enter a unit of measure (typically hours) or press F4 for a list of valid UMs.

1. From the Leave Balance Warning Level dropdown, choose one of the following options:

- Allowed w/Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, the system displays an error message on the HQ Batch Control Error List report, but you can post the batch.

- Allowed w/o Warning - If you select this option and the employee has a negative leave balance, with no other errors during batch validation, the system will not display an error message on the HQ Batch Control Error List report and you can post the batch.

- Not Allowed - If you select this option and the employee has a negative leave balance, the system displays an error message on the HQ Batch Control Error List report and you will be unable to post the batch.

The option selected here determines how the system will process a leave entry batch. You can override this setting at the employee level in the PR Employee Leave form.

1. In the Accrual Type section, select the Fixed Amount radio button.

1. In the Units field, enter the leave accrual amount.

1. In the Accrual Frequency field, specify how often accrual occurs.

1. If applicable, use the Accrual Limit #1 and Accrual Limit #2 sections to set the primary and secondary accrual limits and reset frequencies. Note: Typically, you will set accrual limits for fixed amount leave codes. The system does not prevent you from running the PR Auto Leave Accrual/Usage form more than once in the specified accrual frequency period. This may cause you to inadvertently add additional leave to employee balances.
Important: When implementing leave codes on a new Vista™ system, you should not specify accrual limits and available balance limits until after you enter any balance forwards from your legacy system. For more information, see [Implementing Leave Codes](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes).

1. If applicable, use the Available Balance Limit section to enter the limit, frequency, and carryover limit for the leave code.

1. Use the Accrual/Usage tab to enter accrual and usage information (earn codes, accrual types, and rates) for the leave code. For more information, see [Set Accrual and Usage Information](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/set-accrual-and-usage-information).

1. Save the record.

Once you have created a leave code, you must assign it to applicable employees. You can do this by either manually adding it for employees (using the Employee Leave related grid tab or PR Employee Leave form), or by initializing employees (via the Initialize Employees button).For more information about manually adding employees, see [PR Employee Leave](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form). For more information about initializing employees, see [Initializing Leave Codes for Multiple Employees](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/initialize-a-leave-code-for-multiple-employees).
