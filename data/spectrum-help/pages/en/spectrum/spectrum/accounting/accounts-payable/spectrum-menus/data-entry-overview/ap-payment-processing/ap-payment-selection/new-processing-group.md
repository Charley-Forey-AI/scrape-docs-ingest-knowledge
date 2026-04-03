---
title: "New Processing Group | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/new-processing-group"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing/ap-payment-selection/new-processing-group"
---

# New Processing Group

This window displays when the Payment Selection screen is opened when a
 Processing Group is first initiated.
Note: For multi-currency companies, all selected bank accounts must use the same currency.
 After the Processing Group parameters have been set up in this window and you click Continue, you will be returned to the
 Payment Selection screen.
Fields
Descriptions

Processing group
The processing group entered on the Payment Processing
 screen displays. No changes are allowed.

Cost center
This field displays in cost center companies only. Use the available drop-down list to assign a cost center to the current processing group.

Select vendor payment methods
Choose the payment methods from the available options (more than one may be selected).

- By default, the Print checks option is selected.

- The ePayments option is selected by default if there is at least one vendor set up to use ePayments.

- The Electronic Pay
 and Comdata
 options are only available if the Cash Management module is present
 and the Cash Management Installation screen
 option to Post A/P transactions? is
 selected.

Assign cash accounts

Bank account for ePayments
Select the check funding account specified for ePayments from the available drop-down list. The software will validate the selected account and alert you if the account is not valid.
If cost centers are enabled for this company, the default code (if any) setup
 on Cost Center Maintenance will be used. When one
 exists, it shall be read only.

Bank account for checks / electronic
Select the check funding account from the available drop-down list. The software will validate the selected account and alert you if the account is not valid.
This field is disabled if both the Print checks and
 Electronic
 payment checkboxes are un-selected. or Cash Management is not
 present or the Cash Management Installation screen
 option to Post A/P transactions? is not selected.

Bank account for Comdata
Select the Comdata funding account from the available drop-down list. The software will validate the selected account and alert you if the account is not valid.

- If a Comdata bank account code is specified in the Cash Management
 Installation screen, that account will default
 here.

- If a Cost center is selected above, the Comdata bank account code specified on
 the Cost Center Maintenance screen will default
 in this field.
This field is disabled if Comdata is not selected as a payment method, or Cash
 Management is not present, or the Cash Management
 Installation screen option to Post A/P
 transactions? is not selected.

Cash G/L account
No changes are allowed in this field when Cash Management is present and the
 Cash Management Installation flag to
 Post A/P transactions is selected.
If Cash Management accounts are not being used, select or enter a valid account.
