---
title: "Purchase Order Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/costs-and-contracts/purchase-order-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/costs-and-contracts/purchase-order-features"
---

# Purchase Order Features

Vista 2024 R1 delivers on user-requested Purchase Order enhancements, fixes, and other improvements.

## Update PO Purchase Orders / PO Pending Purchase Orders for SM Tax Handling

 In conjunction with the changes made in Service Management for Tax Handling, the PO Purchase Order Entry and PO Pending Purchase Order forms will now default tax information (Tax Type and Tax Code) for SM-related lines (type 6-SM Work Order) based on the taxability of the work order scope. Taxability is determined by the SM Cost Type entered on the invoice line, and the Material Tax Override and Tax Option Override specified for the work order scope. For detailed information, see the F1 Help.
For more information about the tax changes made in SM, see the [SM Tax Handling](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/service-management/service-management-features#concept-k1quaafr1002--en__SMTaxHandlingRN) feature in the Service Management release notes.

## Require SM Cost Type on SM Work Order Invoice Lines with Tax

If you enter a purchase order item (in PO Purchase Order Entry) with a line type of 6-SM Work Order, and the PO item includes tax (the Tax Rate is not 0.00), you are now required to enter a cost type in the SM Cost Type field.
If you apply taxes to a PO item, but do not enter an SM Cost Type, an error displays indicating the SM Cost Type is missing and required for proper tax distribution. You must enter a cost type in order to save the line.

## Support SM Work Orders on Pending Purchase Orders

You can now add SM work order information to pending purchase order headers and items.
The PO Pending Purchase Order form has been updated to include the following fields:

- PO Header

- SM Co

- Work Order

- PO Items

- SM Co

- SM Work Order

- SM Scope Seq

- Phase

- JC CT

When you select the Process button to add the pending purchase order to a PO batch, the system now includes the SM work order values. You can then edit the PO (if needed) or validate and post the batch.
For information about pending purchase orders, see [PO Pending Purchase Orders Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-pending-purchase-orders-form).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
