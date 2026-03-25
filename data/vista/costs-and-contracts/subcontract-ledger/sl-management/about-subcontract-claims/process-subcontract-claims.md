---
title: "Process Subcontract Claims | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims"
---

# Process Subcontract Claims

Use the Claims process to create, maintain, print, and approve/certify subcontract claims.
This process mainly applies to Australian organizations, but it can also be used by American and Canadian organizations that would like to implement a formal approval process on subcontractor invoices.
The following steps detail the
 subcontract claim process.

1. If you require approval
 for subcontract claims, select the Claim Approval Required check
 box (in SL Subcontract Entry) when creating the subcontract. This forces you to
 route claims through the AP Unapproved Invoice process.If you do not require approval for
 subcontract claims, leave the Claim Approval Required check
 box unselected. This allows you to send the claim to either AP Transaction Entry
 or AP Unapproved Invoice Entry.

1. Create a claim in SL Subcontract Claims. When you create a new claim in
 the SL Subcontract Claims form, all of the existing items on the subcontract
 are automatically added to the Items tab. You can use the Items tab to
 delete any subcontract items that do not apply to the claim.Note: You cannot add an item to a claim after it has
 been sent to the AP module. Additionally, if you add a subcontract item
 to the subcontract after you have created the claim (for example a
 change order creates a new item on the subcontract), the new subcontract
 item will not be on the claim

1. Use the Items tab on the SL Subcontract Claims form to enter the claim amount and certified / approved amount on each subcontract item. By default the system calculates retention on the claim using the work complete retention percentage entered on the subcontract items during creation. You can change the retention amount if needed. For more information, see [Approved Retainage / Certified Retainage / Approved HoldBack](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form/field-definitions-sl-subcontract-claims-form#ID-0003efc4--en).

1. If you are sending the claim to AP Transaction Entry, certify the claim by
 selecting the Certify option in the
 Claim Status field (Info tab). The Claim
 Date field automatically defaults the current date, but you may
 override as needed. Note: If you do not certify the claim, it will not appear in the SL Update to
 AP Trans grid when selecting claims to process.

For claims being sent to AP Unapproved Invoice Entry, you can only certify the
 claim after you approve the invoice (see Step 6).

1. Send the claim to
 Accounts Payable.

- AP Transaction Entry - Use this route if
 you do not require approval for subcontract claims and are sending them
 directly an AP Transaction Entry batch. For more information, see [Send a claim to AP Transaction Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-transaction-entry).

- AP Unapproved Invoice Entry - Use this
 route if you are using the AP unapproved invoice approval process. For more
 information, see [Send a claim to AP Unapproved Invoice Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry).

Note: When you send a claim to AP, the invoice total is
 the claim amount plus/minus the tax on the invoice, depending on the
 country.

- Australia - the invoice total is the claim
 amount less the tax on the invoice. For example, if the claim amount
 is $25,000 and the tax amount is 5%($1,250), the invoice total is
 $23,750.

- US/Canada - the invoice total is the claim
 amount plus the tax on the invoice. For example if the claim amount
 is $25,000 and the tax amount is 5%($1,250), the invoice total is
 $26,250.

1. If you sent the claim(s)
 to AP Unapproved Invoice Entry, do the following:.

1. Approve the claim using the AP unapproved invoice review process. For
 detailed information, see [About Unapproved AP Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/about-unapproved-ap-invoices)

1. Certify the claim in SL Subcontract Claims by selecting the Certify option in the Claim
 Status field. The Claim Date
 field automatically defaults the current date, but you may override as
 needed.

Once you send a claim to AP Transaction
 Entry (either directly or via the unapproved invoice process), you will be unable to
 make changes to the invoice items or the claim items.
If you need to change a claim after if has been sent to the AP module, you must first delete the generated invoice in AP Transaction Entry and then change the claim in SL Subcontract Claims.

Related information

- [SL Subcontract Claims Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/sl-subcontract-claims-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Transaction Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-transaction-entry-form)
