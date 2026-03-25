---
title: "PO Requisition Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form"
---

# PO Requisition Initialization Form

Use this form to create requisition lines based on inventory low stock or open work orders.

The option you select determines where the system looks for materials to requisition, as well as what criteria is used to select the materials. These options are as follows.
Inventory Low StockIf you elect to use this option, the system checks the 'low stock' value for materials (defined in IN Location Materials) based on the IN company, location group, location, and/or material category you specify. Materials with stock below the specified amount are set up on a requisition line. To determine if a material should be requisitioned, the follow formula is used:Available Units (On Hand – Allocated + On Order – Units already in PO) > Low Stock
If a material's available units are less than the Low Stock amount, the system determined the amount to requisition based on the reorder quantity and the amount needed to bring available units equal to the low stock amount.
For example:
Available = - 200
Low Stock = 500
Reorder Qty = 250
Requisition Qty = 750
In this scenario, 700 units are needed to bring the on-hand quantity equal to the Low Stock amount. The reorder quantity is 250; therefore 750 units (3 blocks of 250) are requisitioned. (Note: Open batches are not considered when calculating the number of units to requisition.)
Note: If the Low Stock or Reorder quantities are equal to 0.00, no requisitions will be created for that material.

EM Open Work OrdersIf you select this option, the system will check open work orders for needed parts based on the EM company, shop, scheduled through date, and/or material category you specify. Parts with their P/S flag set to 'P' (Purchase) and their Required flag set to 'Y' (checked) will be set up on a requisition line.

## Add To Existing Requisition

You have the option to specify whether requisition lines created during initialization will be added to an existing requisition or added to a new requisition. If you opt to add to an existing requisition, an additional input is displayed to allow specifying the requisition to which the lines will be added. If you opt to create a new requisition, the initialization process will generate a requisition using the next sequential number available based on the highest requisition number in the system

## Assigning a Reviewer

This option allows you to assign an "Active" reviewer (as activated via HQ Reviewers) to each requisition line created during initialization. The reviewer specified here will be assigned in addition to any default reviewers that may be designated at the company, job, EM department, and/or IN location levels.
Note: If you do not require approval of requisition lines before they are added to a quote or purchase order (flags in company file), you should not need to assign a reviewer here. However, if you do assign a reviewer, the lines will need to be approved (or the reviewer deleted from the Reviewers tab in PO Requisition Entry) before they can be added to a quote or purchase order.

[PO Requisition Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form)
