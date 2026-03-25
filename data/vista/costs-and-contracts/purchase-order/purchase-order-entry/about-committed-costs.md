---
title: "About Committed Costs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-committed-costs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/about-committed-costs"
---

# About Committed Costs

Job purchase orders are used to track committed costs (held
 in the JCCP (Job Costs by Period) file).
The total value of a Job PO increases the
 total committed dollars. This field only changes if you add, change, or delete POs for
 the job. The remaining committed dollars accumulate all of the order information and are
 then decreased each time invoices for the items are posted in AP Transaction Entry.

- If you change a standing PO to a
 regular PO (i.e. modify the original units/cost), JCCD and JCCP will be updated
 with the total committed costs/units and remaining committed costs/units
 adjusted by the amount of received units/costs.

- When you add an item to a PO, the
 system sends the tax rate amount to the committed cost fields. If the tax rate
 amount changes, the system will not update the committed cost amounts. When
 relieving committed costs through AP, the system will relieve the original tax
 rate amount from the committed cost, but will use the current tax rate on the AP
 invoice.

If the unit of measure used to order the
 item equals the unit of measure for the job/phase/cost type (or can be converted), the
 total committed units and/or remaining committed units are also updated accordingly. The
 following equations are the calculations the system makes for committed costs.
Total Committed Units = Received Units +
 Backordered Units
Total Committed $$ = Total Committed Units x
 Current Unit Cost/ECM
Remaining Committed Units = [Units Received
 + Backordered Units] – Invoiced Units
Remaining Committed $$ = Remaining Committed
 Units x Current Unit Cost/ECM
Note: If a purchase order item's unit of measure is unit
 based and the current units are 0.00, the invoiced quantity will not reduce the
 backorder quantity. If the unit of measure is LS and the current cost is 0.00 (e.g.
 freight), the invoiced amount will not reduce the backorder cost. This will prevent
 negative committed units and costs when posting receipts and/or invoices against
 standing PO Items.Additional Information
