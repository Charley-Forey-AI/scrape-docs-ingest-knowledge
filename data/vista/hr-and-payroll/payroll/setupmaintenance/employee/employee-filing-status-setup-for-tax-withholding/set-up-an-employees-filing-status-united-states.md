---
title: "Set up an Employee's Filing Status: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/employee-filing-status-setup-for-tax-withholding/set-up-an-employees-filing-status-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/employee-filing-status-setup-for-tax-withholding/set-up-an-employees-filing-status-united-states"
---

# Set up an Employee's Filing Status: United States

You can use the Filing Status tab in PR Employees to set up
 employee filing statuses for tax withholding.
You can also enter the same information in PR Employee Dedns/Liabs; on that form you can also override the calculation or indicate an add-on amount. However, this tab is more streamlined if you just need to enter the filing status and indicate the number of exemptions.
The following instructions detail how to set up an employee's filing status for tax withholding.

1. In the Dedn
 Code field, enter a deduction code or press F4
 to select from a list of valid deduction codes.

1. In the Filing
 Status drop-down, select the filing status for the employee. For
 a description of all available statuses, see [Filing Status ](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form/field-definitions-pr-employees-form#ID-000383e6--en).

1. In the Regular
 Exempts field, enter the number of exemptions/allowances claimed
 on the employee's W-4.

1. In the Add'l
 Exempts field, enter the number of any additional
 exemptions/allowances claimed on the employee's W-4.

1. Repeat steps 1-4 for any additional deduction codes that you need to add for the employee. Note: The Override Misc Amount #1,
 Misc Amount #1, and Misc Factor fields are
 only used for a few states. For information on these fields, review the F1
 help.

1. Optionally, you can
 select File > Synchronize HR to update all fields on the W4 Info tab in HR Resources (provided
 that you checked the W-4 Info box in the PR Update
 Options section of HR Company Parameters).It is not always necessary to define a
 state filing status if it is the same as the employee’s federal filing status.
 If a state filing status has not been defined for an employee, the system
 automatically uses the federal filing status. However, it is very important to
 check for any special requirements defined for the state to determine whether
 you will need to set up a separate filing status.Note: If the employee is exempt, assign the deduction code
 to the employee on the Filing Status tab. Then, in PR Employee Dedns/Liabs,
 for the assigned deduction code, select the Override
 with a fixed amount option from the Calculations section and enter 0.00 in the Rate/Amount
 field.

Related information

- [Employee Filing Status Setup for Tax Withholding](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/employee-filing-status-setup-for-tax-withholding)

- [Set up an Employee's Filing Status for PAYG Withholding (Australia)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/employee-filing-status-setup-for-tax-withholding/set-up-an-employees-filing-status-for-payg-withholding-australia)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Employee Dedns/Liabs Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-dednsliabs-form)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [About the HR Company Parameters Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-parameters-form)
