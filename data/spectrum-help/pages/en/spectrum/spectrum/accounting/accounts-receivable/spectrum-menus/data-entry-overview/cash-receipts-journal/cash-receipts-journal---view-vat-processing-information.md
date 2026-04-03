---
title: "Cash Receipts Journal - View VAT processing information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---view-vat-processing-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receipts-journal/cash-receipts-journal---view-vat-processing-information"
---

# Cash Receipts Journal - View VAT processing information

When VAT processing is being used, the Cash Receipt
 Journal Report will include VAT tax when an invoice with a 'VAT Code' is paid. The Retention
 VAT will be reclassified to apply the same percentage as the ratio of Retention paid to
 Total Retention. Customer Retention VAT Tax Payable is debited and Customer Current
 VAT Tax Payable is credited. If cost centers are set to 'Yes' for the current company,
 the cost center stored in the header will be assigned to both sides of the
 transaction.
 Example:

- Contract has 10% retention:

- Retention = $105.00

- Retention VAT = $5.00

- Contract retention is reduced to 5%, so half the retention is reclassified to current: Retention drops to $52.50

- Half of the Retention VAT is also reclassified to 'current': $2.50

If the Allocate PST on holdback checkbox is selected, Spectrum will calculate the
 portion of retention PST tax by applying the same percentage as the ratio of 'Retention
 paid' to 'Total retention'. Customer holdback PST Tax Payable is debited, and Customer
 Current PST Tax Payable is credited in the amount of the Retention PST tax. If cost
 centers are set to 'Yes' for the current company, the cost center stored in the header
 will be assigned to both sides of the transaction.
Example:

- Contract has 10% retention:

- Retention = $111.00 (contains retention, retention VAT + retention PST)

- Retention VAT = $5.00

- Retention PST = $6.00

- Contract retention is reduced to 5%, so half the retention is reclassified to
 current: Retention is now $55.50

- Half of the Retention VAT is also reclassified to 'current': $2.50

- Half of the Retention PST is also reclassified to 'current': $3.00

- Half of Retention reclassified to 'current': $50.00
