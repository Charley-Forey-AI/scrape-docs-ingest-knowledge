---
title: "About Calculating and Distributing Claim Retention | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/about-calculating-and-distributing-claim-retention"
---

# About Calculating and Distributing Claim Retention

You can calculate and distribute retainage/retention/holdback (depending on country) for a subcontract claim in SL Subcontract Claims.

Note: The label for retainage fields and buttons in SL Subcontract Claims display differently based on country: Retainage (US), Retention (AU), and Holdback (CA). However, for the purposes of this article, we will use 'retention'.

When you enter items on a subcontract claim, retention is automatically calculated for each item based on the Work Completed Retention % specified for the item (in SL Subcontract Entry) and the Approve Amount specified for each item (on the Items tab of the SL Subcontract Claims form).
Note: You can see the retention amounts by selecting the Show Retention button in SL Subcontract Claims.

The diagram below outlines how the system selects a default retainage percentage when the subcontract item is created.

The system then totals the retention on the subcontract items and applies the maximum retention (if a maximum retention is defined for the subcontract). For an overview on maximum retention, see [About Subcontract Maximum Retention Amounts](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts).
If item retention exceeds the total retainage allowed for the subcontract, the system displays a "Max Retainage limit has been exceeded" warning (in red) next to the Retainage Remaining field in the Subcontract Details section at the top of the form. However, you can still save the claim.
Note: If you selected the Enforce Catch Up checkbox on the SL Company Parameters form, retention on the claim is calculated differently. For more information, see [Enforce Catch Up](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-setupmaintenance/sl-setup/about-the-sl-company-parameters-form/field-definitions-sl-company-parameters-form#ID-0003e70d--en).

## Distribute Item Retention

The Distribute Item Retention button in the Subcontract Details section allows you to recalculate and distribute item retention.
You can use this option any time; however, the most common uses for this option are:

- to reset manually entered retention on the claim. For example if you manually entered retention on the claim, but would like the retention to be calculated using the work complete retention percentage entered on each subcontract item included in the claim, use this option to reset the manually entered retention and restore the default values.

- to reset retention for subcontract items when item retention exceeds the total retainage allowed for the subcontract (as defined by the maximum retention set up on the subcontract in SL Subcontract Entry, Maximum Retention tab).

When selected, the system calculates and distributes the retention on the claim based on the work complete retention percentage entered on each subcontract item included on the claim (this is true even if the percent/amount of retention to distribute is zero). Any manual retention amounts you entered are reset.
If the subcontract's maximum retention percent or amount is set to 0.00, selecting this button sets the retention amount to 0.00 for each subcontract item on the claim.
Note: If the "Max Retainage limit has been exceeded" warning displays due to item retention exceeding the total retainage allowed for the subcontract, selecting the Distribute Item Retention button clears the message.

## What happens when you change the retention amount?

If you change the approved retention on the claim, the system updates the approved retention on the subcontract items included on the claim (SL Subcontract Claims, Items tab).
If you reduce the approved retention on the claim, the retention on the subcontract item with the highest item number is reduced. For example:
BeforeAfter
Approved retention on claim = $20,000Approved retention on claim = $15,000
Item #1$2,500Item #1$2,500
Item #2$7,500Item #2$7,500
Item #3$10,000Item #3$5,000

If the retention on the highest subcontract item is not large enough to cover the entire reduction, the retention on the next highest subcontract item is reduced.
The example below illustrates what would happen if you changed the approved retention on the claim from $20,000 to $5,000.
BeforeAfter
Approved retention on claim = $20,000Approved retention on claim = $5,000
Item #1$2,500Item #1$2,500
Item #2$7,500Item #2$2,500
Item #3$10,000Item #3$0

If you increase the approved retention on the claim, the retention on the first subcontract item is increased.
For example:
BeforeAfter
Approved retention on claim = $20,000Approved retention on claim = $30,000
RetentionApproved AmountRetentionApproved Amount
Item #1$2,500$50,000Item #1$12,500$50,000
Item #2$7,500$150,000Item #2$7,500$150,000
Item #3$10,000$200,000Item #3$10,000$200,000

If the increase is greater than the approved amount on the first subcontract item, the retention on the next subcontract item will be increased, and so on. The approved amount on the subcontract item is the approved amount on the current claim, not the claim to date approved amount.
Note: The approved retention on the claim cannot be greater than the current approved amount on the claim. An error message displays if this occurs.
If you increase the approved amount on a claim and it exceeds the total retainage allowed for the subcontract (as defined by the maximum retention set up on the subcontract in SL Subcontract Entry, Maximum Retention tab), the system displays a warning. You can still save the claim, but "Max Retainage limit has been exceeded" will display next to the Retainage Remaining field in the Subcontract Details section at the top of the form.
For more information about maximum retention, see [About Subcontract Maximum Retention Amounts](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts).
