---
title: "About the EM Work Order Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form"
---

# About the EM Work Order Edit Form

Use this form to create and edit work orders for equipment maintenance.
You can open this form from the EM module
 Programs folder or by clicking Edit WO on the [EM Work Order Update](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form) form.
Work orders provide a way to cost equipment repair activities. You can post all costs associated with performing a work order to items on the work order, either in AP (for outside repairs and directly purchased parts), EM Cost Adjustments (for parts from inventory), or EM or PR timecard entry (for labor). Work orders also provide a convenient way to track the status of repair jobs in progress.
Work orders fall into two categories: scheduled and
 unscheduled. You can create work orders for scheduled work based
 on the scheduled maintenance information already in the system.
 If you need to set up a work order for unscheduled repairs, you
 must enter the work order manually.

## Work Order Display

The Show All Work Orders option (Options > Show All Work
 Orders) controls the display of work orders
 in this form

- If checked, the system will
 load and display all work orders—open and
 complete—each time you open this form.

- If unchecked, only open work
 orders (those with one or more 'open' items) will
 be loaded and displayed. Large numbers of work
 orders can affect the load and display time, so if
 you typically have large numbers of work orders,
 it may be beneficial to set this option to ‘No’
 (unchecked) so that only open work orders are
 loaded and displayed.

Note: It is important to note
 that when the Show All Work Order option is
 unchecked, the form load and F4 will exclude
 completed work orders. Therefore, when entering new
 work orders, you should not use the F4 or grid
 display to determine the next number to use because
 the list of existing work orders may be
 incomplete.
The Show All Work
 Orders checkbox in EM Company
 Parameters determines the default setting for this
 option here. If you override the setting in the EM
 Work Order form, be aware that the override will
 apply only as long as the form is open. Once you
 close the form, it resets to the default value
 defined in EM Company Parameters.

## Work Order Numbers

If you enter work orders manually and are using the 'auto
 sequence' feature (i.e. you checked the Auto Sequence
 Work Order # box in EM Company
 Parameters), entering N, New or +
 in the Work Order field will cause the system to
 automatically assign the work order number for you,
 based on the Last Work Order Option you have
 specified to use.

- If using the EM Company
 option, the system assigns the next sequential
 number based on the Last Company
 W.O. # in EM Company Parameters.

- If using the Shop option,
 you must specify the equipment and shop to which the work order applies (in the
 Equipment and Shop fields in the Auto Seq Work Order
 by Shop section). Once you specify the equipment, the shop will automatically default as
 defined for the equipment in EM Equipment (which you can override). The system then
 assigns the next available sequential work order number based on the Last WO #
 specified for the shop (in EM Shops).

Note: When using
 this option, you will only be able to enter work
 orders using the Header Info tab. Grid entry is
 not supported when using this option and is
 therefore disabled.

## Work Order Header

The work order header identifies the equipment on which
 maintenance is to be performed. If there are
 components of the equipment that are in need of
 repair, you must set them up as items on the work
 order.
Note: If you initialize work
 orders, components set up with a maintenance group
 will automatically be set up as items on a work
 order for the primary equipment. This enables all
 work to be done on a piece of equipment to be pulled
 together on a single work order rather than having
 to set up separate work orders for every
 component.
Once you have
 entered the equipment number, if warranties exist
 for the equipment, a message displays in red (above
 the Warranties button) indicating that active or
 inactive (as applicable) warranties exist. Clicking
 on the Warranties button will open the EM Warranties
 form, allowing you to review and/or modifying
 existing warranty information. For more information
 about the EM Warranties form, see [EM Warranties](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form).
Also, if other
 work orders exist for the specified equipment, a
 message displays below the Work Orders button
 alerting you that information. Clicking on the Work
 Orders button opens the EM Work Order Display form,
 allowing you to show work orders based on a set of
 criteria. For more information, see [EM Work Order
 Display](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form).
Note: There are two Notes tabs
 in the header: Std Maint Group Notes and Notes. The
 Std Maint Group Notes tab contains any header notes
 initialized to the work order from the standard
 maintenance group header. You can modify or add to
 these notes manually by double-clicking the Notes
 column in the desired row; however, no system
 updates will occur (i.e. if additional notes are
 entered for a standard maintenance group header,
 they will not be added here when additional items
 are initialized to an existing work order). The
 Notes tab contains notes entered directly in this
 form and specific to the work order.

## Work Order Items

A work order identifies all of the tasks scheduled for a
 piece of equipment.
Each task is set
 up as a separate item on the work order, and defines
 the cost code charged with the associated labor
 costs. You must indicate whether you will handle the
 work in-house or at an outside facility. This allows
 you to track your own work separately from the
 equipment you have out for repair.
You can set up
 both scheduled and unscheduled items on a work
 order. Unscheduled items are always entered
 manually. However, you can pull scheduled items into
 a work order either through initialization
 (File > Initialize WO
 Item from Std Maint Group) or by manual entry. If entering
 items manually, you will need to specify the
 maintenance group and item, which will then
 automatically pull in the item’s information. For
 information about initializing work order items, see
 [EM WO Item Init](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-wo-item-init-form).
If a task
 fulfills the requirements of a standard maintenance
 item, it is important that you cross-reference it
 correctly. In addition to saving your work when
 setting up the work order, the cross-reference
 provides a way to pass information back to the
 scheduling data when the work is complete, so the
 schedule is reset.
A work order can
 contain items from more than one standard
 maintenance group. The system maintains scheduling
 information for each item separately. This allows
 for situations where not all required items in a
 group are completed. For example, if a needed part
 is unavailable, you could close out the work order
 and send the equipment back out to the field. The
 one item would continue to show on scheduled
 maintenance reports until the equipment is brought
 back in to have it done.

## Details

This tab is used to store additional information about the
 work order item. If the work order item is for a
 component of the equipment, that data is entered
 here. Additionally, if the work order is for a
 specific serialized part on the equipment, the part
 code and serial number may be entered here. If an
 active warranty exists for the part code/serial
 number, a message is displayed to indicate this.

## Parts

Use this tab to enter the all of the parts needed to complete
 the maintenance tasks for each work order item. You
 will typically only need to enter parts information
 for items being handled in-house. Initialized items
 will automatically include all parts set up for the
 standard maintenance item.
Note: When posting parts to
 the work order, the system does not require that you
 use the exact parts indicated or that you modify the
 work order if it turns out that more or different
 parts are required.
If you are
 validating parts (flag in EM Company Parameters),
 the parts must exist in EM Equipment Parts, IN
 Location Materials, or HQ Materials. If you are not
 validating parts, you can specify any part; however,
 if you specify a stocked part (an IN location is
 entered), the material must exist at the specified
 location, regardless of how the flag is set.
Parts
 information will print on the work order. If using
 the Inventory module, the system compares parts
 ‘on-hand’ to the parts needed and indicate the part
 not in stock.
Note: The information entered
 here is only used for planning purposes. In order to
 actually post the parts to a work order and enter
 quantities and pricing, you must use the EM WO Parts
 Posting program.

Related information

- [About the EM Work Order Initialize Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-initialize-form)

- [About the EM Warranties Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form)

- [About the EM Work Order Display Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-display-form)

- [About the EM WO Item Init Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-wo-item-init-form)

- [About the EM Work Order Parts Posting Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form)

- [About the EM Work Order Copy Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-copy-form)

- [About the EM Work Order Update Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-update-form)
