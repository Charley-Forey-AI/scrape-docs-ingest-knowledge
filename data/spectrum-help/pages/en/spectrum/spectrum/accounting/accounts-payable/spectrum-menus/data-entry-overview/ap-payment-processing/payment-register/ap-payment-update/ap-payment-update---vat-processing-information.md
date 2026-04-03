---
title: "A/P Payment Update - VAT Processing Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/payment-register/ap-payment-update/ap-payment-update---vat-processing-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/payment-register/ap-payment-update/ap-payment-update---vat-processing-information"
---

# A/P Payment Update - VAT Processing Information

If VAT processing is enabled in the General Ledger Installation screen, the update will reclassify VAT tax when the retention portion of an invoice with a VAT code is paid. More specifically, the update will

- Calculate the portion of Retention VAT tax to be reclassified as follows:

- Apply the same percentage as the ratio of 'Retention paid' to 'Total retention'

- Credit Vendor Retention VAT Tax Payable (G/L code from new VAT Tax Code Table)

- Debit Vendor Current VAT Tax Payable in the amount of the reclassified 'Retention VAT Tax' (G/L code from VAT Tax Code Table)

- Round to the nearest penny

-  If cost centers are set to Yes in the current company, assign the Cost Center stored in VN_GL_DISTRIBUTON_HEADER_MC Table to both sides of this transaction
