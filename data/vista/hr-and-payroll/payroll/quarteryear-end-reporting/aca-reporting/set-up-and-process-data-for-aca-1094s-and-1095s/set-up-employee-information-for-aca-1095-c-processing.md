---
title: "Set Up Employee Information for ACA 1095-C Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employee-information-for-aca-1095-c-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employee-information-for-aca-1095-c-processing"
---

# Set Up Employee Information for ACA 1095-C Processing

You can manually set up employee information for 1095-C processing using the PR ACA 1095-C Employee form.
 The payroll and health insurance data entered for an employee is necessary for generating the federally mandated 1095-C reports under the United States Affordable Care Act (ACA) that will report offers of coverage made to your employees.Employers that offer employer-sponsored self-insured coverage also use Form 1095-C to report information to the IRS and to taxpayers about individuals who are covered under an employer-provided self-insured plan.
Many PR ACA 1095-C Employee fields initially default at the time a record is created in this form from the corresponding record in PR Employees for the active payroll company.Note: Beginning with year-end 2021, you must use Aatrix to create, print, and eFile 1094s and 1095s. For more information, see [Create, Print, and E-File 1094s and 1095s Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/create-print-and-e-file-1094s-and-1095s-using-aatrix).

The following steps detail how to manually set up or edit employee information for 1095 processing.Note: Users should be familiar with IRS definitions and requirements for ACA reporting before using Vista to enter ACA data. For more information, visit the Internal Revenue Service website at [www.irs.gov](http://www.irs.gov/) and search for "Instructions for Forms 1094-C and 1095-C".

1. From the main menu, select Payroll > Programs > PR ACA Process.

1. In the Tax Year field, enter the tax year.

1. Select on the Employees tab and double select a grid row to open the PR ACA 1095-C Employee form.

1. In the Employee field, enter the employee number or sort name of the employee you want to add to the crew. Press F4 for a list of employees

1. Using the Info tab, set up employee information corresponding to Part I of the 1095-C report.

1. Accept the default for the Last Name, First Name, Middle Init, SSN, Address, City, State, Zip Code, and Country fields.

1. If the employee is employed full time, select the Is Full Time checkbox.

1. If the employer provided self-insurance coverage to the employee, select the Enrolled in Employer Provided Self-Insurance checkbox.

1. If the employee consented to receive 1095s via email, select the 1095 Email Consent checkbox.Note: The 1095 Email Consent checkbox defaults based on how you set the 1095 Email Consent checkbox in PR Employees. If this field defaulted as unselected and you change it to selected, make sure the employee has an email address defined in PR Employees. For more information about this checkbox, see [1095 Email Consent](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-1095-c-employee-form/field-definitions-pr-aca-1095c-employee-form#concept-5464--en).

1. For employees who were offered minimum essential coverage (MEC) for all 12 months, set up information corresponding to Part 2 of the 1095-C report:

1. From the Offered Coverage in All 12 Months drop-down, select the appropriate option relating to offered coverage for the employee.

1. In the Employee Share All 12 Months field, enter the dollar value for the employee’s share of the lowest-cost monthly premium for self-only minimum essential coverage. If the employee is not required to contribute any amount towards the premium, enter 0.00.Note: Values defaulted or entered in this field will only be written into the 1095 if the corresponding offer code is 1B, 1C, 1D , or 1E.

1. From the Section 4980H Safe Harbor All 12 Months drop-down, select the appropriate option relating to the 12-month coverage offered.

1. From the Plan Start Month drop-down, select the calendar month in which the plan year begins. If no health plan coverage was offered, select 00 - No Health Plan Offered.

1. Save the record.

1. For employees who were offered minimum essential coverage (MEC) for fewer than 12 months, set up information corresponding to Part 2 of the 1095-C report:

1.  Select on the Monthly Offer of Coverage tab.

1. For the first applicable month, use the Offer of Coverage drop-down to select the appropriate code relating to offered coverage for the employee.

1. In the Employee Share field, enter the dollar value for the employee’s share of the lowest-cost monthly premium for self-only minimum essential coverage. If the employee is not required to contribute any amount towards the premium in a month, enter 0.00.Note: Values defaulted or entered in this field will only be written into the 1095 if the corresponding offer code is 1B, 1C, 1D , or 1E.

1. From the Section 4980H Safe Harbor drop-down, select the appropriate code relating to that month's coverage offered.

1. Save the record.

1. Repeat for each remaining applicable month.

1. Set up employee and dependent information for Part 3 of the 1095-C report. You must complete this tab only if the employer provides self-insured coverage to their employees (as opposed to subscribing to a traditional health insurance plan), and the Enrolled in Employer Provided Self-Insurance checkbox has been selected on the Info tab.

1. Select on the Covered Individuals tab.

1. Confirm that the employee is listed first in the grid. If not, on the Info tab, select the Enrolled in Employer Provided Self-Insurance checkbox for the employee.

1. Accept the employee's defaults for the Last Name, MidInitial, First Name, SSN, and DOB fields.

1. If the employee is covered for all 12 months, select the Covered All 12 Months checkbox. If the employee is covered for fewer than 12 months, select the checkbox for each appropriate month.

1. To add a dependent for this employee, select the first line after the employee's entry and enter N, New, or + , in the Seq field. The system automatically assigns the next available sequential number.

1.  Fill in the dependent's Last Name, MidInitial, First Name, SSN, and DOB fields.

1. If the dependent is covered for all 12 months, select the Covered All 12 Months checkbox. If the dependent is covered for fewer than 12 months, select the checkbox for each appropriate month.

1. Save the record.

1. Repeat for any additional dependents as needed.

Related information

- [PR ACA Process Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-process-form)

- [PR ACA 1095-C Employee Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-1095-c-employee-form)

- [Initialize ACA Data Automatically from Human Resources](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-human-resources)

- [Initialize ACA Data Automatically from Payroll](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-payroll)
