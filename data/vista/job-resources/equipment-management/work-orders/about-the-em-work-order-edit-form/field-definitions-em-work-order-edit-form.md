---
title: "Field Definitions: EM Work Order Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form/field-definitions-em-work-order-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form/field-definitions-em-work-order-edit-form"
---

# Field Definitions: EM Work Order Edit Form

The following is a list of field descriptions for the EM Work
 Order Edit form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Work Order

Manually Enter Work Order Numbers
If you are not using the 'auto-seq' feature
 (that is, the Auto
 Sequence Work Order # box is unchecked in EM Company Parameters), enter a
 work order number, up to 10 characters.
Auto Sequence Work Order Numbers
If you are using the auto-seq feature (i.e.,
 the Auto Sequence
 Work Order # box is checked in EM Company Parameters), enter N, New, or
 + to have the system
 automatically assign a work order for you. Work Order numbers will be assigned as follows:

- If auto-sequencing by EM Company, the system will assign the next
 sequential work order number based on the Last Company W.O. # in EM Company
 Parameters.

- If auto-sequencing by Shop, the system will assign the next
 sequential work order number based on the Last WO# for the specified shop (in EM
 Shops).

Note: If you are manually assigning work order numbers and
 use the F4 lookup or grid display (Grid tab) to determine existing work order numbers, it
 is suggested that you select Options > Show All Work
 Orders to ensure all work order numbers are visible. If the Show All Work Orders
 option is off (unchecked), the F4 and form load will exclude all completed work orders,
 resulting in an incomplete list of work order numbers in the F4 lookup and the grid.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Equipment

 This field is only accessible if using ‘auto-sequence’ feature and Last Work Order Option is ‘Shop’ (in EM Company Parameters).
 Enter the equipment to which this work order applies. Once the system assigns the work order number, it will update this Equipment to the work order header. Field is then cleared and disabled.
Note: If you initialized this Work Order or are using the ‘auto-sequence’ by company feature, this field defaults as null and is disabled.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Shop

 This field is only accessible if
 using ‘auto-sequence’ feature and Last Work Order Option is ‘Shop’ (in EM Company
 Parameters).
 Specify the shop performing the work on this
 work order. Initially defaults the shop assigned to the equipment (in EM Equipment).
 The system uses the shop specified here to determine the next work order number to assign (based on the Last WO# for the specified shop in EM Shops). Once the system assigns the work order number, it will update this shop to the work order header. Field is then cleared and disabled.
Note: If a ‘Last WO #’ is not specified for this shop (in EM Shops), automatic number assignment will not occur. Cursor will return to the Work Order input and you will be required to manually enter the work order number.
Note: If you initialized this Work Order or are using the ‘auto-sequence’ by company feature, this field defaults as null and is disabled.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Equipment

 Enter the equipment (from EM Equipment) that this work order will service. If you use the auto-sequencing by shop feature, defaults the equipment specified above.
Note: You cannot change the equipment for work orders with
 existing items.
Note: If warranties exist for the equipment, a message
 displays above the Warranties button indicating that ‘active’ or ‘inactive’ warranties
 exist. Clicking the Warranties button will access EM Warranties, allowing you to review
 and/or edit warranty information.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Description

Enter a description for this work order, up to 60 characters. If you initialized this work order (in EM Work Order Initialize), defaults to 'Auto-Init WO -MM/DD/YYYY', where MM/DD/YYYY represents the Work Order Date you specified at the time of initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Created

Enter the date this work order was created. If you initialized this work order, defaults the Work Order Date specified in EM Work Order Initialize.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Due

 Enter the date by which this work order must be completed. If you initialized this work order, defaults the due date specified in EM Work Order Init.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Scheduled

Enter the date the work indicated by the work order is scheduled to be done. This date will be used as the default scheduled date for each item.
If you initialized this work order, defaults the scheduled date specified in EM Work Order Initialize.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Shop

Enter the shop (from EM Shops) that is responsible for completing this work order. If you initialized this work order, defaults the shop specified in EM Work Order Initialize.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## PR Co

 Enter the PR company of the mechanic assigned to this work order. If you initialized this work order, defaults the PR Co specified in EM Work Order Init.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Mechanic

 Specify the mechanic (from PR Employees) assigned to this work order. If you initialized this work order, defaults the mechanic specified in EM Work Order Init.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## INCo

Specify the IN company supplying the parts for this work order. If you initialized this work order, defaults the inventory location specified in EM Work Order Initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## IN Loc

 Specify the inventory location (from IN Locations) supplying the parts for this work order. If you initialized this work order, defaults the inventory location specified in EM Work Order Initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Std Maint Group Notes: Notes

If you initialized this work order, this field will default any notes entered on the Notes tab of the standard maintenance group header. You can add to or modify the notes as necessary by double-clicking the Notes column. However, the system will not update these notes with additional notes entered for the standard maintenance group header (in EM Standard Maintenance Groups); you will need to update the notes manually.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Work Order Item

 Enter the number of an existing work order item or enter N, New, or + to add a new item. The system will automatically assign the next available sequential number.
 To initialize work order items from a selected maintenance group for the equipment, select File > Initialize WO Item From Std Maint Group.
 If you initialized this work order in EM Work Order Initialization, the WO item defaults as assigned for the maintenance item in EM Standard Maintenance Groups.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Description

 Enter a description of the work order item, up to 60 characters. If you initialized this work order, defaults the description assigned to the maintenance item in EM Standard Maintenance Groups.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Component

 Specify the component that applies to this work order item. Component must be set up for the equipment in EM Equipment.
 If you initialized this work order, defaults the component specified for the maintenance item in EM Standard Maintenance Groups, if applicable.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Comp Type

 This field is only accessible if you specified a component above and defaults the component’s type. You can override the component type if necessary; however, you will also need to change the component to one of the specified component type before you can save the record.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Std Maint Group

Enter the standard maintenance group or press
 F4
 to select one from a list. Standard maintenance groups are created and
 maintained using the EM Standard Maintenance Group form. [More](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-standard-maintenance-groups-form)
If you initialized work order items (in EM Work Order Initialization or EM WO Item Init), defaults the maintenance group specified during initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Std Maint Item

If a standard maintenance group was specified in the previous field, enter the standard maintenance item here. If this item is not associated with a standard maintenance group, leave this field blank.
If you initialized work order items (in EM Work Order Initialize or EM WO Item Init), defaults the item from the specified standard maintenance group.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: PR Co

Enter the PR Co of the mechanic assigned to this work order item. If you initialized this work order item (in EM Work Order Initialization or EM WO Item Init), defaults the PR Co specified during initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Mechanic

Enter the mechanic (from PR Employees) for this work order item.
If you initialized this work order item (in EM Work Order Initialization or EM WO Item Init), defaults the mechanic specified during initialization.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Cost Code

Enter the cost code to charge with costs for this work order item. You can only override this cost code if you have specified to allow changes to cost codes when posting work orders (option in EM Company Parameters, Work Orders tab).
If you initialized this work order item (in EM Work Order Initialization or EM WO Item Init), defaults the cost code assigned to the maintenance item in EM Standard Maintenance Groups.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

##  Info: Status

 Enter the status (from EM Work Order Status Codes) for this work order item. Initially defaults the Beginning WO Status code defined in EM Company Parameters, if applicable.
Note: Status codes entered here cannot be of a ‘Final’ type. If you need to set a work order item to a ‘final’ status, use the EM Work Order Update form.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Repair Type

 Enter the repair type (from Work Order Repair Types) for this work order item. If you specified a standard maintenance group item above, defaults the repair type specified for the maintenance item in EM Standard Maintenance Groups. If you did not assign a repair type to the standard maintenance item or you did not reference a maintenance group/item, the repair type defaults from EM Company Parameters.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Info: Priority

 Indicate the priority status of this work order item.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Repair Code

 Enter a repair code, up to 10 characters, for this work order item (e.g. bodywork, chassis, accident, scheduled, etc.). Not validated—entry is informational only, but is useful for tracking repairs.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: HQ Part Code

 Enter the part code for this work order item, if applicable. Must be a valid HQ material, vendor part, or an equipment part cross-referenced to a valid HQ material.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Serial No.

 If you entered a part code in the previous field, enter the serial number of the part, if applicable, up to 20 characters.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Created

 Enter the creation date for this work order item. Initially defaults the Created date specified in the work order header.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Due

 Enter the due date for this work order item (i.e. the date maintenance is to be completed). Initially defaults the Due date specified in the work order header.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Scheduled

 Enter the date on which maintenance is scheduled to begin. Initially defaults the Scheduled date specified in the work order header.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Work Performed

 Indicate where the work indicated for this work order item will be performed.

- In-House - Select this option if performing the work for this item in-house.

- Outside - Select this option if you are having work for this item done by an outside service. When posting costs to work order items flagged with this option, the cost type will default the Outside Repair Cost Type specified in EM Company Parameters (Work Orders tab).

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Est Hours

 This field is only accessible if you elected to perform the work for this item in-house.
 Specify the number of hours estimated to complete the work on this item.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Details: Quote

 This field is only accessible if you elected to have an outside service perform the work for this item.
 Specify the dollar amount quoted to complete the work on this item.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Seq#

 Enter N, New, or + to add a new parts sequence. System will assign the next available sequence number.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: INCo

 If part is a stocked material, specify the IN company from which it will be pulled.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Inv Loc

 If part is a stocked material, specify the inventory location (from IN Locations) from which it will be pulled.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Part Code

Specify the part needed to complete this work order item. If you initialized this work order/item, defaults the part code defined for the standard maintenance item in EM Standard Maintenance Groups, if applicable.
If you are validating parts (i.e., the
 Validate
 Parts/Materials box is checked in EM Company Parameters, Parts tab), and you
 do not specify an IN Co and Location, the part code entered here must be a valid HQ
 material, vendor part, or an equipment part cross-referenced to a valid HQ material. If you
 do specify an IN Co and Location, the material must be valid and active for the
 location.
Note: If you specify a part code that is referenced to an HQ material, the program will use the HQ material and validate the unit of measure from HQ Materials or from IN Location (if you specify an IN Co/Location).
If you are not validating parts, any part code
 may be used, as long as you do not specify an IN Co and Location. If an Inventory location
 was specified in the previous field, part must be set up and active for that location (IN
 Location Materials), regardless of how the Validate Parts/Materials checkbox is set.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Description

 Defaults the description defined for the specified part in HQ Materials. You may override if necessary.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: UM

 If part is a valid HQ material, unit of measure defaults from HQ Materials. You may override if necessary.
 If you entered a non-valid HQ part, specify the unit of measure for this part.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Qty Needed

 Specify the quantity needed of this part to complete this work order item.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: P/S Flag

- P – Purchase. Select this option if you are purchasing this part from an outside vendor.

- S – Stocked. Select this option if you are pulling this part from on-hand stock.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Status

 Enter the status (from EM Work Order Parts Status) for this part. Initially defaults the Beginning Parts Status code from EM Company Parameters, if one specified.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)

## Parts: Required

Check this box if this part is required to complete this work order item.
Leave this box unchecked if this part is not required to complete this item.
Note: This box must be checked in order for quantities to default for this part in EM Work Order Parts Posting. If you leave this box unchecked, quantities will default as 0.00.

Related information

- [About the EM Work Order Edit Form](/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-edit-form)
