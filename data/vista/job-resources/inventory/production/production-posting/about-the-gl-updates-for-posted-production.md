---
title: "About the GL Updates for Posted Production | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/production-posting/about-the-gl-updates-for-posted-production"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/production-posting/about-the-gl-updates-for-posted-production"
---

# About the GL Updates for Posted Production

When producing finished goods, whether through manual
 production in the IN Production Entry form or automatic production in the MS Ticket
 Entry form, the system updates General Ledger based on the GL accounts defined for
 the production location.

- If a standard Bill of Materials is used, General
 Ledger entries are made to the Cost of Production, the Value
 of Production, and the Inventory accounts specified for the
 production location (IN Locations form).

- If an override Bill of Materials is used, the system
 makes General Ledger entries to the Cost of Production, the Value of Production,
 and the Inventory accounts specified for the production location/category in the
 IN Location Category Override form.

The GL entry amounts for Cost of Production and Inventory (Raw Materials) are different than the GL amounts for Inventory (Finished Good) and Value of Production. This is because the cost of the finished good is used, not the total cost of the raw materials. You can control this cost and set it to include other costs of production. The following example shows how the General Ledger entries are made.
Debit
Credit

$100 Cost of Production
$100 (Raw Materials) Inventory

$200 (Finished Good)  Inventory
$200 Value of Production
