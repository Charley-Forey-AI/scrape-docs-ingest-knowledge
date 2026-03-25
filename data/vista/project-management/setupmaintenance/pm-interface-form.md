---
title: "PM Interface Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-interface-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-interface-form"
---

# PM Interface Form

Use the PM Interface form to interface project information entered in the PM module to the Job Cost, Subcontract Ledger, Purchase Orders, Inventory, and Material Sales modules.
You can use this form multiple times on the same project without the risk of duplicating data previously interfaced.
Things you can do with this form:

- Interface new projects or project items, such as subcontract and purchase orders. For more information, see [Interface a New Project or Project Items](/en/vista/vista/project-management/setupmaintenance/interface-a-new-project-or-project-items#task-2886--en__task-2886).

- Interface corrections to transactions that have already been interfaced. If a transaction is a correction, Correction will display in the Transaction Type column. For more information about error corrections, see [Enable/Disable the Error Correction Feature in PM](/en/vista/vista/project-management/setupmaintenance/enabledisable-the-error-correction-feature-in-pm).

## Subcontract Change Orders

If the Subcontract Change Order (Sub CO) you are trying to interface does not appear in the list, verify the following:

- The Sub CO has been approved. You must select the Ready For Accounting checkbox in the upper portion of PM Subcontract Change Orders to indicate the change order is approved. Only approved SubCOs display in PM Interface.

- The Sub CO items are set up to be interfaced. You must select the Interface checkbox in the lower portion of PM Subcontract Change Orders. Only SCO items with this checkbox selected are included in the interface. For example, if there is only one item on the SCO and the Interface checkbox is not selected, the SubCO will not display in PM Interface.

You can also select the Approve button on the PM Subcontract Change Orders form. This will approve the SCO and all items on the SCO items. In addition, it will select the Ready For Accounting checkbox on the subcontract, and the Interface checkboxes on all of the SCO items.

## Interfacing Approved Change Orders

An approved change order (ACO) will display in the selection grid as long as there is information on the ACO that has not been interfaced (for example, there are estimates entered on the Estimate Detail tab of PM Approved Change Orders that have not been interfaced).
When you interface an ACO, only the detail items that have the Interface checkbox selected on the Estimate Detail tab of PM Approved Change Orders are interfaced. This means the ACO will continue to display in the selection grid after it has been interfaced if there is remaining estimate detail that has not been interfaced. If everything on an ACO should be interfaced, make sure you select the Interface checkbox for all items.

## Changes to Interfaced Data

Once you interface a project, subsequent modifications to the estimates on the project must be made through an approved change order or entered directly in the Job Cost module. Phase/cost type detail added to a project will interface; however, changes made to previously interfaced phases will not interface. The only way interfaced data can be changed in Project Management and updated to the appropriate accounting modules, is by approved change order. SL and PO/MO information can be interfaced each time new subcontract and PO/MO numbers are assigned.

## Unposted PM Interface Batches

This grid only displays if you have unposted PM Interface Batches. When it does display, the grid provides a list of all unposted PM interface batches for the active company; however, it will include only those batches with one of the following statuses:

- 0- Open

- 2-Validation Errors

- 3-Validation OK

- 4-Posting in Progress

- 25-Validation Warnings

You can use this grid to unlock or post a listed batch. Right-click on a batch in the grid to access the Unlock Batch or Post Batch options.

You can only unlock a batch if the InUseBy field contains your login information. This option is only enabled when the InUseBy field has data.

You can post any batch that isn't locked. When you select Post Batch, the system displays the Batch Process form for that batch's source. For example, if the Process field says "PO Entry", the system displays the PO Batch Process form, where you can validate and post the batch.
