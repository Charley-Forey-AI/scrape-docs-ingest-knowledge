---
title: "About Adding, Editing, and Deleting Bill Items | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-adding-editing-and-deleting-bill-items"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-adding-editing-and-deleting-bill-items"
---

# About Adding, Editing, and Deleting Bill Items

Once you have created a progress billing, you can modify the items, add new ones, or delete items using the Items tab in JB Progress Billing.
When you create a progress billing (via initialization or manual entry), the system populates the Items tab in JB Progress Billing with all items on the specified contract that have a Bill Type of Progress or Both, and includes the Previous Units and Previous Amount values for each item. You can then modify existing items, add new items, or delete items (if eligible) as needed.
The Items tab displays standard information that can be edited for each item on the invoice. You can display additional fields for entry as needed using the entry options available in the Options menu. For more information, see [About Progress Billing Grid Options](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-adding-editing-and-deleting-bill-items/about-progress-billing-grid-options).

## Adding and Deleting Bill Items

Bill items are added automatically as invoices are entered, so you typically won't need to add them manually. However, if a new item is added to the contract after the billing has already been created (for example, a change order item), you can then add a new bill item manually.
Note: If a billing's contract is closed (soft or hard closed), you can only add items if you allow posting to soft- and/or hard-closed jobs (options in JC Company Parameters).

If you have applied a maximum retention amount for the current contract and you exceed the maximum retention limit, the system displays a warning and you must decide whether to have the system automatically set the maximum retention amounts.
If you do not set maximum retention amounts and then later decide that you want to do so, select File > Limit Current Bill to Maximum Retention Allowed. The system checks to see if the maximum limit has been reached and you can then set the maximum retention amount.
You can delete items from a progress invoice only if all previous and current amounts for the item are zero. To delete an item, select the item and select the Delete button.
Note: If you need to delete a previously interfaced billing, and you've made unposted changes to it, you must revert those changes first. This ensures the billing matches the Accounts Receivable (AR) detail, allowing AR to correctly reverse the previously interfaced values.

## Editing Items

For items with a lump sum unit of measure, update progress by entering a new percent complete (% Complete field), a new to-date amount (To Date Amount field), or the amount to bill for this item this time (This Bill Amount field). When one field is changed, the other two automatically recalculate.
For items with units, you can update progress by changing amounts in the % Complete, To Date Amount, or This Bill Amount fields. If Options > Item Unit Entry is selected, you can also update progress by entering new to-date units (To Date Units field) or the units to bill this time (This Bill Units field). When one field is changed, all others automatically recalculate.
Note: If a billing's contract is closed (soft or hard closed), you can only edit items if you allow posting to soft- and/or hard-closed jobs (options in JC Company Parameters).

If you certify billings, additional fields are available for entering Claimed Units and/or Claimed Amount. However, these fields are initially hidden and must be set to Show in Grid using the Field Properties (F3) form. For more information, see [About Certifying Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-certifying-billings).
