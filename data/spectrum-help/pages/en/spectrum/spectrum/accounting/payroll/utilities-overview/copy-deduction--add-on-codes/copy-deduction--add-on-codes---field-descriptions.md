---
title: "Copy Deduction & Add-on Codes - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes/copy-deduction--add-on-codes---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-deduction--add-on-codes/copy-deduction--add-on-codes---field-descriptions"
---

# Copy Deduction & Add-on Codes - Field Descriptions

Use the table below for reference when completing the
 fields on this screen.
Fields/Buttons
Descriptions

Copy from
The current company code defaults in this section. Enter the deduction/add-on codes you wish to copy from, or press Enter to copy ALL the codes.
If multiple or ALL codes are selected, then you will not be allowed to access
 the Copy to code field.

Copy to
Enter the code for the company you want to copy to and the new deduction and
 add-on codes, or press Enter to accept the default of
 ALL. During the update, the system will verify that the General Ledger
 accounts and vendor codes are valid in this company. If an error is found,
 an exception report is provided.
 New codes can only be set up in companies where you have security access to
 add codes manually into the Deductions & Add-ons Code
 Maintenance screen; otherwise, the code(s) will not be
 added.

Overwrite existing codes?
Select this checkbox if you want to add new codes and overwrite your existing codes. Otherwise, accept the default and leave the checkbox clear if you want to add only those codes that are not set up yet and keep your existing codes.

Include tax effects?
Select this checkbox if you want to include tax effects with codes. If a tax code for a tax effect is used in the original company but not set up in the destination company, this particular tax effect will not be copied. In addition, if the Overwrite existing codes checkbox is clear and you select to include tax effects then the system will not copy tax effects across for deduction codes that already exist.
If you want to retain the current tax effects, accept the default and leave the checkbox clear.

Include Human Resources benefit setup?
Select this checkbox if the Human Resources module is installed and you want
 to copy information from the Data Entry > Benefit Management screen.
