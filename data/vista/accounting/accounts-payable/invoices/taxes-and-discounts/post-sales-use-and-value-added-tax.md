---
title: "Post Sales, Use, and Value Added Tax | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/taxes-and-discounts/post-sales-use-and-value-added-tax"
---

# Post Sales, Use, and Value Added Tax

You can apply taxes to transactions entered in Accounts Payable. However, there are setup requirements that must be met before you begin entering transactions.
There are three different types of tax that you can apply to AP transactions:

- Sales tax - Sales tax - paid directly to the vendor with an invoice. It does not accrue in a liability account, but is directly expensed.

- Use tax - accrues and is paid to a taxing authority later. This tax is directly expensed.

- Value Added Tax (VAT) - paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed.

To enable posting tax to an AP Transaction, take the following steps:

1. Set up tax codes and rates in the HQ Tax Codes form. Also, define the GL tax accrual and expense accounts for posting use and value added taxes.

1. Assign a default tax code for each vendor in the AP Vendors form (Tax Code field).

1. If applicable, assign the default tax code for each job in the JC Jobs form (Tax Code field).

1. When entering AP transactions, select the appropriate tax type and code for each transaction (in the Type and Code fields, respectively). Note: The Tax Code field defaults based on the line type option you select from the Type drop-down field. For more information, see the F1 help for the [Type](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form/field-definitions-ap-transaction-entry-form#ID-00006eda--en) field.For Use tax, calculated amounts do not affect the gross or net balance due to the vendor. The system charges the transaction's gross amount and tax amount to GL and JC, EM, or IN. Use the AP Tax Report to obtain an itemization of use tax amounts.
If you are posting VAT tax, you can use the AP Value Added Tax Report to obtain an itemization of VAT amounts.
