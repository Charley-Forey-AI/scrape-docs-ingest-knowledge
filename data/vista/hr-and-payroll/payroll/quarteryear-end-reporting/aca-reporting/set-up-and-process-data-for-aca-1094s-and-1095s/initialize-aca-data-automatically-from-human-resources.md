---
title: "Initialize ACA Data Automatically from Human Resources | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-human-resources"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-human-resources"
---

# Initialize ACA Data Automatically from Human Resources

You can initialize ACA data for employees using the Initialize ACA option in PR ACA Process.
Initialization brings the appropriate data from elsewhere in Vista into the PR ACA Process and PR ACA 1095-C Employee forms for Affordable Care Act (ACA) compliance. You can initialize data from the Payroll or Human Resources modules, and include only full time employees or all employees.
The following instructions show you how to initialize ACA data from the Human Resources module. If you do not have access to the Human Resources module, see [Initializing ACA Data Automatically from Payroll](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/initialize-aca-data-automatically-from-payroll) for instructions.
Note: Users should be familiar with IRS definitions and requirements for ACA reporting before using Vista to enter ACA data and generate reports. For more information, visit the Internal Revenue Service website at [http://ww.irs.gov](http://www.irs.gov/) and search for "Instructions for Forms 1094-C and 1095-C".

To initialize ACA data for employees automatically from Human Resources:

1. In HR Resources, confirm that your ACA monthly coverage offer history is already set up for each resource in:

- the ACA History tab for monthly coverage offer history, and

- the ACA Tracking and Classification section of the Payroll Info tab for resource tracking and classification.

You can set up this information manually in the tabs themselves, or do so automatically using the [HR ACA Coverage Offer Init](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form) form.

1. In the PR ACA Process form, press F4 in the Tax Year field to select a tax year. If the correct tax year does not exist, enter it and save the form.

1. Select Tasks > Initialize ACA. The PR ACA Initialize form displays.

1. If you want to overwrite existing ACA data for the selected tax year, select the Overwrite Existing Data checkbox.

1. In the Initialize From section, select Human Resources.

1. In the HRCo field, enter the HR company for which you are initializing data or press F4 to select from a list of HR companies.

1. If your offered coverage is self-insured, select the Include Dependents checkbox.

1. In the Employees to Initialize section, select Full Time or All Employees. Note: Full-time employees are defined as those working 30 hours per week or 130 per month as recorded in posted timecards with earnings codes set up to track ACA hours.

1. If MEC (minimal essential coverage) was offered for all 12 months of a calendar year, select the MEC Offer checkbox.Selecting this checkbox sets the Minimum Essential Coverage section to Yes on the 1094-C form.

1. If your employees were part of an Aggregated ALE Group for all 12 months of a calendar year, select the Aggregated Group checkbox. Selecting this checkbox sets the Aggregated Group Indicator on the 1094-C form.

1. Ignore the Offer Code field. The data is pulled automatically from the ACA History tab in HR Resources.

1. If you offer self-only coverage, enter the employee share of the cost for that coverage in the Self Cost Only field. Leave it blank if you do not offer self-only coverage. Note: Values defaulted or entered in this field will be written into the 1095-C if the code in the Series One Code field on the ACA History tab of HR Resources is set to 1B, 1C, 1D , or 1E.

1. Ignore the 4980H Safe Harbor Code list. This data is pulled automatically from the ACA History tab in HR Resources.

1. From the Plan Start Month drop-down, select the calendar month in which the plan year begins. If you did not offer health plan coverage, select 00 - No Health Plan Offered. You can override this setting for individual employees in PR ACA 1095-C Employee.

1. Select Initialize to automatically populate the 1094-C and 1095-C Payroll data into the PR ACA Process and PR ACA 1095-C Employee forms.

1. Complete the remaining information manually.

When you have completed initializing and editing employer and employee data, you can then print and/or eFile your 1095s and 1094s via Aatrix. For more information, see [Create, Print, and E-File 1094s and 1095s Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/create-print-and-e-file-1094s-and-1095s-using-aatrix).

Related information

- [PR ACA 1095-C Employee Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-1095-c-employee-form)

- [PR ACA Process Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-process-form)

- [Set Up Employer Information for ACA 1094-C Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employer-information-for-aca-1094-c-processing)

- [Set Up Employee Information for ACA 1095-C Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employee-information-for-aca-1095-c-processing)

- [PR ACA Initialize Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-initialize-form)
