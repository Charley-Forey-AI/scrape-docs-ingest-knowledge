---
title: "Change Request Entry - Billing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---billing"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---billing"
---

# Change Request Entry - Billing

Use this tab to add billing items for the change request.
If you enter a bill group or bill item that is not already set up on the contract, the following scenarios will require further steps:

- No Bill Group If the contract is a unit price contract and the billing group is not already set up on the contract, a warning message prompts you to set up a new unit billing item. Click the New Group button to open the New Unit Billing Item window and enter details for the specified billing group.

- No Unit Billing Item If the contract is a unit price contract and the billing group is not already set up on the contract, a warning message prompts you to set up a new unit billing item. Click the New Item button to open the New Unit Billing Item window and enter details for the specified billing group and billing item.

- No Fixed Billing Item If the contract is a fixed price contract and the billing item is not already set up on the contract, a warning message prompts you to set up a new billing item. Click the New Item button to open the New Billing Item window and enter details for the specified billing item.

If the change request status is 'Proposed', the billing group and billing item will be blank, the unit of measure will be lump sum, and the amount field will be the total of the cost worksheet plus markups, add-ons and fees.
To change the billing adjustment value, you can either modify the amount on line one of this tab, add two or more billing items, or delete a billing line.
Field/Button
Description

Group
If the contract is set up as a unit price contract, enter a billing group and description.

Bill item
Enter a billing item for this change request. For fixed price job requests with an action type of 3, 4, or 5, this field may be left blank.
Change request status codes are assigned in the [Change Request Status File Maintenance](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-request-status-file-maintenance) screen.

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
For non-unit price contracts, enter the amount in this field. Values entered here will update the Change request total.
