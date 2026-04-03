---
title: "Change Request Status File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-request-status-file-maintenance/change-request-status-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-request-status-file-maintenance/change-request-status-file-maintenance---field-descriptions"
---

# Change Request Status File Maintenance - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field/Button
Description

Status code
Add the code for the change request status.

Description
Add the description for the change request status code. This description displays on the Change Request Status File Listing Report.

Action
Select an action for the change request status code you are assigning from the following options:

1. Recognize revenue and cost revisions, billing allowed Select this option when a change request has costs that will be billed to the customer.

1. Recognize revenue and cost revisions, billing not allowed Select this option when a change request has costs that cannot be immediately billed to the customer.

1. Recognize cost revisions, no billing Select this option when a change request may have cost implications, but you are not certain that they will be reimbursed for those changes. This status allows you to estimate the cost and enter a corresponding revenue amount, but only have the estimated cost update to Job Cost.

1. No recognition of revenue or cost, no billing Select this option when a change request does not have cost implications and there is no billing.

1. Reverse revenue and cost recognition Select this option when you want to reverse a change request's revenue and costs.
Note: Changing the status action or deleting a status code that is already assigned to a change is not permitted.

Rename
Click this button to rename an existing change request status code. Non-cost reimbursable change requests are not affected by renamed codes. For example, if you want the letter B to represent approved change requests instead of the letter A. Enter A in the Old code field and then enter B in the New code field.
You can also change your status codes from letters to numbers. For example, if you currently use A for approved change requests and you want to use the number 7, enter A in the Oldcode field and then enter 7 in the Newcode field.
You can have multiple codes represent the same status. For example, you can use the letters S and O for approved change requests if you want to differentiate between change requests that were approved by a subcontractor compared to the owner.

1. Enter the original change request status code.

1. Enter the new change request status code that will replace the old change request status code.

1. To proceed with the update, select Continue.
If you update the code, the new code you entered will be substituted for the old code throughout the Change Request Log file. Additionally, a new status code record will be created in the Status Code Maintenance file.
This button will be shaded if the Operator does not have security authorization for this feature.
