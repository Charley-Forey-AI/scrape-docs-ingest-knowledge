---
title: "Build Electronic Data File - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/build-electronic-data-file/build-electronic-data-file---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/build-electronic-data-file/build-electronic-data-file---field-descriptions"
---

# Build Electronic Data File - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Table
Enter the table code or master table code that you want to use when building the electronic data file, or double-click on this field to select from a list of available table codes. When a master table code is selected, you will be prompted to make additional selections based on the first electronic data file.

Employee
Double-click in this field to select from a list of employee codes.

Home department
Double-click in this field to select from a list of valid payroll departments.

Employee status
Double-click in this field to select from a list of employee status codes.

From/to check or period end date
The screen prompts for a check or period end date based on the header information from the selected file.

Export file name
This field displays the default file name that is dependent on setup in Electronic File Table Maintenance; for example, the file name may be comprised of an identifier code and a date. The identifier code is unique to the operating company and comes from the Company  field in the Company Installation screen. The date portion of the file name is the current Payroll processing date.
If a master table code was selected in the Table field, when the file is exported, the update concatenates all of the data files specified in the Electronic Master File Maintenance screen for the specified master table. The data files are built in the sequence specified in the master table, and each successive file begins on the very next row (no blanks or page breaks).

Export button
Click this button to run the update and generate the electronic data file.
