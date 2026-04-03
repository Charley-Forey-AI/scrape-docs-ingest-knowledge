---
title: "Other Information for LCPTracker File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/payroll-reports/certified-payroll-report/other-information-for-lcptracker-file"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/payroll-reports/certified-payroll-report/other-information-for-lcptracker-file"
---

# Other Information for LCPTracker File

An Excel file can be uploaded into LCPTracker, saving the user from having to enter data manually.
For an overview of the LCPTracker file, see [LCPTracker XLS Format](/en/spectrum/spectrum/accounting/payroll/payroll-reports/certified-payroll-report/other-information-for-lcptracker-file/lcptracker-xls-format).

## Union File Maintenance

By union, enter the Certified craft code. These numerical codes come from the state or agency to
which the payroll is being submitted. Enter only the code in this field, as entry of the description will
cause errors.
Non-union employers must set up a cash fringe add-on code with calculation method of Prevailing
Wage Adjustment, and health and welfare add-on code with calculation method of Health and
Welfare.

## Wage Code Maintenance

By wage code, enter the 'Certified labor code'. These numerical codes come from the state or agency to
which the payroll is being submitted. Enter only the code, as its description is not part of the XML file.

## Apprentice Program

Certain states or agencies require reporting apprentice information by employee.
On the Employee Pay Rates page, select the Apprentice program checkbox and enter the employee's
apprentice ID # from an approved program. The Wage % field is used to record the percentage of the full
classification wage rate to be paid to the apprentice based on the apprentice program.

## Job Main Properties

Enter the project's Contract number in Job Main Properties.

## Job Payroll Set up

Enter the Work state on the Job Main Properties screen. This field is required, as the Certified Benefit
mapping will not work without a work state specified.Note: The 'Work state' entered here must be the same as was used as the 'Job state' when
defining the Certified Benefit Program above. It is the state code that links this job to the correct benefit
program.
On the Job Payroll Setup, select the Certified payroll checkbox and either the Davis-Bacon or
Prevailing wage job checkbox.
Enter the project ID number for the project in the Certified project ID field.

## Creating the LCPTracker Excel File

Within Spectrum, the Certified Payroll Report screen is used to create the file. Preview the report prior to creating the file and submitting it. Select the file
format and select Preview to start compiling the file. Once complete, it downloads to
your workstation.
This format does not use all of the available selections on the start screen. Only the following fields are
used: Job numberWhile you can enter more than one job at a time, best practice is
to create the export file on a job-by-job basis.
Pay periodEnter the pay period end date.
Work week ending dateEnter the work week ending date.
Show employee address?Answer is based on the agency's requirement:

- Select the checkbox to include the address.

- Leave the checkbox clear to omit the address from the file.

Show entire social security
number?Answer is based on the agency's requirement:

- Select the checkbox to identify the employee with their
full SSN.

- Leave the checkbox clear to identify using the last four digits of the
SSN (Partial SSN).

Identify workers using
employee code?Answer is based on the agency's requirement:

- Select to identify using the employee code. When this
checkbox is selected, no SSN information will be
included in the file.

- Leave the checkbox clear to use the SSN or partial SSN.
