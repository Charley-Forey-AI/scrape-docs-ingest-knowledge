---
title: "About Posting Adjustments in General Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/transfersadjustments/about-posting-adjustments-in-general-ledger"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/transfersadjustments/about-posting-adjustments-in-general-ledger"
---

# About Posting Adjustments in General Ledger

When an adjustment batch is posted, General Ledger entries
 are automatically made to the Inventory and Inventory Adjustments accounts specified for the
 location (unless overwritten on an expense entry) in IN Locations.

However, if overrides are set up by
 category, then updates will be made to the accounts specified in IN Location Category
 Override.
The following example illustrates how a
 negative inventory adjustment affects GL accounts.
Units:
-5.00
(Damaged/Lost)

Unit Cost:
20.00

Total Cost:
-100.00

Debit
Credit

$100
$100

IN Adjustments
Inventory

Note: If the example used a positive amount, the $100 would be
 debited from the Inventory account and credited to the Inventory Adjustments account
 specified in IN Locations.
