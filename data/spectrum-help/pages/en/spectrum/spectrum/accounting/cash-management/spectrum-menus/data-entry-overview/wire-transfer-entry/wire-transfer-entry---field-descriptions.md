---
title: "Wire Transfer Entry - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-entry---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-entry---field-descriptions"
---

# Wire Transfer Entry - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Listing
Click this button to open the [ Wire Transfer Listing](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-listing) screen. This button will only be available before entering into transaction mode.

Update
Click this button to open the [Wire Transfer Register](/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/data-entry-overview/wire-transfer-entry/wire-transfer-register) screen. This button will only be available before entering into transaction mode.

Wire transfer

Bank account
Enter the bank account code from which the money will be drawn on.
Note: Spectrum automatically disallows any accounts that are not
 bank accounts from being entered into this field. In other words, credit
 card accounts are not permitted in this field.

Wire #
Enter the wire transfer number, or press Enter to accept the next
 wire transfer number. The wire transfer number defaults to the next
 available number from the Cash Management Bank Account
 Maintenance screen.

Transfer type
Select the transfer type: Bank (internal transfer) or Payment (third party).

Cost center
If the cost center feature is enabled in the Enterprise
 Installation screen, enter the wire transfer cost center code
 in this field. This cost center will be used as a default during entry.

G/L transaction date
Enter the transaction date, or press Enter to accept the default of the current Cash Management Processing Date.

Transfer information

Amount
Enter the amount (up to $99,999,999.99) of the wire transfer to be wired from the bank account indicated above. The undistributed amount will display to the right of this field.

Memo
Enter any comments associated with this wire transfer.

Detail lines

Comp
Enter the transfer company code.

Bank account
Depending on the transaction type, enter the transfer bank account code or
 general ledger account code. If the Transfer Type specified in
 the heading portion of the screen was Bank, enter the bank
 account to which money will be transferred. If the Transfer
 Type specified was Payment, enter the General
 Ledger account code to be debited for transfer to a third party.
Note: Entry is prevented when the account code status is set to
 Not used. A warning displays when the status is
 set to Inactive.

Account description
Depending on the transaction type, the bank description or general ledger description (up to 30 characters) displays.

Amount
Enter the amount of the transfer or press Enter to accept the default amount.

Memo
Enter any comments for this line item, or press Enter to accept the
 software default of the text entered in the Memo field above.

Cost center
A Cost center field is provided on each detail line for
 expense distribution. As the cost center is recorded, Spectrum compares the
 bank account's list of shared cost centers with cost centers in the
 operator's assigned scheme; if there are no common cost centers, then that
 cost center is not allowed.
