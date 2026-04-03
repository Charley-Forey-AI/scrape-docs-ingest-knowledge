---
title: "New User-Defined Field | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/new-user-defined-field"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/new-user-defined-field"
---

# New User-Defined Field

Use this window to add new General Ledger user-defined fields.
Field
Description

Company
Enter the code for the company that will use this user-defined field, or click the drop-down arrow to select from a list of valid company codes.

Type
Enter one of three types of user-defined fields:

- Alpha: This text field type supports up to 20 characters and a validated table of answers. To create this list, select the Validated checkbox. Click the Validation Codes button to define valid entries and descriptions.

- Date: This field type contains numerical dates. Like other date fields in Spectrum, enter the day and the system will complete the rest of the entry.

- Numeric: You can define the numeric mask. This field type contains dollar amounts and numeric figures. It supports up to 14 digits before the decimal point.

Prompt
Enter the field title (for example, DUE DATE).

Validated
This checkbox is only available for Alpha type user-defined fields. Select it if you want to enter user-defined validation codes. Press Enter or click OK to display the [User-Defined Fields Validation](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-user-defined-fields-maintenance/user-defined-fields-validation) window.

Mask
This field is only available for Numeric type fields. Enter the user-defined field's alignment mask.
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

When a report is initially created, the software produces a default display code, but the default may be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed.
Table of display codes:

Status
Select the user-defined field's status: Active or Not used.
