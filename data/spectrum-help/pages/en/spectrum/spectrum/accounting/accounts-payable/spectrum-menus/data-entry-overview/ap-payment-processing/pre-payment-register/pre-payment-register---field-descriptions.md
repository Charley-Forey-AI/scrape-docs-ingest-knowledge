---
title: "Pre-Payment Register - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/pre-payment-register/pre-payment-register---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/pre-payment-register/pre-payment-register---field-descriptions"
---

# Pre-Payment Register - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields
Descriptions

Processing group
Processing group is the payment batch code that defaults from the Payment Processing starting screen.

Bank account for ePayments
If ePayments has been selected as the vendor payment method, the bank account specified for ePayments will display in this field. If ePayments has not been selected for the check run, this field will be unavailable.

Bank account for checks / electronic payments
If the Cash Management module is present, the bank account code for regular checks displays in this field. The cash account from the installation screen will display by default, but changes are allowed.
This field displays if the processing group vendor payment methods include
 both 'Print checks?' and 'Electronic payment?' in the [New Processing Group](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/new-processing-group) window.
If the 'Override default payment method to use ePayments' option is selected, this field will be unavailable.

Bank account for Comdata
If the Cash Management module is present and Comdata is being used, the bank account code for Comdata Virtual Cards displays in this field. When a separate account is designated, the Comdata payments will be updated to the alternate bank account in Cash Management for reconciliation.
The Comdata bank account will default from the check bank account above, but can be overwritten.
If the 'Override default payment method to use ePayments' option is selected, this field will be unavailable.
Comdata does not issue zero balance virtual card account numbers; therefore if any 'void checks' (a check that nets to a zero dollar payment) are found in the virtual card processing group you must deselect them before proceeding.

Cash G/L account
The cash G/L account code defaults based on the bank account code selected. No changes are allowed.

Cost center for check
This cost center will be assigned to each check as the payment transaction cost center, and will be recorded in during the General Ledger during the Payments G/L update. This cost center will also be stored in Account Payable payment history records and in Cash Management, if present. Spectrum validates the specified cost center with cost centers in your assigned cost center scheme.

Include link to A/P invoice images?
Select this checkbox to include a link to the Document Imaging image associated with the each invoice that appears on the report; otherwise, leave this checkbox clear.
Note: This checkbox is available only if you have the Document Imaging module installed and if your operator has the security necessary to access vendor document images.
