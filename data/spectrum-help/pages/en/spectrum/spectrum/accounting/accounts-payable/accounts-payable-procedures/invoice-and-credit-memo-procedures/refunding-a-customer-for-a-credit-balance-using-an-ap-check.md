---
title: "Refunding a Customer for a Credit Balance Using an A/P Check | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/refunding-a-customer-for-a-credit-balance-using-an-ap-check"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/refunding-a-customer-for-a-credit-balance-using-an-ap-check"
---

# Refunding a Customer for a Credit Balance Using an A/P Check

This procedure is useful for issuing an Account Payable check to refund an Accounts Receivable customer with a credit balance. Before recording a refund check, you must first enter an invoice in Accounts Receivable to offset the credit balance stored in the customer file.

## Part A: Recording an Invoice

In the steps below, you will enter an invoice to zero or net out the credit balance on the customer's account.

1. On the Site Map, click Accounts Receivable  >  Data Entry Customer Invoices.

1. Click the G/L date button at the top of the screen and review the date. This is the date that this transaction will post to the General Ledger.

1. Complete the Customer code field for the customer to whom you will issue an A/P check. Double-click on this field to select from a list of available customer codes.

1. At the Job # field, enter the job number if the credit balance is an overpayment on a contract; otherwise leave this field blank.

1. At the Invoice # field, enter an invoice number. You may want to use the original invoice number, plus an alpha character or reference code (for example, 1001A or 1001REF).

1. At the Type field, select Invoice from the drop-down list.

1. At the Invoice date field, enter the date.

1. Press Enter until the Properties window appears.

1. Review the information contained in the Properties window, and click OK.

1. Press Enter to move through the Quantity field, and add a Description (For example: Refund of Overpayment).

1. At the Extension field, enter the amount of the credit balance to be refunded.

1. At the G/L account field, enter the G/L code for your suspense account or contra account. Press Enter. (Make a note of this G/L code because it will be needed in Part B of this procedure.)

1. If this invoice should be taxable select the Tax checkbox; otherwise leave it blank. Press Enter and then click OK.

1. Click the Print button and print a copy of this invoice.

1. Click on the Update button.

1. Review the A/R Transaction Register for accuracy, select Continue, and then click OK.
This will clear out the credit balance on the customer. A zero dollar adjustment can be made in Cash Receipts / Adjustment Entry to offset the two balances in the open line items.

## Part B: Issuing a Refund Check in Accounts Payable

In this section, we will enter an A/P Invoice in the amount of the customer overpayment. The customer can be setup as a vendor in Accounts Payable  >  Maintenance  >  Vendor.
If desired a prepaid invoice and check can be issued immediately.

1. On the Site Map, click Accounts Payable  >  Data Entry Vendor Invoices.

1. If the customer has been set up in Vendors, enter the new Vendor, otherwise enter the word TEMP and press Enter. The Temporary Vendor window displays and allows you to enter the information for the customer to whom the check will be issued. Click OK.

1. At the Invoice # field, enter an invoice number.

1. At the Entry Type field, select Invoice from the drop-down list.

1. Press Enter to move through the Subcontract # field to the Invoice date field. Add a date. This should correspond with the date entered on the credit memo entered in Accounts Receivable.

1. At the Amount field, enter the amount being refunded to the customer.

1. At the Remarks, enter any applicable comments.

1. Press Enter until the Properties window displays.

1. Review the information contained in the Properties window and click OK.

1. At the Account code field, enter the same suspense or contra account code used in the Accounts Receivable invoice. Double-click on this field or press F4 to select from a list of available G/L account codes.

1. At the Amount field, press Enter to accept the amount that displays based on the amount you entered in the Invoice portion of the screen. Click OK.

1. Click the Update button.

1. Print the A/P Transaction Register.

1. Select Continue, and then click OK.

Related information

- [Recording a Prepayment](/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures/recording-a-prepayment)
