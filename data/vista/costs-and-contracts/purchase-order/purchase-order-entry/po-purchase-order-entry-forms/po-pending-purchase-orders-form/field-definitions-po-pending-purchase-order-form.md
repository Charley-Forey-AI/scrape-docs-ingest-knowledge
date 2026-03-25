---
title: "Field Definitions: PO Pending Purchase Order Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-pending-purchase-orders-form/field-definitions-po-pending-purchase-order-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-pending-purchase-orders-form/field-definitions-po-pending-purchase-order-form"
---

# Field Definitions: PO Pending Purchase Order Form

The following is a list of field descriptions for the PO
 Pending Purchase Order form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## PO

The PO field on the PO Pending Purchase Order form.
Enter a PO number. If you are using auto-numbering (the Automatically Generate PO #'s checkbox is selected in PO Company Parameters, Info tab), enter +. The system automatically assigns the next PO available number based on the Next Auto PO #'s field in PO Company Parameters, Info tab.
Note: This feature only works if you are using numeric PO numbers - PO numbers that do not contain letters or special characters.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Vendor

The Vendor field on the PO Pending Purchase Order form, header Info tab.
Enter the vendor (from the AP Vendors form) that is supplying the merchandise on this purchase order. If you do not know the vendor number, you can enter the vendor’s sort name to display the appropriate vendor number.
You can change vendors on existing POs even after having applied invoices. This is to accommodate instances where your original supplier had to be replaced by another vendor.
Note: If you enter a non-compliant vendor, the header displays a red warning in the header section of the form.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Description

The Description field on the PO Pending Purchase Order form, header Info tab.
Enter a description of the purchase order. The description can be up to 60 characters long.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Expected Date

The Expected Date field on the PO Pending Purchase Order form, header Info tab.
Enter the date that this order is expected to arrive.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Prevent Auto Close

The Prevent Auto Close checkbox on the PO Pending Purchase Order form, header Info tab.
Select this checkbox to prevent the purchase order from auto-closing on final invoice.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## JC Co

The JC Co field on the PO Pending Purchase Order form, header Info tab.
Specify the Job Cost company to which this PO should be posted. This company is used in conjunction with the specified job to default a shipping address (defined in JC Jobs) for this purchase order. The default ship address may be overridden by entering a Ship Location.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Job

The Job field on the PO Pending Purchase Order form, header Info tab.
Enter the Job for this PO. This job is used as the default job for Job PO items and to default a shipping address for the purchase order. It is not required in the header, and items may be entered to other jobs or no job.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## IN Co

The IN Co field on the PO Pending Purchase Order form, header Info tab.
Enter the Inventory company where the PO should be posted. This company is used in conjunction with the location to default a shipping address (defined in IN Locations) for this purchase order. The default shipping address may be overridden by entering a Ship Location.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Location

The Location field on the PO Pending Purchase Order form, header Info tab.
Enter an IN module location for this PO or press F4 to select it from a list. Inventory module locations are created using IN Locations.
This location is used as the default location for Inventory type PO items and it will default a shipping address for the purchase order.
Note: This field is not required and can be entered on PO items using the Location field on the Info tab in the lower portion of the form when creating Inventory type PO items.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## SM Co

The SM Co field on the PO Pending Purchase Orders form, header Info tab.

Enter the SM Company for this pending purchase order or press F4 to select from a list of valid SM companies.
Note: Purchase order items with a type of 6-SM Work Order will automatically default the SM company specified here; however, you may change the default as needed. This allows for work orders from multiple companies on the same purchase order.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Work Order

The Work Order field on the PO Pending Purchase Order form, header Info tab.

Enter the SM work order for this pending purchase order or press F4 to select from a list of valid SM work orders.
Note: Purchase order items with a type of 6-SM Work Order will automatically default the work order specified here; however, you may change the default as needed. This allows for multiple SM work orders on the same purchase order.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  Order Date

The Order Date field on the PO Pending Purchase Order form, header Info tab.
 Enter the date that this order was placed. This field defaults to the current date.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  Ordered By

The Ordered By field on the PO Pending Purchase Order form, header Info tab.
 Enter the name (or initials) of the person that placed the order.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Hold Code

The Hold Code field on the PO Pending Purchase Order form, header Info tab.
Enter the hold code for this purchase order or press F4 to select from a list of valid hold codes (defined in HQ Hold Codes). Entering a hold code here automatically places AP transactions posted to this purchase order on payment hold.
Note: You cannot select a hold code set up for 'Retainage' in AP Company Parameters.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  Pay Terms

The Pay Terms field on the PO Pending Purchase Order form, header Info tab.
Name change from AP Vendor Master to AP Vendors applies to 2021 R2 and forward only.Press F4 to select the payment terms for the vendor/purchase order from a list, or accept the default pay terms assigned to this vendor using the AP Vendors form.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Cmpl Group

The Cmpl Group field on the PO Pending Purchase Order form, header Info tab.
Enter the compliance group (set up in HQ Compliance Groups ) for this purchase order or press F4 to select from a list of valid compliance groups. The compliance group is used to initialize compliance codes for this purchase order in PO Compliance Tracking. If you leave this field blank, compliance codes will need to be entered manually.
Note: If you change the compliance group for this purchase order after initialization has occurred, all compliance codes not already on the purchase order will be added when re-initialized.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Ship Location

The Ship Location field on the PO Pending Purchase Order form, header Info tab.
Enter the shipping location or press F4 to select it from a list of valid shipping locations (defined in PO Shipping Locations).
The shipping location defines the default 'ship to' address, which will print on the Purchase Order Form, and overrides the job's shipping address. You may override the address on the Shipping tab. If the job address is the shipping address, no ship location is needed.
Note: If a tax code is assigned to the ship location using PO Shipping Locations, it will be used as the tax code default for all non-job lines, and will override the standard tax code defaults assigned by vendor using AP Vendors or location using IN Locations.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Address

The Address fields on the PO Pending Purchase Order form, Shipping tab.
Enter the address information for this pending purchase order. The information entered here prints in the Ship To section of the Purchase Order Form.
AddressThis field initially defaults the shipping address from either JC Jobs for the selected job, IN Locations for the specified IN location, or the shipping address specified for the Ship Location entered on the PO Header. You may override the default as needed.
Add'l AddressEnter the additional address information for this shipping location, up to 60 characters (for example, Bldg 1, Suite 250). This field initially defaults the additional shipping address from either the JC Jobs for the selected job, or the shipping address specified for the Ship Location entered on the PO Header. You may override the default as needed.CityEnter the city for this 'ship to' address or accept the default.StateEnter a valid state or press F4 to select from a list of valid HQ States.
The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
Zip CodeSpecify the zip code, up to 10 characters, for this 'ship to' address or accept the default.CountryRequired if the address is outside the default country set up in HQ Company Setup.Enter a 2-character country code or press F4
 to select from a list of valid countries. The country you select must be valid for the selected state, province, territory, and so forth (as defined in HQ States).
Shipping InstructionsSpecify the shipping instructions for this purchase order, up to 30 characters. These instructions print on the Purchase Order Form. AttentionUse this field to add attention information to the ship to address. This information displays on the standard PO Purchase Order Form report.
Note: If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## PO Address Seq#

The PO Address Seq # field on the PO Pending Purchase Orders form, Address Overrides tab.
Use this field to override the vendor's standard purchasing address.
Specify the address sequence to use for this transaction. Must be a valid address sequence (defined for the vendor in AP Additional Addresses) with an address type of 'Purchase Order' or 'Both'. This address sequence will identify the address to use when printing the purchase order.
Note: If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Payment Address Seq#

The Payment Address Seq # field on the PO Pending Purchase Order form, Address Overrides tab.
Use this field to override the vendor's standard payment address.
Specify the address sequence to use for this transaction. Must be a valid address sequence (defined for the vendor in AP Additional Addresses) with an address type of 'Payment' or 'Both'. This address sequence will identify the address to use when entering AP invoices referencing this purchase order (in AP Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry).

- The system uses this address sequence only if an override address or address sequence is not specified in the invoice header and it is the first PO line for the invoice.

- If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Notes

The Notes field on the PO Pending Purchase Order form, header Notes tab.
Enter any notes about the pending purchase order. You can also enter notes about specific pending purchase order items using the Notes tab in the lower portion of the form.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  Item #

The Item # field on the PO Pending Purchase Order form, items Info tab.
 Enter an existing PO item or enter N or + to add a new PO item.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Item Type

The Item Type drop-down on the PO Pending Purchase Order form, items Info tab.
Select the type of PO item to create. The data required for the purchase order item will differ slightly depending on
 the type selected.

Line Type
Specific Fields

1-Job
JC Co, Job, Phase, CT

2-Inventory
IN Co, Loc

3-Expense

4-Equipment
EM Co, Equip, Comp Type,
 Component, Cost Code, CT

5-EM Work Order
EM Co, WO, WO Item, Cost
 Code, CT

6-SM Work Order SM Co, SM Work Order, SM Scope Seq, SM Cost Type, Phase, JC CT.

## JC Co/IN Co/EM Co

The JC Co/IN Co/EM Co fields on the PO Pending Purchase Order form, items Info tab.
Depending on the type of purchase order, this field will prompt for JC Co (Job PO), IN Co (Inv PO), or EM Co (Equip and Work Order PO’s).
Specify the company to which this purchase order item should be posted.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  Job

The Job field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 1-Job line types.
Initially defaults the job code specified in the purchase order header. Accept the default, or specify the job for which you are purchasing the specified material.
Note: If you enter a soft- or hard-closed job, the status displays in red below the job description. (Job status will also display as the job description.) You can only save the record if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Phase

The Phase field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 1-Job line types.
Specify the phase to which this job purchase order item applies. Initially defaults the material phase assigned to this line's specified material (in HQ Materials). If no material phase specified for the material, defaults as null. May be overridden.
Note: If the 'Lock Phase' option in JC Jobs is in use, this phase must be set up for this job in JC Job Phases. If the 'Lock Phases' option is not in use, must be a valid phase from JC Phases.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## CT

The phase CT field on the PO Pending Purchase Order form, item Info tab.
This field only displays for 1-Job line types.
This field initially defaults the material cost type assigned to this line's specified material (in HQ Materials). If no material cost type specified for the material, defaults as null. May be overridden.
Note: If the Phases on this job are locked box is checked in JC Jobs, the cost type specified here must be set up for the specified phase in JC Job Phases. If the Phases on this job are locked box is not checked, you must specify a valid cost type for the phase in JC Phases.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Ticket

The Ticket field on the PO Pending Purchase Orders form, items Info tab.

This field displays for Job lines only.
Enter the field ticket number that applies to this pending purchase order item or press F4 to select from a list of valid field tickets for the specified job/contract.
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to pending purchase order items for a job is only useful if the job's contract/contract item has a bill type of T&M or Both. For more information about Field Tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Loc

The Loc field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 2-Inventory line types.
Enter the inventory location from where you are purchasing the specified material or press F4 for a list of valid IN locations.
Locations are created and maintained in the Inventory module using IN Locations.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Equip

The Equip field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 4-Equipment line types.
Enter the equipment for this PO or press F4 to select from a list of valid equipment.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Comp Type

The Comp Type field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 4-Equipment line types.
Enter the component type or press F4 to select from a list of valid components for the specified equipment.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Component

The Component field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 4-Equipment line types.
If you entered a component type in the previous field, this field will default the first component of this type for the indicated equipment (as defined in EM Equipment). May be overridden, but must be a valid component for this equipment.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Cost Code

The Cost Code field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 4-Equipment and 5-EM Work Order line types.
 Enter the equipment cost code or press F4 to select from a list of valid cost codes.
 If this is an Equipment line and you entered a component for this equipment (in the Component field), this field defaults the cost code assigned to the component's type in EM Component Types. May be overridden.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

##  CT

The equipment CT field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 4-Equipment and 5-EM Work Order line types.
Enter the equipment cost type or press F4 to select from a list of valid EM cost types for the specified cost code.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## WO

The WO field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 5-EM Work Order line types.
Specify the work order (as set up in EM Work Orders) for which you are purchasing the specified material.
This field only displays when EM Work Order is selected in the Type  field.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## WO Item

The WO Item field on the PO Pending Purchase Order form, items Info tab.
This field only displays for 5-EM Work Order line types.
Indicate the work order item (as set up in EM Work Orders) to which this purchase order item applies.
This field only displays only when line type is 5-EM Work Order.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## SM Co

The SM Co field on the PO Pending Purchase Orders form, items Info tab.

This field only displays when the line type is 6-SM Work Order.
Enter the SM company to which this pending purchase order item applies or press F4 to select from a list of valid SM companies. This will be the SM company in which the SM work order was set up.
 If you specified an SM Co in the pending purchase order header, that company defaults here; however, you may change the default as needed.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## SM Work Order

The SM Work Order field on the PO Pending Purchase Orders form, items Info tab.

This field only displays when line type is 6-SM Work Order.
Enter the SM work order to which this purchase order item applies (that is, the work order for which the material was, or is being, purchased). Press F4 for a list of valid work orders for the specified SM company.
Note: If you specify a job-related work order and the job associated with the work order has been soft or hard-closed, the system will only allow the entry if you allow posting to closed jobs ('allow posting to closed jobs' options in JC Company Parameters). If you do not allow posting to closed jobs, a message displays indicating the job is closed and you will be unable to proceed.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## SM Scope Seq

The SM Scope Seq field on the PO Pending Purchase Order form, items Info tab.

This field only displays when line type is 6-SM Work Order.
 Enter the work order scope to which this purchase order item applies (that is, the scope for which the material was, or is being, purchased). Press F4 for a list of valid scopes for the specified work order.
Note: If you select a scope that has been closed, a warning displays and you will be unable to save the record. You must either reopen the scope in SM Work Orders or select an open scope.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## SM Cost Type

The SM Cost Type field on the PO Pending Purchase Order form, items Info tab.

This field displays only when line type is 6-SM Work Order.
 Enter the SM cost type for this purchase order item or press F4 to select from a list of valid SM cost types.
 The system uses the cost type category for this cost type, along with the department associated with the service center for the work order to determine the GL account defaults for the resulting work completed purchase line (in SM Work Orders, Work Completed tab). If you do not specify a cost type here, the system use the material cost type category to determine the GL accounts to use based on the service center's department.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Phase

The Phase field on the PO Pending Purchase Order form, items Info tab.

This field only displays if the line type is 6-SM Work Order.

Display only, the phase assigned to the work order scope (in SM Work Orders).
If you have not assigned a phase to the work order scope, an error displays indicating that the specified scope is missing a phase and that you must enter a phase for the scope before continuing. The record will not be saved unless you open the work order and assign a phase to the work order scope.

## JC CT

The JC CT field on the PO Pending Purchase Order form, items Info tab.

This field only displays if the line type is 6-SM Work Order and is only enabled for job-related SM work orders.
 Enter the JC cost type (from JC Cost Types) for this pending purchase order item. Initially defaults as follows:

- If you specified an SM Cost Type for the purchase order item, this field defaults the JC Cost Type assigned to the SM Cost Type (in SM Cost Types).

-  If a JC Cost Type is not specified for the SM Cost Type, this field defaults the Matl CT from HQ Materials for the material specified on the purchase order.

-  If no Matl CT is specified for the material, this field defaults as blank.

 Once you review, approve, and process the purchase order, the system assigns this cost type to the work completed purchase line generated from this item during the batch process. Edits to this cost type can only be made at the PO item level; they cannot be made at the work completed purchase line level.
Note: If this is a job-related SM work order and the specified job is locked (that is, the Phases on this job are locked checkbox is selected in JC Jobs), the cost type specified here must be set up for the job/phase in JC Job Phases.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Material

The Material field on the PO Pending Purchase Order form, items Info tab.
Enter the material being ordered on this PO. You can enter any material, valid or non-valid unless entering an Inventory line, in which case the material must be a valid material set up for the location in IN Location Materials.
If you enter a non-valid material, the material description defaults as 'Not in material file' and the unit of measure defaults as EA.
If you specify a valid material (set up in HQ Materials), the description, unit of measure, and unit cost defaults from HQ Materials.
If the material exists in PO Vendor Materials for the specified vendor/material group/material, the description, unit of measure, and unit cost defaults from PO Vendor Materials.
Equipment LinesIf the material number exists in EM Equipment Parts, the description and unit of measure default from EM Equipment Parts, but the unit cost defaults from HQ Materials.
If the material number also exists in PO Vendor Materials, the description and unit of measure default from EM Equipment Parts, but the unit cost defaults from PO Vendor Materials.
EM Work Order LinesIf the material number exists in EM Work Order Parts or EM Equipment Parts, the description and unit of measure default from EM Work Order Parts or EM Equipment Parts, respectively; however, the unit cost defaults from HQ Materials.
If the material number also exists in PO Vendor Materials, the description and unit of measure defaults from EM Work Order Parts or EM Equipment Parts, but the unit cost defaultsfrom PO Vendor Materials.

Note: If notes exist for this material in HQ Materials, you can add them to the notes for the purchase order item by selecting Copy Notes. Material notes are appended to any existing PO item notes. If no notes exist for the material, the Copy Notes button is disabled.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Vendor Matl

The Vendor Matl field on the PO Pending Purchase Order form, items Info tab.
Enter the vendor's identification number for this material, if applicable. Press F4 for a list of vendor material numbers.
If a material exists in PO Vendor Materials for the specified vendor/material group/material and the vendor material UM is equal to the HQ materials purchase UM, this field defaults the vendor's Material ID number. If the vendor material UM does not equal the HQ purchase UM, this field defaults the vendor's Material ID from the lowest UM (in PO Vendor Materials) for the vendor/material group/material.
Note: Because the vendor's material ID# is used as a cross-reference to the HQ material, you can enter this number if you do not know the HQ material number, and the system will auto-default the HQ material number in the Material field. This feature is only applicable to materials set up in PO Vendor Materials.You can also enter the vendor material ID# for any substitute materials that may have been set up for the HQ material in PO Vendor Materials, and have the HQ material number provided. Vendor material numbers are not validated.

Equipment LinesIf you specify a material that exists in PO Vendor Materials, but that material number also exists in EM Equipment Parts (EMEP), the system pulls the description and UM from EMEP, and the vendor material number will not default.EM Work Order LinesIf you specify a material that exists in PO Vendor Materials, but that material number also exists in EM Work Order Parts (EMWP) or EM Equipment Parts (EMEP), the system pulls the description and UM from EMWP or EMEP, respectively, and the vendor material number will not default.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Receiving

The Receiving checkbox on the PO Pending Purchase Order form, items Info tab.
Select this checkbox to receive this purchase order item in PO Receipts Entry.
Leave this checkbox unselected to receive this purchase order item using AP Transaction Entry. Received and Backordered quantities are updated as Invoiced.
For information about receiving POs, see [About Receiving Purchase Orders](/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders).
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Description

The Description field on the PO Pending Purchase Order form, items Info tab.
Enter a description for this purchase order item. The description can be up to 60 characters long.
If you enter a material in the Material field, this field defaults the material's description from HQ Materials. If you enter a non-valid material (not applicable for Inventory lines), this field defaults as 'Not in material file'. If you do not specify a material (not applicable for Inventory lines), this field defaults as null.
Other factors (line type and material chosen) will affect how this field defaults. The following discusses the default settings for each line type.
Job, Inventory, Expense, and SM Work OrderThe default settings follow this hierarchy:

- If you entered a valid vendor material in the Vendor Matl field and the vendor material UM matches the Purchase UM in HQ Materials, this field defaults from the Description field in PO Vendor Materials.

- If you entered a valid vendor material in the Vendor Matl field and the vendor material UM does not match the Purchase UM in HQ Materials, this field defaults the description from the lowest UM record for the vendor/material group/material in PO Vendor Materials.

.Equipment and EM Work Order The default settings follow this hierarchy:

- If you entered a valid vendor material in the Vendor Matl field and the vendor material UM matches the Purchase UM in HQ Materials, this field defaults from the Description field in PO Vendor Materials.

- If you entered a valid vendor material in the Vendor Matl field and the vendor material UM does not match the Purchase UM in HQ Materials, this field defaults the description from the lowest UM record for the vendor/material group/material in PO Vendor Materials.

- For Equip lines only: If the specified material (Material field) exists in EM Equipment Parts (EMEP) for the equipment, this field defaults from the Description field in EMEP.

- For EM Work Order lines only: If the specified material (Material field) exists in EM Work Order Parts (EMWP) or EM Equipment Parts (EMEP), defaults the description from EMWP or EMEP, respectively

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## GL Co

The GL Co field on the PO Pending Purchase Order form, items Info tab.
This field is only enabled for 3-Expense line types.
Enter the GL company for this purchase order item or press F4 to select from a list of valid GL companies.
For the remaining line types, this field is display only and defaults the GL company as follows:

- 1-Job - Defaults the GL company assigned to the JC company in JC Company Parameters.

- 2-Inventory - Defaults the GL company assigned to the IN Company in IN Company Parameters.

- 4-Equipment / 5-EM Work Order - Defaults the GL company assigned to the EM company in EM Company Parameters.

- 6-SM Work Order - Defaults the GL company assigned to the SM company in SM Company Parameters.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## GL Account

The GL Account field on the PO Pending Purchase Order form, items Info tab.
Enter the GL account to charge for this purchase order item. The system uses this account as the default account in AP Transaction Entry; GL updates do not occur from the PO module.
The defaults for this field depend on the line type:

- 1-Job – Defaults from the JC Department file, based on phase or cost type.

- 2-Inventory – Defaults from the Inventory Location file.

- 3-Expense – Defaults from the AP Vendors.

- 4-Equipment – Defaults from the EM Department file, based on cost type, and cost code (if applicable).

- 5-EM Work Order – Defaults from the EM Department file, based on cost type, and cost code (if applicable).

- 6-SM Work Order – Defaults the WIP account from the SM department assigned to the service center or division specified on the SM work order. The system determines the default as follows:

1. If you specified a division on the work order scope and an alternate department is assigned to the division, the system looks for an override WIP account for parts based on the call type assigned to the work order scope. If an override account is found for the call type, it defaults here.

1. If no override WIP account is found for the call type, the system uses the standard WIP account for parts defined at the department level (in SM Departments, Info tab)

1. If no alternate department is assigned to the division, the system uses the department assigned to the service center to determine the default WIP account using the same process defined in steps 1 & 2 above.

Note: For all line types, you can only override the defaulted value if you selected the Allow GL Account Override when Posting Costs checkbox in JC Company Parameters; otherwise, the system disables this field. However, if the default is blank, the system allows entry and then disables the field once you save the record.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Req Date

The Req Date field on the PO Pending Purchase Order form, items Info tab.
Enter the date that this PO item is required.
This field defaults to the value entered in the Expected Date field on the header Info tab.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Pay Category

The Pay Category field on the PO Pending Purchase Order form, items Info tab.
This field only displays if you selected the Using Payable Category checkbox in AP Company Parameters (Pay Types/Discounts/ICR tab).
Enter the pay category or press F4 to select from a list of valid pay categories. This field initially defaults a value as follows:

- If a pay category is defined in VA User Profile for the current user, defaults the specified pay category.

- If no pay category is specified in VA User Profile, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the company, this field defaults as blank. (In this case, the pay type defaults from AP Company Parameters based on the line's type.)

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Pay Type

The Pay Type field on the PO Pending Purchase Order form, items Info tab.
This field is only enabled if the Specify Pay Type during PO Entry checkbox is selected in PO Company Parameters.
Enter the pay type for this purchase order item or accept the default. Default is determined as follows:

- If you are using pay categories (Use Payable Category box checked in AP Company Parameters), this field will default the pay type from this line's pay category based on the line type:

- Job - Uses the Job pay type

- Inventory, Expense, Equipment, and EM Work Order - Uses the Expense pay type

- SM Work Order - Uses the SM Work Order pay type

The default may be overridden; however, the pay type must be either assigned to the specified pay category (in AP Pay Category) or an 'unassigned' pay type (a pay type that has not been restricted to a pay category in AP Payable Types).

- If you are not using pay categories, default will be the standard pay type from AP Company based on the line type. May be overridden.

Note: The pay type specified here overrides any defaults set up in VA User Profile or AP Company Parameters when the purchase order is invoiced in AP Transaction Entry.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## UM

The Tax Code field on the PO Pending Purchase Order form, items Info tab.
Enter a valid unit of measure for this purchase order item.
If you enter a valid material for this PO item, this field defaults the Purchase UM defined for the material in HQ Materials. If you enter a non-valid material (non-Inventory lines only), this field defaults as EA.
However, other factors (line type and material) affect how this field defaults. The following discusses the default settings for each line type.
Job, Inventory, Expense, and SM Work Order linesIf overrides exist for the specified material/vendor in PO Vendor Materials (POVM), defaults the vendor material UM matching the Purchase UM in HQ Material; if no match is found, it will default the lowest UM for the vendor/material group/material.Equipment linesIf the specified material exists in EM Equipment Parts for the equipment, this field defaults the UM from EM Equipment Parts if it matches the Purchase UM in HQ Materials; otherwise, default will be the HQ Materials Purchase UM. If you specified a vendor material that does not also exist in EM Equipment Parts, defaults the vendor material UM if it matches the Purchase UM in HQ Materials; otherwise, defaults the lowest UM (in PO Vendor Materials) for the vendor/material group/material. If material does not exist in EM Equipment Parts or PO Vendor Materials, defaults the Purchase UM from HQ Materials.EM Work Order linesIf the specified material exists in EM Work Order Parts for the work order, this field will default the UM from EM Equipment Parts, regardless of whether it matches the Purchase UM in HQ Materials. If the specified material exists in EM Equipment Parts and does not also exist in EM Work Order Parts for the work order, it will default the UM from EM Equipment Parts if it matches the HQ Materials Purchase UM; otherwise, it will default the Purchase UM from HQ Materials. If you specified a vendor material that does not also exist in EM Work Order Parts and/or EM Equipment Parts, defaults the vendor material UM if it matches the Purchase UM in HQ Materials; otherwise, defaults the lowest UM (in PO Vendor Materials) for the vendor/material group/material. If the material does not exist in EM Work Order Parts, EM Equipment Parts, or PO Vendor Materials, will default the Purchase UM from HQ Materials.
If no material is entered:

- Job - Defaults the UM from JC Job Phases based on the cost type entered for the PO item.

- Inventory - Not applicable; a material must be specified for this line type.

- Expense, SM Work Order - If the purchase order item is the first item in a new batch, defaults the UM as null. Otherwise, defaults the UM from the previous record.

- Equipment, EM Work Order - Defaults the UM from EM Cost Codes based on the cost type entered for the PO item.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Units

The Units field on the PO Pending Purchase Order form, items Info tab.
Specify the number of units ordered for this item, or leave at 0.00 if this is a blanket (standing) PO. If you modify the original units/cost for a PO (regular or standing) and it will cause the backordered units/cost to go negative (i.e. original units/cost minus the invoiced units/cost is less than 0.00), a warning is displayed; however, the entry is allowed.
Note: If the unit of measure is other than LS and you enter zero units, the total cost must be zero.

If you change a standing PO to a regular PO (i.e. modify the original units/cost), JCCD and JCCP will be updated with the total committed costs/units and remaining committed costs/units adjusted by the amount of received units/costs.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## UC

The UC field on the PO Pending Purchase Order form, items Info tab.
Enter the unit cost for this purchase order item or accept the defaulted value.
 The following discusses how the system defaults this value.
Job / Exp / Equip / EM Work Order / SM Work Order Lines

- If the material's Purchase UM is equal to the Standard UM, defaults the standard unit cost defined in HQ Materials.

- If the Purchase UM is not equal to the Standard UM, defaults the unit cost defined on the Additional Units of Measure tab (in HQ Materials) for the Purchase UM.

- If pricing overrides exist in PO Category Discounts or PO Vendor Materials, defaults the unit cost as defined in the Category/Vendor Pricing section below.

- If you entered a non-valid material or did not enter a material, the unit cost defaults as 0.00.

Inventory LinesDefaults the Last Unit Cost for the material from IN Location Materials, unless pricing overrides exist in PO Category Discounts or PO Vendor Materials. In which case, the unit cost defaults as described in the Category/Vendor Pricing section below.

### Category / Vendor Pricing Overrides

If you have set up vendor pricing overrides in either PO Category Discounts or PO Vendor Materials, the system uses the overrides to default the unit cost for purchase order items (all line types).
 If a discount exists for the vendor and material category in PO Category Discounts, the system applies the discount to the standard unit price in HQ Materials to determine the default unit cost.
 If an override exists for the vendor/material group/material/UM in PO Vendor Materials, the unit cost defaults based on the specified Cost Option (Standard Unit Cost, Vendor's Unit Cost, Standard Book Price less discount, or Vendor's Book Price less discount). For job lines, if job overrides exist, the unit cost defaults from the job, if a unit cost is specified; otherwise, it defaults the unit cost based on the Cost Option.

- If the unit of measure is other than LS, and you enter a zero unit cost, the total cost must be zero. In addition, you will need to invoice the items to ensure that JCCD (Cost Detail) and POIT (PO Items) are in balance before you close the PO.

- If overrides exist for the vendor/material in both PO Category Discounts and PO Vendor Materials, the system pulls the unit cost from PO Vendor Materials.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## ECM

The ECM drop-down field on the PO Pending Purchase Order form, items Info tab.
Specify which quantity the unit cost represents, or accept the default.

- E - Per each

- C - Per Hundred

- M - Per Thousand

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Total

The Total field on the PO Pending Purchase Order form, items Info tab.
If the unit of measure is LS (Lump Sum), enter the total cost for this purchase order item.
If the UM is not Lump Sum, this field defaults an amount based on Units x (Unit Cost / ECM). Accept the default total or enter the new total. If you override the default, the unit cost will be recalculated.
 If you entered zero units and/or unit cost, the total cost must also be zero.
Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Tax Type

The Tax Type drop-down on the PO Pending Purchase Orders form, items Info tab.

Specify the tax type for this purchase order item.

- !-Sales – Tax amounts are payable to the vendor and are added to the purchase order total. This tax amount is directly charged to Job Cost, Equipment, and GL. This type is the default for U.S. companies.

- 2-Use - Tax amounts are accrued and paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction's gross amount and tax amount are charged to Job Cost, Equipment, and GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) – This tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. It is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. This type is the default for Canadian and Australian companies.

Note: Once you specify a code in this field and a tax type in the ax Type field, the system displays the tax amount in the Tax Rate display field. The tax amount will also display on the Purchase Order when printed, and will also show when invoicing in AP.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

### SM Work Completed Lines

For purchase order items posted to an SM Work Order (line type 6), the system defaults the tax information based on the SM Cost Type entered on the purchase order item, and the Matl Tax Override and Tax Option Override options selected on the associated work order scope. You may override the defaults as needed.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the PO vendor is not assigned a tax code and the work order scope's tax source (service site or service center) is not assigned a tax code, all tax fields default as blank, but may be overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank
BlankP - Taxable at Purchase Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at Billing OnlyAllBlank

Once you post the purchase order, the system auto-generates a work completed Purchase line on the specified work order (in SM Work Orders) for each SM Work Order line. The Tax Type specified here for each line updates the Cost Tax Type field on the generated work completed line.

## Tax Code

The Tax Code field on the PO Pending Purchase Order form, items Info tab.

Entry in this field requires that you first enter a Tax Type.
Enter the tax code to use for this purchase order item or accept the defaulted value. Press F4 to select from a list of valid tax codes for the specified Tax Type.
This field defaults as follows:
Job LinesThe default for job lines is determined by the setting of the Base Tax On field in JC Jobs.

- J-Job - The tax code defaults from JC Jobs ( Tax Code field). If no tax code is specified for the job, the default will be null.

- V-Vendor - The tax code defaults from AP Vendors ( Tax Code field). If a tax code is not specified for the vendor, the default will be null.

- O-Vendor Override - The tax code defaults from AP Vendors. If a tax code is not specified for the vendor, the tax code will default from JC Jobs. You can override the default as necessary.

Inv / Exp / Equip / EM WO / SM WO LinesFor all non-job lines, the tax code defaults as follows:

- If you specified a Ship Location (PO header) and the ship location is assigned a tax code, that tax code defaults here.

- If the ship location is not assigned a tax code or you do not specify a ship location, this field defaults as follows:

- Inventory lines - Defaults the tax code specified for the inventory location. If no tax code is specified for the location, this field defaults as blank.

- Exp / Equip / EM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults as blank.

- SM Work Order lines - Defaults the tax code from AP Vendors for the vendor specified in the PO header. If a tax code is not assigned to the vendor, this field defaults based on the Tax Type.

- If the tax type is Sales or VAT, this field defaults the Tax Code assigned to the service site or service center, depending on the tax source specified for the work order scope.

- If the tax type is Use, this field defaults the Use Tax Code assigned to the service site or service center, depending on the scope's tax source. If no Use Tax Code is specified, it defaults the Tax Code specified for the tax source.

- If no tax codes (sales or use) are defined for the tax source, this field defaults as blank.

Intercompany TransactionsFor intercompany invoices, the tax code defaults as follows:

- If the tax type is Sales or VAT (Value Added Tax), the tax code defaults based on the Tax Group assigned to the AP Company.

- If the tax type is Use, the tax code defaults based on the Tax Group assigned to the 'posted to' company

### Committed Costs (Job Lines)

If you post a job cost line (JC type) with tax, the system relieves committed costs from the phase/cost type in JC Cost Detail table for the tax amount as follows:

- if phase or cost type overrides do not exist for the tax code, the system uses the phase and cost type specified for the PO item.

- if phase and cost type overrides exist for the tax code, the system uses the tax code phase and cost type.

- if a phase override exists for the tax code, but a cost type override does not exist, the system uses the tax code phase and the cost type from the PO line.

- if a cost type override exists for the tax code, but a phase override does not exist, the system uses the phase from the PO line and the tax code cost type.
Note: In all cases, the system updates JC with the tax rate amount. When you create an AP transaction for this PO item, the system relives the original tax rate amount from JC, but uses the current tax rate when creating an invoice.

### Redirect Phase/Cost Type

If this PO item is for a job (line type 1-Job) or a job-related SM work order (line type 6-SM Work Order) and the tax code is assigned a redirect phase and/or cost type (JC Tax Phase and/or JC Cost Type in HQ Tax Codes), the system validates the phase and/or cost type based on the Phases on this job are locked checkbox in JC Jobs.
If the Phases on this job are locked checkbox is selected and:

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases for the PO Item job (if a 1-Job line) or the work order job (if a 6-SM Work Order line).

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

If the Phases on this job are locked checkbox is not selected and

- The tax code specifies a redirect phase only, the phase must exist in JC Job Phases or JC Phases for the PO Item job or the SM work order job.

- The tax code specifies both a redirect phase and cost type, the phase/cost type combination must exist for the specified job in JC Job Phases or JC Phases.

- The tax code specifies a redirect cost type only, the cost type must exist in JC Job Phases or JC Phases for the PO item phase (Job line) or the work order scope phase (SM Work Order line). For SM Work Order lines, if you have not assigned a phase to the work order scope, the cost type must exist for the PO item phase.

Note: If validation determines that the conditions indicated above do not exist, you will need to either use a different tax code or add the phase and/or cost type combination to JC Job Phases or JC Phases (depending on the "locked phases" flag) before you can post the batch.

## Supplier

The Supplier field on the PO Pending Purchase Order form, items Info tab.
Enter the supplier number for this purchase order. Press F4 to select from a list of valid vendors.
Note: You will only need to use this field for purchase order items where a second party, other than the vendor, is involved.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.

## Notes

The Notes field on the PO Pending Purchase Order form, item Notes tab.
Use this field to enter any notes about the selected pending PO item.
Note: You can also enter notes that apply to the entire pending PO using the Notes tab in the upper portion of the form.

Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

Note: Once you approve and process a pending change order, you can only make changes to it by pulling it into a PO Purchase Order Entry batch.
