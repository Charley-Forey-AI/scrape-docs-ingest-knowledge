---
title: "Process Prepaid Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/process-prepaid-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/process-ap-invoices/process-prepaid-invoices"
---

# Process Prepaid Invoices

Prepaid invoices are invoices that are paid using a manual check before the invoice paid by the check is even entered into the system.
Enter prepaid invoices in AP Transaction Entry the same as regular invoices. The difference is that the payment information is entered at the same time as the invoice.There are certain rules that apply when posting prepaid invoices:

- They must be for the full amount of the invoice (less retainage, which is placed on hold) and cannot be a partial payment. For example, if the invoice total is $1,500 with retainage of $150, the check is assumed to be for $1,350.

- Any discount shown on the invoice line WILL be taken (regardless of the discount date in the header information).

- The payment month must be the same or later than the expense month.

To process a prepaid invoice:

1. Add the invoice in the AP Transaction Entry form.

1. On the Payment Overrides tab, select the Prepaid Transaction checkbox.The system enables the Check #, Paid Date, and Paid Month fields.

1. Iin the Check # field, enter the check number used for the manual check.

1. Enter the payment date in the Paid Date field. The system defaults the month and year in the Paid Month field.

1. Accept the default in the Paid Month field or override if necessary.

1. Enter the rest of the invoice and [process the batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form). Once the system has processed the invoice batch, a message appears asking if you want to process the prepaid transactions in the batch.

1. Click Yes to open a payment batch. The Batch Selection form displays.

1. Select the batch to open (make sure the batch month is the same as the batch month for the prepaid transactions) and click OK.The AP Prepaid Process form displays.

1. Use the selection criteria to restrict by CM account or by batch. Leave the selection criteria fields blank if you want to select all prepaid transactions.To restrict by CM Account:

1. Select the Restrict by CM Account checkbox to restrict processing prepaid transactions by assigned CM account. The system enables the CM Account field.

1. Enter the CM account number in the CM Account field or press F4 for a list of accounts. To restrict by batch:

1. Select the Restrict by Batch checkbox to restrict processing prepaid transactions by batch. The system enables the Posted by field.

1. Enter the user name of the person who posted the batch in the Posted by field or press F4 for a list of accounts.

1. Click Update. All prepaid invoices meeting the selection criteria display in the grid.

1. Click Post to process the batch like any normal invoice.

The invoice was processed in the first batch, and the payment was processed in the second batch.
