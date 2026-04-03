---
title: "Sales Journal / Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/sales-journal--update"
---

# Sales Journal / Update

This screen is used to print a list of invoices to be
 updated, and optionally, to update the sales transactions to the customer and job files.
The function only allows you to update invoices that have been printed.
 Updating to Job Cost is dependent on the Post to J/C field on the
 Accounts Receivable Installation screen. When an override terms
 code is assigned to the contract, assign this code during the update.
First, print the Sales Journal/Update and review it for accuracy. If the report is accurate, proceed with the update. If an error is found on the Sales Journal/Update, do not perform the update. Make necessary corrections, then reprint the Sales Journal/Update.
"Balanced Entry" protection is incorporated into the update to assure the General Ledger will stay in balance. If debits do not equal credits (due to a power failure or data error, for example), the software will provide a special screen message and disallow update until the problem is corrected. Consult the support desk at Viewpoint for instructions if it is necessary to correct an out-of-balance error.
This function updates the Accounts Receivable, Job Cost, Equipment Control and General Ledger systems with the posted billed totals. This may be done as often as desired (typically daily); you don't have to wait for monthly closings. This function also updates the Equipment Control files, if non-job Equipment Usage invoices were entered in Customer Invoice Entry.

- If Multi-Currency processing is being used, when updating an invoice assigned a local currency, the software will post the transaction to General Ledger using the alternate A/R Retention G/L Account Code (defined for the currency).

- If the online tax calculation service is in use and the invoice
 tax status is 'Uncommitted,' all invoices will be deselected. All invoices that are
 not flagged to use the online tax calculations service will be processed as normal.


- The Retention G/L code is assigned as part of the update. The
 'Override retention receivable G/L' account code will default into the A/R
 retention field. If this field is blank, the G/L code from
 the Installation screen will default instead.

- If related party tax codes are included on the draw request and the user enters an
 override G/L code on the Schedule of Values, the system will default the related party
 G/L codes.

- For Canadian companies, if VAT tax is included in the update and
 the Allocate PST on holdback option is selected, the PST amount will be
 reduced by the amount of holdback PST and this amount will be debited to the
 Retention Receivable account.
Important: This report should be
 retained as a permanent audit record of the company.
