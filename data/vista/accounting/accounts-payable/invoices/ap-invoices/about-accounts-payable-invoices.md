---
title: "About Accounts Payable Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices"
---

# About Accounts Payable Invoices

You can enter Accounts Payable invoices using the AP Transaction Entry form.
The AP Transaction Entry form is the primary method for entering vendor invoices into the Accounts Payable (AP) module for payment processing. The term "transaction" is used in place of "invoice" because AP processing may sometimes require that an invoice be posted as two or more separate transactions to be processed appropriately.
Note: You can also enter invoices into the system with the AP Recurring Invoices and AP Unapproved Invoice Entry forms. For more information, see [Recurring Invoices](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices) or [Unapproved Invoices ](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices).
Invoices can consist of many lines, each of which may pertain to a different job, phase, or even to a different line type. For example, an invoice may include materials for two different jobs and some miscellaneous materials that are put into inventory or directly expensed (line 4) as seen in the table below.
LineJobPhaseCost TypeGL AccountAmount
1100-0112-00531210.03$2,500
2100-0112-00641210.04$1,270
3100-0212-00531210.03$590
4------8502.00$450
Transaction Total: $4,180

The system internally assigns one or more sequence numbers to each invoice line. Each sequence represents a separation of the line amount for payment control purposes. Typically, additional sequences are added to lines for [retainage](/en/vista/vista/accounting/accounts-payable/payments/retainage/about-retainage) and [partial payments](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form).
For example, because retainage is a portion of the invoice line total that is not paid immediately, the system always makes the retainage amount a separate sequence as follows:
Line #Seq A#Pay TypeAmount
11Job$2,250
12Retg$250
Total for Line #1: $2,500

Related information

- [Processing VAT Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/processing-vat-invoices)

- [About Deleting Invoice Transactions](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-deleting-invoice-transactions)
