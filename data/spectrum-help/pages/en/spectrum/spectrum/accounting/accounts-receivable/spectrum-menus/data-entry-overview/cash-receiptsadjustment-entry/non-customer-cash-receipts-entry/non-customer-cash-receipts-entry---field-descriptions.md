---
title: "Non-Customer Cash Receipts Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/non-customer-cash-receipts-entry/non-customer-cash-receipts-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/non-customer-cash-receipts-entry/non-customer-cash-receipts-entry---field-descriptions"
---

# Non-Customer Cash Receipts Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Header

Batch
Enter the customer batch code for non-customer cash receipts, or enter
 ALL to include all transactions regardless of
 batch assignment.
The Batch Summary link to the right of this field will report the dollar amount total and transaction count of the specified batch code. Click this link to open the Unposted Cash Receipt Batch Detail Inquiry window to view each transaction contained in the current batch.

Transaction code
Enter a transaction code for this non-customer cash receipt entry. Up to 10 characters are permitted.

Check # / Reference
For payment transactions, enter the non-customer check number in this field. For adjustment transactions, enter the reference number in this field.

Payer
Enter the source of the non-customer receipt in this field.

G/L date
Enter the G/L date for the transaction in this field. The Fiscal year and Period will display to the right of this field.

Check amount / Amount
For payment transactions, enter the non-customer check amount in this field. For adjustment transactions, enter the adjustment transaction amount in this field. The Undistributed balance amount will display to the right of this field, unless you are entering a new adjustment transaction.

ABA routing #
Enter the ABA routing # for the non-customer cash receipt in this field, if applicable.

Remarks
Enter any other information about the non-customer receipt in this field.

Distribution

G/L account
Enter the G/L account code to be credited for this payment. The account
 description displays to the right of this field. If the G/L code's status is
 set to Not Used, no entry is allowed.
The debit account for this payment was specified in the transaction code entered above. For example, if an insurance refund has been received, it might be appropriate to enter the insurance expense account here.

Amount
Enter the dollar amount to be credited to this G/L account. The sum of all amounts entered here must equal the total amount of the check entered above. The software will not allow the operator to exit the screen until these amounts balance.

Remarks
Enter any remarks explaining this non-customer cash receipt. These remarks
 will appear on the Cash Receipts Journal Report.

Job
If a Direct job cost G/L account was selected, enter
 the job number for this transaction. The job description will display to the
 right of this field.

Phase
Enter a phase code for the job. The phase code description will appear to the right of this field.
Note: Data entry is prevented if the phase status is set to
 Complete. A warning displays if the status is set
 to Inactive.

Ct
Enter a cost type for this transaction. The cost type description will display beneath this field.
Once the cost type is entered, enter the dollar amount to be credited to this G/L account and any remarks explaining the non-customer cash receipt.

Equipment
If a Direct equipment cost G/L account was selected,
 enter the equipment code. The equipment description will display to the
 right of this field.

Cost cat
Enter a cost category code for the equipment type. The cost category description will display to the right of this field.
If an inactive cost category is entered in this field, a warning displays but does not prevent further data entry.
When adding a new row, Spectrum will verify that the assigned G/L account is not a restricted G/L account for this cost category code.

- If no records are found for this cost category in the restrictions table, you will advance to the next column.

- If the cost category is found and the G/L account is not among the list of allowed accounts, and error message appears and you will not be able to proceed.

Equip WO
Enter an equipment work order number. If a closed work order is entered in this field, a warning displays, but does not prevent further data entry.
Once the equipment work order number is entered, enter the dollar amount to be credited to this G/L account and any remarks explaining the non-customer cash receipt.
