---
title: "Field Definitions: EM Work Order Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-copy-form/field-definitions-em-work-order-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-copy-form/field-definitions-em-work-order-copy-form"
---

# Field Definitions: EM Work Order Copy Form

The following is a list of field descriptions for the EM Work
 Order Copy form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Work Order

Enter the work order to copy or press
 F4
 to select from a list of valid EM work orders.

##  Select Equipment to Copy

Select the equipment to copy option. This option, along with the value specified to the right, will determine the list of equipment shown in the grid for selection.

- Category – Select this option to copy this work order to selected equipment within a designated category (specified to the right). The copy process will create a new work order for selected equipment within the specified category.

- Equipment Range – Select this option to copy this work order to selected equipment within a range of equipment (specified to the right). The copy process will create a new work order for selected equipment within the specified range.

- Equipment Series – Select this option to copy this work order to selected equipment within a specific equipment series (indicated to the right). The copy process will create a new work order for selected equipment matching the specified year, make, and model.

##  Category

 Enter the category of equipment to which you are copying the specified work order. Must be a valid equipment category set up in EM Categories.
Note: You can include the source work order equipment when copying to a range of equipment as long as the source work order is complete and all items on the work order have a final status (i.e. the status code has a Status Type of ‘Final’). If the source equipment does not meet these requirements, it will be excluded from the grid.

## Begin/End Equipment

Enter the beginning and ending equipment in a range of equipment (set up in EM Equipment) to which you are copying the specified work order.

- If you use alphanumeric work order numbers, the beginning/ending equipment number must be the same. You can only copy alphanumeric work orders if you are copying to a single work order (i.e. a single piece of equipment).

- You can include the source work order equipment when copying to a range of equipment as long as the source work order is complete and all items on the work order have a final status (i.e. the status code has a Status Type of ‘Final’). This allows for ‘blanket’ work orders that do not require the use of standard maintenance groups. If the source equipment is not complete, it will be excluded from the grid.

##  Year

 Enter the year by which to restrict the work order copy. Only equipment assigned this year (in EM Equipment) will be set up on a new work order.
Note: The ‘copy to’ equipment cannot be the same as the ‘copy from’ equipment. If the ‘copy from’ equipment is included in the ‘copy to’ category, equipment range, or equipment series, it will be skipped during the copy process.

## Make

 Specify the Make by which to restrict the work order copy. Only equipment of this make (as specified in EM Equipment) will be set up on a new work order.
Note: The ‘copy to’ equipment cannot be the same as the ‘copy from’ equipment. If the ‘copy from’ equipment is included in the ‘copy to’ category, equipment range, or equipment series, it will be skipped during the copy process.

## Model

 Specify the Model by which to restrict the work order copy. Only equipment of this model (as specified in EM Equipment) will be set up on a new work order.
Note: The ‘copy to’ equipment cannot be the same as the ‘copy from’ equipment. If the ‘copy from’ equipment is included in the ‘copy to’ category, equipment range, or equipment series, it will be skipped during the copy process.

##  Include Source Work Order Notes?

 Check this box to copy header and item notes from the source work order to the destination work order.
 Leave this box unchecked if not copying header and item notes from the source work order to the destination work order.

##  Shop Options

 Indicate how to assign shops to new work orders.

- Source Work Order Shop – Select this option to assign new work orders to the shop specified for the source work order.

- Equipment Shop – Select this option to assign work orders to the shop specified for each piece of equipment in the selected ‘copy to’ category, equipment, or equipment series range.

Note: You should only select this option if you have assigned a shop to all equipment in the selected range. If a missing shop is encountered during the copy process, an error displays and the copy is aborted.

- Other Shop – Select this option to specify the shop to which each work order will be assigned.

##  Other Shop

 Specify the shop (from EM Shops) to which all new work orders will be assigned.

## Beginning WO

This option is only available if you are not using the 'Auto Sequence Work Order #' feature (in EM Company Parameters) for work order numbers.
Specify the number, up to 10 characters, with which to start numbering the work orders generated by the copy process.
Note: If you use alphanumeric work order numbers, you can only specify an alphanumeric work order number here if you are copying to a single work order (i.e. a single piece of equipment). If copying to multiple work orders (i.e. multiple pieces of equipment), the work order number must be numeric.

##  Begin Status: Work Order

 Specify the 'beginning' status to assign to each work order generated by the copy process. Status code must be set up in EM Work Order Status Codes) and have a status type of ‘N’ (Normal).

##  Begin Status: Parts

 Specify the 'beginning' status to assign to each part on work orders generated by the copy process. Status code must be set up in EM Work Order Parts Status).

## Date Sched

Enter the date on which to schedule the work defined on the specified work order. This date will default as the ‘Scheduled’ date in the header of the new work order, as well as for each of the work order items.

## Date Due

Enter the due date for this work order (i.e. the date on which the work is due to be completed). This date will default as the Due date in the header of the new work order, as well as for each of the work order items.
