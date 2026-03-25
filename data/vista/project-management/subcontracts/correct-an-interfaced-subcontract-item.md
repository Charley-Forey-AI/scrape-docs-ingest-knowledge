---
title: "Correct an Interfaced Subcontract Item | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/correct-an-interfaced-subcontract-item"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/correct-an-interfaced-subcontract-item"
---

# Correct an Interfaced Subcontract Item

You can make changes to a subcontract item that you have already interfaced using PM Subcontract Detail and then interface the changes to the appropriate modules via PM Interface.
You must have been given permission to access the error correction feature in VA User Profile. For more information, see [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm).
When you are making corrections to a subcontract item, the
 interface batch month of the correction must be the same as the interface batch
 month of the original transaction. For example, if you interfaced a subcontract item
 using a batch month of 6/19, the batch month of the correction must also be 6/19. If
 the original batch month is closed, you must open the month before you can post the
 change.
ther things you should know:

- You can make changes to an existing transaction, but
 you cannot delete a transaction. For example you can change the number
 of units on a units-based sucontract item, but you cannot delete the
 subcontract item.

- You can only correct subcontract items that you
 created in the PM module. Subcontract items that you created in the SL
 module must be corrected in SL.

- Other users cannot change items that are being
 corrected. For example if you are making a correction to a
 subcontract item in the PM Subcontract Detail form, an error
 message will display if another user tries to create an SL change order
 for that item in the PM Subcontract Change Orders form.

To correct and reinterface a subcontract
 item:

1. From the main menu, go to Project Management > Programs > PM Subcontract Detail.

1. Select the Interfaced
 tab.

1. Select a subcontract
 item by clicking in the column to the left of the Sequence field.

1. From the toolbar, select
 Tasks > Correct Item. The selected row is highlighted and most of the fields are
 enabled.

1. Enter the
 correction.

1. Save the record.Note: If you make changes to an item in error and have
 already saved the change, reselect the line and select Tasks > Correct Item. This turns off editing in the form and displays a message
 warning you that any changes to the interfaced item will be lost. Select OK
 to undo the change.

1. To interface the change,
 go to Project Management > Programs > PM Interface.  The change to the subcontract item will display in the form. The entire
 amount of the corrected transaction will display in the Amount field (not just the amount of the change), and
 Correctionwill display in the Transaction
 Type column.

1. Interface the
 change.

1. On the PM Subcontract
 Details form, all of the fields on the corrected subcontract item are disabled
 again.

The change is interfaced and all fields on the
 corrected item are disabled again in PM Subcontract Detail.
