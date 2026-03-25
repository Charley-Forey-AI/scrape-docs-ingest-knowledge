---
title: "Updates to Other Modules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/receiving/updates-to-other-modules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/receiving/updates-to-other-modules"
---

# Updates to Other Modules

When you receive purchase order items, Job Cost and Inventory are the only modules that are directly affected.

Receiving items on expense, equipment, and work order POs changes the status of Received Units and Backordered Units, but does not make any interfacing entries to other modules.
The following shows the updates that occur when receiving PO items (that are flagged for receiving).Job Lines

- Remaining Committed Units (if backorder is changed)

- Remaining Committed Dollars (if backorder is changed)

- Received Not Invoiced Units

- Received Not Invoiced Dollar Amount

Actual Units and Costs if the Update G/L Sub-Ledgers on Receipts box is checked and the JC Interface Level option in PO Company Parameters is set to Detail.
Inventory Lines

- Received Not Invoiced Units

- On Order Units (if backorder is changed)

- Actual Units and Costs if the Update G/L Sub-Ledgers on Receipts checkbox is selected and the IN Interface Level option in PO Company Parameters is set to Detail.

If the Std U/M for the purchased material is not the same as the Purch U/M (defined in HQ Materials), the system performs a conversion and recalculates the item to the Std U/M before it updates the units fields. If the U/M is Lump Sum, no conversion is performed.
Equipment / EM Work Order Lines Actual Units and Costs if the Update G/L Sub-Ledgers on Receipts box is checked and the EM Interface Level option in PO Company Parameters is set to Detail.Expense LinesExpense entries are updated to General Ledger if the Update G/L Sub-Ledgers on Receipts checkbox is selected and the GL Expense Interface option in PO Company Parameters is set to Summary or Detail.SM Work Order LinesExpense entries are updated to General Ledger if the Update G/L Sub-Ledgers on Receipts checkbox is selected and the GL Expense Interface option in PO Company Parameters is set to Summary or Detail. Note: If the work order is job-related, updates to Job Cost will occur if the JC interface box is checked in SM Company Parameters.
