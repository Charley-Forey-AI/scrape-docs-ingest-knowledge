---
title: "New/Edit Positive Pay Format - Properties tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/newedit-positive-pay-format---properties-tab"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/newedit-positive-pay-format---properties-tab"
---

# New/Edit Positive Pay Format - Properties tab

Use the Properties tab to define positive pay export parameters for the selected format code. Once you have made your selections in the window, click OK to return to the Positive Pay File Maintenance screen. All of the selections you make in this window will be applied to the selected format code.
Field
Description

Format code
Enter a format code and description.

Format summary

Description
Enter a description for the format code.

Data type
Select the file data type:

- Delimited

- Fixed width

Delimiter
If Delimited is selected in the Data type field, select the type of field delimiter you want to use in the export file:

- Comma

- Tab

- Semicolon

- Space

Delimiters can also be single characters such as 'Q' or 'X'.
Note: The delimiter options uses quotation marks around any
 strings that contain the delimiter. Any strings that contain quotation marks
 will be automatically converted to double quotation marks; this is the same
 method used by Microsoft Excel when creating .csv files.

Transfer file name
Enter the transfer file name, including the path, to use as a default when exporting files for the selected format code.

Identifier file name
Enter the file name, including the path, of the file containing the identifier text. Entry in this field is optional.
The file name entered here will also serve as a transmission header for banks that require two header lines.

Check type constants

Issued check code
Enter the code for the issued and void check formats. This constant will be included on the Detail tab for checks only if it is selected from the MISC table.

Void check code

Detail options

Include net-zero checks ($0.00)?
Select this checkbox if you want to include void and Accounts Payable net-zero checks on the export.

Show original check amount on void records?
Select this checkbox if you want to display the original check amount on voided checks.

Automatically capitalize alpha characters?
Select this checkbox if you want to automatically capitalize alphabetical characters in the export file.

Footer options

Include void amounts in standard footer totals?
Select this checkbox if you want to include voided amounts in the standard footer totals.

Suppress standard footer if no checks issued?
Select this checkbox if you want to hide standard footers when a check is not issued.

Suppress void footer if no void checks?
Select this checkbox if you want to hide the void check footer when there are no void checks on file.
