---
title: "Send a claim to AP Unapproved Invoice Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry"
---

# Send a claim to AP Unapproved Invoice Entry

This will create an unapproved invoice that you can process
 using the AP unapproved invoices feature.
For an overview of the claims process, see [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims).
Unapproved invoices are invoices that you want held apart from other AP transactions - for example the invoices need to be reviewed and approved before they are posted and paid. Unapproved invoices do not update any subledger or GL, are not eligible for payment, and are not reported as Open Payables. Instead, they are stored and tracked in a separate set of files until the review/approval process is complete.
Note: You must enter an approved amount on a claim (SL Subcontract
 Claims> Items tab> Certified Amount / Approve Amount
 field) before you can send it to AP. If a claim does not have an approved amount, it
 will not display in this form.
Follow the steps below to send a claim to the AP Unapproved Invoice Entry form.

1. Open the SL Subcontract
 Claims form.

1. Select File > Update to AP Unapproved Invoice Entry.The SL Claim Update to AP Unapproved form displays.

1. In the UI
 Month field, enter the unapproved invoice month. This is
 generally the expense month, although you can change this month when the
 transactions are approved and posted.

1. If you are using pay categories (flag in AP
 Company Parameters), Pay
 Category and Pay
 Type fields display to the right of the month and batch. Use
 these fields to enter the pay category and pay type to assign to all items on
 the subcontract. If you leave these fields blank, you can
 assign a pay category and/or pay type to each item in AP Unapproved Invoice
 Entry.
Note: These fields require that you either enter both a
 pay category and pay type or that you leave both fields blank.

1. To filter the claims
 displayed in the grid, select the Include claims from all
 vendors checkbox.To see claims for a specific vendor or
 range of vendors, deselect the Include claims from all
 vendors checkbox. Then use the Begin Vendor
 Sort Name and End Vendor Sort Name fields
 to enter the vendor or range of vendors.

1. To send all claims in
 the grid to Accounts Payable, select the Update all Claims to Accounts
 Payable checkbox.To individually select claims to send to
 Accounts Payable, select the Update checkbox for each applicable claim.

1. Click Update. The selected claims are sent to AP Unapproved
 Invoice Entry.

1. If you want to process
 additional claims, repeat the steps above. Otherwise, click Close.

Once you send a claim to AP Unapproved Invoice Entry, you can no longer edit the
 claim using the SL Subcontract Claims form.
Each subcontract item on the claim is assigned the reviewer group specified for the
 job in the JC Jobs form (Invoices field, Info tab).
Invoice totals will be the claim amount plus/minus the tax on the
 invoice, depending on the country.

- Australia - the invoice total is the claim amount less
 the tax on the invoice. For example, if the claim amount is $25,000 and the
 tax amount is 5%($1,250), the invoice total is $23,750.

- US/Canada - the invoice total is the claim amount plus
 the tax on the invoice. For example if the claim amount is $25,000 and the
 tax amount is 5%($1,250), the invoice total is $26,250

Complete the review/approval process using the AP
 Unapproved Invoice process. For more information, see [About Unapproved AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices).
