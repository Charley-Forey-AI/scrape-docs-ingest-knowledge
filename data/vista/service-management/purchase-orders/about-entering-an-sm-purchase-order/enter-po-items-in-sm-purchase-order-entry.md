---
title: "Enter PO Items in SM Purchase Order Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-po-items-in-sm-purchase-order-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order/enter-po-items-in-sm-purchase-order-entry"
---

# Enter PO Items in SM Purchase Order Entry

When you set up an SM purchase order (in SM Purchase Order Entry or PO Purchase Order Entry), you must enter at least one purchase order item.
Set up the purchase order in SM Purchase Order Entry or PO Purchase Order Entry. For more information, see [About Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order).
The following details how to enter a purchase order item using the SM Purchase Order Entry form.

1. In the
 Item
 field, enter
 N
 or + to add
 a new purchase order item. The system automatically assigns the next sequential PO
 item number.

1. In the
 Scope Seq
 field, enter the work order scope to which this purchase order item applies.

1. In the SM Cost Type
 field, enter the SM cost type for this purchase order item or press F4  to select
 from a list of valid SM cost types.Leave this field blank if not associating
 an SM cost type with this purchase order item.

1. In the Material field,
 enter the material for this purchase order item or press F4 to select
 from a list of valid HQ materials.

1.  In the
 Vendor Matl
 field, enter the vendor's number for this material. Leave blank if not applicable.Note: If the vendor/material is set up in PO Vendor Materials,
 this field automatically defaults the vendor's material number. For more information,
 see the [F1
 help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-000467b1--en).

1. In the
 Description
 field, accept the default description or enter a new description.For information about how the default
 description is derived, see the [F1
 help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-000467c0--en).

1. Select the Receiving check
 box to receive this purchase order item in PO Receipts Entry. If not selected, you can receive
 the PO at the time of invoicing (in AP Transaction Entry).

1. In the
 Req Date
 field, enter or select the date the material/merchandise is required.

1. If you allow entry of a pay category and/or pay type (checkboxes in AP Company Parameters and PO Company Parameters, respectively):

1. In the Pay
 Category field enter the pay category for this purchase order item or
 accept the default pay category.

1. In the Pay Type
 field, enter the pay type for this purchase order item or accept the default pay type.
 For information about the pay type default behavior, see the [F1
 Help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-000467ee--en).

1. In the UM, Units,
 UC,
 ECM,
 and Total fields, accept the system defaults or enter the appropriate values.
 For more information, see the F1 help for each field.

1. From the tax Type
 drop-down, select one of the following:

- 1-Sales

- 2-Use

- 3-VAT

Leave blank if not applying taxes to the PO item.For information about this field's default behavior, see the [F1 Help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046861--en).

1. In the
 Tax Code
 field, enter the tax code for the purchase order item or accept the default.For information about this field's default behavior, see the [F1 Help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-00046877--en).

1. For job work orders only, in the
 JC Cost Type
 field, enter the JC cost type for this purchase order item or accept the default cost type. For information about this field's default behavior, see the [F1 Help](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form/field-definitions-sm-purchase-order-entry-form#ID-000468b8--en).

1. Save the record.

Once you close the form (by selecting the X in the upper corner of the window), the system automatically posts the batch and generates a work completed Purchase line (in SM Work Orders, Work Completed tab).
