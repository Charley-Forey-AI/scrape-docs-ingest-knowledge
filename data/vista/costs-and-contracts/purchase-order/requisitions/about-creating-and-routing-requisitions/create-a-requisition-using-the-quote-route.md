---
title: "Create a Requisition Using the Quote Route | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions/create-a-requisition-using-the-quote-route"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-creating-and-routing-requisitions/create-a-requisition-using-the-quote-route"
---

# Create a Requisition Using the Quote Route

You can create a requisition and route it through a quote, as well as include an approval process, if applicable.
When purchasing materials or part for jobs, equipment, inventory, or other needs, you may prefer to solicit price quotes from one or more vendors before making a purchase. Using the PO module, you can incorporate this process by initializing quotes from existing requisition lines, print the quotes to send to vendors for pricing, get quote approval, and initialize quotes to purchase orders.To create a requisition using quote routing:

1. Create a requisition using one of the following options:

- Initialize the requisition from either the Equipment Management (EM) or Inventory (IN) modules using PO Requisition Initialization, if applicable. Make sure to select '0-Quote' from the Route drop-down.Note: When initializing from EM, the system creates requisitions based on open work orders. When initializing from IN, the system creates requisitions from low stock based on preset reorder quantities.

- Initialize the requisition from the Project Management (PM) module using PM Material Detail, if applicable. For more information, see [PM Material Detail](/en/vista/vista/project-management/materials/pm-material-detail-form).Note: When initializing from PM, the system creates requisitions based on materials that you entered for jobs in PM Material Detail.

- Create the requisition in PO Requisition Entry and specify Quote as the route type. For more information, see [PO Requisition Entry](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form).

Initialized requisitions appear in the PO Requisition Entry form and can be edited as needed. For more information about initializing requisitions, see [About Initializing Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-initializing-requisitions).

1. If you require approval for requisitions, reviewers must approve the requisitions using PO Requisition Reviewer prior to initialization. For more information on setting up the approval process for requisitions, see [Assigning Reviewers to Requisitions](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-assigning-reviewers-to-requisitions).

1. Initialize the quote using PO Quote Initialization. For more information, see [PO Quote Initialization](/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-initialization-form). Note: You cannot enter quotes manually; they must be set up via initialization. This allows for vendor pricing based on volume purchasing.

1. Assign the appropriate vendor(s) to the quotes using PO Quote Edit. For more information, see [PO Quote Edit](/en/vista/vista/costs-and-contracts/purchase-order/quotes/po-quotes-forms/po-quote-edit-form).

1. Print the PO Requisition Quote Form report and send it to the appropriate vendor(s).

1. Once you determine the quote and vendor to use, enter the associated information into PO Quote Edit.

1. If you require approval for the quote, reviewers must approve the quote using PO Requisition Reviewer prior to initializing a purchase order. For more information see [PO Requisition Reviewer](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-reviewer-form).

1. Initialize the requisition to a purchase order using PO Initialization. For more information, see [Creating the PO Batch](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-batch-creation). Note: You can edit requisition lines as necessary (in PO Requisition Entry) as long as you have not added them to a quote. The system disables lines associated with a quote to prevent any further changes. However, if you should need to change the information on a requisition line, you can remove the line from its associated quote (only for non-posted purchase order batches). This enables the requisition line (in PO Requisition Entry) and allows you to make any necessary changes.

 You can now process the purchase order.
