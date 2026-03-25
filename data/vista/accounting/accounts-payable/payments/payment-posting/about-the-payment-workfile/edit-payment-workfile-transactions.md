---
title: "Edit Payment Workfile Transactions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/edit-payment-workfile-transactions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-the-payment-workfile/edit-payment-workfile-transactions"
---

# Edit Payment Workfile Transactions

Once you have added transactions to the AP Payment Workfile form, you can use the header and detail grids to edit transaction information.
The grids contain all transaction (and associated lines) that met the selection criteria you entered for the initialization process. Out-of-compliance transactions and lines display in red.

1. In the header grid, as needed, edit the



 Disc Date,



 Due Date,



 Pay Control,



 Pay Method,



 CM Acct, and



 Supplier fields.Note: If you added payments without specified vendors into
 the workfile, the
 Vendor field is typically the only field requiring an edit.

1. In the detail grid, as needed for each line item, edit the



 Disc Offered,



 Disc Taken,



 Due Date, and



 Supplier fields. Refer to the F1 help for more information on each header and line field.Note: If you change a line’s Due Date
 field, the system does not update the header’s Due Date
 field. However, the system uses it as the default date when you
 add the transaction to a payment batch or re-add it to a
 workfile.

1.  If you need to modify payment information for a transaction/line, select File > Tasks > Additional Pay Control
 Functions to access the AP Payment Control Detail form.

1.  Make edits as needed (such as hold status, applying a partial payment, change the offered or taken discount, etc.). For more information, see [AP Payment Control Detail](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-control-detail-form).Note: Although you can put a line on hold or remove a hold, this
 applies only to non-retainage holds. You cannot use this form to
 hold or release retainage. Retainage holds are placed on
 transactions in the AP Transaction Entry, AP Unapproved Invoice
 Entry, or AP Recurring Invoices forms, and must be released using
the AP Release Retainage form. For more information, see [Release Retainage for an AP Invoice](/en/vista/vista/accounting/accounts-payable/payments/retainage/release-retainage-for-an-ap-invoice).
