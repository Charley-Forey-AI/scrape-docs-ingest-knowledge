---
title: "How the System Uses Payment Terms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/payment-terms-setup/how-the-system-uses-payment-terms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/payment-terms-setup/how-the-system-uses-payment-terms"
---

#  How the System Uses Payment Terms

Several processing forms throughout the software are affected by the payment terms assigned to customers, contracts, and/or vendors. The following is list of these forms and a brief description of how they use payment terms.

- Invoice Entry - Payment terms are used to calculate invoice due dates and discount dates, as well as discount amounts for each transaction or transaction line entered. This is true for invoices created in Accounts Payable (AP Transaction Entry, AP Unapproved Invoice Entry, and AP Recurring Invoices), Job Billing (JB Progress Bill Initialize, JB Progress Billing, JB T&M Bill Initialization, and JB T&M Bill Edit), and Material Sales (MS Invoice Initialize and MS Invoice Edit).

- Cash Receipts Entry - Payment terms are used to determine discount amounts when posting customer-related payments in AR Cash Receipts Entry. If a discount was not previously entered when the invoice was posted, and the payment is made by the discount date specified, the system will calculate a “Discount Taken” amount, using the discount rate specified in the payment terms. If a discount was “offered” on the invoice, that amount will automatically display in the Discount Taken field when you post the payment.

- Calculating Finance/Service Charges - Payment terms are used to calculate invoice due dates when assessing or adding new finance/service charges (in AR Finance Charge). The system automatically creates a new invoice for each customer to which finance/service charges are applied, using the specified payment terms to calculate a due date for the invoice. The calculation is done internally and does not display in the form.

- Releasing Retainage - Payment terms are used to calculate an invoice due date for each invoice created when posting released retainage transactions (in AR Release Retainage and JB Release Retainage). Due date field allows the system calculation to be overridden if desired. You will need to set up each type of payment terms your company uses are set up by you in the Payment Terms Setup form.

Related information

- [About the HQ Payment Terms Form](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)
