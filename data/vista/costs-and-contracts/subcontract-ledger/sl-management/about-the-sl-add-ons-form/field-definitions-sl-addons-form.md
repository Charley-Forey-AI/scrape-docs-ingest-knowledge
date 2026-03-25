---
title: "Field Definitions: SL AddOns Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-ons-form/field-definitions-sl-addons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-add-ons-form/field-definitions-sl-addons-form"
---

# Field Definitions: SL AddOns Form

The following is a list of field descriptions for the SL
 AddOns form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Add-on#

 Enter a number (between 0 and 255) that identifies this add-on.

##  Description

Enter a description for this add-on, up to 30 characters.

## Type

Percent – Select this radio button if you want the add-on amount to be calculated on the subcontract’s total amount.
Amount – Select this radio button if you want to specify a flat amount for this add-on.

## Percent

Specify the default percentage rate for this add-on. This rate is used to calculate the add-on amount when this add-on is set up on a subcontract in SL Entry.
Note: If this add-on is to be calculated as a negative amount, make sure you enter a minus (–) sign before the rate. (Example: –1.00%)

## Amount

Enter the flat amount for this add-on. This amount will be used as a default each time this add-on is set up on a subcontract in SL Subcontract Entry.
Note: Negative add-on amounts should be denoted by a minus (–) sign before the amount (for example: –500.00).

## Apply Percentage To Each Invoice

This checkbox is only available when the Percent radio button is selected.
Check this box if the percentage specified for this add-on is to be applied to each invoice. Each time an invoice that references this add-on is posted, the system calculates the add-on’s current invoice amount based on the specified percent and the sum of the invoice amounts for all regular and change order items on the subcontract.
If this checkbox is not selected, the full amount of the add-on is invoiced all at once.
There is a subcontract totaling $50,000 and a –1.00% add-on is set up for the subcontract. The total add-on amount for that subcontract will be $–500.00. If the Apply Percentage to Each Invoice checkbox is selected, and an invoice is posted against the subcontract for $10,000, the add-on amount for that invoice will be $–100.00. If the Apply Percentage to Each Invoice is not in use, the total add-on amount of $–500.00 will be applied to the invoice.

## Phase

Specify the phase to which the add-on amount is to be posted whenever the add-on is set up on a subcontract. This phase will default when added to a subcontract.

##  Cost Type

 Specify the cost type to which the add-on amount is to be posted whenever the add-on is set up on a subcontract. This cost type will default when added to a subcontract.
