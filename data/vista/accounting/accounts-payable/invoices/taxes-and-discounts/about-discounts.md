---
title: "About Discounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts"
---

# About Discounts

You can have discount amounts, discount dates, and due dates
 automatically computed for transactions entered in the AP Transaction Entry, AP Unapproved
 Invoice Entry, and/or AP Recurring Invoice Entry forms.
The system uses the payment terms (from HQ Payment Terms) assigned to each
 vendor in the AP Vendors form to calculate discount amounts and to determine due/discount
 dates. If using discounts, you can control whether or not discount amounts are subtracted from
 the invoice amount when an expense batch is posted. The Post Discounts Offered to GL and Net Amounts to
 Subledgers checkbox in the AP Company Parameters form is used to determine how
 discount amounts are expensed.

- Expense Full Gross
 Amounts - This is the typical choice and is implemented by leaving the
 Post Discounts Offered to GL and Net
 Amounts to Subledgers checkbox unselected. This causes the system to
 expense each invoice’s gross amount to GL and the subledgers at posting time. Later,
 when the invoice is paid, any applicable discount is credited to the designated Discount
 Taken GL Account specified in AP Company Parameters.

- Expense Net
 Amounts - This option is implemented by selecting the Post Discounts Offered to GL and Net Amounts to
 Subledgers checkbox. This causes the system to expense each invoice’s net
 amount (gross less discounts) to GL and the subledgers, and, at the same time, the
 designated Discount Offered GL Account (AP Company Parameters) is debited with the
 discount amount. Then, when the invoice is paid, the discount is credited to the Discount
 Taken GL Account. When this option is used, the system always requires that the discount
 amount entered when posting the transaction be taken at payment time (regardless of
 whether or not the payment date is after the discount date). This is because the net
 amount is expensed to GL when the invoice is entered and, therefore, it must post the same
 net amount when processing the payment.

- Tax
 Discounts - If you offer discounts, you also have the option to implement
 tax discounts. Tax discounts allow you to calculate tax on the discounted invoice amount
 instead of the invoice's gross amount. In order to use this feature, you must check the
 "Using Tax Discounts" option in AP Company Parameters. When checked, the system
 automatically calculates tax discounts whenever transactions include a discount.When entering invoices (in AP Transaction Entry and AP Unapproved
 Invoices), tax discounts are calculated by first subtracting the discount amount from
 the invoice's gross amount, then calculating tax on the resulting value (i.e. tax
 basis). The tax amount is then added to the gross amount, and the discount subtracted
 from the total.

For example if the
 invoice gross amount is $1,000, the discount amount is $50.00, and the tax rate is 6.5%,
 the system calculates the tax amount as follows:
 $1000.00 -
 $50.00 = $950.00
$950.00 x 6.5% = 61.75
$1,000.00 + 61.75 - 50.00 = $1011.75
When
 initializing invoices for payment (AP Payment Workfile, AP Payment Initialize), the
 offered (tax) discount is automatically taken when the invoice is flagged for
 payment.

[How Discounts are Calculated](/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/about-discounts/how-discounts-are-calculated#ID-00005135--en__ID-00005135)
[AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form#ID-00006ce9--en__ID-00006ce9)
[AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form#ID-000071df--en__ID-000071df)
[AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form#ID-00006a8f--en__ID-00006a8f)
[AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form#ID-00005805--en__ID-00005805)
