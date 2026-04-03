---
title: "New/Edit Electronic File Table - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-master-file-maintenance/newedit-electronic-file-table---properties"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-master-file-maintenance/newedit-electronic-file-table---properties"
---

# New/Edit Electronic File Table - Properties

Use this tab to enter table, sorting and file name information.
Fields/Buttons
Descriptions

Table code
Enter a table code for inclusion in the master file.
Note: You cannot add or delete a table code that already exists in
 Electronic Master File Maintenance.

Table summary

Descriptions
Add a description for the new table.

Data type
Select the data type: Fixed width or Delimited.

Delimiter
 This field is enabled only if the Data type field is set to Delimited.
Note: The delimiter options use quotation marks around any strings
 that contain the delimiter. Any strings that contain quotation marks will be
 automatically converted to double quotation marks; this is the same method
 used by Microsoft Excel when creating .csv files.

Report only records with current activity?
 Select the checkbox if you want to include only those records with current activity. This checkbox only displays if the Period option selected is Both.

Automatically capitalize alpha characters?
Select this checkbox to ensure that text characters will be stored in upper case letters only. When this box is selected, and the Build Electronic Data File is performed, lower case alpha-numeric characters will be converted from 'a-z' to 'A-Z'.

Period option
Select the period option from the drop-down menu: Current, Year-to-date, or Both.
If the period option is set up as Year-to-date or Both, then in the table header the starting date will default as 01/01. Current period is usually the current week or month, Year-to-date is usually for the yearly or quarterly totals, and Both includes Current and Year-to-date.

Date selection
Select the date from the drop-down menu. Options include Check or Pay period end to define the date for the period selection.

YTD starting date
If the period option is set up as Year-to-date or Both, then this field will default with a starting date of 01/01, 01/02, and so forth. Be certain to enter the date as MM/DD, including the forward slash.

Sorting

Sort variable
Enter a sort variable. Up to five sort variables may be included; the first receives the highest priority, then the second, and so forth.
Including at least one sorting variable is strongly recommended as it will help to organize the data once the file is built and the information exported. For example, if you were building a file for employee pay raises, you might want to select the employee code as the first sorting variable.

File name

Automatically insert Payroll processing date into file name?
Select this checkbox to default the Payroll processing date into the file name. Position the pound sign (#) to indicate where to insert the date in the file name below.

Automatically insert company ID into file name?
Select this checkbox to default the company ID into the file name. Position the dollar sign ($) to indicate where to insert the company ID in the file name below.

File name
The file name can include an optional identifier code and/or date, depending on whether the Automatically insert Payroll processing date into file name? and Automatically insert company ID into file name? checkboxes are selected. If both checkboxes are selected, the file name path must include both the pound sign (#) and the dollar sign ($) respectively in order to automatically insert the Payroll processing date and company ID information, (for example, C:\DATA\#$).
