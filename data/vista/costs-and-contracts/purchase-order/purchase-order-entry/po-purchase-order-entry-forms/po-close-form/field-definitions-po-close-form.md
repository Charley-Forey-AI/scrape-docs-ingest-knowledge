---
title: "Field Definitions: PO Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form/field-definitions-po-close-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form/field-definitions-po-close-form"
---

# Field Definitions: PO Close Form

The following is a list of field descriptions for the PO
 Close form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Restrict By Vendor

Check this box to specify the vendor whose PO’s you want to close. Vendor is specified below.
Do not check this box if you want to close PO’s for all vendors.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Restrict By Job

Check this box to close purchase orders for a specific job. JC Company and Job are specified below.
Do not check this box if you want to close PO’s for all jobs.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Restrict By PO#

Check this box to specify the purchase order, or range of purchase orders, to close.
Do not check this box if you want to close all eligible purchase orders.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Vendor

 For “Restrict By Vendor,” specify the vendor whose PO’s you want to close.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## JC Co#

For “Restrict By Job,” specify the JC company in which to close PO’s.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Job

For “Restrict By Job,” specify the job whose PO’s you want to close.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Beginning PO#

Enter the PO number for beginning the selection
 process or press F4  to select it from a list.
This field is only enabled when the Restrict by
 PO# box is checked.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Ending PO#

Enter the last PO that should be closed. This field
 will default to the PO entered in the
 Beginning
 PO#
 field.
This field is only enabled when the
 Restrict by PO#
 box is checked.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close

## Restrict by SM

Restrict by SM checkbox on the PO Close form.
Select this checkbox to enable SM-specific filtering options for closing POs.

## SM Co

SM Co # field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the SM company whose POs you want to close. Press F4 for a list of SM companies.

## SM Customer

SM Customer field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the SM customers whose POs you want to close. Press F4 for a list of SM customers.

## SM Site

SM Site field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the SM site whose POs you want to close. Press F4 for a list of SM service sites.

## SM Work Order

SM Work Order field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the SM work order whose POs you want to close. Press F4 for a list of SM work orders.

## SM Svc Center

SM Svc Center field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the SM service center whose POs you want to close. Press F4 for a list of SM service centers.

## SM Division

Division field under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” specify the division whose POs you want to close. Press F4 for a list of SM divisions.
Note: This field is only editable when you have entered a value in the SM Svc Center field.

## SM Scope Status

SM Scope Status drop-down list under the Restrict by SM section of the PO Close form.
For “Restrict by SM,” select the SM scope status whose POs you want to close.

## Include POs With Backorders

The Include POs With Backorders checkbox on the PO Close form.
Select this checkbox to include purchase orders with remaining backorder units/amounts. The close process will set backordered units/amounts to 0.00 for all items on the purchase order.
Leave this checkbox unselected to exclude purchase orders with remaining backorder units/amounts. Only purchase orders with invoiced units and costs equal to their current units and costs on all items will be closed.

## Include Open Standing POs

The Include Open Standing POs checkbox on the PO Close form.
Select this checkbox to close open standing POs (non-LS POs with 0.00 units) without first marking them as complete. When selected, standing POs meeting the following criteria will be included in the close batch:

- Status is 'Open' or 'Complete'

- Received and Invoiced are equal

- Not already in a close batch

 Leave this checkbox unselected to exclude open standing POs (non-LS POs with 0.00 units) that are not marked as complete.

## Close Date

Specify the close date for all purchase orders in this batch.
Once you have entered the close date, click the Update button. The system will pull in all purchase orders that meet the selection criteria, and whose Received and Invoiced amounts are equal, and display them on the grid below. If you do not want a specific purchase order to be included in the close, click the row it is on and press the delete key. This will remove the purchase order from the close batch only.
Once you have reviewed all purchase orders on the grid and made the necessary deletions, click the Close POs button to finish the close process. The close process will set all Backordered amounts to 0.00, relieve any Remaining Committed Units and Costs in Job Cost, and On Order units in Inventory. The PO’s status is then set to Closed, and the MthClosed is updated with the specified close date.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form)PO Close
