---
title: "Reverse Open Invoice Entry Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-open-invoice-entry-update"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-open-invoice-entry-update"
---

# Reverse Open Invoice Entry Update

The Update window is used to update the
 reversals made in A/P Reverse Open Invoice Entry.
User security levels determine which Update window
 displays when you click OK in the Reverse Open
 Invoice Entry screen.

- [Scenario # 1](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-invoice-update-1): If the
 reversal cannot be updated to open items or history

- [Scenario # 2](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-invoice-update-2): If the
 reversal can be updated to open items, but not transferred to the history

- [Scenario # 3](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice/reverse-invoice-update-3): If the
 reversal can be updated and transferred to the history

The following grid explains the various options you will have depending on these scenarios. Contact your company's System Administrator if you have questions about your security settings.
Security
Security
Security
Dates
Results

Do you have security to the Transaction Register Update?
Do you have security to the Manual Check Register Update?
Do you have security to the Check Register Update?
Are the G/L Dates for both the Invoice & Credit Memo within the same fiscal period?
What options are available to you based on these scenarios?

Scenario #1
No
Yes
Yes
Yes
 Create the unposted reversal.

Scenario #2
Yes
No
Yes
Yes
Create the reversal and update the transaction register.

Scenario #2
Yes
Yes
No
Yes
Create the reversal and update the transaction register.

Scenario #2
Yes
Yes
Yes
No
Create the reversal and update the transaction register.

Scenario #3
Yes
Yes
Yes
Yes
Create reversal, update the transaction register and transfer it to vendor history.

Note: If Cash Management is being used, there must be an Accounts
 Payable default bank account code entered on the Bank
 Accounts tab of the Cash Management
 Installation screen. If this bank account is not entered, then
 the result is "Create the reversal and update the transaction register", and it
 does not get transferred to vendor history.
