---
title: "Canadian Vacation Pay | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/canadian-vacation-pay"
---

# Canadian Vacation Pay

Employees working in Canada must be paid for vacation based
 on a statutory vacation rate that is either accrued or paid to the employee on their
 paycheck.
This rate can vary by employee. In order to streamline this process, Payroll 'recurring
 add-ons' offer a calculation method that adds vacation pay to each time card line and
 distributes the vacation expense based on that time card line (for example, for a 'Direct job
 cost' line, the 'vacation pay' add-on will be charged to the same job and phase).
When setting up the 'Percent of gross by time card' add-on code in Deduction / Add-on Code Maintenance, the Payroll Administrator will be able to specify which types of direct cost time card lines to include, and the applicable G/L account code to debit for each authorized type. Users can specify whether to pay union benefits on the 'vacation pay'. Users can specify any other add-on codes stored in the time card file that should also be included in the calculation. These new codes can be set up with Tax Effects, and can either be paid to the employee on the check or accrued for later disbursal. Employee balances can be 'cleared' at year end or rolled over into the following year. Employers using this calculation method can track employee accrued vacation balances and vacation hours paid through the [Add-on History Report](/en/spectrum/spectrum/accounting/payroll/employees/employee-reports/add-on-history-report).
After the add-on code has been defined, the Payroll Administrator will add a recurring entry to each qualifying employee in Employee Recurring Deductions / Add-ons. It is also possible to set this code up as a Human Resources benefit, for use in Authorize Recurring Benefits, Benefit Management and the Employee Benefits page.

## Sample Setup for Canadian Vacation Pay

There are three types of add-ons that may be used for Canadian Vacation Pay:

- Software
 automatically calculates 'Percent of gross by time card' during Check Calculation
 and adds the amount to the employee's current paycheck. Say that
 Employee A elects to receive vacation pay on every check. In this case, the first
 type of add-on will be assigned in Employee Recurring Deductions/ Add-ons. To manage
 vacation pay for this case, this employee will be assigned sample add-on code
 VPAYNOW, detailed
 below.

- Software
 automatically calculates 'Percent of gross by time card' during Check Calculation
 and accrues the amount to the employee's 'vacation benefit balance'.
 Say that Employee B elects to keep a running balance of vacation earned week-to-week,
 and then draws down the balance on the paycheck when the vacation time occurs. In
 this case, the second type of add-on will be assigned in Employee Recurring
 Deductions/ Add-ons. To manage vacation pay for this case, this employee will be
 assigned sample add-on code VACCRUE, detailed below.

- Time card entry is added for 'Payout' of vacation taken from the
 'vacation benefit balance'. The third type of add-on will also be used for Employee
 B. It will be entered in Time Card Entry each time Employee B actually takes a
 vacation. To manage vacation payout, this employee will have a time card with sample
 add-on code VPAYOUT, detailed below.
