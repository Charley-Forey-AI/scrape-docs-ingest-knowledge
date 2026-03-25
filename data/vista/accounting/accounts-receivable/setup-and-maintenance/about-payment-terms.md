---
title: "About Payment Terms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-payment-terms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-payment-terms"
---

# About Payment Terms

Payment terms (set up in HQ Payment Terms) are used to determine due dates, discount dates, and discount rates for customers when posting transactions in AR.
 If discounts are not used, the payment terms will not require discount information input and will only be used to calculate invoice due dates. The following is a list of the processing programs in AR that are affected by the payment terms assigned to each customer, as well as a brief description of how the payment terms are used.

- AR Invoice Entry – The payment terms are used to calculate invoice due dates and discount dates, as well as discount amounts for each transaction or transaction line entered. The same is true for invoices created in Job Billing and Material Sales.

- AR Cash Receipts – Payment terms are used to determine discount amounts when posting customer-related payments. If a discount was not previously entered when the invoice was posted, and the payment is made by the discount date specified, the system will calculate a Discount Taken amount, using the discount rate specified in the payment terms. If a discount was offered on the invoice, that amount will automatically display in the Discount Taken field when you post the payment.

- AR Finance Charge – Payment terms are used to calculate invoice due dates when assessing or adding new finance/service charges. If finance/services are calculated on the account balance, the system automatically creates a new invoice for each customer to which finance/service charges are applied, using the specified payment terms to calculate a due date for the invoice. The calculation is done internally and does not display in this program.

- AR Release Retainage – Payment terms are used to calculate an invoice due date for each invoice created in this program when posting released retainage transactions. The due date field allows the system calculation to be overridden if desired.

If a transaction is related to a contract, the system will automatically use the payment terms assigned to the contract in JC Contract Maser to implement calculations. If no payment terms were specified for the contract, then the payment terms assigned to the selected customer are used.
[ About the HQ Payment Terms Form](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)
