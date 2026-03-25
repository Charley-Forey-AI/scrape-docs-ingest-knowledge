---
title: "About Assigning Reviewers to Requisitions | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-assigning-reviewers-to-requisitions"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/requisitions/about-assigning-reviewers-to-requisitions"
---

# About Assigning Reviewers to Requisitions

You can assign reviewers to requisitions to establish an approval process.
This provides an option for you to control the flow of requisitions from creation to submission for quotes and/or purchase.
To enable the review process, you must assign a single reviewer or multiple reviewers to approve and reject requisitions. You can assign reviewers manually or you can have the system automatically assign reviewers.
Note: If you assign reviewers to a line, you can remove the reviewer to bypass the approval process. However, you can enforce the approval process by having the system require a reviewer to approve all requisition/quote lines. This is done by setting options in the PO Company Parameters form. For more information, see [Setting Requisition Approval Options](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/about-setting-requisition-audit-options).

## Manual Assignment

You can manually assign reviewers to a requisition by adding them to the requisition line using the Reviewers tab in PO Requisition Entry as you create the requisition. Reviewers must be 'active' and can be assigned regardless of whether you have set the company flags to require approval before adding requisition lines to a quote and/or purchase order.
If you have assigned a default reviewer in PO Company Parameters (Requisition Info), that reviewer is assigned automatically to each line added to a requisition, in addition to any default reviewers assigned at the job, IN location, and/or EM department levels (depending on the line type).
You can add, change, or delete reviewers on the Reviewers tab as desired. Keep in mind that if you have set the company flags to require approval of requisitions, you must assign at least one reviewer to each line. Otherwise, the requisition line will not go through the approval process and therefore, cannot be added to a quote or purchase order. If the company flags are set to not require approval, assignment of reviewers is strictly optional; however, if you do assign a reviewer, the line must be approved before it can be added to a quote or purchase order.
When you add reviewers to a requisition line, the Status is set to New and the Assigned Date defaults to the current date. Once the line is approved or rejected (in PO Requisition Reviewer), the Status and Review Date are updated accordingly. If the line was rejected, the rejection reason entered by the reviewer will display in the Description column.

## Automatic Assignment

To have the system automatically assign reviewers, you must set up default reviewers in one or more of the following forms.

- JC Jobs – Use the Reviewers tab to set up default purchase reviewers for Job-related requisition lines. The system assigns these reviewers in addition to any default reviewers specified in PO Company Parameters.

- EM Departments – Use the Purchase Reviewer field to set up default reviewers by department. The system assigns these reviewers to Equipment and Work Order requisition lines, in addition to any default reviewers specified in PO Company Parameters.

- IN Locations – Use the Purchase Reviewer field to set up default reviewers by inventory location. The system assigns these reviewers to inventory requisition lines, in addition to any default reviewers specified in PO Company Parameters.

You can also assign a default reviewer to requisition lines during initialization with either of the following forms:

- PO Requisition Initialization – When initializing requisitions with this form, you can specify a default reviewer to Inventory and/or Work Order requisition lines.

- PO Quote Initialization – When initializing requisition lines to quote lines, you can specify a default reviewer.

As long as you have assigned a reviewer, the system requires that the requisition or quote line must be approved by a reviewer (using PO Requisition Reviewer) before proceeding to the next stage in the process. However, you can remove default reviewers from the requisition or quote line to allow proceeding to the next level, if necessary.
