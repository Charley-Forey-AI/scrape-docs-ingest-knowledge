---
title: "Change Order Entry - Billing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---billing"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-order-entry/change-order-entry---billing"
---

# Change Order Entry - Billing

Use this tab to add billing items for the change order, and add undistributed amounts to the billing adjustment value.
If you enter a bill group or bill item that is not already set up on the contract, the following scenarios will require further steps:

- No Bill Group If the contract is a unit price contract and the billing group is not already set up on the contract, a warning message prompts you to set up a new unit billing item. Click the New Group button to open the New Unit Billing Item window and enter details for the specified billing group.

- No Unit Billing Item If the contract is a unit price contract and the billing group is not already set up on the contract, a warning message prompts you to set up a new unit billing item. Click the New Item button to open the New Unit Billing Item window and enter details for the specified billing group and billing item.

- No Fixed Billing Item If the contract is a fixed price contract and the billing item is not already set up on the contract, a warning message prompts you to set up a new billing item. Click the New Item button to open the New Billing Item window and enter details for the specified billing item.
Note: If you want to remove a billing item that came from a change request, you will need to modify the [Change Request Entry - Billing](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---billing) in Change Request Entry.

Field/Button
Description

Group
If the contract is set up as a unit price contract, enter a billing group.

Group Description
If the contract is set up as a unit price contract, enter a description for the billing group.

Bill item
If the contract is set up as a unit price contract, enter a billing item for this change request.

Description
Enter a description for the billing item in this field.

Um
If the contract is set up as a unit price contract, enter a unit of measure for the billing item.

Unit price
If the contract is set up as a unit price contract, enter a price per unit. Entering zero or leaving this field blank is allowed.

Quantity
If the contract is set up as a unit price contract, enter a quantity for the billing item. Entering zero or leaving this field blank is allowed.

Amount
For unit price contracts, the amount in this field is the sum of Unit price multiplied by Quantity.
For non-unit price contracts, enter the amount in this field. Values entered here will update the Change order total.

CR?
This column will say 'Yes' if this item originated in Change Request Entry.
