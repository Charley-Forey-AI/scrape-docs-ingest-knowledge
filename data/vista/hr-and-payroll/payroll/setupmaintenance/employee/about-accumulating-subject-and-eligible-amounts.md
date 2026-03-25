---
title: "About Accumulating Subject and Eligible Amounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-accumulating-subject-and-eligible-amounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-accumulating-subject-and-eligible-amounts"
---

# About Accumulating Subject and Eligible Amounts

Subject amounts (the amount subject to the calculation of a deduction or liability) are accumulated for each deduction/liability and are used on several reports in the Payroll system.
Eligible amounts are typically accumulated to track taxes with a limit (such as FUTA, and SUTA), but can be accumulated in any deduction/liability with a limit. Accumulations are automatically maintained in the system and can be edited with the PR Employee Accumulations form.

## Subject Amounts

The Payroll system considers subject
 amounts to be all wages that are subject to a certain deduction or liability.
 Subject amounts do not stop accumulating at the limit; however, if a limit exists,
 then it is checked before calculating the amount for the deduction or liability. If
 the limit has been reached, then the subject amount is accumulated, but the
 calculation is not made for it. The limit is also checked when W-2s are run so that
 correct amounts are printed.
This system of updating subject amounts
 works well when limits (such as SUTA) are changed mid-year because the system will
 recognize that the deduction/liability needs to be calculated based on the limit.
 When determining if a liability or deduction should be taken, the system compares
 the annual limit from PR Deductions & Liabilities (which is the annual income
 limit times the rate) to the year-to-date deduction/liability amount. If the
 year-to-date amount is lower than the annual limit, then the system calculates the
 deduction/liability by multiplying the pay period subject amount by the rate (making
 sure not to exceed the annual limit).

## Eligible Amounts

 The eligible amount is the subject
 amount up to the annual limit for the deduction/liability being reported or tracked.
 Eligible amounts stop accumulating when the limit is reached, whereas subject
 amounts continue to increase, but the deduction or liability is not accumulated once
 the system determines the limit has been reached. The eligible amount is tracked for
 unemployment deduction/liabilities.

Related information

- [PR Employee Accumulations Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form)
