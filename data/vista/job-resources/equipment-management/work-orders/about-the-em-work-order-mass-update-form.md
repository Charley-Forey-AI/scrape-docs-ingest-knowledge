---
title: "About the EM Work Order Mass Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-mass-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-mass-update-form"
---

# About the EM Work Order Mass Update Form

Use this form to update or close multiple work orders.
You will typically only use this form when you need to close a range of work orders or update a range of work orders with the same information (i.e. assign a specific mechanic, status, or repair type to a group of work orders). If you only need to update or close a single work order, you can use EM Work Order Update.
Note: This form can only be used to close or update open work orders. You cannot use this form to reopen closed work orders or to make changes to closed work orders. If you need to reopen or update closed work orders, use EM Work Order Update.

## Work Order Header Selection Criteria

Use this section to restrict the work orders to update based on work order range,
 job, location, category, department, shop, and/or mechanic.
You also have the option to search for
 work orders based on the creation, due, or scheduled dates. Once you enter the
 criteria and click the Refresh button, the system populates the Work Order grid with
 all work orders meeting the specified criteria.
The system automatically checks the
 Update box for all work orders added to the grid. You can manually
 uncheck this box for those work orders you do not want to update or use the Unselect
 All button (above the grid) to uncheck the box for all items at one time.
Note: If the Update box is unchecked for all
 work orders/items, the Unselect All button changes to a Select All button, allowing
 you to auto-select all items for update if desired.

## Work Order Grid

This grid shows Work Order header information (WO number/description, equipment,
 current and total hour/odometer readings, assigned shop and mechanic, and created,
 scheduled, and due dates).
If you are closing work orders, you can
 enter the equipment's Hours and/or Odometer readings at the time the work order was
 completed (which may differ from the current readings).
Note: The hours and/or odometer values entered for a
 piece of equipment cannot exceed the Total Hours and/or Odometer reading for the
 equipment. If the equipment hour or odometer readings are inaccurate, use EM Meter
 Readings to update them.

## WO Items

This grid shows all work order items for the listed work orders, with items grouped
 by work order.
Information shown includes (but is not
 limited to) the related equipment and component, standard maintenance group/item,
 mechanic, item status and type, total hour/odometer readings, and the component's
 current and total hour/odometer readings.
The system will check/uncheck the
 Update box for each work order item based on how the Updatecheckbox is set for the related work order at the header level.
 You can manually override the setting for each work order item; however, checking
 this box for an item will automatically check the box at the work order header level
 if it was previously unchecked.
If you are closing work orders, you can
 enter the Hours and/or Odometer readings for each item on the work order; however,
 you must first assign a 'Final' status to the item and enter a completion date.

- If you entered Hours/Odometer readings at the work order
 header level, you will be unable to edit the hours/odometer at the item level.

- If the work order item is for a component, the
 hours/odometer readings entered will be specific to the component, not the
 equipment to which it is attached.

- If the Hours and/or Odometer values are null (blank) for a
 work order item and its associated work order, the system will use the current
 hours/odometer values (shown in grid). If the work order item is for a
 component, the system will use the component's current hours/odometer values.


## Work Order Item Update Overrides

Use this section to enter overrides to the PR company, mechanic, status, and repair
 type. If you are closing a range of work orders, once you select the appropriate
 ‘Final’ status, the Complete Date field is enabled,
 allowing you to specify the completion date. If you are updating to a non-Final
 status, the Complete Date field is disabled.
Once you enter the appropriate
 overrides, you must specify whether to apply the changes to the work order currently
 selected in the grid (Update box must be checked) or to all work orders with the
 Update box checked. Then click the Apply button to update the changes to the grid.
 You can manually change the settings for individual work order items if necessary.
 Once you are satisfied with the changes, click the Save Changes button. If the
 update completes with no errors, both the Work Order and WO Items grids are
 cleared.
If errors occur during the update, an
 error message displays indicating that one or more items failed to be updated. The
 system clears the grid of all work orders that updated successfully, sets the
 ‘Failed’ box to Y (checked) for remaining work orders, and displays the reason for
 the error in the Update Results column. You will need to correct the errors before
 you can retry the update.

Related information

- [About the EM Work Order Update Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form)
