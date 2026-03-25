---
title: "AP Release Retainage/Retention/Holdback Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form"
---

# AP Release Retainage/Retention/Holdback Form

Use the AP Release Retainage/Retention/Holdback form to release retainage for AP invoices or to place released retainage back on hold.
The title of this form changes depending on the Default Country specified in the HQ Company Setup form.

- AP Release Retainage (US)

- AP Release Retention (AU)

- AP Release Holdback (CA)

Note: This topic uses the term "retainage" to mean retainage, retention, and holdback.

Retainage is the portion of an invoice's gross amount that you withhold from payment until job completion. When you enter an invoice that includes retainage, the system automatically creates an additional sequence number to accommodate the retainage portion of each transaction, and assigns the retainage hold code designated in the AP Company Parameters form.
When you use this form to create a release retainage batch, the sequences (transactions) you create are available for selection. You can add transactions to the batch manually or by initialization. Initialization allows you to filter transactions based on specific criteria and then specify whether to release a specific amount, a percent of the vendor's total retainage, or release a percentage of each invoice. For a detailed description of how the system uses these options, see the [F1](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-release-retainageretentionholdback-form/field-definitions-ap-release-retainage-form#concept-9980--en) help.
You can run the initialization process as many times as needed, using different criteria. Since initialization is an iterative process, the system only adds transactions that do not already exist in the grid. When your batch contains the transactions you want, you can proceed to posting the batch.
Once you post the batch, the system releases the retainage and updates the appropriate GL accounts. This includes the ITC Contra accounts used for GST/PST (Australian and Canadian companies). You can then access the transactions for payment in the AP Payment Posting form.
In addition, the system includes released retainage on aging reports (for example, AP Aged Open Payables), using the Release Date to determine the appropriate aging brackets to use.
If you release retainage in error, you can create a new batch to place the released retainage back on hold. The system places the full released amount back on hold and updates the GL accounts accordingly. See [Place Released Retainage Back on Hold](/en/vista/vista/accounting/accounts-payable/payments/retainage/place-released-retainage-back-on-hold).Note: When putting retainage back on hold, the batch month must be the same as the month in which you originally released the retainage. For example, if you release retainage in month 06/20, you must undo the release in month 06/20. In addition, the amount placed back on hold must be equal to the amount previously released. For example, if you released $1,000, you must 'un-release' the full $1,000.

Note: You must use separate batches for releasing retainage and for placing retainage back on hold. The system does not allow mixed release types in the same batch.
For instructions, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).

Related concepts

- [About Updates to GL for Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-updates-to-gl-for-retainage)

- [About Retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage)

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)
