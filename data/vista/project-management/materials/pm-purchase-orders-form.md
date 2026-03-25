---
title: "PM Purchase Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/pm-purchase-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/pm-purchase-orders-form"
---

# PM Purchase Orders Form

 Use this form to edit/modify summary and item detail for purchase orders created in PM Material Detail.
You can access this form either from the PM module Programs folder or by selecting File > PM Purchase Orders in PM Material Detail.
Purchase order information (header and item) is added automatically to this form when purchase order numbers are assigned (manually or by initialization) to material detail in PM Material Detail (recommended method). However, you can add purchase orders manually in this form as necessary.
The PO Status (display only) identifies the status of the purchase order (0-Open, 1-Complete, 2-Closed, or 3-Pending). All purchase orders created in this form or via PM Material Detail are automatically assigned a status of 3-Pending and will retain this status until you interface the purchase order to PO. Once interfaced, the status is updated to 0-Open and no further changes can be made to the interfaced data here. However, you can add new items to an interfaced purchase order.
Tip: You can restrict the recordset to exclude purchase orders that have been fully interfaced by selecting Options > Show Only PO’s with Non-interfaced Detail. This will display only those POs that have not been interfaced or that have been partially interfaced.

## Shipping / Address Overrides

Use the Shipping tab to enter shipping information specific to each purchase order. If the materials on the purchase order are to be shipped to the Job address specified in JC Jobs, select the Ship to Job checkbox.
If shipping the materials to a predefined location, use the Shipping Location to identify the address (Ship to Job option must be unselected). When you enter a valid shipping location, the shipping address defaults from the PO Shipping Locations file.
The Address Overrides tab allows you to override the vendor's standard purchasing and/or payment addresses. However, purchase orders must be in a status of Pending to use this tab.
 If overriding the purchase address, use an address sequence with an address type of Pending or Both. The selected address prints on the purchase order. If overriding the payment address, use an address sequence with an address type of Payment or Both. The selected address is updated to the invoice header (in AP Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry) when entering lines for the selected PO.
Note: Payment address overrides specified here are only used if there is no override address or address sequence designated in the AP invoice header and if it is the first PO line on the invoice.

## Non-Interfaced / Interfaced Items

Use the Non-Interfaced Items tab to enter or modify items on a purchase order that have not yet been interfaced.
Note: If the purchase order requires approval and any user (approver or not) adds a new item to the Non-Interfaced Items tab at any time during the review/approval workflow (submitted, partially approved, fully approved, or interfaced), the system displays a message indicating that adding an item will reset the Workflow. If you select OK, the new item is added, the workflow is set back to Approval Required, and the PO Status is set to 3 - Pending. If you select Cancel, you will be unable to save the new item.

Material detail records entered in PM Material Detail (with a material type of P-Purchase Order) that are assigned a purchase order/item number are automatically set up as items on this tab. You can also enter new purchase order items; items entered directly in the grid will update the PM Material Detail file.
Note: Material detail records entered (in PM Material Detail) for approved or pending change orders will include their associated change order information; however, the change order fields are display only. PO items entered manually in this grid cannot be associated with a pending or approved change order; you can only do that via the PM Material Detail form.

When you are ready to interface a purchase order item, select the Send checkbox. The system includes items flagged as 'Send' when you interface the PO via PM Interface. Once an item is interfaced, it is moved to the Interfaced Items tab and can only be edited in PO Purchase Order Entry.

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are only visible when you select the Non-Interfaced Items tab, and show estimate information for the selected PO item. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Material Detail and based on certain factors, the subtraction of some PO Item and PO Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a project, and facilitate owner billing. When you add items to a PM purchase order, you can assign the items to a field ticket associated with the contract for the specified project. You can assign multiple purchase order items to a single field ticket, as long as the ticket is open (that is, it has a status of Open). Once the status for a field ticket is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to purchase order items for a job is only useful if the project's contract/contract item has a bill type of T&M or Both. For more information about field tickets, see JC Field Ticket.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## PO Compliance

If you are tracking compliance on purchase orders in the PO module, you can assign a compliance group to POs so that compliance codes are added to them when they are interfaced. If you defined a default PO compliance group for the project (in PM Projects), that compliance group automatically defaults for each purchase order entered in this program for the project, but may be overridden if needed.
Note: If you delete the compliance group after you save the PO, its assigned compliance codes are not automatically deleted from the PO. You must do that manually in PO Compliance (File > PO Compliance as applicable. The same is true if you change the compliance group; the new codes are added, but you must manually delete the old codes.

For more in-depth information about compliance codes and compliance tracking, see [PO Compliance Form](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-compliance-form).

## Review/Approval Workflow

If you have the Workflow module and are using the Process Workflow feature, the system determines when a purchase order (PO) requires approval based on the PO/Item amounts and the spending limits associated with the user who entered the PO. If a user is not set up with a spending limit, the PO automatically requires approval.
If a PO requires approval, the Workflow Status changes to Approval Required and you must then submit the PO for approval using the Submit for Approval button. All reviewers assigned to the PO are notified (via email or VP message) that a PO is awaiting their review/approval. For more information about this process, see [About the Purchase Order Review/Approval Workflow](/en/vista/vista/project-management/materials/about-the-purchase-order-reviewapproval-workflow).

Related information

- [Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)

- [Create a Workflow for Purchase Orders Using the PM Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
