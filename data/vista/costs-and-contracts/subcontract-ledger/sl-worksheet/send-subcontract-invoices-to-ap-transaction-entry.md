---
title: "Send Subcontract Invoices to AP Transaction Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/send-subcontract-invoices-to-ap-transaction-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/send-subcontract-invoices-to-ap-transaction-entry"
---

# Send Subcontract Invoices to AP Transaction
 Entry

Follow the steps below to update AP.
This replaces the need to enter these invoices in
 the AP Transaction Entry form; however, they will still be available to edit the
 invoices just like any other AP transaction.

1. In the SL Worksheet
 form, make sure that all information and invoice amounts are entered for the
 subcontracts.

1. Select File > Update to Accounts Payable  > Update to AP Transaction Entry. The Batch Selection form opens.

1. Select an existing batch
 or create a new one and then click the OK button. The SL Update to
 AP form opens.

1. Select which
 subcontracts will update to AP.

1. Complete the Pay
 Category and Pay Type fields.

Note: These fields only display if the Using Pay
 Category box on the Pay Types/Discounts/ICR tab in the AP
 Company Parameters form is checked, and they are only enabled if the Allow Payable
 Type Override box on the same tab and form is checked.
Pay Category
 This field defaults a pay category based on the following:

- If a standard or user pay category override is set up in F3 Properties (not
 recommended), defaults the F3 pay category.

- If an F3 override does not exist, defaults the pay category specified for
 the current user in VA User Profile.

- If an override pay category is not specified for the user, defaults the pay
 category defined in AP Company Parameters.

- If a default pay category is not defined for the company, default will be
 null. In this case, the pay type defaults from AP Company Parameters based
 on the line's type.

 If pay category is null, pay type will also be null. If both are left null, the update automatically assigns the subcontractor pay type from AP Company Parameters to each subcontract added to AP Unapproved Invoice Entry.
Pay Type
This field defaults based on the subcontract pay
 type on the selected pay category. This is set up using the Subcontract field on the AP Pay Category form.
You can only select a pay type that is associated with the selected pay category, or set up as unassigned. Assigned pay types are pay types that are restricted to a designated pay category (in AP Payable Types). Unassigned pay types are pay types that have no pay category restriction.
If pay category is null, pay type will also be null. If both are left null, the update automatically assigns the subcontractor pay type from AP Company Parameters to each subcontract added to AP Unapproved Invoice Entry.

1. Click Update. After the update is complete the AP Batch Processing
 form displays. Entries in the AP batch do not become AP transactions until the
 batch is validated and posted.

Which subcontracts will not be added?
Subcontracts will not be added to the AP Transaction
 Entry batch if:

- The Ready flag is not checked

- They are “in use” by some other SL or AP batch

- They point to a JC GL Co# in which the month is “closed”

- They do not have current amounts due

[Clear the SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/clear-the-sl-worksheet)
