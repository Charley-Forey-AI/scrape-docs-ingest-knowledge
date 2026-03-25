---
title: "Send Subcontract Invoices to AP Unapproved Invoice Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/send-subcontract-invoices-to-ap-unapproved-invoice-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/send-subcontract-invoices-to-ap-unapproved-invoice-entry"
---

# Send Subcontract Invoices to AP
 Unapproved Invoice Entry

Before updating to AP, make sure that you enter all subcontract information and invoice amounts in SL Worksheet. This includes selecting the Ready checkbox for all subcontracts that are being updated. When the system processes the batch, it adds all subcontracts that meet the selection criteria to an AP Unapproved Invoice Entry and deletes them from the worksheet.
To update subcontracts to AP Unapproved Invoice Entry:

1. Select File > Update to Accounts
 Payable  > Update to AP Unapproved
 Invoice Entry from SL Worksheet. This will open the SL Update to AP
 Unapprove form.

1. Enter the
 selection criteria to determine which subcontracts will update to
 AP.

1. In the Pay Category field, enter the pay category to apply to all of the subcontracts being updated to AP Unapproved Invoice Entry. This field defalts defaults to the pay category defined in AP Company Parameters. If a default pay category is not defined for the company, default will be null.

1. In the Pay Category field, enter the pay type to apply to all of the subcontracts being updated to AP Unapproved Invoice Entry. This field defaults the subcontract pay type for the selected pay category. If pay category is null, pay type will also be null. If both are left null, the update automatically assigns the subcontractor pay type from AP Company Parameters to each subcontract added to AP Unapproved Invoice Entry.

Note: These fields only display if the Using Pay Category box on the Pay Types/Discounts/ICR tab in the AP Company Parameters form is checked, and they are only enabled if the Allow Payable Type Override box on the same tab and form is checked

1. Click Update. After the update is complete the system displays a message stating the number of unapproved invoices that were created.

The system adds the subcontracts to the AP Unapproved
 Invoice form. Subcontracts will not be added if:

- The Ready flag is not
 checked

- They are “in use” by some other SL or AP batch

- They point to a JC GL Co# in which the month is
 “closed”

- The subcontract job has neither an assigned reviewer
 or reviewer group

- They do not have current amounts due

[AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)
