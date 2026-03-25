---
title: "Subcontract Change Orders - Overview | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview"
---

# Subcontract Change Orders - Overview

Subcontract change orders (SCOs/SubCOs) are used to record changes to existing subcontracts.
Generally, you will use a subcontract change order when the scope of a subcontract has changed. For example additions or subtractions to existing items, or the creation of new scope items. The subcontract that is being changed has to be approved, but it does not have to be interfaced with the accounting modules.
Note: Subcontracts are approved using the Approve  box on the Info tab of the PM Subcontracts form, and they are interfaced with the accounting modules using the PM Interface form.
You can create a subcontract change order using SL Change Order Entry, but the information will not be available in the PM module. By entering the subcontract change order in the PM module and then interfacing it with the SL module, the information is available in both the PM and SL modules.
The basic workflow is outlined in the diagram below. These steps are almost identical to the PO change order process.
Step 1 - Create the SCO
You can create subcontract change orders(SCOs) in several different ways.

- Manually create a SubCO- You can manually create a SCO using [PM Subcontract Change Orders Form](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form). Once the SCO is created, you can process it and then interface it with the accounting modules, or you can associate it with a pending change order(PCO) detail item using the SubCO and SubCO Seq fields on the Estimate/Purchase Details tab of [PM Pending Change Orders Form](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)

- From a PCO - When creating a pending change order using PM Pending Change Orders , you can associate a PCO detail item with an existing and approved subcontract using the SL and PO/SL Item fields on the Estimate/Purchase Details tab. Once a PCO detail item is associated with a subcontract, you can create a SCO in two ways:

- Automatically on Approval - When the pending change order is approved, the PCO detail will be used to automatically create an SCO. Pending change orders are approved using [About the PM Approve PCOs Form](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form).

- Manually before Approval - You can also manually create an SCO using the detail already entered on a PCO item - for example if you need to create a SubCO document before the pending change order is approved. Select Create >  Subcontract Change Order in PM Pending Change Orders . This will open [About the PM PCO Items Create SubCOs Form](/en/vista/vista/project-management/change-orders/about-the-pm-pco-items-create-subcos-form).

- Using PM Subcontract Detail - You can manually create a new SCO using the Sub CO field on [PM Subcontract Detail Form](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form). This only applies when the subcontract detail is associated with a pending or approved change order. To create a new subcontract change order, select Pending COs or Approved COs in the Record Type drop down and then enter a unique value in the Sub CO field. Click [here](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form/field-definitions-pm-subcontract-detail-form#ID-0002d8c7--en) for more information.

- Using PM Subcontracts - You can manually create a new SCO using the SubCO field on the Non-Interfaced tab of PM Subcontract.

When creating a subcontract change order(SCO), the subcontract being changed has to be approved but it does not have to be interfaced with the accounting modules.
The line items on the subcontract change order(SCO) can:

- Change an existing subcontract line item

- Create a new item on the selected subcontract

Step 2 - Create and Send the SubCO Document
Use the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature to generate a subcontract change order document and email/fax it to a list of contacts. This is an optional step.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for general information about the Create and Send feature in the PM module.
Step 3 - Approve the SCO
Before an SCO can be interfaced with accounting, it has to be approved. Click the Approvebutton on [PM Subcontract Change Orders Form](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form) to approve an SCO and all items on the SCO.
If you would like to approve only specific items on an SubCO:

- Check the Interface box on each SubCO item that should be interfaced (Grid or Info tab in the lower portion of PM Subcontract Change Orders)

- Check the Ready for Accounting box on the Info tab in the upper portion of PM Subcontract Change Orders

Once a subcontract has been approved, you can enter changes on it using a subcontract change order. Click here for general information on subcontract change orders.
Step 4 - Interface the SCO
Interface the SCO with the accounting modules using [PM Interface Form](/en/vista/vista/project-management/setupmaintenance/pm-interface-form). You can launch this form from [PM Subcontract Change Orders Form](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form) by selecting Tasks > Open PM Interface.

Related information

- [About Subcontract Buyout](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)
