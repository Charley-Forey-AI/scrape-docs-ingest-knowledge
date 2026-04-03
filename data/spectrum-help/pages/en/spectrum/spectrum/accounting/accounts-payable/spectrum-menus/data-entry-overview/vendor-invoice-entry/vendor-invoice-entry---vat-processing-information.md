---
title: "Vendor Invoice Entry - VAT Processing Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---vat-processing-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---vat-processing-information"
---

# Vendor Invoice Entry - VAT Processing Information

If VAT processing is enabled in
 General Ledger Installation, additional VAT
 tax and VAT tax amount fields will display. The VAT code
 will default from the Default tax code field in General
 Ledger Installation (when adding a Subcontract Progress Billing invoice the VAT
 code recorded in Job Cost > Tax Classification Maintenance will default).
Every time the 'VAT code' on the main screen changes the 'VAT tax amount' is
 recalculated unless Keep as Entered is specified in the [Value Added Tax Breakdown](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---vat-processing-information/value-added-tax-breakdown) window.

- VAT Tax Amount = 'Total before tax' x 'VAT tax percent' / 100

- Retention VAT = new 'VAT tax amount' x 'Retention amount' (before tax) / 'Total before tax'

- Current VAT = new 'VAT tax amount' minus new 'Retention VAT
