---
title: "Change an Employee's PAYG Income Type: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/set-up-payg-withholding-for-employees/change-an-employees-payg-income-type-australia"
---

# Change an Employee's PAYG Income Type: Australia

You can change the PAYG income type for an employee (for instance, if a working holiday maker employee becomes a permanent employee) to ensure proper tax withholding and income limits.
You can change the PAYG income type for an employee to ensure proper tax withholding and income limits, as well as proper reporting. One example is when a working holiday maker employee becomes a permanent employee.
Income types are reflected on reporting periods and payment summaries in the legacy PAYG Summary features and on submissions in the STP Phase 2 feature, where they are displayed as "Income Stream Types". To ensure the correct income type is reflected for each reporting period, we recommend that you close the current reporting period to enable the system to generate a new reporting period.
The following steps guide you through this process.

When you change the income type for an employee, you
 "terminate" the employee to close the reporting period and then enter a rehire date to
 generate the new reporting period with the new income type.

1. From the Main Menu, select Payroll  > Programs  > PR Employees.

1. In the Employee field, enter the employee.

1. Click on the Add'l Info tab.

1. Deselect the Active checkbox.The Cessation Reason
 and Termination Date
 fields are enabled.

1. From the Cessation
 Reason drop-down, select Transfer.

1. In the Termination Date field, enter a termination date that falls after the starting date of the current reporting period.

1. Click Save.

1. Click on the Info tab.

1. In the PAYG Income Type field, select the new income type.

- S - Salary and Wages (SAW)

- H - Working holiday maker (WHM)

1. If you selected H - Working holiday maker
 (WHM) in the PAYG
 Income Type field, use the Country Code field to enter
 the two-letter code representing the home country of the working holiday
 maker.

1. In the Most Recent Rehire Date field, enter an effective date that falls after the Termination Date you entered above.

1. Click Save.A message displays indicating the Termination Date will be cleared.

1. Click OK.

1. Click on the Add'l Info tab.

1. Select the Active checkbox.

1. Click Save.

The Cessation Reason and Termination Date fields are
 cleared, the employee's income type is updated, and a new reporting period is
 created.
When you run year-end summaries in the legacy PAYG Summary feature, the
 system will generate a summary for each reporting period, with each summary showing the
 income type associated with its corresponding reporting period. This ensures accurate
 PAYG reporting.On the next occasion when you pay the employee and
 create an STP Phase 2 submission, reportable amounts for the employee will appear
 within the submission in records qualified by the new Income Stream Type and, if
 applicable, Income Stream Country (as indicated by the Country Code field in PR
 Employees).

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)
