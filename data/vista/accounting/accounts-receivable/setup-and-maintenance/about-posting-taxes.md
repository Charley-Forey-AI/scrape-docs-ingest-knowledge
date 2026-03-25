---
title: "About Posting Taxes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-posting-taxes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-posting-taxes"
---

# About Posting Taxes

Within the AR Company Parameters file, there are two tax posting options that control whether taxes may be posted to AR transactions.
The options are:

- On Invoices

- On Receipts

If you select to post taxes on invoices (contract and non-contract), additional options are available for including retainage in tax calculations/distributions.

- Calculate Tax on Retainage – With this option, the retainage amount is included in the tax basis. When you post an invoice (in AR Invoice Entry), the full tax amount is updated to the tax payables account (the Credit GL Account specified in HQ Tax Codes, Info tab) and is due for payment. When unchecked, retainage is excluded from tax calculations.

- Distribute Tax to Retainage – With this option,
 retainage tax is tracked separately and is made payable at the time retainage is
 released. The tax basis amount for the invoice will exclude retainage tax;
 retainage tax is calculated separately and displayed in the Retainage
 Tax field. When the invoice is posted, the retainage tax is
 updated to the Credit GL Retg Account specified for the tax code (HQ Tax Codes,
 Add’l Opts tab). When you release retainage, the retainage tax is moved to the
 tax payables account (indicated above) and is due for payment.

For contract-related invoices, tax defaults are based on the contract item setup (in JC Contract Items). Invoice lines will default the tax code specified for the contract item (or as null when no tax code is specified for the contract item). However, you can add or change tax codes as necessary.
If you select to post taxes on receipts, you can post taxes on miscellaneous cash receipts or ‘on account’ payments (typically posted for ‘balance forward’ customers). If you will be posting taxes to ‘on account’ payments, it is suggested that you also check the Post Taxes on Invoices option. This ensures the customer’s account balance accurately reflects the tax amount posted to payments on account.
If both the On Invoices and On Receipts options are left unchecked, taxes will not be calculated for AR invoices or cash receipts, regardless of whether the invoice/cash receipt is contract-related and the contract allows the posting of taxes.
Note: It is important that you avoid changing these flags once you have set them, as they can seriously affect input defaults and retainage processing in AR and other modules. If you do change a flag, a warning message displays giving you the option to continue or cancel the change.
