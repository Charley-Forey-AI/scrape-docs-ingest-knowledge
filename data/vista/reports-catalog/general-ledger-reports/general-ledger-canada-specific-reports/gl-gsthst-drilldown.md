---
title: "GL GST/HST Drilldown | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-canada-specific-reports/gl-gsthst-drilldown"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-canada-specific-reports/gl-gsthst-drilldown"
---

# GL GST/HST Drilldown

You can use the GL Activity by Source Module report to aid
 Canadian users in preparing GST/HST returns for filing with the Canada Revenue Agency (CRA)
 by selecting General Ledger > Reports > GL Activity by Source Module.
This report aids Canadian users in preparing GST/HST returns for filing with the Canada Revenue Agency (CRA).
For the specified reporting period, the report evaluates receivables for all AR companies whose GL company matches the specified input, and payables for all AP companies whose GL company likewise matches.
Per CRA rules, sales and associated GST/HST are reportable as collectible when you issue an invoice to your customer, without regard for the timing of any subsequent receipt of payment. Similarly, GST/HST is reportable as payable when you receive an invoice from your vendor, without regard for the due date or date of your subsequent payment. Thus, all AR transactions, except payments, whose posted month is within the period are included and evaluated in the report: this includes invoices, adjustments, credit memos, write-offs, released holdback, etc. Similarly, all AP transactions whose posted month is within the period are included and evaluated.
Holdback, both in AR and AP, is considered not to be invoiced until it is released. At that time, receivables previously held back become reportable as sales, and any GST/HST associated with receivables or payables previously held back also becomes reportable. Thus, the report includes and evaluates any holdback-type AP sequence whose paid month is within the period, whether or not its posted month also falls within the period.
On the report's main page, Line 101 summarizes sales for the period, excluding holdback and taxes. This sum may be increased by invoices, adjustments, etc., or decreased by credit memos, write-offs, etc. Line 103 summarizes collectible GST/HST from AR transactions; GST/HST associated with holdback is included only if the holdback is released during the period. Line 106 summarizes payable GST/HST from AP transactions; GST/HST associated with holdback is included only if the holdback is paid during the period.
In special circumstances, GST/HST appears summarized on Line 107. If a write-off or credit memo transaction occurs during the period, and applies to an AR invoice that was posted in a prior period, then any GST/HST associated with the transaction appears on Line 107 as a (positive) input tax credit (ITC), rather than on Line 103 as a (negative) collectible amount. This conforms to CRA rules regarding GST/HST associated with uncollectible sales (bad debts); you may recoup any such GST/HST previously remitted to the CRA by claiming an equivalent ITC on Line 107.
Receivables Detail displays all AR lines included and evaluated, showing how each contributes to the sums for Lines 101, 103, and 107. AR lines are shown at the second level, being grouped and summarized at the first level under the Invoice to which they apply. Payables Detail displays all AP sequences included and evaluated, showing how each contributes to the sum for Line 106. AP sequences are shown at the second level, being grouped and summarized at the first level under their AP Reference.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Month
Enter beginning month (MM/YY) for transactions to be included or leave blank for all.

Ending Month
Enter ending month (MM/YY) for transactions to be included or leave blank for all.
