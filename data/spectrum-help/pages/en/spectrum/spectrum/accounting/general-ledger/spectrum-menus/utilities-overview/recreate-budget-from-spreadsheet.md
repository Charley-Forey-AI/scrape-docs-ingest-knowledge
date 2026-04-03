---
title: "Recreate Budget from Spreadsheet | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/recreate-budget-from-spreadsheet"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/recreate-budget-from-spreadsheet"
---

# Recreate Budget from Spreadsheet

Use the Recreate Budget from Spreadsheet screen to import
 budget information from a spreadsheet schedule. Companies that create budgets in a spreadsheet
 program may use this menu option to bring those budget dollar amounts into Spectrum.
If the import file
 contains records for periods that are not part of the selected year, these budget figures
 will be considered invalid and will be discarded. Warning: When running this option, all budget
 information for the specified year will be erased and replaced with information from the
 spreadsheet.
Your spreadsheet must have 13 columns, each 11
 characters wide. Column 1: G/L account code (with or without dashes). Columns 2-13:
 Budget dollar amounts for fiscal periods 1-12 (whole numbers only). Column 14: Cost
 center (if used).
Complete the following steps to print a
 Microsoft Excel spreadsheet to a file.

1. After creating a template in Excel, highlight all the rows used and 13 columns (14 if using Cost Centers) spreadsheet to select them.

1. Set Column Width to 11.

1. Save the spreadsheet file type as Formatted Text (space delimited, *.prn).Note: If the spreadsheet is comprised of multiple pages, a warning
 will display indicating the file does not support multiple pages. When managing
 workbooks, you must save each active page as an individual file.

1. After printing to file from the spreadsheet program, log into Spectrum and access this screen. Enter the year under which this budget should be stored, and the software will import the dollar amounts. This information may then be viewed and edited through Budget File Maintenance and printed through Budget File Report.

Troubleshooting:
If you have trouble importing budget information, check the following:

- The spreadsheet must be set up with 13 columns, and the column width should be resized to 11. Note: If the current company has cost centers enabled then spreadsheets must be set up with 14 columns in order to accommodate a cost center code.

- The file must have the extension ".prn".

- If saved in Excel, it must be file type "formatted text (space delimited) (*.prn)."

Note: Regarding Non-standard Fiscal Years:

- When importing a budget with more than 12 periods, you will need to manually type the additional period budget amounts directly into the [G/L Budget File Maintenance](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-budget-file-maintenance) screen.

- If you are importing a budget with less than 12 periods, the budget import file needs to have 0.00s in the columns that are not real months. For example, if it was a special four-month year, build the budget file so that it only includes no-zero budget values in columns 2 through 4 (periods 1-4). The software will ignore and discard any values for non-valid periods.

Related information

- [Printing a Spreadsheet to File: Microsoft Excel](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/printing-a-spreadsheet-to-file-microsoft-excel)
