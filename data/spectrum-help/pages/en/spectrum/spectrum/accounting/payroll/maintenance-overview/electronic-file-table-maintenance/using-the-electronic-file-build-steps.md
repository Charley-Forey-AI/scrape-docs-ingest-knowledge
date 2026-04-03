---
title: "Using the Electronic File Build Steps | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps"
---

# Using the Electronic File Build Steps

This brief tutorial explains the steps involved in setting
 up the file structure as well as how to build the file and review the resulting data using the
 structure you created.
Occasionally you may want to set up your own 401(k) text
 files, unemployment text files, worker's compensation text files, or other third party
 files using Payroll information. Before you begin, it is recommended
 that you:

1. Design the desired report on paper. This will help you to determine what information you want to pull from Spectrum.

1. Familiarize yourself with the available Spectrum tables and determine which tables are needed. The available tables include:

- MISC (Miscellaneous non-file variables)

- PA.INFO (Company Information)

- PR.EEO (EEO Classification)

- PR.EHIST (Check History) [Note](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/note)

- PR.EHVD (Check History Deductions / Add-ons) [Note](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/note)

- PR.EM1 (Employee Master)

- PR.TAX_TABLE (Non-company specific tax table)

- PR.STHIS (State History Tax)

- PR.UDEMP (Employee Master User-Defined Fields)

- PR.VDCTL (Payroll Deductions / Add-ons Master) [Note](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/note)te

- PR.WCCTL (Worker's Compensation Master)

- PR.WCHIS (Employee Worker's Compensation History)
Note: This list of tables is also available
 in the Search File Variables window.

1. Familiarize yourself with the Formula
 File Maintenance screen. Knowledge of this screen will help you to
 understand how formulas are set up in Spectrum.

1. Determine what formulas and/or categories you need to include before you set up
 your build file structure. For example, if you are going to be giving all employees a
 pay raise based on a percentage of their current salary, you would need to set up a
 formula that took the employee's earnings and multiplied this amount by a certain
 percent.

1. Click on the Maintenance  >  Electronic File Table Maintenance  >  Formulas button. Enter any formulas you may need here and then print the
 listing report to review the results. Continuing with our example, you would set up a
 formula that looked at the PR.EHIST (the check history file) as the first factor
 multiplied by the percentage increase as the second factor (for example, .05 would
 yield a 5% raise). See the [Electronic File Formula Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-formula-maintenance) topic for more information.

1. Click on the Maintenance  >  Electronic File Table Maintenance  >  Categories button. This feature is handy if, for example, you wanted to include
 only the amount of your employee's 401(k) deductions in the text file. Enter any
 deduction or add-on categories you may need here and then print the listing report to
 review the results. See the [Electronic Category Group Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-category-group-maintenance) topic for more information.

1. Set up the file layout.

1. Click on Data Entry  >  Build Electronic Data
 File and complete the screen using the table information you just set up in
 the Electronic File Table Maintenance
 screen. You are given the option to print the results or save them as an
 electronic file.

Related information

- [Setting up the File Layout](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/setting-up-the-file-layout)

- [Setting up Formulas](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/setting-up-formulas)

- [Example #1: Employee Raise](/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-1-employee-raise)

- [Example #2: Employee File Including Add-Ons](/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-2-employee-file-including-add-ons)
