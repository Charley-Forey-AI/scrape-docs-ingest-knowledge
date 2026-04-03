---
title: "Void Check Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-entry---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-entry---field-descriptions"
---

# Void Check Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
FieldsDescriptions
AccountIf the Cash Management module is present, enter the bank account code or credit card account code.Note: Some of the field titles in this screen vary depending upon whether the Account field contains a bank account code or a credit card account code.

Check numberIf the Account field contains a bank account code, enter the number of the check to be voided. Only valid check numbers are allowed. Some operations elect to install the software with an "H" automatically recorded as part of the check number (in Accounts Payable Installation or Cash Management Bank Account Maintenance). If using this feature and the check to be voided was a prepaid or manual check, type "H" followed by the check number (H stands for Hand check).
When voiding out an electronic payment, use the 'E' check from the [Vendor Payment History](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-financial-summary/vendor-payment-history). When updated, the invoices are all returned to Vendor Open items just like when voiding a payables check.
Important: You cannot enter the summary transaction's 'E' check number to void out the total ACH/AFT transaction.

- Transaction #: If the Account field contains a credit card code, enter the number of the credit card transaction to be voided.

Properties
VendorThe code of the vendor to whom the check was written displays.
Check amountIf the Account field contains a bank account code, the dollar amount of the check displays.

- Transaction amount: If the Account field contains a credit card code, the dollar amount of the credit card transaction displays.

Discounts takenThe amount of discounts taken in this check displays.
Check date

- If the Account field contains a bank account code, the date of the check displays.

- Transaction date: If the Account field contains a credit card account code, the transaction date displays.

Retention amountThe amount of retention, if any, paid with this check displays.
Cost centerThe cost center associated with the payment transaction displays after the check number is entered. This cost center will be assigned to the void transaction. This field only displays if cost centers/cost groups are enabled for the current company in the Enterprise Installation screen.
G/L accounts
A/P G/L accountThe Accounts Payable G/L account that should be reversed displays.
Cash G/L account

- If the Account field contains a bank account code, the cash account that should be reversed displays.

- Liability G/L account: If the Account field contains a credit card account code, the Liability G/L account that should be reversed displays.

Void date
Transaction dateThe current A/P processing date displays. Press Enter to accept this default transaction date, or enter the desired date.
Fiscal yearThe fiscal year corresponding to the transaction date displays.
PeriodThe fiscal period (numbers and month name) corresponding to the transaction date displays.
Update buttonSelect to display the [Void Check Register](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/void-check-entry/void-check-register) screen where you can print a listing of checks and transactions already voided.
