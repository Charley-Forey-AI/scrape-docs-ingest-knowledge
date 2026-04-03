---
title: "A/R Invoice Print - Work Order Invoice Print | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/ar-invoice-form/sample-reports---ar-invoice-print/ar-invoice-print---work-order-invoice-print"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-invoice-entry/ar-invoice-form/sample-reports---ar-invoice-print/ar-invoice-print---work-order-invoice-print"
---

# A/R Invoice Print - Work Order Invoice Print

The 'Work Order' format of the A/R invoice includes total VAT tax when a 'VAT tax code' is present on the invoice (because this format does not break out retention and current balances due).

- The Work Order format of the A/R invoice looks to the Work Order history detail line extension to determine if the extension should display on the report.

- If the A/R invoice detail is greater than the Work Order history lines, then
 difference displays as labor summary under Labor (this is the case of a
 reversal). Also note that if the Bill
 customer for this entry checkbox is selected in the Work Order > Data Entry > Labor Hours Entry screen, the labor will display on this report.

- If the A/R invoice detail is less than Work Order history lines, then the difference displays in the Other section and won't be identified as labor (this is when hours are decreased in A/R invoice detail).

- Based on the 'Price' type selected in Work Order Entry, the report will include the following:

- If 'Flat rate' work order is selected, always include labor and material lines that are flagged 'bill to customer', and conditionally include labor and material lines that are not flagged 'bill to customer' when the 'Print detail for flat rate Work Order invoices' checkbox is selected. Always show other charge lines with non-zero bill amounts.

- If 'T+M' work order is selected, always include labor and material lines that are flagged 'bill to customer', and always show other charge lines with non-zero bill amounts.
