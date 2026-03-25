---
title: "Correct an Interfaced Purchase Order Item | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/correct-an-interfaced-purchase-order-item"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/correct-an-interfaced-purchase-order-item"
---

# Correct an Interfaced Purchase Order Item

You can make changes to purchase order items that you have
 already interfaced using the PM Material Detail form, and then interface the changes to the
 appropriate modules via PM Interface.
You must have been given permission to access the error
 correction feature in VA User Profile. For more information, see [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm) .
 When you are making corrections to a
 purchase order item, the interface batch month of the correction must be the same as the
 interface batch month of the original transaction. For example, if you interfaced a
 purchase order item using a batch month of 6/19, the batch month of the correction must
 also be 6/19. If the original batch month is closed, you must open the month before you
 can post the change.Other things you should know:

- You can make changes to an existing transaction, but you cannot delete a
 transaction. For example you can change the number of units on a units-based PO
 item, but you cannot delete the PO item.

- You can only correct purchase order items that you created in the PM module.
 Purchase order items that you created in the PO module must be corrected in
 PO.

- Other users cannot change items that are being corrected. For example if you are
 making a correction to a PO item in the PM Material Detail form, an error
 message will display if another user tries to create a PO change order for that
 item in the PM PO Change Orders form.

 To correct and reinterface a purchase order item:

1. From the main menu, select Project Management > Programs > PM Material Detail.

1. Select the Interface tab.

1. Select a PO item by clicking in the column to the
 left of the Sequence field.

1. From the toolbar, select Tasks > Correct Item.

1. The selected row is highlighted and most of the
 fields are enabled.

1. Enter the correction.

1. Save the record.

1. To interface the change, go to Project Management > Programs > PM Interface. The change to the PO item will display
 as an item in the form. The entire amount of the corrected transaction will
 display in the Amount field (not just the
 amount of the change), and Correctionwill display in the
 Transaction Type column.

1. Interface the change.

 The change is interfaced and all fields on the
 corrected item are disabled again in PM Material Detail.
