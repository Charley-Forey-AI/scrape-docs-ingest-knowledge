---
title: "About Initializing Requisitions from Inventory | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-initializing-requisitions/about-initializing-requisitions-from-inventory"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-initializing-requisitions/about-initializing-requisitions-from-inventory"
---

# About Initializing Requisitions from Inventory

Use of the IN module allows you to initialize requisitions
 from low stock based on preset reorder quantities.
To enable a successful initialization, the
 materials must be set up at valid Inventory locations and you must specify values in the
 Low Stock and Reorder Qty fields (IN Location Materials).
During initialization, the system uses the
 following formula to determine whether to create a requisition: Available Units (On Hand
 – Allocated + On Order – requisitions Units already in PO) > Low Stock. Values for
 each item in the equation are taken from fields on IN Location Materials. If a
 material’s available units are less than the Low Stock amount, the system generates a
 requisition line and calculates the requisition amount based on the reorder quantity and
 the amount required to bring available units equal to the Low Stock
The following tables displays an example of
 how the system creates requisitions, based on amounts in the Available, Low Stock, and
 Reorder Qty fields on IN Location Materials.
For example, if the Available field is -200,
 and you have set the Low Stock field at 500 and the Reorder Qty field at 250, the system
 will determine that 700 units are needed to bring the on-hand quantity equal to the Low
 Stock amount (-200 + 700 = 500). Because the Reorder Qty field is set to 250, the system
 creates the requisition for 750 units (250 x 3).
Use PO Requisition Initialization to
 initialize requisitions from IN. Once you initialize the requisition, the system assigns
 it an Inventory line type. For more information, see PO Requisition Initialization in
 Related Topics below.
