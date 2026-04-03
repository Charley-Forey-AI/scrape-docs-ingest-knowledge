---
title: "Merge Add-on / Deduction Codes - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/merge-add-on--deduction-codes/merge-add-on--deduction-codes---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/merge-add-on--deduction-codes/merge-add-on--deduction-codes---field-descriptions"
---

# Merge Add-on / Deduction Codes - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

New add-on/deduction code
Enter the new code you want to use to merge or replace the old code with. Up to 10 characters are allowed. You can enter multiple new codes before updating.
The new code must have been set up previously in the Deduction /
 Add-on File Maintenance screen.

Old code
Enter the old code you want to merge or replace with the new code.
The software will validate that all of the tax effects, G/L account codes, direct cost setting, week #, year-end clear flag, and A/P invoice details for the specified old code match the new code items. If these settings do not match, the old code will not be added.
The G/L account codes do not have to match for the old and new codes only if
 the Job Cost Installation > Set add-on G/L account from
 Payroll department checkbox is selected. In this case, the software will ignore
 the G/L division of the G/L account code and just verify that the account
 number portion is the same.

Descriptions
The description associated with the old code displays.

Update
Click this button to the Merge Add-on / Deductions Codes
 Listing screen. Enter the new code you want to update, or
 press Enter to
 accept the default and include ALL new codes. The listing will show the new
 code and description with the corresponding old codes and descriptions.
After the listing has been previewed or printed, the Merge Add-on /
 Deductions Codes Update screen displays. At the Proceed with update
 prompt, select Yes, proceed with
 update to continue, or No, cancel update without
 saving your changes. If you select Yes, the update will run
 through all the Payroll files and the setup screen changing the old code(s)
 to the specified new code. When the update is complete, the old codes are
 deleted from the Deduction / Add-on File Maintenance
 screen, and both the old and new codes will be removed from the new utility
 file.
Any rate per limit Worker Compensation tax codes that are flagged in the Deduction / Add-on Code Maintenance > Tax Effects screen will be included when the update is performed.
