---
title: "Positive Pay Export - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/positive-pay-export/positive-pay-export---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/positive-pay-export/positive-pay-export---field-descriptions"
---

# Positive Pay Export - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Bank account
If you have the appropriate security settings, the bank account code will
 default from the Cash Management Installation > Bank Accounts screen. Otherwise, enter the bank account code.
Note: During this export, Spectrum automatically deselects any
 accounts that are not bank accounts. In other words, all credit card
 accounts are excluded from this export.

Positive pay file format
Enter the positive pay file format code.

From/to check date
Enter the beginning and ending check dates to include in the export.

Transaction types
Select the checkboxes corresponding to the transaction types you want to include on the export:

- Regular checks

- Manual checks

- Void checks

Transaction source
Use the Transaction source checkboxes to select the transaction types you want to include on the export.
All of the transaction source checkboxes are selected by default unless one of the following conditions is present:

- If bank account security is used and export authorization is withheld for one or more check sources; none of the transaction sources may be selected.

- If the default Payroll bank account code specified in the Cash Management Installation > Bank Accounts screen does not correspond to the bank account
 specified in the Bank
 account code field (above); the Include Payroll
 checks checkbox can be selected under this
 circumstance unless security authorization is not present.

- If the default Accounts Payable bank account code specified in the Cash Management Installation > Bank Accounts screen does not correspond to the bank account
 specified in the Bank
 account code field (above), then both the Include Accounts Payable
 checks and Include Cash Management
 checks checkboxes will default to clear; both of these
 checkboxes can be selected under this circumstance unless security
 authorization is not present.

- If you do not have security access to Payroll or Accounts Payable, then the respective transaction source checkboxes may not be selected.
