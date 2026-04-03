---
title: "Build Electronic Data File | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file"
---

# Build Electronic Data File

Use this screen to produce an electronic data file based on
 the table setup in Electronic File Table Maintenance.
You can filter the table information by selecting an employee code, home
 department, or employee status. After the build is run, you can either save it as an
 electronic file or print it using the Crystal-Link Preview.
 When compiling the data file, this build uses the employee's current
 filing status for the particular tax code to look up the data whenever an employee is known
 and a filing status for that code is present (on the 'Taxes' tab in the
 Employees screen). The filling status will be <blank> if
 the tax code is not set up for the employee in Employees (or an invalid filing status is
 found for the employee).In this case, the Update uses the SINGLE filing status. When
 including variables from the PR_TAX_TABLE table in an Electronic Data File, it is
 recommended that the SINGLE filing status be added to any tax tables that will be included
 in the Electronic File Build if it is not already set up in Tax Table
 Maintenance. This is because it will be used secondarily (in the hierarchy)
 if an employee is encountered with incomplete or invalid setup.

Related information

- [Build Electronic Data File - Create File](/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/build-electronic-data-file---create-file)

- [Build Electronic Data File - Send to Printer](/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/build-electronic-data-file---send-to-printer)
