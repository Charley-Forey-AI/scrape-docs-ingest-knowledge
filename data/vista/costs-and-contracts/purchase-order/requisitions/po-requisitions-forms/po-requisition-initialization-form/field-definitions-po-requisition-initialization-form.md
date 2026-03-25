---
title: "Field Definitions: PO Requisition Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form/field-definitions-po-requisition-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form/field-definitions-po-requisition-initialization-form"
---

# Field Definitions: PO Requisition Initialization Form

The following is a list of field descriptions for the PO
 Requisition Initialization form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Initialize Requisition Lines From

- Inventory Low Stock – Select this option to initialize requisition lines based on low stock in IN Location Materials. Materials with quantities below the specified Low Stock amount will be set up on a requisition line. System determines requisition eligibilty as follows:

Available (On Hand – Allocated + On Order – Units already in PO) > Low Stock
If the 'available' units are less than the Low Stock amount, the system will then determine the amount to requisition based on the reorder quantity and the amount needed to bring available units equal to the low stock amount:
Available = -200
Low Stock = 500
Reorder Qty = 250
Requisition Qty = 750
In this scenario, 700 units are needed to bring the on-hand quantity equal to the Low Stock amount. The reorder quantity is 250, so 750 units (3 blocks of 250) are requisitioned. (Note: Open batches are not considered when calculating the number of units to requisition.)
Note: If Low Stock or Reorder Qty are equal to 0.00, no requisitions will be created for that material.

- EM Open Work Orders – Select this option to initialize requisition lines based on open work orders in Equipment Management. When selected, the initialization process will check open work orders for needed parts, then create requisition lines for all parts with the P/S flag set to 'P' (Purchase) and the Required flag set to 'Y' (checked).

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  IN Company

 Enabled only when initializing from Inventory Low Stock.
 Specify the IN company by which to restrict initialization of requisition lines. Only materials in this IN company that meet all other selection criteria and are below 'low stock' quantities, will be initialized onto requisition lines.
Note: IN company is required if restricting by Location Group and/or Location.
[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  IN Location Group

 Enabled only when initializing from Inventory Low Stock.
 Specify the location group (from IN Location Groups) by which to restrict initialization of requisition lines. Only materials in this location group that meet all other selection criteria and are below 'low stock' quantities, will be initialized onto requisition lines. Leave blank if not restricting by location group.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  IN Location

 Enabled only when initializing from Inventory Low Stock.
 Specify the location (from IN Locations) by
 which to restrict initialization of requisition lines. Only materials stocked at this
 location that meet all other selection criteria and are below 'low stock' quantities, will
 be initialized onto requisition lines. Leave blank if not restricting by location.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Material Category

 Specify the material category (from HQ Material Categories) by which to restrict initialization of requisition lines. Only materials in this category that meet all other selection criteria and are below 'low stock' quantities (if initializing from low stock) or are on open work orders (if initializing from open work orders), will be initialized onto requisition lines. Leave blank if not restricting by material category.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  EM Company

 Enabled only when initializing from EM Open Work Orders.
 Specify the EM company by which to restrict initialization of requisition lines. Only materials (parts) on open work orders in this EM company that meet all other selection criteria will be initialized onto requisition lines. Leave blank if not restricting by EM company.
Note: EM company is required if restricting by EM Shop.
[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  EM Shop

 Enabled only when initializing from EM Open Work Orders.
 Specify the shop (from EM Shops) by which to restrict initialization of requisition lines. Only materials (parts) on open work orders in this EM company that meet all other selection criteria will be initialized onto requisition lines. Leave blank if not restricting by EM shop.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Open WO Through Date

 Enabled only when initializing from EM Open Work Orders.
 Specify the shop (from EM Shops) by which to restrict initialization of requisition lines. Only materials (parts) on open work orders in this EM company that meet all other selection criteria will be initialized onto requisition lines. Leave blank if not restricting by EM shop.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Add to Existing Requisition

 Check this box to add all lines created via the initialization process to an existing requisition (specified to the right).
 Do not check this box if you want the initialization process to create a new requisition header. All lines created via the initialization process will be added to the new requisition.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Requisition ID

 Check this box to add all lines created via the initialization process to an existing requisition (specified to the right).
 Do not check this box if you want the initialization process to create a new requisition header. All lines created via the initialization process will be added to the new requisition.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Requestor

The Requestor field on the PO Requisition Initialization form.
 Enabled only if the Add to Existing Requisition checkbox is unselected.
 Required.
 Enter the name or initials (up to 128 characters) of the person requesting the requisition.

##  Description

 Enabled only if Add to Existing Requisition option is N (unchecked).
 Required. Enter a description of the requisition, up to 30 characters. The description entered here will default as the description in the requisition header.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Ship Location

Press F4to select a shipping location from a
 list. The selected location will be assigned to each line on the requisition.
Shipping locations are created and maintained using the [PO Shipping Locations ](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-shipping-locations-form) form.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Vendor

 Press F4 to select an
 AP vendor from a list. The selected vendor will be assigned to each line
 on the requisition.
AP vendors are created and maintained using the
 [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) form.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Required Date

 Enter a requisition date. The selected requisition date will be assigned to each line on the requisition.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

## Route

Specify the route type for the requisition.

- 0-Quote – Select this type if the requisition lines must go through the quote process.

- 1-Purchase – Select this type if the requisition lines will be sent directly to a PO.

The route type selected here will be assigned to each line on the requisition.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization

##  Reviewer

 If applicable, enter the reviewer for this requisition. This reviewer will be assigned to each line on the requisition, in addition to the default reviewers designated at the company, job, EM department, and IN location levels.

[](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)PO Requisition Initialization
