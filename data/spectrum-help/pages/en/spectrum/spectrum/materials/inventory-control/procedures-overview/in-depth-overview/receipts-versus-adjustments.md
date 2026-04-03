---
title: "Receipts Versus Adjustments | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/receipts-versus-adjustments"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/procedures-overview/in-depth-overview/receipts-versus-adjustments"
---

# Receipts Versus Adjustments

Learn about the differences between receipts and
 adjustments.
When adding manual
 adjustment entries to Inventory Control, if costing methods LIFO or FIFO are being used,
 the entries are handled as described below.Receipts: Receipts always add new value layers (level 1) as
 they are posted.
Adjustments:
 Adjustments behave differently based on whether there is an existing layer with the same
 cost. Adjustments are considered to be changes to a previously posted transaction (such
 as a receipt) and are therefore matched with a previous layer with the same cost if it
 exists.

1. Adjustments with the same value as other layers add to the oldest layer (for example, level 5) with the same value. This applies to increases in the physical inventory as well, in which case the quantities are added at the current standard cost.

1. Adjustments with a different value than all other layers will create a new layer (level 1) record.

1. Use a receipt type transaction if the desired result is to create a new inventory layer.

1. The normal data entry flow while entering a negative adjustment transaction skips over the cost field. To manually enter the value for a negative adjustment use shift-tab to return to the cost field and input the desired value.
