---
title: "Work Center Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/system-tools/work-center-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/system-tools/work-center-features"
---

# Work Center Features

Vista 2024 R1
 delivers on user-requested Work Center enhancements, fixes, and other
 improvements.

## Improved PO/SL Review/Approval Workflow

Several improvements were made to the PO/SL Review/Approval
 Workflow:
PO/SL Approval from the Work Center Automatically Translates Approval Status to PO
 and Subcontract Forms
When you approve a purchase order in the PM Work Center, the
 system now automatically selects the Approved checkbox for the purchase order in PM Purchase Orders or
 PO Pending Purchase Orders, depending on where you created the purchase order.
For more details about the approval process for POs, see the following:

- [Create a Workflow for Purchase Orders Using the PM Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-pm-module)

- [Create a Workflow for Purchase Orders Using the PO Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/create-a-workflow-for-purchase-orders-using-the-po-module)

Similarly, when you approve a subcontract in the PM Work Center,
 the system now automatically selects the Approved checkbox for the
 subcontract in PM Subcontracts or PM Subcontract Detail, depending on where you
 created the subcontract.
For more details about the approval process for subcontracts, see
 the following:

- [Initiate the Review/Approval Workflow for Subcontracts](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/initiate-the-reviewapproval-workflow-for-subcontracts)

- [Review Subcontracts Submitted for Approval](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/review-subcontracts-submitted-for-approval)

In PM Work Center queries where you can approve a purchase order or
 subcontract (this includes All Documents in Workflow, My Documents in Workflow, My
 Documents to Review, Purchase Orders, and Subcontracts queries), if you fully
 approve the record using the Approve Document icon (), the system automatically selects the Approved checkbox for the
 purchase order / subcontract and sets the Workflow Status field to Approved. If there are multiple
 reviewers, the system sets the Workflow Status field to Partial Approval until all
 reviewers have approved.
For fully approved POs / subcontracts, the system also sets the
 approver Status to 2 -
 Approved in the PM PO Workflow Item Reviewers and PM SL Workflow
 Item Reviewers forms, respectively.
PM Work Center Approval Restricted to Valid Reviewers Only
When a reviewer uses the PM Work Center to review/approve a
 purchase order or subcontract, that user will only be allowed to approve those
 documents for which they are a valid reviewer. If the user is not a valid reviewer,
 a message displays indicating that the subcontract or purchase order could not be
 updated because the user is not eligible.
Add New Items to a PO or Subcontract
 and Reset the Approval Workflow
If any user (approver or not) adds a new item to the
 Non-Interfaced Items tab of either PM Purchase Orders or PM Subcontracts, the new
 item will reset the entire workflow to Approval Required. This reset can occur when the PO / subcontract
 has been submitted for approval, partially approved, fully approved, or interfaced.
 When the workflow is reset, the PO or SL Status is reset to 3 - Pending.
The Workflow History tab on PM Purchase Orders or PM Subcontracts
 reflects this workflow reset, recording the date, time, and user who reset the
 workflow.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
