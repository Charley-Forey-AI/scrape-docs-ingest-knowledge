---
title: "Clearing Data File Format Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/clearing-data-file-format-maintenance/clearing-data-file-format-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/clearing-data-file-format-maintenance/clearing-data-file-format-maintenance---field-descriptions"
---

# Clearing Data File Format Maintenance - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Data file format
Enter the data format code and a description. This is typically the name of the bank that provided the ASCII data file, for example, U.S. Bank.

Data type
Select the file data type:

- Comma delimited

- Fixed width

The format specified here determines the information that will display on the lower portion of this window. For files with data formatted in a fixed position, it will be necessary to specify below where each field's position starts and stops. For files that are comma delimited, start/stop information is unnecessary and the lower portion of this screen will display the field number instead.

Format

Import check amount as a whole number if no
 decimal?
Select this checkbox to process check amount as a whole number if no decimal.

Date format
Enter the format in which the date will appear (for example, MMDDYYYY or MM/DD/YY), or "DATE" to set at import.

Header record?
Select this checkbox if this format has one or more header records, and enter the number of lines (1-99) in the header record.
Some banks provide additional information at the beginning of the import file. These records do not contain information about specific checks being applied to the bank account, and will not be used during the import process.

Trailer record?
Select this checkbox if this format has a trailer record, and enter the variable number and the expected data value for this variable in the trailer record. A trailer record is a single record indicating the end of the information to be imported.
When the trailer record is encountered, the software will interpret the import as complete; that record and any later records in the file will be ignored.

Variable
Enter the variable number (1 - 4) associated with the Trailer record (entry is mandatory when the Trailer record checkbox is selected). During the update, the specified variable will be used to identify the trailer record. For example, if the trailer record will be indicated by check number '999999', variable 1 should be specified. Be sure to enter the variable number rather than the user-defined field #.

> Variable #
Variable Name

1
Check number

2
Check amount

3
Bank clearing date

4
Bank account number

Data value
Enter the expected data value for this variable in the trailer record. For example, if '999999' will be indicated for the check number variable, enter 999999. In order to recognize the trailer record, the data value specified must be an exact match. Therefore, it is typically necessary to indicate the full character string based on the maximum field size. This field is enabled only if the Trailer record field is set to Yes.

Detail area

Variable
The variable displays. The description, type (numeric or alpha-numeric) and maximum length of the variable will display below.

Required
If the data type is Comma delimited, this field indicates whether or not this variable is required in the file format. No entry is allowed.
The number and check amount are required. The date the check cleared the bank and the bank account number are optional. If the data type is Fixed width, enter the starting position for this variable (maximum record length is 500).
