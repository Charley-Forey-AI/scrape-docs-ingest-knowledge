---
title: "Set Up Mandatory Roth Catch-up Contributions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/set-up-mandatory-roth-catch-up-contributions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/set-up-mandatory-roth-catch-up-contributions"
---

# Set Up Mandatory Roth Catch-up Contributions

If your company's workplace retirement plan allows catch-up contributions, use this as a guide through the phases of configuring specific deduction codes and assigning those codes to the employees who have been identified as subject to the rule.

- Verify the current year's IRS income threshold for prior-year wages.

- The report used to identify subject employees analyzes W-2 information, so W-2s for the prior year must already be finalized (both processed and saved) for the report to be meaningful.

As of 2026, IRS regulations require that catch-up contributions for employees aged 50 and older be made on a post-tax (Roth) basis if their prior-year wages exceeded a specific threshold. To remain compliant, organizations must identify these high wage earners and ensure their catch-up deductions are directed to the appropriate Roth-designated accounts rather than traditional pre-tax 401(k) accounts.
Configuring Spectrum to handle mandatory Roth catch-ups involves three primary phases:

- Configuration - Creating or updating deduction codes specifically designated for the Roth catch-up requirement and establishing shared limits with standard 401(k) codes.

- Identification - Running a report to determine which employees meet both the age and income thresholds from the previous year.Note: Note: Income thresholds and IRS rules are subject to annual changes.

- Assignment - Associating the correct catch-up codes with eligible employee records.

1. For every group of 401(k) codes with a shared limit, that is, that have the same calculation method, [create the necessary 401(k) deduction code(s)](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code) dedicated to the catch-up rule.

- You may need multiple codes, depending on your plan rules; create a deduction code for each calculation method needed, the same as with your existing 401(k) standard and Roth contribution codes. See [Deduction Code Properties tab](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties/newedit-deductionadd-on-code---properties---field-descriptions).

- Standard Elective Deferral Limit - Determine the current standard deferral limit for 401(k) plans; the IRS adjusts it each year.

- Catch-Up Deferral Limits - Determine the additional catch-up limits for employees of certain ages; the IRS adjusts it each year.

1. Establish shared limits by linking the standard 401(k) pre-tax codes and the new Roth catch-up codes to ensure the combined total does not exceed IRS annual limits. See [Shared Limit Setup](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/shared-limit-setup).

1. Run the [Roth 401K Catch-Up Report (U.S.)](/en/spectrum/spectrum/accounting/payroll/employees/employee-reports/roth-401k-catch-up-report-u.s.) to identify which employees meet the age (50 or older) and income (adjusted annually) thresholds and are therefore required to use post-tax Roth if they want to make catch-up contributions.Note: Employees in their first year at this company and thus have no prior year W-2 income are not subject to the rule. They may contribute their catch-up contributions to a traditional pre-tax 401(k) plan if they choose.

1. Assign the code(s) you created in Step 1 to the employees you identified in Step 3. See [Employee Recurring Deductions/Add-ons](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons) and its companion [Employee Recurring Deductions/Add-ons - Field Descriptions](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-recurring-deductionsadd-ons/employee-recurring-deductionsadd-ons---field-descriptions).

- Ensure that any existing pre-tax catch-up codes are end-dated or replaced as necessary for these specific individuals.

- Set the catch-up limit to the *smaller* of the employee catch-up contribution amount or the current IRS limit.

When calculating payroll checks, once the Shared Limit has been reached, the system will process catch-up contributions as post-tax Roth deductions for the designated employees, while maintaining the correct shared limits across all 401(k) contribution types.
