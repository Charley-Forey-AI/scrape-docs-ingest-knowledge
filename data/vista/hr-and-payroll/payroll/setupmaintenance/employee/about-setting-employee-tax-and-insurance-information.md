---
title: "About Setting Employee Tax and Insurance Information | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-setting-employee-tax-and-insurance-information"
---

# About Setting Employee Tax and Insurance Information

You can set up tax, unemployment, and insurance timecard
 defaults for employees in PR Employees.
The information that you specify on this form depends on where the employee lives, where the employee works, and your company's location.
The following list provides a list of typical examples of how you might set up tax and insurance information for your employees.

- If an employee lives and works in the same state,
 enter the applicable information in the Resident Tax State,
 Resident Unemp State, Resident Ins State, and
 Resident Local Code fields. When you create a timecard
 batch, the system defaults information from these fields.

- If an employee lives in one state, and the work
 location is in a different state, enter the work location information in the
 Work Office Tax State field. When creating a timecard entry
 for the employee, the system checks to see if there is a reciprocal
 agreement between these two states and defaults the information from the
 Resident fields.

- If an employee lives in one city/county, and the
 work location is in a different city/county, enter the work location
 information in the Work Office Local Code
 field.

Note: If you have entered information in the Office
 State or the Office Local fields in PR Company
 Parameters, the system checks these fields for reciprocal agreements instead of the
 Work
 Office Tax State and the Work Office Local Code fields.

- If you want to use tax,
 unemployment, and insurance information from a job when entering
 timecards, [set the appropriate options in PR Company
 Parameters](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). When entering a job timecard for an employee, the
 tax, unemployment, and insurance state defaults from JC Jobs (PR
 State field). For non-job employees, or if a job is not
 specified, the system uses the state or local information from the
 Office State or
 Office Local fields
 in PR Company Parameters (State/Local) tab. If those fields are blank,
 the system uses the Work Office fields in PR Employees. If those fields
 are blank, the system uses the Resident fields in PR Employees .

- If you want to use tax,
 unemployment, and insurance information from an SM work order when
 entering timecards, [set the appropriate options in PR Company
 Parameters](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information). When entering an SM Work Order timecard for an
 employee, the tax, unemployment, and insurance state defaults from the
 work order (PR State field, SM
 Work Orders). If a PR State is not specified on the work order, the
 system uses the system uses the Resident fields in PR Employees.

- If you have set tax,
 unemployment, or insurance information to default from a job or SM work
 order, and you want information to default from PR Employees for
 specific employees, select the appropriate checkboxes in the Default
 Options - Always use Employee's Work/Resident section of PR Employees.
 When you check one of these boxes, the system will default the
 corresponding values from the Work Office fields in PR Timecard Entry.
 If those fields are blank, then the system defaults information from the
 Resident fields in PR Employees.

Note: This situation might occur when you have some employees
 working in a remote office in a different state than the state where your company is
 actually located. In this situation, you would want to use the state that you
 specify in Work Office Tax State field (PR Employees).
For more detailed default information, refer to the
 F1 help for the following PR Timecard Entry fields: [Ins State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b0e7--en), [Tax State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b148--en), [Local ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b1ba--en), and [Unemp State ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form/field-definitions-pr-timecard-entry-form#ID-0003b23a--en).

Related information

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [About Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)
