---
title: "Correct an Interfaced Subcontract Change Order Item | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/correct-an-interfaced-subcontract-change-order-item"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/correct-an-interfaced-subcontract-change-order-item"
---

# Correct an Interfaced Subcontract Change Order Item

 You can make changes to a subcontract change order item that
 you have already interfaced using PM Subcontract Change Orders and then interface the
 changes to the appropriate modules via PM Interface
 You must have been given
 permission to access the error correction feature in VA User Profile. For more
 information, see [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm).
 When you are making corrections to a subcontract change
 order item, the interface batch month of the correction must be the same as the
 interface batch month of the original transaction. For example, if you interfaced a
 subcontract change order item using a batch month of 6/19, the batch month of the
 correction must also be 6/19. If the original batch month is closed, you must open the
 month before you can post the change.Other things you should
 know:

- You can make changes to an existing transaction, but
 you cannot delete a transaction. For example you can change the number
 of units on a units-based sucontract change order item, but you cannot
 delete the subcontract change order item.

- You can only correct subcontract change order items
 that you created in the PM module. Subcontract change order items that
 you created in the SL module must be corrected in SL.

- Other users cannot change items that are being
 corrected. For example if you are making a correction to a subcontract
 change order item in the PM Subcontract Change Order form, an error
 message will display if another user tries to change the same
 subcontract change order item in the PM Subcontract Change Orders
 form.

To correct and reinterface
 a subcontract change order item:

1. From the main menu, go
 to Project Management > Programs > PM Subcontract Change
 Orders.

1. In the Items grid,
 select the subcontract change order item to change. The subcontract change order item must be
 interfaced (that is, have an Interface Date). You cannot edit an item before it
 has been interfaced.

1. From the toolbar, select
 Tasks > Correct Item.  The Description , Amount
 , and Notes fields are now enabled.
 If the subcontract change order item is unit-based, the Description
 , Units, and Notes field are enabled (you cannot change the unit cost of an
 interfaced SubCO item).

1. Enter the correction(s)
 as needed.

1. Save the record.

1. To interface the change,
 select Tasks > Open
 PM Interface from the toolbar. The PM Interface form
 displays.

1. From the Item
 Type drop-down, select 6-Subcontract Change
 Orders.Your changed subcontract displays in the
 grid with the Interface checkbox selected. The entire amount of the
 corrected transaction (including the change amount) displays in the Amount field, and Correction displays in the Trans Type field
 displays as Correction will display in
 the Transaction Type column.

1. Click Validate to validate the batch.

1. Review/Print audit reports.

1. Click Interface.

On the PM Subcontract Change
 Orders form, all of the fields on the corrected subcontract change order item are
 disabled again.
