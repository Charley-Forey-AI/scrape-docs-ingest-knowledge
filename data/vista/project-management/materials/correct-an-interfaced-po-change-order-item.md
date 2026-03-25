---
title: "Correct an Interfaced PO Change Order Item | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/correct-an-interfaced-po-change-order-item"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/correct-an-interfaced-po-change-order-item"
---

# Correct an Interfaced PO Change Order Item

You can make changes to PO change order items that you have already interfaced using the PM PO Change Orders form, and then interface the changes to the appropriate modules via PM Interface.
You must have been given permission to access the error correction feature in VA User Profile. For more information, see[Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm) .
 When you are making corrections to a PO change order item, the interface batch month of the correction must be the same as the interface batch month of the original transaction. For example, if you interfaced a PO change order item using a batch month of 6/19, the batch month of the correction must also be 6/19. If the original batch month is closed, you must open the month before you can post the change.Other things you should know:

- You can make changes to an existing transaction, but you cannot delete a transaction. For example you can change the number of units on a units-based PO change order item, but you cannot delete the PO change order item.

- You can only correct PO change order items that you created in the PM module. PO change order items that you created in the PO module must be corrected in PO.

- Other users cannot change items that are being corrected. For example if you are making a correction to a PO change order item in PM PO Change Orders form, an error message will display if another user tries to change the same PO change order item in the PM PO Change Orders form.

 To correct and reinterface a purchase order item:

1. From the main menu, select Project Management > Programs > PM PO Change Orders.

1. Select the Interface tab.

1. Select a PO item by clicking in the column to the left of the Sequence field.

1. From the toolbar, select Tasks > Correct Item. The Description, Units (if unit-based) or Amount (if not unit-based), and Notes fields are now enabled.

1. Enter the correction.

1. Save the record.

1. To interface the change, go to Project Management > Programs > PM Interface. The change to the PO item will display as an item in the form. The entire amount of the corrected transaction will display in the Amount field (not just the amount of the change), and Correctionwill display in the Transaction Type column.

1. Interface the change.

The change is interfaced and all fields on the corrected item are disabled again in PM Material Detail.

Related concepts

- [PM PO Change Orders Form](/en/vista/vista/project-management/materials/pm-po-change-orders-form)

- [PM Interface Form](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)
