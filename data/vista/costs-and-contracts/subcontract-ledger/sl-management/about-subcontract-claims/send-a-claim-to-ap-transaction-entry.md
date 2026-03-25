---
title: "Send a claim to AP Transaction Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-transaction-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-transaction-entry"
---

# Send a claim to AP Transaction Entry

You will use the SL Claim Update to AP Trans form to invoice a claim in an AP Transaction Entry batch.
For an overview of the claims process, see [Process Subcontract Claims](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims).
In order for a claim to appear in the SL Claim Update to AP Trans form, you must do the following in SL Subcontract Claims:

- Enter an approved amount for the claim in the Approve Amount field (Items tab).

- Certify the claim by selecting the Certified option in the Claim Status field.

If the claim still does not appear in the grid, one of the following applies:

- The Claim Approval Required checkbox was selected when the subcontract was created in SL Subcontract Entry, which means the claim cannot be sent to AP Transaction Entry. Instead, it must be [sent to AP Unapproved Invoice Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry).

- The claim was already processed.

1. Open the SL Subcontract Claims form.

1. Select File > Update to AP Transaction Entry . The Batch Selection form opens.

1. Open a batch using one of the following options:

- Select Create a new batch, enter the batch month, and click OK.

- Select Use an
 existing batch, choose the desired batch from the Unposted
 Batches grid, and click OK.

The SL Claim Update to AP Trans form opens.

1. If you are using pay categories (flag in AP Company Parameters), Pay Category and Pay Type fields display to the right of the month and batch. Use these fields to enter the pay category and pay type to assign to all items on the subcontract. If you leave these fields blank, you can assign a pay category and/or pay type to each item in AP Transaction Entry.
Note: These fields require that you either enter both a pay category and pay type or that you leave both fields blank.

1. To filter the claims displayed in the grid, select the Include claims from all vendors checkbox.To see claims for a specific vendor or range of vendors, deselect the Include claims from all vendors checkbox. Then use the Begin Vendor Sort Name and End Vendor Sort Name fields to enter the vendor or range of vendors.

1. To send all claims in the grid to Accounts Payable, select the Update all Claims to Accounts Payable checkbox.To individually select claims to send to Accounts Payable, select the Update checkbox for each applicable claim.

1. Click Update. The selected claims are sent to the selected
 AP Transaction Entry batch.Note: You cannot have multiple claims for the same
 subcontract in open AP Transaction Entry batches (a validation error will
 display when you try to send the second claim to AP Transaction Entry). You
 must post the AP Transaction Entry batch that contains the claim before you
 can send another claim to AP Transaction Entry.

1. If you want to process
 additional claims, repeat the steps above. Otherwise, click Close.

Once you sent a claim to AP Transaction Entry, you cannot make changes to the claim items or the generated invoice items. If you need to change a claim after if has been sent to Accounts
 Payable, you must delete the generated invoice in AP Transaction Entry and then
 change the claim in SL Subcontract Claims.
Invoice totals will be the claim amount plus/minus the tax on the invoice, depending
 on the country.

- Australia - the invoice total is the claim amount less the tax on the
 invoice. For example, if the claim amount is $25,000 and the tax amount is
 5%($1,250), the invoice total is $23,750.

- US/Canada - the invoice total is the claim amount plus the tax on the
 invoice. For example if the claim amount is $25,000 and the tax amount is
 5%($1,250), the invoice total is $26,250

 Open the AP Transaction Entry batch and process the
 invoices.
