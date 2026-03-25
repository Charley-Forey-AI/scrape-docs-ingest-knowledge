---
title: "About Leave Code Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/about-leave-code-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/about-creating-leave-codes/about-leave-code-settings"
---

# About Leave Code Settings

When creating leave codes in PR Leave Codes, you will need to determine a variety of settings.
These settings include the accrual type, accrual accumulation limits, balance limits, and accrual and usage information. You can override all of these settings per employee using PR Employee Leave. This topic discusses how each of these settings work and how they affect leave accrual and usage.

## Setting the Accrual Type

You can associate one of two accrual types with a leave code: Fixed Amount or Rate-Based. Use fixed amount leave codes to accrue leave units based on a specific frequency. For example, you could use a fixed amount for employees who earn 80 hours of vacation per year. Use rate-based leave codes to have leave accrue at a rate based on applicable earnings codes. For example, you could use this for an employee who earns .5 hours of vacation time for each hour worked.

## Using Accrual Limits

Accrual limits allow you to limit the amount of leave that can accrue per leave code. You can track leave code accruals for up to two periods, such as monthly and yearly. Each accrual limit has a separate limit and reset frequency (how often the leave units are set back to zero).
Note: Use the PR Leave Code Reset form to reset accrual frequencies. For more information, see [PR Leave Code Reset](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-code-reset-form).

Using accrual limits is optional, but if you are creating a fixed amount leave code, it is advisable to include an accrual limit. The system does not prevent you from running the PR Auto Leave Accrual/Usage form more than once in the specified accrual frequency period. This may cause you to inadvertently add additional leave to employee balances.
When implementing leave codes on a new Vista™ system, you should not specify accrual accumulation and available balance limitations until after you enter any balance forwards from your legacy system. For more information, refer to [Implementing Leave Codes](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes).

## Limiting Available Balances

You can limit the available balance for a leave code. This caps the amount of leave that accrues for the leave code. When setting a balance limit, you can also specify a reset frequency, which determines when the balance is set back to zero.
Additionally, you can set a carryover limit that enables leave to pass through to the next time-period (frequency). When setting a carryover limit, you should ensure that the available balance limit accommodates any additional leave that you specify for the carryover. For example, if you have a fixed amount leave code that accrues 80 hours per year, and has a carryover limit of 40, the available balance limit should be 120.

## Setting Accrual and Usage Information for Leave Codes

Use the Accrual/Usage Info tab to track usage for both fixed amount and rate-based leave codes. You will also use this tab to assign earnings codes that determine when rate-based leave accrues.
This tab lists all earnings codes that affect this leave code, whether through usage or accrual. Each earnings code is associated with a basis and rate; the system multiplies the basis by the rate to determine the rate of leave accrual or usage for the earnings code. The basis can be in either hours or an amount. Typically, when setting up a leave code, the basis will be in hours. For example, if an employee earns .025 hours of leaver per hour worked, enter a basis of hours with a rate of .025.

## Active Status

When you add a new leave code, the system automatically defaults the Active checkbox as selected. Although you can deselect this checkbox if needed, you must select this checkbox before you can assign the leave code to employees in PR Employee Leave (manually or via initialization).
If you deactivate a leave code after you have already assigned it to employees, the system prompts you to deactivate the leave code for the applicable employees. If you reactivate a leave code, you must manually reactivate it for all applicable employees.

Related information

- [PR Leave Codes Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-codes-form)

- [Employee Leave Tracking](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes/employee-leave-tracking)

- [Implement Leave Codes](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/implement-leave-codes)

- [PR Employee Leave Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-leave-form)
