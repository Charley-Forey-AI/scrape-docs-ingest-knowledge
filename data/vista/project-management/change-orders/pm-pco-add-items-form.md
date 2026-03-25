---
title: "PM PCO Add Items Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/pm-pco-add-items-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/pm-pco-add-items-form"
---

# PM PCO Add Items Form

Use the PM PCO Add Items Form to quickly create new PCO items or add information to an existing PCO item.
For example, you can use this form to add multiple phases, subcontracts, and purchase orders to a pending change order (PCO).
Access this form by selecting the Add PCO Items button on the [PM Pending Change Orders](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) form.
Follow the steps below to either create new PCO items or add information to an existing item.

1. Open PM PCO Add Items.

1. In the PCO Item field, do one of the following:OptionDescription
To update an existing PCO ItemEnter the PCO item to update or press F4 to select from a list of PCO items.By default, this field populates with the PCO item selected in PM Pending Change Orders when this form was launched.

To create a new PCO ItemLeave this field blank or enter a new PCO Item number.

1. Use the View By section to select the information that you would like to add to the PCO item. The selection in this field determines the columns and items that display in the grid.

- Vendor (SL) - Select to add a subcontract to the PCO item. Only subcontracts that have been interfaced will display.Note: This option is only enabled if you selected the SL checkbox (in the Change Impact section) in PM Pending Change Order before you selected the Add PCO Items button.

- Vendor (PO) - Select to add a purchase order to a PCO item. Only purchase orders that have been interfaced will display.Note: This option is only enabled if you selected the PO checkbox (in the Change Impact section) in PM Pending Change Order before you selected the Add PCO Items button.

- Phase - Select to add phases to the PCO item. The grid will populate with the phases associated with the project, but only phases that are associated with a cost type will display.Note: Phases are associated with a project and contract item using the Phases tab on PM Project Phases.

1. Use the Keyword field to filter the information that displays in the grid.Enter a keyword and the system will search all of the columns that display in the grid. For example, enter a vendor name, phase description, or cost type to filter the vendors or phases that display in the grid.Note: You can use this field multiple times without closing the form. For example, enter a keyword to filter the grid, make your selections, enter a new keyword, and then make additional selections. All selections are applied to the PCO item, even if they do not currently display in the grid.

1. Select the items that you would like to add to the PCO item.

- Manual selection - Select the checkbox for individual items to add to the PCO.

- Select All/Deselect All - Use the Select All or Deselect All buttons to make selections; however, these buttons only affect the items that display in the grid. For example, selecting Deselect All  will not deselect any items that have been selected but do not display in the grid.

Note: Only subcontracts and purchase orders that have been approved and interfaced will display in the grid. If the subcontract or purchase order that you want to select does not display, verify that it has been approved and interfaced (using the PM Interface form).

1. If you want to create a new item on the selected subcontract or purchase order, select the Create New PO/SL Item(s) checkbox. When you select this checkbox, the system creates a new item on the selected subcontract or purchase order using the next available item number. It then populates the PO/SL Item column on the Estimate/Purchase Details tab (in PM Pending Change Orders) with the new item number.
Note: If a subcontract or purchase order has multiple items, each of those items will display in the grid. When creating a new subcontract or PO item, it doesn't matter which item you select. If you select several items on the same subcontract or PO, the system will create several new items on that subcontract/PO.


1. If you want the contract items associated with the selected items to populate on the pending change order, select the Prefill Contract Item checkbox. For example, if you choose a purchase order item and select Prefill Contract Item, the system uses the phase on the selected PO item to find the associated contract item, and then populates the Contract Item field on the Info tab in the lower portion of the PM Pending Change Orders form.

1. Select Add Items.All selected items are added to the specified PCO item.Note: If you accidentally selected duplicate information, a message appears informing you that the duplicate items were skipped. Close the message window and select Close (in PCO Add Items) to return to the PM Pending Change Orders form.
