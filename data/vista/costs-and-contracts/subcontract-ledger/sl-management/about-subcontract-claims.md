---
title: "About Subcontract Claims | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims"
---

# About Subcontract Claims

Use the Claims process to create, maintain, print, and approve/certify subcontract claims.
 The claims process mainly applies to Australian organizations, but it can also be used by American and Canadian organizations that would like to implement a formal approval process on subcontractor invoices.
The claims process starts in the SL Subcontract Claims form, which allows you to create a claim, select the subcontracts/items to include, and then send the claim to Accounts Payable for further processing.
There are two options for sending claims to Accounts Payable:
[Send a claim to AP Unapproved Invoice Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-unapproved-invoice-entry)
[Send a claim to AP Transaction Entry](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/send-a-claim-to-ap-transaction-entry)

## Custom Fields

When you add a custom field to the SL Subcontract Claims form using the VA Custom Field Wizard, you can also add the custom field to the AP Transaction Entry and/or AP Unapproved Invoice Entry forms. This means that the values entered in the custom field on the SL Subcontract Claims form will update the same custom field when the claim is sent to the AP module.

- When you add a custom field to the Info of the SL Subcontract Claims form, you can also add that field to the upper portion of the AP Transaction Entry and AP Unapproved Invoice Entry forms.

- When you add a custom field to the Items tab of the SL Subcontract Claims form, you can also add that field to the lower portion of the AP Transaction Entry and/or AP Unapproved Invoice Entry forms.

## Retention

When you create a claim using the SL Subcontract Claims form, by default retention is calculated using the work complete retention percentage set up on each subcontract item when the subcontract was created.
You can accept this default, or you can do one of the following:

- Change the retention at the claim level using the Approved Retention field on the Info tab in SL Subcontract Claims.Note: Changing the calculated retention at the claim level overrides the maximum retention defined for the subcontract in SL Subcontract Entry, Maximum Retention Settings tab).

- Change the retention at the subcontract item level using the Approved Retention field on the Items tab in SL Subcontract Claims.

There are three basic validation rules that apply to the retention amount entered on the claim, and the retention amounts entered on the subcontract items included in the claim:

- The retention amount cannot exceed the approved amount. This applies to both the subcontract items on the claim, and the claim itself.

- The retention amount cannot be positive if the subcontract item on the claim has a negative amount. For example if a subcontract item included on the claim is a deduction item (has a negative value), the retention on that subcontract item cannot be positive.

- The retention amount can be negative.

Note: If you want to allow users to create claims that are greater than the subcontract amount using the SL Subcontract Claims form, select the Allow Exceeded Claim Entry checkbox on the SL Company Parameters form.
For more information about claim retention, see [About Calculating and Distributing Claim Retention](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention) and [About Subcontract Maximum Retention Amounts](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts).
