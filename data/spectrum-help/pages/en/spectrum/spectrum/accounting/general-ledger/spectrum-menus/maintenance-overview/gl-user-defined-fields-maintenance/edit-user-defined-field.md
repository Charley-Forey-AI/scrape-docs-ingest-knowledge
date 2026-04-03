---
title: "Edit User-Defined Field | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-user-defined-fields-maintenance/edit-user-defined-field"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-user-defined-fields-maintenance/edit-user-defined-field"
---

# Edit User-Defined Field

Use this window to edit the user-defined fields found on the G/L User-Defined Fields Maintenance screen.
Field
Description

Type
The field type (Alpha, Date, or Numeric ) displays.

Prompt
Enter the title for this field (for example: DUE DATE), or press Enter to accept the current title.

Validated?
This checkbox is only available for Alpha type user-defined fields. Select it if you want to enter user-defined validation codes. Press Enter or click OK to display the User-Defined Fields Validation window.

Mask
 This field is only available for Numeric user-defined fields. Edit the user-defined field's alignment mask, or press Enter to accept the current mask.
Alignment mask examples:

> Mask
How it Displays
Description

999.99
005.15
Use the number "9" to define the mask and display leading zeros.

ZZZ.ZZ
50.12
Use the letter "Z" to define the mask and suppress any leading zeros.

ZZZ.9999-
45.1234-
You can also combine "Zs" and "9s". For negative numbers, add a minus sign at the end of the mask.

ZZZ,ZZZ,ZZZ.999-
512,852,500.125-
You can also use commas.

When a report is initially created, the software produces a default display code, but the default may be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed. See the table below for appropriate codes.
Table of display codes:

Status
Select the user-defined field's status: Active or Not used.

Validation Codes
This button is only available for alpha type user-defined fields that have validation codes.
Click to display the User-Defined Fields Validation window.

Related information

- [User-Defined Fields Validation](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-user-defined-fields-maintenance/user-defined-fields-validation)
