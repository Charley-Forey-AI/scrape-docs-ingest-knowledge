---
title: "About the Processing Seq # | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-the-processing-seq-"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-the-processing-seq-"
---

# About the Processing Seq #

When you are setting up employee-based deductions and
 liabilities in PR Employee Dedns / Liabilities (deduction/liability codes with the Employee-Based
 checkbox selected), you will need to specify a processing sequence number.
The processing sequence number controls the order in which an employee-based deduction/liability is calculated (ascending). Employee deductions that calculate as a rate of net should be set up to process last.
If you have set up wage garnishments for an employee, it is particularly important that you correctly assign the processing sequence based on the standard precedence:

1. Tax levies (payment of federal and state back-taxes)

1. Child support orders

1. Other garnishments

1. Student loans and other federal garnishments
The only time a tax levy can be processed after child support would be if the child support order was received by the employer prior to the tax levy.

Related information

- [Set Up Garnishments](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-garnishments)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)
