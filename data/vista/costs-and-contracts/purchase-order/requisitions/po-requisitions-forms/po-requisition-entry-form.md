---
title: "PO Requisition Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-entry-form"
---

# PO Requisition Entry Form

Use the PO Requisition Entry form to set up and/or modify requisitions.
You can manually add requisitions in this form or initialize them using the PO Requisition Initialization form or the PM Material Detail form. However, requisitions created using PO Requisition Initialization and PM Material Detail are limited to specific line types. PO Requisition Initialization generates either Inventory or Work Order requisition lines based on low stock or parts needed for work orders, respectively. PM Material Detail will generate only Job requisition lines based on materials set up for a project. For information about requisitions created using these forms, see Related Topics below.
Note: When you open this form, it defaults to the last requisition ID that you accessed.

- Manually Assigning Reviewers - You can manually assign "Active" reviewers (setup in the HQ Reviewers form) to any requisition line, regardless of whether you have set the company flags to require approval before adding requisition lines to a quote and/or purchase order. For details, see [Manually Assign Reviewers](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-assigning-reviewers-to-requisitions#ID-0002f1c6--en__POReq_ManualAssignReviewers).

- Automatically update the lines on a requisition - Use the Update All Items button to update all requisition lines that are not on a quote or purchase order with a selected vendor, ship location, required date, and/or route status. For more information, see [PO Requisition Item Apply Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-item-apply-form).

- Requisition # - Requisition numbers can be assigned manually or automatically. If you always use numeric requisition numbers, use the "auto-generate" feature (flag in PO Company Parameters) to have requisition numbers assigned automatically during requisition entry. When 'N', 'New', or '+' is entered for a new requisition, the system will generate a sequential number based on the Last Used RQ # specified in the company file. Once assigned, the requisition number is updated to the Last Used RQ #. If you use both alphanumeric and numeric requisition numbers, then manual entry will probably work best for you. Note: You can manually assign requisition numbers even if you are using the 'auto generate' feature. However, manually assigned numbers will not update the Last Used RQ# field. If the 'auto-generate' process encounters an existing number (e.g. one that was entered manually), it will pull up the existing requisition. You will need to enter 'N', 'New', or '+' to start a new requisition with the next available number.

- Requisition Item Status - The status of a requisition line indicates where the requisition is during its processing. Initially, each requisition line is assigned a status of 'Open'. Then as the requisition is approved, added to a quote or purchase order, and so forth, the system automatically updates the status accordingly. There are seven statuses that can be assigned to a requisition. For more information, see [Requisition Item Status](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/requisition-item-status#concept-3797--en__concept-3797).

- Shipping - This tab is used to enter or modify the shipping address for a requisition line. Each line will automatically default a shipping address based on the line type (e.g. if a job, defaults the job's shipping address from JC Jobs). If a Ship Location is specified, it will override the default address with the shipping address defined in PO Shipping Locations. You can also override the address manually.

- Quote Tab - This display-only tab provides Quote and PO information for each requisition line. Once the line is added to a quote, the associated quote number, quote line, and expected date are displayed. Then when the line is added to a purchase order, it shows the purchase order and item number.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you add a job line to a requisition, you can assign the entry to a field ticket associated with the contract for the specified job. You can assign multiple job lines to a single field ticket, as long as the ticket is still open (that is, has a status of Open in JC Field Ticket). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job lines on a requisition is only useful if the job's contract/contract item has a bill type of T&M or Both.Additionally, once you process the requisition, entries associated with approved field tickets appear on the Cost Detail tab in JC Field Ticket for the specified field ticket.

 For more information about field tickets, see [JC Field Ticket](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

[PO Requisition Initialization Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-initialization-form)
[PM Material Detail Form](/en/vista/vista/project-management/materials/pm-material-detail-form)
[PO Requisition Item Apply Form](/en/vista/vista/costs-and-contracts/purchase-order/requisitions/po-requisitions-forms/po-requisition-item-apply-form)
