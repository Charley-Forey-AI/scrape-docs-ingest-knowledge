---
title: "About the PM Zero Out Add-ons Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-zero-out-add-ons-form"
---

# About the PM Zero Out Add-ons
 Form

Use this form to zero out the add-ons for
 non-approved items on pending change orders. This form is accessed by selecting
 Tasks > Zero Out PCO
 add-Ons in [PM Pending Change
 Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form).
The Project, CO, and CO Item inputs will default
 from the currently selected project based on how you accessed the form. If you accessed
 it from the Pending tab of PM Change Orders, the zero-out level defaults to ‘Change
 Order’ and the Project and CO Item inputs are disabled. The project will be the current
 project, the CO input defaults the currently selected pending change order, and the CO
 Item input defaults as null (since the zero-out will affect the entire change order). If
 you accessed the form from the PM Pending Change Orders form, the zero-out level
 defaults as ‘Change Order Item’ and only the Project input is disabled. The CO defaults
 the currently selected pending change order and the CO Item defaults the currently
 selected pending change order item. The ‘zero-out level’ and resulting defaults may be
 overridden as desired.
Zero Out Pending Add-ons
This section allows you to specify the level at which to zero out add-ons for project. Options are:

- Change Order Item – Use this option to zero out all add-ons for
 the current project, change order, and change order item. When selected, the CO and
 CO Item inputs are enabled, allowing you to specify which change order/change order
 item to update.

- Change Order – Use this option to zero out add-ons for the
 current project and change order. When this option is selected, the CO input is
 enabled, allowing you to specify which change order to update. The CO Item input is
 disabled and set to null, and the update will zero out the add-ons for all items on
 the pending change order that have not been approved.

- All Project PCO Items – Use this option to zero add-ons for the
 current project. When this option is selected, the change order and change order item
 inputs are set to null, the CO Item input disabled, and the update will zero out the
 add-ons for all items on all pending change orders for the project that have not been
 approved.

Once you have specified the ‘zero-out level’ and
 entered the appropriate values, click Update. The update will
 cycle through all specified pending change order items and set the add-on amounts and
 percentages to 0.00. Pending change order items that have been approved will be
 skipped.
If the update is successful, you will receive a
 message indicating the number of add-ons that were zeroed out. However, if no unapproved
 change order items are encountered during the update process, no update will occur. The
 message you receive depends on the 'zero out' option you selected.
Note: Zeroing out add-on values does not prevent you from manually
 entering add-on values. For information about add-ons, see Related Topics below.
[](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form)PM Pending Change Orders
[](/en/vista/vista/project-management/change-orders/change-management---overview)Change Orders - Overview
[](/en/vista/vista/project-management/change-orders/pco-setup-options/add-ons)Add-ons
