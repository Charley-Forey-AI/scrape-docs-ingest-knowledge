---
title: "PR Employee Accumulations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employee-accumulations-form"
---

# PR Employee Accumulations Form

The PR Employee Accumulations form enables you to manually access and maintain the monthly totals of earnings, deductions, and liabilities for each employee.
This form is used initially while implementing Vista to set up earnings, deductions, and liabilities that are tax-related and/or have annual limits. Once the system is set up, these accumulations are automatically updated, so you may not need to use this form after the initial implementation.
However, there are cases where you may want to add data or edit existing data (U.S. only). This includes using the form to:

- insert values not otherwise directly related to an existing PR Timecard or the processing of a timecard for end-of-year reporting.

- enter balance forward information when upgrading Vista mid-year.

Note: For Australian and Canadian companies, you can only add new
 accumulations records in this form. If you need to edit the details for an existing
 accumulations record, you must use the PR Employee Accums Detail form (accessed by
 double-clicking a record in the grid).When you add a new
 accumulations record, the system automatically adds a single accumulations
 detail record in the PR Employee Accums Detail form for the new
 employee/month/type/EDL code. Once added, you can edit the record as needed in
 PR Employee Accums Detail.

## Adding Accumulations When Going Live with Vista

Accumulations are stored by month, so it is important to enter data appropriately to generate accurate quarterly reports.
To enter data at go live:

- If going live at the beginning of a calendar quarter, enter total year-to-date accumulations in the month prior to the live month.

- If starting in the middle of a quarter, enter year-to-date accumulations through the prior quarter into the last month of the prior quarter. Enter quarter-to-date accumulations in the month prior to the live month.

## About Deductions, Subject Amounts, and Eligible Amounts

Subject amounts include all earnings subject to the deduction, even amounts not included in the calculation basis (e.g., earnings flagged as "subject only" in PR Earnings Codes, and earnings exceeding the subject limit).
Eligible amounts include only those earnings used in the calculation basis for the deduction amount. This amount will be 0.00 once the subject limit is reached, but can be negative if the deduction's Auto Correct if Limit is Exceeded option in PR Deductions/Liabilities is checked and the limit has been exceeded.
For W-2s (US), the federal, FICA, and state wages are pulled from the subject amount of the deductions and not the earnings section of the accumulations. If there is a limit on the deduction, such as FICA, the eligible amount is used. The eligible amount is the amount that is subject to the deduction/liability, up to the subject limit.

[Add or Edit Employee Accumulations Records (US)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/add-or-edit-employee-accumulations-records-us)
[Add Employee Accumulations Records (CA)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/add-employee-accumulations-records-ca)
[Add New or Edit Existing Accums Detail Records (CA)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/add-employee-accumulations-records-ca/add-new-or-edit-existing-accums-detail-records-ca)
[Add Employee Accumulations Records (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/add-employee-accumulations-records-au)
[Add New or Edit Existing Accums Detail Records (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/add-employee-accumulations-records-au/add-new-or-edit-existing-accums-detail-records-au)
