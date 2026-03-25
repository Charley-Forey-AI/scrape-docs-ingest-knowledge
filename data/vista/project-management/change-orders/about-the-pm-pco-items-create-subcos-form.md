---
title: "About the PM PCO Items Create SubCOs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form"
---

# About the PM PCO Items Create SubCOs Form

Use this form to create subcontract change orders (SCOs) using PCO detail items. It can be accessed by selecting Create > Subcontract Change Orders on the PM Pending Change Orders form.
The following must be true to create SubCOs from PCO detail items:

- There must be a subcontract and subcontract line item associated
 with a PCO detail item - PCO detail items are entered using the Estimate/Purchase
 Details tab on PM Pending Change Orders, and they are associated with a subcontract
 and subcontract item using the SL and PO/SL
 Items fields

- The subcontract item cannot already be associated with an SubCO-
 each subcontract item can only be associated with one SubCO

- The subcontract associated with the PCO detail item must be
 approved, or interfaced- subcontracts are approved using the Approvedcheckbox on the Info tab of [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form) and they are interfaced using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)

Key Features
This form has the following key features:

- You can create one or many SubCOs - A separate SubCO will be created for each PCO detail item associated with a unique subcontract. This is because an SubCO can only be associated with a single subcontract. PCO detail items associated with the same subcontract will be grouped together onto a single SCO.

- You can add items to an existing SubCO - If all of the PCO detail items are associated with the same subcontract, you can add these items to an existing SubCO on that subcontract.

- Created SCOs will be linked to the
 PCO - When you create SCOs using this form, the created subcontract change orders will be linked to the PCO using the [Related Items](/en/vista/vista/project-management/about-related-items) feature.

- The subcontracts do not have to be
 interfaced - You can create SCOs for subcontracts that are approved, or interfaced with the accounting modules using PM Interface.

Create SubCOs using PCO Detail Items
Follow the steps below to create SubCOs using PCO item detail.

1. In [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form), select a pending change order that contains PCO detail items that meet all of the conditions outlined at the top of this document.

1. Select Create >  Subcontract Change Orders in PM Pending Change Orders. This will open PM PCO Items Create SubCOs.

1. All of the PCO detail items that meet the conditions outlined at the top of this document will display in the grid.

1. Use the Keyword field to locate the PCO detail items that should be added to subcontract change orders. Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form/field-definitions-pm-pco-items-create-subcos-form#ID-00029faf--en) for more information on this field.

1. Check the box next to each PCO detail item that should be added to a subcontract change order. Note: You can also use the Select All and Deselect All buttons to check or uncheck all of the boxes that display in the grid. These buttons only affect the items that display in the grid.

1. If you are adding the
 selected PCO detail items to an existing subcontract change order, press F4 in the
 Add to
 SubCOfield to select it from a list. This field will be disabled if
 you selected PCO detail items that are associated with more than one subcontract. You
 can see the subcontract associated with each PCO detail item using the SL
 column.Note: You can run this process multiple times if you have several PCO detail items that should be grouped onto a single SubCO, and you also have PCO detail items that should be added to new SubCOs.

1. Click the Create SubCOs button when complete.

1. A message will appear. Click Yes if you would like to open the created SubCO using [PM Subcontract Change Orders](/en/vista/vista/project-management/change-orders/pm-subcontract-change-orders-form).

1. For each PCO item added to
 an SubCO, the subcontract change order number and sequence will populate in the
 SubCO and SubCO Seq fields on the
 Estimates/Purchasing Details tab in the lower portion of [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form).

Related Items
The subcontract change order(SubCO) and the pending change order(PCO) will automatically be related using Related Items feature. Click [here](/en/vista/vista/project-management/about-related-items) for general information on the Related Items feature.

[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PCO - What do you want to do? A series of slides that guide you through most of the major tasks.
