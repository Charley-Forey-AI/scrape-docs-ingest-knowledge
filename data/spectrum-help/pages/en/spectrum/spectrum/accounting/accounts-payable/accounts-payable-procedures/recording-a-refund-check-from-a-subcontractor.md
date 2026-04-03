---
title: "Recording a Refund Check from a Subcontractor | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/recording-a-refund-check-from-a-subcontractor"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/recording-a-refund-check-from-a-subcontractor"
---

# Recording a Refund Check from a Subcontractor

When a check is issued to a Subcontractor and then you discover you have over billed and over paid your subcontract, a credit memo has to be entered into the system to reduce the billed to date amount on the subcontract and reduce the job-to-date costs.
After a credit memo has been created, an invoice must be entered without the subcontract number on it to offset the credit balance on the vendor. You will not use the Reverse option because a special G/L account code needs to be used in the details of the invoice. One possible cause could be a reduction to the subcontract via a negative change order after the subcontract has been billed and paid.
There are three parts to this procedure.

- If you have billed the subcontract using Subcontractor Progress Billing follow Part A, Option 1 then proceed to Part B, followed by Part C.

-  If you do not use Subcontractor Progress Billing, proceed to Part A, Option 2 and then proceed to Part B, followed by Part C.

## Part A, Option 1: Subcontract Progress Billing – Credit Memo

1.  On the Site Map, click Accounts Payable  >  Data Entry  >  Vendor Invoices.

1.  If this credit memo is to be routed through Invoice Approval select the option to Route for approval. At the Vendor field, enter the vendor code. Enter the Invoice #. The Invoice type is Credit Memo.

1.  Leave the Purchase Order field blank. Enter the Subcontract #.

1.  In the Subcontract Invoice Entry Type window, select Progress billing. The next Progress Billing # defaults in. Click Continue.

1. Enter the Entry date and Invoice date of this credit memo.

1. Enter the Total before tax of the credit memo.

1. Enter the Sales Tax if applicable.

1. Let the Payment due date default in. Zero out the Retention percentage.

1.  Press Enter repeatedly until the More Invoice Information box displays. If Invoice Approval is in use, verify the Routing Code. Invoice remarks are optional.

1. Let the A/P G/L account code default in. Zero out Discount amount. Click OK.

1. Complete the Subcontract Progress Billing Detail screen, entering a positive quantity and/or Amount this period for each line item overbilled

1.  Click Save .

1. Click Update. Preview the A/P Transaction Register. Click Continue to complete the update.

## Part A, Option 2: Vendor Invoice – Credit Memo

1. On the Site Map, click Accounts Payable  >  Data Entry  >  Vendor Invoices.

1. If this credit memo is to be routed through Invoice Approval, select the option to Route for approval.

1. At the Vendor field, enter the vendor code. Enter the Invoice #. The Invoice type is Credit Memo. Leave the Purchase Order field blank. Enter the Subcontract #.

1. From the Subcontract Invoice Entry Type window select Standard Invoice. Click Continue.

1. Enter the Entry date and Invoice date of this credit memo.

1. Enter the Total before tax of the credit memo. Enter the Sales Tax if applicable.

1. Let the Payment due date default in.

1. Zero out the Retention percentage.

1. Press Enter repeatedly until the More Invoice Information box displays. If Invoice Approval is in use, verify the Routing Code. Invoice remarks are optional. Let the A/P G/L account code default in. Zero out Discount amount. Click OK.

1. Complete the Invoice Detail screen entering the Job, Phase and Subcontract cost type for each item to be credited.

1. Click Save.

1. Click Update. Preview the A/P Transaction Register. Press Continue to complete the update.

## Part B, Option 1 & 2: Vendor Invoices - Invoice

1. On the Site Map, click Accounts Payable  >  Data Entry  >  Vendor Invoices.

1. If this invoice is to be routed through Invoice Approval select the option to Route for approval.

1. At the Vendor field, enter the vendor code. Enter the Invoice #. The Invoice type is Invoice. Leave the Purchase Order and the Subcontract # blank.

1. Enter the Entry date and Invoice date of this invoice.

1. Enter the Total before tax of the invoice. Enter the Sales Tax if applicable.

1. Let the Payment due date default in.

1. Zero out the Retention percentage.

1. Press Enter repeatedly until the More Invoice Information box displays. If invoice Approval is in use, verify the Routing Code and enter any applicable Invoice remarks. Let the A/P G/L account code default in. Zero out Discount amount.Click OK.

1. Complete the Invoice Detail screen. At the G/L Account code field, enter your Suspense or Contra G\L account code. Press F4 to search and select from a list of available G\L account codes. The amount will default in from the invoice header.

1. Click Save..

1. Click Update. Preview the A/P Transaction Register. Press Continue to complete the update.
A zero dollar Manual Check can be entered in Accounts Payable  >  Data Entry  >  Manual Check to offset the invoice and credit memo in open items. This will also reduce the paid-to-date amount on the subcontract.

## Part C, Option 1 & 2 Recording the Refund Check

A cash receipt can now be recorded in Accounts Receivable  >  Data Entry  >  Cash Receipts/Adjustment to record receipt of the refund check.

1. On the Site Map, click Accounts Receivable  >  Data Entry  >  Cash Receipts/Adjustment.

1. On the Action bar, click Non-Customer.

1. At the Transaction code, enter in the transaction code used for a normal Cash Receipt. Press F4 to search and select from a list of available transaction codes.

1. At the Check # type the check number of the refund check.

1. Enter the name of the vendor in the Payer field.

1. Enter the G/L date of this transaction. It is recommended that you use the same date as the AP invoice previously entered.

1. Enter the Check amount.

1. The ABA # is optional.

1. A Remarks box is optional.

1. At the G/L Account type in the same Suspense or Contra G\L account code used on the A\P invoice. Press F4 to search and select from a list of available G/L account codes.

1. Type in the Amount.

1. Click Save.

1. Click Update. Review the A\R Update Transaction Register for accuracy. Click Continue to complete the update.
