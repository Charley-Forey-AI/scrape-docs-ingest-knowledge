---
title: "GL Income Statement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-income-statement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-income-statement"
---

# GL Income Statement

You can use the GL Income Statement report to display a
 standard income statement by selecting General Ledger > Reports > GL Income Statement.
This report displays a standard Income Statement. It runs for accounts under the company specified on the parameter screen, and will display activity from the "Beginning Month" parameter through the "Ending Month" parameter. (If "Beginning Month" is left blank, the beginning of the fiscal year will be used.)
The report can be further narrowed by the optional Part 2 and Part 3 parameters. These parameters will accept a comma-separated list of values (no spaces). Lookups are available for these parameters, but the lookups do not support multiple values.
This report requires Major categories to be properly set up on the GL Account Part 1. Specifically, each Income or Expense account that should show on this report should be assigned to a Major Category that has the Income Statement Order filled in with a value that reflects the order in which that Major Category should appear on the Income Statement. Minor Categories are available for further grouping, but are not required.
This report will exclude any Memo or Header type account.
The report will round up an amount to the nearest whole dollar. Because of this, discrepancies may appear between the amounts displayed and their calculated totals.
More information for setting up GL Account Parts for the Income Statement can be found under the GL help topic for Major Categories.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Month
Enter or select the applicable beginning month.

Ending Month
Enter or select the applicable ending month.

Account Part 2
Click the Field Lookup
 button or press F4 to select and restrict by account part 2 or
 leave blank for all. Separate by commas if more than one part is
 needed.

Account Part 3
Click the Field Lookup
 button or press F4 to select and restrict by account part 3 or
 leave blank for all. Separate by commas if more than one part is
 needed.
