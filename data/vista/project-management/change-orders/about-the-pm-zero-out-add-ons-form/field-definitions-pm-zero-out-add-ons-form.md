---
title: "Field Definitions: PM Zero Out Add-ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form/field-definitions-pm-zero-out-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form/field-definitions-pm-zero-out-add-ons-form"
---

# Field Definitions: PM Zero Out Add-ons Form

The following is a list of field descriptions for the PM Zero
 Out Add-ons form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CO

Enabled for ‘Change Order Item’ and ‘Change Order’ selection options only.
Specify the change order for which to zero out pending add-ons. Initially defaults the currently selected pending change order.
Update
Click this button to initiate the update process. The update will cycle through all specified pending change order items and set the add-on amounts and percentages to 0.00. Pending change order items that have been approved will be skipped.
If the update is successful, you will receive a message indicating the number of add-ons that were zeroed out. However, if no unapproved change order items are encountered during the update process, no update will occur. You will receive an appropriate message depending on the 'zero out' option you selected.

[](/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form)PM Zero Out Add-ons
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Overview of Change Orders

## CO Item

Enabled for ‘Change Order Item’ selection option only.
Specify the pending change order item for which to zero out add-ons. Initially defaults the currently selected pending change order item. Update will only zero out the add-ons for this change order item if the item has not been approved.
Update
Click this button to initiate the update process. The update will cycle through all specified pending change order items and set the add-on amounts and percentages to 0.00. Pending change order items that have been approved will be skipped.
If the update is successful, you will receive a message indicating the number of add-ons that were zeroed out. However, if no unapproved change order items are encountered during the update process, no update will occur. You will receive an appropriate message depending on the 'zero out' option you selected.

[](/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form)PM Zero Out Add-ons
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Overview of Change Orders

##  Project

Display only, the project for which you are zeroing out pending add-ons. Initially defaults the currently active project.

[](/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form)PM Zero Out Add-ons
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Overview of Change Orders

## Zero Out Pending Add-ons For

Specify the level at which to zero out add-ons for this project:

- Change Order Item – Select this option
 to zero out all add-ons for the current project, change order, and change order item.
 When selected, the CO Item input is enabled, allowing you to specify which change order
 item to update.

- Change Order – Select this option to
 zero out add-ons for the current project and change order. When this option is selected,
 the CO Item input is set to null and disabled, and the update will zero out the add-ons
 for all items on the pending change order that have not been approved.

- All Project PCO Items – Select this
 option to zero add-ons for the current project. When this option is selected, the CO
 Item input is disabled, and both the CO and CO Item inputs are set to null. The update
 will zero out the add-ons for all items on all pending change orders for the project
 that have not been approved. Update

Click this button to initiate the update process. The update will cycle through all specified pending change order items and set the add-on amounts and percentages to 0.00. Pending change order items that have been approved will be skipped.
If the update is successful, a message displays indicating the number of add-ons that were zeroed out. If no unapproved change order items are encountered during the update process, no update will occur. You will receive an appropriate message depending on the 'zero out' option you selected.

[](/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form)PM Zero Out Add-ons
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Overview of Change Orders
