---
title: "About the EM Work Order Copy Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-copy-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-copy-form"
---

# About the EM Work Order Copy Form

Use this form (accessed from the EM Programs menu or by selecting File > Copy Work Order in EM Work Order Edit) to copy work order detail from an existing work order to a new work order.

## Select Equipment to Copy

Once you have selected the source work order (i.e. the work order to copy), use this
 section to specify the destination category of equipment, range of equipment, or
 equipment series (i.e. the equipment to which you are copying the work order). Then
 click the Refresh button to populate the grid with all equipment within the selected
 category, range, or series. The Copy option is automatically checked for all
 equipment listed in the grid. Uncheck this option for any equipment that you do not
 want included in the copy process.
Note: You can include the source work order equipment when copying
 to a range of equipment as long as the source work order is complete and all items
 on the work order have a final status (i.e. the status code has a Status Type of
 ‘Final’). This allows for ‘blanket’ work orders that do not require the use of
 standard maintenance groups. If the source equipment is not complete, it will be
 excluded from the grid.

## About Copying Work Orders

Use the Copy Work Orders section of the
 EM Work Order Copy form to assign the work order shop, beginning work order and part
 statuses, and work order numbering method. When assigning the shop that will perform
 the work on each work order, you have the option to select the shop assigned to the
 source work order, the shop assigned to each piece of equipment (in EM Equipment),
 or a specific shop. You should only use the Equipment Shop option if you have
 assigned a shop to all equipment within the selected range. If a missing shop is
 encountered during the copy process, an error displays and the copy is aborted.
If you are using the ‘Auto Sequence Work
 Order #’ option (EM Company Parameters), the system will automatically generate work
 order numbers using the last company or shop work order number (depending on the
 ‘Last Work Order’ option selected in EM Company Parameters). If you are not using
 the ‘auto’ numbering feature, you must specify a Beginning WO number, and the system
 will assign work order numbers sequentially based on that number.
Note: If you manually assign work orders and use
 alphanumeric work order numbers, you can copy to an alphanumeric work order, as long
 as you are copying to a single work order (i.e. a single piece of equipment). If you
 try to copy to multiple work orders using an alphanumeric beginning WO number, you
 will get a message indicating that you cannot create multiple work orders when using
 an alphanumeric work order. If you wish to continue, you will need to either enter a
 numeric beginning WO number, or create your work orders one at a time.
You must also designate a 'beginning'
 status to assign to each work order item and each part specified on the work order,
 as well as the date work is scheduled to begin and the date it is due to be
 completed.
When you are ready to copy, click the
 Copy button. This copy process will copy the information set up on the source work
 order to each new work order (i.e. items, equipment, components, parts, cost code,
 status, etc.). If you checked the ‘Include Source Work Order Notes’ option, any
 header and item notes existing for the source work order will be copied to the
 destination work order.
Note: If the source work order includes parts, the
 parts IN Co and Location will be copied from the source work order, regardless of
 the shop you assigned to the new work order(s).
Information not copied to new work
 order(s) includes:

- Std Maint Group and Std Maint
 Item

- Part Codes and Serial Numbers


Once the process is complete, a message
 displays indicating the number of work orders generated. The Results column in the
 grid will show the work order created for each piece of equipment. You can view the
 items and parts copied to the new work orders using the New WO Items and New WO
 Parts tabs.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

- [About the EM Work Order Parts Posting Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form)

- [About the EM Work Order Update Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form)
