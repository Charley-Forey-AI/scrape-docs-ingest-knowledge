---
title: "Create a Requisition Using the Purchase Route | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions/create-a-requisition-using-the-purchase-route"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions/create-a-requisition-using-the-purchase-route"
---

# Create a Requisition Using the Purchase Route

If you do not require a quoting process, you can simply create requisitions and route them directly to purchase orders.
 If you do not require approval for purchase, you can streamline the process even further by setting approval requirements for each situation.The following instructions describe how to create requisitions using purchase routing.

1. Create a requisition using one of the following options:

- Initialize the requisition from either the Equipment Management (EM) or Inventory (IN) modules using PO Requisition Initialization, if applicable. Make sure to select '1-Purchase' from the Route drop-down.Note: When initializing from EM, the system creates requisitions based on open work orders. When initializing from IN, the system creates requisitions from low stock based on preset reorder quantities.

- Initialize the requisition from the Project Management (PM) module using PM Material Detail, if applicable. For more information, see [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form).Note: When initializing from PM, the system creates requisitions based on materials that you entered for jobs in PM Material Detail.

- Create the requisition in PO Requisition Entry and specify Quote as the route type. For more information, see [PO Requisition Entry](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form).

Initialized requisitions appear in the PO Requisition Entry form and can be edited as needed. For more information about initializing requisitions, see [About Initializing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-initializing-requisitions).

1. If you require approval for requisitions, reviewers must approve the requisitions using PO Requisition Reviewer prior to initialization. For more information on setting up the approval process for requisitions, see [Assigning Reviewers to Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-assigning-reviewers-to-requisitions).

1. Initialize the requisition to a purchase order using PO Initialization. For more information, see [Creating the PO Batch](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-batch-creation). Note: You can edit requisition lines using PO Requisition Entry as long as you have not added them to a purchase order. The system disables lines associated with a purchase order to prevent any further changes. However, if you should need to change the information on a requisition line, you can remove the line from its associated purchase order (only for non-posted purchase order batches). This enables the requisition line (in PO Requisition Entry) and allows you to make any necessary changes.

You can now process the purchase order.
