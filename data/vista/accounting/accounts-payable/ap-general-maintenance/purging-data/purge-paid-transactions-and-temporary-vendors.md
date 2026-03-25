---
title: "Purge Paid Transactions and Temporary Vendors | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/purging-data/purge-paid-transactions-and-temporary-vendors"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/purging-data/purge-paid-transactions-and-temporary-vendors"
---

# Purge Paid Transactions and Temporary Vendors

You can use the Paid Trans/Temp Vendors tab on the AP Purge
 form to remove paid transactions through a specified month/year.
In order to remove
 transactions:

- the month must be closed in the subledgers of the GL company assigned in
 AP Company Parameters (GL
 Co#
 field, GL Expense Posting tab)

- all lines of a transaction
 must be fully paid

- the month for the last payment made for the transaction must
 match the month that you specify

When
 purging paid transactions, if the vendor has been set to be temporary (you selected the
 Temporary checkbox in the AP Vendors form) the system checks for any
 remaining open or paid transactions. If nothing is found, the vendor's annual totals and
 static information in AP Vendors are also deleted.
The Paid Trans/Temp Vendors tab removes records and their attachments
 from the bAPTH, bAPTL, bAPTD, bAPUR, and bAPVM database tables. While the information in
 these tables can be kept indefinitely, this information takes up considerable space and you
 should develop a regular purge cycle.
To purge paid transactions and temporary
 vendors:

1. Open the AP Purge form and select the Paid Trans/Temp Vendors tab.

1. Check the
 Paid Transactions and Temporary Vendors
 box. The system enables the
 Through Month
 and
 Restrict by Vendor
 fields.

1. In the
 Through Month
 field, enter the month through which the system will purge paid transaction and temporary vendor information.

1. If you want to purge
 transactions for a specific vendor only, select the Restrict by Vendor checkbox. You will
 need to select this checkbox if you want to purge transactions for a vendor who has been
 set to be selectively purged (you selected the Selective Purge checkbox in the AP
 Vendors form). The system enables the Vendor
 field.

1. If you are purging transactions for a specific vendor, enter the vendor in the
 Vendor
 field. Press
 F4
 for a list of vendors.

1. Click
 Purge
 . The system displays a confirmation dialog.

1. Click
 Yes.

The system purges all fully paid transactions up through the specified month/year. If you have not specified a specific vendor, the system will delete transactions for all vendors that have not been set as requiring a selective purge.
