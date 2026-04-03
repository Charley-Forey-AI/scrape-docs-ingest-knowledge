---
title: "Cash Receipts/Adjustment Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/cash-receiptsadjustment-entry/cash-receiptsadjustment-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-entry/cash-receiptsadjustment-entry/cash-receiptsadjustment-entry---field-descriptions"
---

# Cash Receipts/Adjustment Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Header

Batch
Enter a customer batch code. Unposted batch transactions will display in the Batch Summary link to the right of this field.

Customer
Enter a valid customer code. If this screen was accessed from the Customer Info Bar, the selected customer code will default.
After a valid customer code has been entered, the Current due, Retention due and Customer balance amounts display to the right of this field. These balances are the same as those shown in the Customers window, and do not include any unposted cash receipts or adjustments in progress.
If a customer is set up to use multi-currency processing, but has open invoices that do not support multi-currency processing, this screen will only support single currency processing. Once invoices are paid, you will be able to use multi-currency processing on this screen. When in use, the local currency code and exchange rate will display above the Batch code.

Transaction code
Enter an A/R transaction code for new transactions. Up to 10 characters are permitted.

Check # / Reference
If a 'payment' transaction was entered above, enter a check number. If an 'adjustment' transaction was entered above, enter a reference number.
If the check is unposted for this customer, the detail portion of this screen will display the applied items. If a new check number is entered, a new transaction will be created.

Cost center
If cost centers are enabled for the current company, enter a cost center code.

G/L date
Enter a G/L date for the receipt. This date must be within the current minimum and maximum processing date range. If entering a new receipt, the current A/R processing date will default. The selected fiscal year and period will display to the right of this field.

Check amount / Amount
If a 'payment' transaction was entered above, enter the check amount. If an 'adjustment' transaction was entered above, enter a reference number. The Undistributed amount will display to the right of this field. The amount will be equal to the check amount minus the sum of amounts applied in the distribution portion of this screen.
If multi-currency processing is being used, the local currency check amount will display directly above this field.

Translate button
This button is only applicable if multi-currency processing is being used. Click this button to open the International Deposit window, which facilitates the translation of a cash receipt submitted in a currency other than the reporting currency.
Complete the Payer currency and amount fields and the system will use the G/L date from the main screen to calculate the translated value in the reporting currency.

ABA routing #
Enter the ABA routing # for this check, if applicable.

Invoice / Credit memo
If the selected line item is an invoice or credit memo, open invoice details (Extension and Invoice date) will display in the header. Click the lookup icon to open the Invoice Inquiry window to view more details about the selected invoice.

Distribution

Search
Click this button to search for a specific transaction.

Entry by invoice
Click this button to open the [Cash Receipts Entry by Invoice](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receipts-entry-by-invoice) window. Use this window to enter the list of invoice numbers listed on the remittance advice of the payment.

Auto-Apply
Click this button to open the Auto-Apply Receipt to Open Items window. Use this window to apply the remaining undistributed balance to open items currently selected.

Pre-Payment
Click this button to open the Pre-Payment Cash Receipt window. Use this window to apply the undistributed balance as a pre-payment/deposit.

Invoice / check
The invoice or check number, transaction type, open balance amount due, job number associated with the invoice or credit memo and customer purchase order # display for existing transactions.

Apply
Click this button to apply the check amount to the Applied amount for the respective line item. The undistributed balance amount in the header will recalculate after each line is saved. If there is already an amount in the Applied amount field, clicking the Apply button will reset this total to zero.
This calculation does not take other unposted cash receipt transactions into account when computing the default value for the particular line.

Adjust
Click this button to open the Quick Adjustment Entry window. Use this window to enter adjustments for the selected item.
Enter a valid adjustment transaction code, adjustment reference number and the amount to be adjusted for this item. Entry of a positive number will reduce the balance due for the customer. If a debit adjustment is desired in order to increase the customer balance, enter a negative dollar amount.

Balance due
The balance due amount on the invoice displays in this field.
If multi-currency processing is in use for the selected customer code, the local currency code balance amount will display in the column before the USD balance.

Applied amount
Enter the dollar amount to be applied to this item, or press Enter to leave this field blank.
If the Include invoices and Auto apply receipt checkboxes are selected in the Selections window, the total amount of the check will be allocated automatically as the invoice(s) display. Starting with the first invoice or credit memo entered in the selection window, the current balance will be allocated based on the invoice balance. The system will continue to the next invoice, allocating any remaining amounts. If the last invoice balance is greater than the remaining current balance, only the remainder will be applied to that item. The operator may then make any desired changes as needed.
If multi-currency processing is in use for the selected customer code, the local currency applied amount will display in the column before the USD amount. Add a local currency applied amount in this column and the USD amount will be automatically calculated based on the exchange rate above.

Discount taken
Enter the discount taken, if applicable, or press Enter to leave the field blank.
If multi-currency processing is in use for the selected customer code, the local currency discount amount will display in the column before the USD amount. Add a local currency discount in this column and the USD amount will be automatically calculated based on the exchange rate above.
