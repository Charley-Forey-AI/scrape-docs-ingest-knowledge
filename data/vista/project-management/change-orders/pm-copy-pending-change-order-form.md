---
title: "PM Copy Pending Change Order Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/pm-copy-pending-change-order-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/pm-copy-pending-change-order-form"
---

# PM Copy Pending Change Order Form

Use this form to copy a pending change order(PCO). This allows you to:

- Create revisions of existing PCOs - for example, you can copy PCO #1,
 including all of the items on the PCO, and save the copy as PCO #1.1.

- Copy a PCO and save it to a different project or PCO type

- Copy a PCO and then modify the copy to reduce data entry - for example if
 you have to create several similar PCOs, you can create one and then copy it several
 times.

Note: The default status of a copied PCO is set in the Default Beginning
 Status field of the [PM Company Parameters](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) form.
This form will copy all information on the selected
 PCO, including PCO detail items entered using the Estimates/Details tab in the lower
 portion of PM Pending Change Orders.
When copying PCOs associated with subcontracts/POs/SCOs/POCOs
The following applies when copying a PCO item that is associated with subcontracts, POs, SubCOs, or POCOs.
If the pending change order item is not approved:

- Subcontract/PO - The subcontract or PO detail will be copied to the new PCO
 and assigned a new sequence number. The subcontract/PO detail on the original PCO
 will not be affected.

- Subcontract Change Order(SubCO)/PO Change Order(POCO) - The SubCO/POCO
 detail will be taken off the original PCO and added to the new PCO.

If the pending change order item is approved:

- Subcontract/PO - The subcontract or PO detail will be copied to the new PCO
 and assigned a new sequence number. The subcontract/PO detail on the original PCO
 will not be affected.

- Subcontract Change Order(SubCO)/PO Change Order(POCO) - The subcontract or
 PO detail will be copied to the new PCO and assigned a new sequence number, but the
 SubCO/POCO associated with that detail will not be copied. The approved
 subcontract/PO detail on the original PCO will not be affected.

Follow the steps below to copy a pending change order(PCO).

1. Open the PCO that you would
 like to copy in PM Pending Change Orders.

1. Select Tasks > Copy
 PCO. This will open PM Copy Pending Change Order.

1. Use the Project
 field to select where the new PCO should be saved. This field will default to the
 project associated with the copied PCO, but you can change it if you would like to
 save the copy to a different project. Press F4 to select a project from a
 list.

1. Use the PCO Type
 field to select the type of PCO that is created. Press F4 to
 select it from a list. By default this field will populate with the type on the PCO
 being copied.

1. Use the PCO field
 to enter the PCO number that is created. By default this field will populate with the
 next available PCO number based on the selected project and PCO type.

1.  Use the Description field to enter the description of the PCO that will be
 created.This field will default with the
 description of the copied PCO, but you can change the value in this field if it
 does not apply. The description can be up to 60 characters long.

1. Click the Copy
 button to create the copy.

1. A message will appear. Click
 YES to open the new PCO in the PM Pending Change Orders form.

1. Review the copied PCO and
 make any needed changes.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview) Change Orders -
 Overview
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders Step-By-Step
