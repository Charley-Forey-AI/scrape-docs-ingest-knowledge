---
title: "About Standing Purchase Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-standing-purchase-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-standing-purchase-orders"
---

# About Standing Purchase Orders

Standing or blanket purchase orders are open orders that you may post receipts to indefinitely - for example if you have negotiated a contract for materials at a specific unit cost but do not have a set limit (such as asphalt or concrete).
There are generally two types of standing/blanket POs:
Unit -based Unit of Measure

- Original Units = 0.00

- Unit Cost <> 0.00

- Cost = 0.00
LS Unit of Measure

- Cost = 0.00

- Units (disabled and set to 0.00)

- Unit Cost (disabled and set to 0.00)

Standing POs do not work with the PO item distribution feature since you can only distribute PO items into lines if there are units or amounts associated with those PO items. For more information about the PO Item Distribution feature, see [PO Item Distribution Overview](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview).
Setting up standing POs will not create a committed cost in Job Cost. When the goods are invoiced in AP Transaction Entry, the Committed Costs/Units will be updated as follows:

- Standing PO with Receiving checkbox selected:

- Remaining Committed Units/Cost = 0.00

- Total Committed Units/Cost = Invoiced Units/Cost

JCCD (Cost Detail)

Source
TotalCmtdUnits
TotalCmtdCost
RemCmtdUnits
RemCmtdCost

AP Entry
100.00
200.00
0.00
0.00

- Standing PO with Receiving checkbox selected:

- Remaining Committed Units/Cost = - Invoiced Units/Costs

- Total Committed Units/Cost = 0.00
If the Update GL/Subledgers on Receipt checkbox (in the PO Company Parameters form) is not selected:

JCCD (Cost Detail

Source
TotalCmtdUnits
TotalCmtdCost
RemCmtdUnits
RemCmtdCost

PO Receipts
100.00
200.00
100.00
100.00

AP Entry
0.00
0.00
-100.00
-200.00

If the Update GL/Subledgers on Receipt checkbox (in the PO Company Parameters form) is not selected:
JCCD (Cost Detail)

Source
TotalCmtdUnits
TotalCmtdCost
RemCmtdUnits
RemCmtdCost

PO Receipts
100.00
200.00
100.00
200.00

0.00
0.00
-100.00
-200.00

AP Entry
0.00
0.00
100.00
200.00

0.00
0.00
-100.00
-200.00

Note: If a purchase order item's unit of measure is unit-based and the current units are 0.00, the invoiced quantity will not reduce the backorder quantity. Likewise, if the unit of measure is LS and the current cost is 0.00 (e.g. freight), the invoiced amount will not reduce the backorder amount. This prevents negative committed units and costs when posting receipts and/or invoices against standing PO Items.
Standing POs remain open until you manually change the Status field in the PO Purchase Order Entry form to 1 - Complete.
Note: If you change a standing PO to a regular PO (by modifying the original units), JCCD and JCCP will be updated with the total committed costs/units and remaining committed costs/units adjusted by the amount of received units/costs.
