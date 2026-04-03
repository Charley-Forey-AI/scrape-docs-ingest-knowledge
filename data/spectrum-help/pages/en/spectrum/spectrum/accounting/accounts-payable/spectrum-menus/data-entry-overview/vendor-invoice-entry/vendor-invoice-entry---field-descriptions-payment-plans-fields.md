---
title: "Vendor Invoice Entry - Field Descriptions: Payment Plans Fields | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-payment-plans-fields"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-payment-plans-fields"
---

#  Vendor Invoice Entry - Field Descriptions: Payment Plans Fields

Use the field descriptions in table below for reference
 when completing the header portion of the Vendor Invoice Entry
 screen.
Fields/Buttons
Descriptions

Payment Plans

Pay-when-paid
This checkbox displays when the current invoice is job-related and that job
 is assigned 'pay-when-paid' in Job Setup. For
 subcontract invoices, this checkbox will initially default from settings in
 [Subcontract Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-defaults) (when the 'override' feature is enabled), and
 otherwise from [Vendor Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults).
When Pay-when-paid? is selected, the Payment
 due date field is blank. By rule, all pay-when-paid invoices
 are considered current and thus no payment due date appears. This checkbox
 can be changed during data entry.
Important: The 'Payment due' date will
 default to the current date when clearing the checkbox.

You can also change the pay-when-paid terms using the Change
 Invoice Due Dates screen or in an open Vendor
 Invoice Inquiry window.
 In Vendor Invoice Entry, the system looks to the
 purchase order or subcontract to determine the job number. For non-purchase
 order and non-subcontract invoices, the system looks for the job entered on
 the first distribution row. Once the job number has been determined, the
 Pay-When-Paid policy will then be determined.

Payment due
The date the invoice should be paid, calculated from the payment terms entered
 in Vendors, displays. For new subcontract invoices, the system will
 determine whether the referenced subcontract includes any override payment
 terms.
If a purchase order was specified, this date will be calculated based on the invoice date and the payment terms already defined for the purchase order.

Retention
The retention percentage amount is calculated (invoice amount multiplied by the retention percentage) and displayed. A percentage amount may be entered, normally between 0% and 100%, the software will calculate the retention % based on the entered invoice and retention dollar amounts.
To view an example where the retention percentage is changed for an A/P subcontract that has already been billed, refer to the [Retention Billings From Subcontractors](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/retention-billings-from-subcontractors) topic.

Retention amount
The retention amount from the subcontract file will display, but may be overwritten if desired.
To view an example where the retention amount is changed for an A/P subcontract that has already been billed, refer to the [Retention Billings From Subcontractors](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/retention-billings-from-subcontractors) topic.

Hold payment?
If the hold status displayed is incorrect enter the desired option; if necessary, change the hold status in the vendor's master file.
If a hold was placed on this vendor in the main Vendors
 screen, the checkbox will be selected, and the invoice cannot be paid until
 the hold is removed.
This checkbox will be selected if this vendor/subcontract has any [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) with Action #3 that are not complete. Action #3 sets all invoices and credit memos to hold status as the are entered. Furthermore, if sub-tier vendor tracking is being used, new invoices will be on hold whenever any related sub-tier vendors are flagged for hold status (triggered by action #3).

Check/Credit Card
Paid by Instant Check
Credit Card Purchase button
This button does not display if the current transaction is on hold, or if there is a non-zero retention amount.
The button label varies based on the transaction type; likewise, the fields that display will vary based on the transaction type (all possible fields are shown in the table below).
View Payment Details fields:

> Fields/Buttons
Descriptions

Payment
 type

- The Instant manual check option (formerly 'pre-paid') is unavailable if entering an unapproved invoice.

-  If this option is selected, complete the Payment info portion of the window, then click OK and the data automatically fills in for this transaction.

- Click Save and the Instant Manual Check screen displays.

-  For more information about pre-paid invoices, click [Instant Manual Check Information](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/manual-check-entry/instant-manual-check-information).

- The Credit card option is only available if the Cash Management module is present.

Manual check info

Bank account
This field is only enabled if Cash Management is present. Use the available drop-down list to select an account.

Cash G/L account
If Cash Management is present, the G/L account from the bank account specified displays.

Check #
Enter a check number, or press Enter to use the next check.

Check date
Enter the check date. The check date determines the General Ledger fiscal period.

Check amount
No changes allowed.

Print check now?
The appearance of this prompt is based on whether the Print instant manual check checkbox is selected in on the Accounts Payable Installation-Printing tab.
Companies that have a dedicated check printer typically use this feature. Once the invoice is completely distributed in the line transaction portion of the screen the check will begin printing immediately. Ensure that checks are loaded into the printer and aligned correctly before continuing.
Select the checkbox if the check has not already been handwritten and system should print this prepaid check. Do not select the checkbox if this check is being written by hand, and the system does not need to print this prepaid check.
If this checkbox is selected, the software automatically displays a Spectrum tab in order to 'print' the check when the new or existing transaction is saved and committed.

Credit card info

Credit card account
Enter the credit card account code, or select from a list of available credit card accounts.
Note: Spectrum does not permit bank accounts in this field.
 Payments from this screen must be made from a credit card
 account.
Cost Center Information
 If cost centers are being used and the Cash Management module is present, Spectrum allows entry of a credit account code only if you have permission to assign that code. Spectrum compares the credit card account's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that credit card account cannot be assigned.

G/L liability account
Once the Credit card account field is completed, the G/L liability account code and description associated with the credit card account display. No entry is allowed.

Card number
Enter the credit card number used to complete this purchase, or select from a list of available credit card numbers.
 This field only displays if the Track sub-account card detail checkbox is
 not selected in Cash Management > Account Code File Maintenance.

Transaction date
The current G/L processing date displays. Press Enter to accept this default or enter the applicable credit card transaction date. The date in this field must fall within the current Accounts Payable minimum/maximum date range.

Charge amount
The amount of the credit card purchase displays. Use this field to confirm the amount of the charge.
