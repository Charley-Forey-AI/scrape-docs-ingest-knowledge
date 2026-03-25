---
title: "Cash Receipts Setup Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/cash-receipts-setup-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/cash-receipts-setup-options"
---

# Cash Receipts Setup Options

There are several setup options available in AR Company Parameters that may have an effect on posting in AR Cash Receipts.
The following is a list of these options and a brief description of their use.

- Allow Discounts on Invoices and Receipts – Select this option and specify a discount amount in AR Invoice Entry to have the system automatically default the offered discount. If initializing, select the Apply Discount checkbox in AR Initialize Receipt to have the system default the offered discount. If the payment date is on or before the date in the Disc Date field, and the payment covers the entire balance, the system automatically applies the discount to the payment. To apply the discount manually, place the cursor in the Total Applied column, enter the payment amount, and press Ctrl + W. This populates the Disc Taken column with the offered discount amount.

- Allow Discounts Taken on Receipts – Select this option to enter discount amount manually when applying payments to invoices, even if discounts were not offered during invoice entry. As input restrictions in AR Cash Receipts prevent entering discount amounts greater than offered discounts, and using this option prevents discounts from being calculated during invoice entry, you must override the input restriction to enter discount amounts. To do so, select the invoice line in AR Cash Receipts, click Payment Detail, and enter the payment discount in the Disc Taken field.

- Post Taxes on Receipts – Select this checkbox to post taxes for Miscellaneous Cash Receipts or "on account" Payment transactions in AR Cash Receipts. If a tax code does not default in the Tax Code field (AR Invoice Entry), enter the code manually. You cannot post taxes in AR Cash Receipts without selecting this box.

- Allow Override of Receivable Type – This option affects "on account" payments only. If you do not select this option, the Rec Type field on AR Payment on Account is inaccessible. All payments posted in this screen will automatically default to the receivable type assigned to the referenced customer in AR Customers. If the customer does not have a specified receivable type, the default comes from the receivable type in the Company file. If you selected this option, the Rec Type default may be overridden during "on account" payment posting.

Related information

- [Posting Shortcuts](/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-cash-receipts-form/posting-shortcuts)
