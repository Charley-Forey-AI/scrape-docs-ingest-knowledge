---
title: "Scale Data Format Maintenance - File Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance/scale-data-format-maintenance---file-layout"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance/scale-data-format-maintenance---file-layout"
---

# Scale Data Format Maintenance - File Layout

Use this tab to determine the appearance of imported information and to recalculate ticket pricing for cash-only sales or charge only sales.
Field
Description

Line
 Sequential line numbers are assigned and maintained by the software. No entry is allowed.

Variable
 Each piece of information imported into Spectrum for use in Materials Management is assigned to a variable name. The 31 variable names display in this column. No entry is allowed.

Description
The variable description displays.

Type
The variable type code displays, indicating whether this data is Numeric or Alphanumeric. No entry is allowed.

Max length
The maximum length allowed for each variable displays. For example, six characters are allotted for the ticket number, ten for the customer code, and so on. No entry is allowed. The maximum record length for import files is 2000 characters. Only the first 2000 characters of each record can be read, keep this in mind when setting up the import file.

Required?
the software displays either Yes or No to indicate whether this variable is required to be in the import file. No entry is allowed. Note that required variables must have the corresponding validation flag set to Yes.

Validated?
When prompted, enter Yes if the variable is to be validated, or No if the variable does not need to be validated. Note that required variables must be validated.

Field#
If the Data type field is set to Comma delimited, enter the field number for this variable.
