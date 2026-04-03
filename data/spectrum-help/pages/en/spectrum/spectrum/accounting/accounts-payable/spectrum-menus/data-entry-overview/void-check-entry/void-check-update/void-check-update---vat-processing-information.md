---
title: "Void Check Update - VAT Processing Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-update/void-check-update---vat-processing-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-update/void-check-update---vat-processing-information"
---

# Void Check Update - VAT Processing Information

If VAT processing is enabled in the General Ledger Installation screen, the update will reverse VAT tax reclassification when a check that included retention paid is voided. For invoices included on the check being voided that had an assigned VAT code, retention VAT will be returned to the 'Retention A/P VAT Tax Payable' G/L account. This update already creates unposted G/L transaction records in a temporary Payment Table for 'Cash', 'Discount taken', 'Accounts Payable' and 'Retention Payable'. More specifically, the update will:

- Calculate the portion of Retention VAT tax to be reclassified as follows:

- Apply the same percentage as the ratio of 'Retention paid' to 'Total retention'

-  Debit Vendor Retention VAT Tax Payable (G/L code from new VAT Tax Code Table)

- Credit Vendor Current VAT Tax Payable in the amount of the reclassified 'Retention VAT Tax' (G/L code from VAT Tax Code Table)

- Round to the nearest penny

-  If cost centers are set to Yes in the current company, assign the Cost Center stored in VN_GL_DISTRIBUTON_HEADER_MC Table to both sides of this transaction
