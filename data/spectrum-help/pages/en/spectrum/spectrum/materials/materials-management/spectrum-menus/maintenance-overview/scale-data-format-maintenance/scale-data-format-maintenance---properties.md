---
title: "Scale Data Format Maintenance - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance/scale-data-format-maintenance---properties"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/scale-data-format-maintenance/scale-data-format-maintenance---properties"
---

# Scale Data Format Maintenance - Properties

Use this tab to select import formats, weight conversions, and import calculations for this scale data format.
Field
Description

Description
 Enter a full description of the data format code. For example, the code might be "A1," and the full description might be "Acme Scale."

Data type
Enter the file data type: Fixed width or Comma delimited. The data type format specified here determines the information that will display in the list box below.
 For files with data formatted in a Fixed width position, it will be necessary to specify where each field's position starts and stops.
For files that are Comma delimited, start/stop information is unnecessary and the lower portion of this screen will simply display the field number.

Import formats

Date format
Enter the format in which the date will appear: MMDDYY, MMDDYYYY, MM/DD/YY, or "DATE" to set at import.
When this field is set to DATE, the date specified on the Import Scale Tickets start screen is assigned automatically, regardless of dates stored in the import file.
When the import date is left blank or the format specified in this window (for example, MMDDYYYY) does not match the format of the import date, the software will automatically assign the date specified on the Import Scale Ticket's start screen.

Time format
Enter the format you would like to appear for the time. Example: HH:MM:SS.

Weight conversion

Weight conversion required?
Select this checkbox if you would like a weight conversion calculated. Otherwise, leave this checkbox clear.

Conversion factor
Enter the conversion factor for the weight conversion. This field displays only if the Weight conversion required checkbox is selected.

Import calculations

Calculate pricing on charge sales? Calculate pricing on cash sales?
Select this checkbox to calculate pricing on charge sales. If you wish to calculate pricing on cash sales, select the Calculate pricing on cash sales checkbox as well.

Sell price calculated? Freight charge calculated? Miscellaneous charges calculated? Sales tax calculated?
Select these checkboxes to calculate the sell price, freight charge, miscellaneous charges, and sales tax.
