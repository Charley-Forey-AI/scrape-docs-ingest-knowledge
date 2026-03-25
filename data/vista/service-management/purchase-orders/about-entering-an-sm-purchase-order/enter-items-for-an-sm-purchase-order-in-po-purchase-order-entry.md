---
title: "Enter Items for an SM Purchase Order in PO Purchase Order Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-items-for-an-sm-purchase-order-in-po-purchase-order-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-items-for-an-sm-purchase-order-in-po-purchase-order-entry"
---

# Enter Items for an SM Purchase Order in PO Purchase Order Entry

When you set up an SM purchase order (in SM Purchase Order Entry or PO Purchase Order Entry), you must enter at least one purchase order item.
Set up the purchase order in SM Purchase Order Entry or PO Purchase Order Entry. For more information, see [About Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order).
The following details how to enter items for an SM purchase order using the PO Purchase Order Entry form.

1. In the Item# field, enter an item number or N, New, or + to have the system auto-assign the item number.

1. From the Type drop-down, select 6-SM Work Order.

1. In the SM Co field, enter the SM company to which this purchase order item applies.

1. In the SM Work Order field, enter the work order to which this purchase order item applies or press F4 to select from a list of valid SM work orders.Note: If this a job-related work order and the job
 is soft or hard-closed, the system will only allow the entry if you selected the
  Allow Posting
 to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs check
 boxes in JC Company Parameters

1. In the SM Scope Seq field, enter the work order scope to which the purchase order item applies or press F4 to select from a list of valid scopes for the specified SM work order.Note: If this is a job-related work order and you specify a scope that is not assigned a phase, you must assign a phase before you can continue. You can do this by pressing F5 from the SM Scope Seq field to access the work order scope (in SM Work Orders). Then enter a valid phase and save the record. Once you close the SM Work Order form and return to PO Purchase Order Entry, re-enter the scope.

1. In the SM Cost Type field, enter the SM cost type or press F4 to select from a list of valid SM cost types.Leave this field blank if not associating an SM cost type with this purchase order item.

1. In the Material field, enter the material you are ordering/purchasing or press F4 to select from a list of valid materials.Leave this field blank if this item is for something other than a material. You can use the Description field to identify the purpose of the PO item.

1. In the Vendor Matl field, enter the vendor's number for the material.Leave this field blank if no vendor material number applies.

1. Select the Receiving box to receive this item in PO Receipts Entry or PO Initialize Receipts.Leave this box unselected to receive this item at the time it is invoiced in AP Transaction Entry.

1. For purchase orders on a job-related SM work order only, in the JC Cost Type field, enter the cost type to which costs will be posted for this PO item.

1. In the Description field, enter a description for the purchase order item or accept the default description. For information about how the system defaults the description, see the [F1](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-00030b95--en) help.

1. In the Req Date field, enter the date the material is required or accept the default (the Expected Date entered above).

1.  If you allow entry of a pay category and/or pay type (checkboxes in AP Company Parameters and PO Company Parameters, respectively):

1. In the Pay Category field enter the pay category for this purchase order item or accept the default pay category.

1. In the Pay Type field, enter the pay type for this purchase order item or accept the default pay type. See the [F1 help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-000467ee--en) for information about how the system derives the default pay type.

1. In the UM, Units, UC, ECM, and Total fields, accept the system defaults or enter the appropriate values. For more information, see the F1 help for each field.

1. From the tax Type drop-down, select the tax type or accept the default.

- 1-Sales

- 2-Use

- 3-VAT

Leave blank if not applying taxes to the PO item.For information about this field's default behavior, see the [F1 Help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046861--en).

1. In the Tax Code field, enter the tax code for the PO item or accept the default tax code. For information about this field's default behavior, see the [F1 help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046877--en).

1. If applicable, in the Supplier field, enter the supplier; otherwise, leave blank.

1. Save the record.

Once you have completed entering purchase order items, you must post the batch (FileProcess Batch. Once the batch is posted, the system generates a work completed Purchase line on the work order in SM Work Orders (Work Completed tab).
