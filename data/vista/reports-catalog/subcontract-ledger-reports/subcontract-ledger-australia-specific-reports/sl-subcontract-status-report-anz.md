---
title: "SL Subcontract Status Report A/NZ | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/subcontract-ledger-reports/subcontract-ledger-australia-specific-reports/sl-subcontract-status-report-anz"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/subcontract-ledger-reports/subcontract-ledger-australia-specific-reports/sl-subcontract-status-report-anz"
---

# SL Subcontract Status Report A/NZ

You can use the SL Subcontract Status Report A/NZ report
 by selecting Subcontract Ledger > Reports > SL Subcontract Status Report
 A/NZ.
Similar to the SL Subcontract Ledger report, the SL Subcontract Status report prints a summarized section of original and change order amounts for the subcontract, as well as change order and AP transaction information for each item. In addition to subtotals for the adjusted contract, invoiced, and paid amounts, the report provides the current payable, unpaid retention, and committed balance (Adj Contract minus Invoiced). The report can be sorted by Subcontract #, Job #, or Vendor Sortname. The invoice detail section lists AP transaction information sorted by invoice date and CM Reference.
Special conditions/formulas.

1. If Exclude Backcharges parameter is set to "N", backcharges are listed after all other item types and the report prints another subtotal line reducing the amount invoiced.

1. Retention amounts reflect the unpaid portion of AP transactions posted to the retention payable type set up in AP Company parameters. Therefore, a separate payable retention pay type must be set up in AP Co. parameters in order for the report to display the correct amount of retention.

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Subcontract #
Select the Field Lookup button or press F4 to select the beginning subcontract.

Ending Subcontract #
Select the Field Lookup button or press F4 to select the ending subcontract.

Beginning JCCo
Select the Field Lookup button or press F4 to select the beginning job cost company.

Ending JCCo
Select the Field Lookup button or press F4 to select ending job cost company or leave blank to select all.

Beginning Job
Select the Field Lookup button or press F4 to select the beginning job.

Ending Job
Select the Field Lookup button or press F4 to select the ending job.

Beginning Vendor Sort Name
Click the Field Lookup
 button or press F4 to select the Beginning Vendor Sort Name.

Ending Vendor Sort Name
Click the Field Lookup
 button or press F4 to select the Ending Vendor Sort Name.

Through Month
Enter Through Month.

Subcontract Status (O)pen, (C)losed, or (A)ll
Enter O, C or A.

Sort by (S)ubcontract, (J)ob, (V)endor
Enter S, J or V.

Page Break by Sort?
checkbox to insert Page Break by Sort.

Include Invoice Details?
checkbox to Include Invoice Details.

Exclude Back Charge Items?
checkbox to Excludes Back Charge Items.

Include Taxes?
checkbox to Include Taxes.
