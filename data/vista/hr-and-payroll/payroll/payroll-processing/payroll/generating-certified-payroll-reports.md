---
title: "Generating Certified Payroll Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/generating-certified-payroll-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/generating-certified-payroll-reports"
---

# Generating Certified Payroll Reports

Certified Payroll reports are used to confirm that correct Prevailing Wages have been paid. Use these instructions to extract and submit certified payroll reports that meet federal requirements or that are transmitted to third parties to meet other requirements.
You can generate and submit certified payroll reports in two ways.

- Vista standard reports, which comply with basic federal requirements.

- Third-party-assisted reporting that complies with more specific reporting formats and methods, as well as more comprehensive Certified Payroll Reporting (CPR) compliance services that meet specific jurisdictional CPR requirements.

Before you generate certified reports, you must set timecards to be certified. Once you have done that, you can generate reports.

Setting Timecard Records as CertifiedYou can set timecards to be certified manually during timecard entry or have the system automatically apply the setting to the timecard lines prior to timecard entry. The following steps outline how to have the system apply the setting automatically and how to change the settings that affect reports.

1. There are four different ways you can have the system apply an initial default setting to timecards. Select from any of the following:

- If you want all timecard lines for an employee to default to certified, select the Include on Certified Reports checkbox for that employee in the PR Employees form, Add'l Info tab.

- If you want all timecard lines from a job to default to certified, select the Certified Payroll checkbox for that job in the JC Jobs form, PR Info tab.

- If you want all timecard lines related to a service site or to a work order to default to certified, select the Certified Payroll checkbox in the SM Work Orders or SM Service Sites forms.

- If you want all timecard lines related to a PM Project to default as certified, select the Certified checkbox for that project in the PM Projects form, PR Info tab.

1. If you want a liability to print in a standard certified payroll report on a separate line with a description, select the Print as separate detail line on standard certified reports checkbox for the applicable liability in the PR Deductions/Liabilities form.

1. If you want an earnings code broken out on its own detail line of a standard certified payroll report, select the Include detail on certified reports checkbox for the applicable earnings code in the PR Earning Codes form.

1. If you are using a third party vendor to generate and submit certified payroll reports, do the following as necessary:

- For both eMars and LCPtracker, in the PR Deductions/Liabilities form:

- make a selection in the Dedn Class Type field for all deductions

- make a selection in the Fringe Benefit Type field for any applicable liabilities

- For both eMars and LCPtracker, in the PR Earnings Codes form, make a selection in the Fringe Benefit Type field for any applicable earnings codes.

- For eMars only, in the PR Craft Classes form, for EEO classes A-Apprentice and T-Trainee:

- in the Wage Pct field, enter a whole-number value for any applicable craft classes. See [Wage Pct](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form/field-definitions-pr-craft-classes-form#ID-00035fba--en) for more details.

- in the Apprentice Level field, enter the apprentice level, 1 through 9. See [Apprentice Level](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form/field-definitions-pr-craft-classes-form#ID-00035fc9--en) for more details

Generating and Submitting Standard Certified Payroll Reports
Before you can create and submit a standard certified payroll report, you need to verify that the prevailing wage payroll has been processed properly and that employees have been paid the correct amounts.

1. In PR Reports, select and run the report that creates the best results for you:

- PR Certified Payroll Transcript

- PR Certified Report with Liabilities

1. Submit the report using the method required by the governing agency.

Generating and Submitting Third-Party Certified Payroll Reports
After payroll has been processed with the proper settings in place, take the following steps to generate and submit your report:

1. In PR Reports, select the applicable version of the PR Certified Export report:ReportReport ID
PR Certified Export Template - LCPtracker (Pre-6.19 version) 1300
PR Certified Export - LCP Tracker 1327
PR Certified Export Template - eMars (Pre-6.16 version) 1298
PR Certified Export - eMars 1315

Tip: See the Report Info tab for each version of the eMars report for more complete information

1. Enter the appropriate values in the fields of the report launcher.

1. Click Export.

1. In the RP Report Export Options form, select one of the following as directed by LCPtracker or eMars:

- Excel Format Data Only (.xls)

- Excel Format Data Only (.xlsx)

You do not need to change any of the default values that appear under your selection.

1. Click Save.

1. Follow the instructions provided by eMars or LCPtracker for transmitting the file to their site. They will file the report for you using the format and method required by the governing agency.

Related information

- [Prevailing Wage Calculations](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/prevailing-wage-calculations)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)
