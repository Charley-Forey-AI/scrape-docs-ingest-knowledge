---
title: "Change Order Status File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-order-status-file-maintenance/change-order-status-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/change-order-status-file-maintenance/change-order-status-file-maintenance---field-descriptions"
---

# Change Order Status File Maintenance - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Status code
Add the code for the change order status.

Description
Add a description for the change order status code. This description displays on the Change Order Status File Listing.

Action
Select an action for the change order status code you are assigning from the following options:

1. Recognize revenue and cost revisions, billing allowed Select this option when a change order has costs that will be billed to the customer.

1. Recognize revenue and cost revisions, billing not allowed  Select this option when a change order has costs that cannot be immediately billed to the customer.
Note: Changing the status action or deleting a status code that is already assigned to a change is not permitted.

Rename
Click this button to rename an existing change order status code. Non-cost reimbursable change orders are not affected by renamed codes. For example, if you want the letter B to represent approved change orders instead of the letter A. Enter A in the Old code field and then enter B in the New code field.
You can also change your status codes from letters to numbers. For example, if you currently use A for approved change orders and you want to use the number 7, enter A in the Oldcode field and then enter 7 in the Newcode field.
You can have multiple codes represent the same status. For example, you can use the letters S and O for approved change orders if you want to differentiate between change orders that were approved by a subcontractor compared to the owner.

1. Enter the original change order status code.

1. Enter the new change order status code that will replace the old change order status code.

1. To proceed with the renaming update, click Continue.
If you update the code, the new code you entered will be substituted for the old code throughout the Change Order Log file. Additionally, a new status code record will be created in the Status Code Maintenance file.
This button will be shaded if the Operator does not have security authorization for this feature.
