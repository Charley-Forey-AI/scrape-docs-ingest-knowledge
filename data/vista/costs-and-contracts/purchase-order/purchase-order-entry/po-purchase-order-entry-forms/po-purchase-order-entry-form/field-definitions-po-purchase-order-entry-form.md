---
title: "Field Definitions: PO Purchase Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form"
---

# Field Definitions: PO Purchase Order Entry Form

The following is a list of field descriptions for the PO
 Purchase Order Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 If this is a new batch, this field automatically defaults to New. The system assigns sequence numbers, so you must accept the default.
 If this is an existing batch, you can either enter the sequence number to work on, or enter New to add a new sequence to the batch.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Action

The Action drop-down on the PO Purchase Order Entry form, header Info tab.
This field is only enabled when you add an existing purchase order to the batch (via PO Add Transaction to Batch).

- Add - Defaults for all new purchase orders and cannot be changed.

- Change - Select this option if you are changing an existing purchase order. This is the default option for all purchase orders added to the batch via PO Add Transaction to Batch.

- Delete - Select this option to delete a purchase order that has already been posted. You cannot delete a PO that has activity (for example, if you have posted a receipt to it).

## PO #

The PO # field on the PO Purchase Order Entry form, header Info tab.
Enter the purchase order number for this PO.
If the
 Automatically Generate PO #'s
checkbox is selected in PO Company Parameters (Info tab), you can enter "+" or "N" and the system automatically assigns the next available PO number. This number is based on the Next Auto PO #'s
value in PO Company Parameters form.
Note: This feature only works if you are using numeric PO
 numbers; that is, PO numbers that do not contain letters or special characters.
Note: You can also use the PO Pending Purchase Orders form to create POs if you use any PO workflow review/approval processes. When creating new POs in either form, the system validates that the PO # is not already in use.

Related information

- [PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Vendor

The Vendor field in the PO Purchase Order Entry form, header Info tab.
Enter the vendor (from the AP Vendors form) that is supplying the merchandise on this purchase order. If you do not know the vendor number, you can enter the vendor's sort name to display the appropriate vendor number.
Note: If you enter a non-compliant vendor, the header displays a red warning in the header section of the form

You can change vendors on existing POs even after having applied invoices. This is to accommodate instances where your original supplier had to be replaced by another vendor. Note: If you have received any items on the PO (via PO Receipts Entry), this field is disabled and cannot be changed.

## Description

The Description field on the PO Purchase Order Entry form, header Info tab.
Enter a description of the purchase order. Up to 60 characters allowed.

##  Order Date

The Order Date field on the PO Purchase Order Entry form, header Info tab.
 Enter the date that this order was placed. This field defaults to the current date.

## Prevent Auto Close

Prevent Auto Close checkbox on the Info tab of the PO Purchase Order Entry form.
Select this checkbox to prevent the purchase order from being auto-closed on final invoice.

##  Ordered By

The Ordered By field on the PO Purchase Order Entry form, header Info tab.
 Enter the name (or initials) of the person that placed the order.

## Expected Date

The Expected Date field on the PO Purchase Order Entry form, header Grid tab.
Enter the date that this order is expected to arrive.

## Status

This field indicates the current status of the purchase order. When adding a new purchase order, this field defaults to “Open”.

- Open - Can make changes, and post receipts and invoices against a PO with this status.

- Complete - PO is complete and no changes or posting should be allowed.

- Closed - This status can only be assigned by closing the PO using [PO Close](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-close-form). Committed costs/units are relieved, and inventory adjusted as needed. You cannot make changes to purchase orders flagged as “Closed.” This includes change orders.

Note: Closed PO’s may be reopened, with the exception of a job PO where the job has been closed. If you change the status of a closed PO to 'Open' (or 'Complete'), when the batch is posted, the MthClosed will be set to null, and the status updated to 0 (Open) or 1 (Complete) in the POHD (PO Header) table. If there are any records created to relieve backorder amounts on the PO, the status cannot be changed.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## SM Co #

SM Co # field on the Info tab of the PO Purchase Order Entry form.
Enter the SM Company or press F4 to select from a list of valid SM companies.

## Work Order

Work Order field on the Info tab of the PO Purchase Order Entry form.
Enter the work order, or press F4 for the SM Work Order Lookup from which to select a work order.

## JC Co #

The JC Co # field on the PO Purchase Order Entry form, header Info tab.
Enter the Job Cost company for this purchase order. This company is used as the default for Job PO items (line type 1-Job), which may be overridden.
This company is also used to default a shipping address for this purchase order. You may override the default shipping address by
 entering a Ship Location.
You may leave this field blank if desired.

## Job

The Job field on the PO Purchase Order Entry form, header Info tab.
Enter the job for this purchase order. This job is used as the default for job PO items (line type 1-Job) and default a shipping address for the purchase order.
You may leave this field blank if desired.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).  

## IN Co #

The IN Co# field on the PO Purchase Order Entry form, header Info tab.
Enter the Inventory company for this purchase order. This company is used as the default for Inventory PO items (line type 2-Inv), which may be overridden.
This company is also used in conjunction with the location to default a shipping address (defined in IN
 Locations) for this purchase order. You may override the default shipping address by
 entering a Ship Location.
You may leave this field blank if desired.

## Location

The Location field on the PO Purchase Order Entry form, header Info tab.
Enter the Inventory location for this purchase order or press F4 to select it from a
 list of valid inventory locations for the specified IN company.
 This location is used as the default location for Inventory type PO items (line type 2-Inv), which may be overridden. It is also used to default a shipping address for the purchase order.
You may leave this field blank if desired.

## Ship Location

The Ship Location field on the PO Purchase Order Entry form, header Info tab.
Enter the shipping location or press F4 to select from a list of valid shipping locations (defined in PO Shipping Locations).
The shipping location defines the default "ship to" address for the purchase order (shown on the Shipping Tab) and will print on the Purchase Order Form. You may override the address on the Shipping tab if needed.
Note: If a tax code is assigned to the ship location using PO Shipping Locations, it will be used as the tax code default for all non-job lines and will override the standard tax code defaults assigned by vendor or location.

## Hold Code

The Hold Code field on the PO Purchase Order Entry form, header Info tab.
Enter the hold code for this purchase order or
 press F4 to select from a list of valid hold codes (defined in HQ Hold Codes). Entering a hold code here automatically
 places AP transactions posted to this purchase order on payment hold.
Note: You cannot select a hold code set up for 'Retainage'
 in AP Company Parameters.

##  Pay Terms

The Pay Terms field on the PO Purchase Order Entry form, header Info tab.
Enter the payment terms for this vendor/purchase order or accept the default payment terms assigned to the vendor in AP Vendors. Press F4 to select from a list of valid payment terms.

## Cmpl Group

The Cmpl Group field on the PO Purchase Order Entry form, header Info tab.
Enter the compliance group for this purchase order or press F4 to select from a list of valid compliance groups. The compliance group is used to initialize compliance codes for this purchase order in PO Compliance Tracking. If you leave this field blank, compliance codes will need to be entered manually.
Note: If you change the compliance group for this purchase order after initialization has occurred, all compliance codes not already on the purchase order will be added when re-initialized.

## Address

Initially defaults the shipping address
 from:

- the JC Jobs for the selected job

-  IN Locations for the specified IN Location

-  the shipping address specified for the Ship Location on the PO
 Header

-  the shipping address entered on the Shipping tab in SM Purchase
 Order Entry (SM-related purchase orders only)



You may override the address if needed (up to 60 characters).

The address
 specified here will print in the "Ship To" section when printing the
 Purchase Order Form.


If you have Internet access, you can click the Map button for direct access
 to the default map site for your login (as defined in User Options, Main
 Menu). Map will default the approximate location of the specified country
 and address. If a country is not specified, attempts to locate address
 based on Default Country specified in HQ Company Setup.
[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Attention

 Enter the attention information for this shipping location, up to
 60 characters. For example, "Shipping Department".

 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the attention information from the Shipping tab in SM Purchase Order Entry.

[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## City

Specify the city for this 'ship to' address, or accept the default.
 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the city from the Shipping tab in SM Purchase Order Entry.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in [HQ Company Setup ](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form).

[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## State

Enter a valid state or press F4 to select one from a list. States are set up using [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form).
 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the state from the Shipping tab in SM Purchase Order Entry.
The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Zip Code

Specify the zip code, up to 10 characters, for this 'ship to' address, or accept the default.
 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the zip code from the Shipping tab in SM Purchase Order Entry.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.
[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Country

Enter a 2-character country code or press F4 to select a country from a list. This field is required when the address is outside the default country set up using [HQ Company Setup ](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form).
 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the country from the Shipping tab in SM Purchase Order Entry.
Tip: If you have Internet access, you can click the
 Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified in HQ Company Setup.
Note: The selected country must be valid for the selected
 state (e.g. state, province, territory, etc.), which is defined using [HQ States ](/en/vista/vista/administration/headquarters/region-setup/hq-states-form).

[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Add'l Address

Enter the additional address information for this shipping location, up to 60
 characters (e.g. Bldg 1, Suite 250). Initially defaults the additional shipping address from:

- the JC Jobs for the selected job

-  the shipping address specified for the Ship Location on the PO
 Header

-  the shipping address entered on the Shipping tab in SM Purchase Order
 Entry (SM-related purchase orders only)

 You may override the address if needed (up to 60 characters).


The address
 specified here will print in the "Ship To" section when printing the
 Purchase Order Form.


If you have Internet access, you can click the Map button for direct access
 to the default map site for your login (as defined in User Options, Main
 Menu). Map will default the approximate location of the specified country
 and address. If a country is not specified, attempts to locate address
 based on Default Country specified in HQ Company Setup.
[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Shipping Instructions

Specify the shipping instructions for this purchase order, up to 30 characters. These instructions will print on the Purchase Order Form.
 If this is an SM-related purchase order that was entered in SM Purchase Order Entry, this field defaults the shipping instructions from the Shipping tab in SM Purchase Order Entry.

[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## PO Address Seq#

The PO Address Seq# field on the PO Purchase Order Entry form, Address Overrides tab.
Use this field to override the vendor's standard purchasing address.
Specify the address sequence to use for this transaction. Must be a valid address sequence (defined for the vendor in AP Additional Addresses) with an address type of 'Purchase Order' or 'Both'. This address sequence will identify the address to use when printing the purchase order.
Note: If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Payment Address Seq#

The Payment Address Seq# field on the PO Purchase Order Entry form, Address Overrides tab.
Use this field to override the vendor's standard payment address.
Enter the address sequence to use for this transaction. Must be a valid address sequence (defined for the vendor in AP Additional Addresses) with an address type of 'Payment' or 'Both'.
This address sequence identifies the address to use when entering AP invoices referencing this purchase order (in AP Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry). It will only be used if an override address or address sequence is not specified in the invoice header and it is the first PO line for the invoice.

##  Item #

 Enter a line number for this purchase order item (max 32,767).
Note: If you are working with an existing purchase order item, you can use the Costs tab (display only) to review the current costs, invoiced amounts, and remaining amounts associated with the item.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Action

The Action drop-down on the PO Purchase Order Entry form, header Info tab.
This field is only enabled when you add an existing purchase order to the batch (via PO Add Transaction to Batch).

- Add - Defaults for all new purchase orders and cannot be changed.

- Change - Select this option if you are changing an existing purchase order. This is the default option for all purchase orders added to the batch via PO Add Transaction to Batch.

- Delete - Select this option to delete a purchase order that has already been posted. You cannot delete a PO that has activity (for example, if you have posted a receipt to it).

## Type

The Type field on the PO Purchase Order Entry form, Items info tab.
Select the type of PO item that you would like to create. The data required for the purchase order item will differ slightly depending on the type selected.
Note: This field is disabled if there has been activity posted against the PO item (for example, if you have posted a receipt to it).

1-JobUse this type to order materials for jobs. Multiple jobs may be on the same PO and do not have to match the job specified in the header. Job items interface with the JC module to update committed costs and units to specific job/phase/cost type combinations. Actual costs are updated through the processing of an invoice against the Purchase Order.When you select this type, additional fields display for entering JC Co, Job, Phase, CT, and Ticket.
2-InventoryRequires the Inventory module.Use this type to purchase items that you stock in your inventory. This type of PO interfaces with the IN module to automatically track items on order and those that have been received but not yet posted as payable in AP.
When you select this type, additional fields display for entering the IN Co and Location. In addition, display only On Hand and On Order fields show the on-hand and on-order amounts for the specified location/material.
3-ExpenseUse this type of PO for ordering goods to be expensed for your company. For example, office supplies and office machines. If you are using the EM module, you should use this type for actual equipment purchases. This type of purchase order only interfaces with AP and GL, and does not generate any committed costs.4-EquipmentRequires the Equipment Management module.
Use this type to purchase items for use with equipment (such as oil, fuel, etc.). Items that fall in this category are typically operating costs such as parts and repair costs. Assigning cost types and cost codes (EM) allows you to track these costs for each piece of equipment. Entries for this type of PO do not directly update EM. The update to EM occurs when the invoice is posted in AP. If you selected the Display last used date for parts in AP/PO/EM checkbox in EM Company Parameters (Parts tab), the screen displays the last used date of the part specified for the PO item (in the informational display above the Item tabs).When you select this type, additional fields display for entering the EM Co, Equip, Comp Type, Component, Cost Code, and CT. The Comp Type and Component fields are only enabled if the equipment is flagged as a component type in EM Equipment.
5-EM Work OrderRequires the Equipment Management module.
Use this type of PO to order items needed to complete work orders set up in the EM module. Entries for this type of PO do not directly update EM. The update to EM occurs when the invoice is posted in AP. If you selected the Display last used date for parts in AP/PO/EM checkbox in EM Company Parameters (Parts tab), the screen displays the last used date of the part specified for the PO item (in the informational display above the Item tabs).When you select this type, additional fields display for entering the EM Co, WO, WO Item, Cost Code, and CT.
6-SM Work OrderRequires the Service Management module.
Use this type of PO to purchase the material needed to complete service work orders (that is, work orders set up in Service Management). Entries of this type will generate a work completed purchase line in SM Work Orders (Work Completed tab), and update the Purchase Orders grid (in SM Work Orders). You can also enter purchase orders for SM work orders in SM Purchase Order Entry. For more information, see [SM Purchase Order Entry
 Form](/en/vista/vista/service-management/purchase-orders/purchase-order-forms/sm-purchase-order-entry-form).Note: You cannot edit purchase order information from a work completed purchase line; edits must be made directly to the purchase order item via PO Purchase Order Entry or SM Purchase Order Entry, or to the PO item line in PO Item Distribution. Changes will be updated to the related work completed purchase line.

When you select this type, additional fields display for entering the SM Co, SM Work Order, and SM Scope. If you reference a Job SM work order, additional fields include Phase (display only) and JC Cost Type.

## JC Co/IN Co/EM Co

The JC Co, IN Co, or EM Co fields in PO Purchase Order Entry, items Info tab.
Depending on the type of purchase order, this field prompts for a company number:

- JC Co (1-Job lines)

- IN Co (2-Inv lines)

- EM Co (4-Equip / 5-EM Work Order lines)

Specify the company for this purchase order item.

## Job

 Initially defaults the job code specified in the purchase order header. Accept the default, or specify the job for which you are purchasing the specified material.
Note: If you enter a soft- or hard-closed job, the status displays in red below the job description. (Job status will also display as the job description.) Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Phase

Specify the phase to which this job purchase order
 item applies. Initially defaults the material phase assigned to this line's specified
 material (in HQ Materials). If no material phase specified for the material, defaults as
 null. May be overridden.
Note: If the 'Lock Phase' option in JC Jobs is in use, this
 phase must be set up for this job in JC Job Phases. If the 'Lock Phases' option is not in
 use, must be a valid phase from JC Phases.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## CT

Enter the JC cost type the job purchase order
 applies to or press F4  to select one from a list.
This field initially defaults the material
 cost type assigned to this line's specified material (in HQ Materials). If no material cost
 type specified for the material, defaults as null. May be overridden.
Note: If the Phases on this job are locked box is
 checked in JC Jobs, the cost type specified here must be set up for the specified phase in
 JC Job Phases. If the Phases on this job are locked box is not
 checked, you must specify a valid cost type for the phase in JC Phases.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Ticket

The Ticket field on the PO Purchase Order Entry form, Items section, Info tab.
This field only displays for lines with a Type of
 1-Job.
Enter the field ticket number for this purchase order item or press
 F4 to select from a list of valid open field tickets for the
 specified job/contract.
Note: Costs associated with approved field tickets only impact T&M billings;
 therefore, assigning field tickets to job lines is only useful if the job's
 contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Location

Enter the inventory location from where you are purchasing the specified
 material or press F4 for a list of valid IN locations.
Locations are created and maintained in the
 Inventory module using [IN Locations ](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form).
Materials are assigned to locations using [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form).

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

##  Equipment

Press F4 to select the equipment that you are
 purchasing.
Equipment is created and maintained using
 [EM
 Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form). You can open this form by pressing F5 in this
 field.
Why is this field disabled?
This field is disabled if there has been activity posted on the PO item - for example if a receipt has already been posted to it.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Component Type

Press F4 to select a component type for the
 equipment from a list.
Component types are created and maintained using the [EM Component Types ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-component-types-form) form.
Why is this field disabled?
This field is disabled if there has been activity posted on the PO item - for example if a receipt has already been posted to it.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Component

 If you entered a component type in the previous field, this field will default the first component of this type for the indicated equipment (as defined in EM Equipment). May be overridden, but must be a valid component for this equipment.
Why is this field disabled?
This field is disabled if there has been activity posted on the PO item - for example if a receipt has already been posted to it.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Work Order

Specify the work order (as set up in EM Work Orders) for which you are purchasing the specified material.
This field only displays when
 EM Work Order
 is selected in the
 Type
 field.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Item

Indicate the work order item (as set up in EM Work Orders) to which this purchase order item applies.
This field only displays only when line type is 5-EM Work Order.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

##  Cost Code

 Press F4 to select a cost code that the
 equipment order item applies to from a list.
Cost codes are created and maintained using the [EM Cost Codes ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-cost-codes-form) form.
 If this is an Equipment line, and you entered a component for this equipment (previous field), this field defaults the cost code assigned to the component’s type in EM Component Types. May be overridden.
Why is this field disabled?
This field is disabled if there has been activity posted on the PO item - for example if a receipt has already been posted to it.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## CT

Enter the equipment cost type that the
 Equipment or Work Order item applies to or press F4 to select it from a list.
Equipment cost types are created and maintained using the [EM Cost Types ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-cost-types-form) form.
Why is this field disabled?
This field is disabled if there has been activity posted on the PO item - for example if a receipt has already been posted to it.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## SM Co

The SM Co field on the PO Purchase Order Entry form, items Info tab.
This field only displays for line type 6-SM Work Order.
Enter the SM company to which this purchase
 order item applies. This will be the SM company in which the SM work order was set up.
 Press F4 for a list of valid SM companies.

## SM Work Order

The SM Work Order field on the PO Purchase Order Entry form, items Info tab.
This field displays for 6-SM Work Order line types only.
Enter the SM work order to which this purchase order item applies (that is, the work order for which the material was, or is being, purchased). Press
 F4
 for a list of valid work orders for the specified SM company.
Note: If you specify a job-related work order and the job
 associated with the work order has been soft or hard-closed, the system will allow the
 entry if you allow posting to closed jobs (that is, the
 Allow Posting to
 Hard-Closed Jobs
 and/or
 Allow Posting to
 Soft-Closed Jobs
 boxes are checked in JC Company Parameters). If you do not allow posting to closed jobs, a message displays indicating the job is closed and you will be unable to proceed.

## SM Scope Seq

The SM Scope Seq field on the PO Purchase Order Entry form, items Info tab.
This field displays for 6-SM Work Order lines types only.
Enter the work order scope to which this
 purchase order item applies (that is, the scope for which the material was, or is being,
 purchased). Press F4 for a list of valid scopes for the specified work order.
Note: If you select a scope that has been closed, a warning
 displays and you will be unable to save the record. You must either reopen the scope in SM
 Work Orders or select an open scope.
Note: If this is an existing line in an open batch and the
 scope is closed prior to processing the batch, you will be unable to post the batch until
 you either reopen the scope or change to an open scope.

## SM Cost Type

The SM Cost Type field on the PO Purchase Order Entry form, items Info tab.
This field displays for line type 6-SM Work Order only.
Enter the SM cost type for this purchase order item or press F4 to select from a list of valid SM cost types.
The system uses the cost type category for this cost type, along with the department associated with the service center for the work order, to determine the GL account defaults for the resulting work completed purchase line (in SM Work Orders, Work Completed tab).
If you do not specify a cost type here, the system uses the material cost type category to determine the GL accounts to use based on the service center's department.
Note: If you are posting taxes to the purchase order item, entry of an SM Cost Type is required to ensure proper tax distribution. If you do not enter an SM Cost Type, an error is displayed and you will be unable to save the record.

## Phase

This field only displays if the line type is 6-SM
 Work Order and you specified a job-related SM work order.
The system only enables this field when you
 specify a work order scope (in the SM Scope field) that is not assigned a
 phase (in SM Work Orders).
Required.
Enter the phase (from JC Job Phases) to which
 this purchase order item applies.
Note: The system will also enable this field if the work
 order scope phase does not match the PO item phase. This condition will only occur if you
 assign a phase to the work order scope after you enter the PO Item or if you change the
 phase on the work order scope and it differs from the PO item phase.Locked Phases vs.
 Non-Locked Phases
If the job specified for the work order is
 locked (i.e. the Phases on this job are locked box is checked in JC Jobs), the phase entered
 here must be set up for the job in JC Job Phases. If the phase is not set up for the job,
 you can press F5 from this field to access JC Job Phases. Once you add the phase and exit
 JC Job Phases, you can specify the phase here.
If the job is not locked (i.e. the Phases on this job are
 locked box is not checked in JC Jobs), you can enter any phase from JC Job
 Phases or JC Phases, or any phase that matches the valid part of phase defined in JC
 Company Parameters.
 For example, say the Number of valid characters
 in Phase code field is set to 8 (in JC Company Parameters). The JC Phases
 contains phases 03110-120 and 03110-140-. If you enter phase 03110-120-100, the system will
 allow it since the first 8 characters (bolded) match the first 8 characters of phase
 03110-120-. However, if you enter phase 03110-130-, it will not be allowed, since the first
 8 characters do not match any phase in JC Phases.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## JC Cost Type

The JC Cost Type field on the PO Purchase Order Entry form, items Info tab.

This field only displays for line type 6-SM Work Order when you specify a
 job-related SM work order.
Enter the JC cost type (from JC Cost Types) for this purchase order item. Initially defaults as follows:

- If you specified an SM Cost Type for the purchase order item, this field defaults the JC Cost Type assigned to the SM Cost Type (in SM Cost Types).

- If a JC Cost Type is not specified for the SM Cost Type or you did not enter an SM Cost Type, this field defaults the Matl CT from HQ Materials for the material specified on the purchase order.

- If no Matl CT is specified for the material, this field defaults as blank.

If the job specified for the work order is locked (that is, the Phases on this job are locked checkbox is selected in JC Jobs), the cost type specified here must be set up for the job/phase in JC Job Phases. If the cost type is not set up for the job phase, you can add it by pressing F5 from this field to access JC Job Phases. Once you exit JC Job Phases, you can enter the cost type here.
If the job is not locked (that is, the Phases on this job are locked checkbox is not selected in JC Jobs), you can use any cost type defined for the phase in JC Job Phases or JC Phases.
Note: The system assigns the cost type specified here to the work completed purchase line generated (during the batch process) from this PO item. You can only make changes to the cost type at the PO item level (in PO Purchase Order Entry or SM Purchase Order Entry); you cannot change the cost type at the work completed purchase line level.

## Material

The Material field on the PO Purchase Order Entry form, items Info tab.

Entry in this field is not required unless posting an Inventory transaction (type 2-Inv).
Enter the material for this purchase order item or press F4 to select from a list of valid materials.
Note: You can enter any material, valid or non-valid unless entering an Inventory line, in which case the material must be a valid material set up for the location in IN Location Materials.

If you specify a valid material (set up in HQ Materials), the description, unit of measure, and unit cost will default from HQ Materials. If you specify a non-valid material, the material description defaults as 'Not in material file' and the unit of measure defaults as EA.
If the material exists in PO Vendor Materials for the specified vendor/material group/material, the description, unit of measure, and unit cost default from PO Vendor Materials.
Equipment LinesIf the material number exists in EM Equipment Parts, the description and unit of measure will default from EM Equipment Parts, but the unit cost will default from HQ Materials.If the material number also exists in PO Vendor Materials, the description and unit of measure will default from EM Equipment Parts, but the unit cost will default from PO Vendor Materials.
EM Work Order LinesIf the material number exists in EM Work Order Parts or EM Equipment Parts, the description and unit of measure will default from EM Work Order Parts or EM Equipment Parts, respectively; however, the unit cost will default from HQ Materials.If the material number also exists in PO Vendor Materials, the description and unit of measure will default from EM Work Order Parts or EM Equipment Parts, but the unit cost will default from PO Vendor Materials.
Note: If notes exist for the material in HQ Materials, you can add them to the notes for the purchase order item by selecting Copy Notes. Material notes are appended to any existing PO item notes. If no notes exist for the material, the Copy Notes button is disabled.

Note: This field is disabled once you distribute the PO item (in PO Item Distribution), receive the item (in PO Receipts Entry), or invoice the item (in AP Transaction Entry).

## Vendor Material Number

Enter the vendor’s identification number for this material, if applicable. Press
 F4
 for a list of vendor material numbers.
Note: When using the
 F4
 lookup, sort by the HQMT Material column. This enables the standard and substitute vendor materials to be grouped together for selection.
If a material exists in PO Vendor Materials for the specified vendor/material group/material, and the vendor material UM is equal to the HQ materials purchase UM, it will default the Vendor’s Material ID number. If the vendor material UM does not equal the HQ purchase UM, it will default the Vendor’s Material ID from the lowest UM (in PO Vendor Materials) for the vendor/material group/material.
Equipment Lines
If you specify a material number that exists in PO Vendor Materials, but that material number also exists in EM Equipment Parts (EMEP), it will pull the description and UM from EMEP, and the vendor material number will not default.
EM Work Order Lines
If you specify a material number that exists in PO Vendor Materials, but that material number also exists in EM Work Order Parts (EMWP) or EM Equipment Parts (EMEP), it will pull the description and UM from EMWP or EMEP, respectively, and the vendor material number will not default.
Note: Because the vendor’s material ID# is used as a cross-reference to the HQ material, you can enter this number if you do not know the HQ material number, and the HQ material number will be provided. This feature is only applicable to materials set up in PO Vendor Materials.
You can also enter the vendor material ID# for any substitute materials that may have been set up for the HQ material in PO Vendor Materials, and have the HQ material number provided.
Vendor material numbers are not validated.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Receiving

Check this box if you will be receiving this item in the PO module. Click [here](/en/vista/vista/costs-and-contracts/purchase-order/receiving/about-receiving-purchase-orders) for an overview on receiving POs in the PO module.
Do not check this box if you will be using AP Transaction Entry to receive this item. Received and Backordered quantities are updated as Invoiced.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Description

Enter a description for this purchase order item. The description can be up to 60 characters long.
If you enter a material in the Material field,
 this field defaults the material's description from HQ Materials. If you enter a non-valid
 material (not applicable for Inventory lines), this field defaults as 'Not in material file'.
 If you do not specify a material (not applicable for Inventory lines), this field defaults as
 null.
Other factors (line type and material chosen)
 will affect how this field defaults. The following discusses the default settings for each
 line type.
Job, Inventory, Expense, and SM Work Order
 Lines
The default settings for job, inventory, and
 expense lines follow this hierarchy.

- If you entered a valid vendor material in the
 Vendor
 Matl field, this field defaults from the Description
 field in PO Vendor Materials.

- If you entered a valid vendor material in the
 Vendor
 Matl field and the vendor material UM does not equal the Purchase UM in HQ
 Materials, this field will default the description from the lowest UM record for the
 vendor/material group/material in PO Vendor Materials.

Equipment Lines
The default settings for equipment lines
 follow this hierarchy.

- If you entered a valid vendor material in the
 Vendor
 Matl field, this field defaults from the Description
 field in PO Vendor Materials.

- If you entered a valid vendor material in the
 Vendor
 Matl field and the vendor material UM does not equal the Purchase UM in HQ
 Materials, this field will default the description from the lowest UM record for the
 vendor/material group/material in PO Vendor Materials.

- If the specified material (Material field) exists in
 EM Equipment Parts (EMEP) for the equipment, this field defaults from the Description
 field in EMEP.

EM Work Order Lines
The default settings for work order lines
 follow this hierarchy.

- If you entered a valid vendor material in the
 Vendor
 Matl field, this field defaults from the Description
 field in PO Vendor Materials.

- If you entered a valid vendor material in the
 Vendor
 Matl field and the vendor material UM does not equal the Purchase UM in HQ
 Materials, this field will default the description from the lowest UM record for the
 vendor/material group/material in PO Vendor Materials.

- If the specified material exists in EM Work Order
 Parts (EMWP) or EM Equipment Parts (EMEP), defaults the description from EMWP or EMEP,
 respectively.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## GL Co

The GL Co field on the PO Purchase Order Entry form, items Info tab.

This field is enabled for Expense lines only (type 3-Exp).
Enter the GL company for this purchase order item or press F4 to select from a list of valid GL companies. Initially defaults the GL company specified in AP Company Parameters.
For all other line types, this field defaults as follows:

- Job - Defaults the GL company assigned to the JC company in JC Company Parameters.

- Inventory - Defaults the GL company assigned to the IN Company in IN Company Parameters.

- Equip / EM Work Order - Defaults the GL company assigned to the EM company in EM Company Parameters.

- PO / SL - These two modules have a one-to-one relationship with AP; therefore, this field defaults the GL company assigned to the active AP company.

- SM Work Order - Defaults the GL company specified for the department assigned (in SM Departments) to the work order's service center.

## GL Account

The GL Account field on the PO Purchase Order Entry form, items Info tab.
Enter the GL account to charge for this purchase order item. The system uses this account as the default account in AP Transaction Entry; GL updates do not occur from the PO module.
The defaults for this field depend on the line type:

- 1-Job – Defaults from the JC Department file, based on phase or cost type. You can override this default if you checked the Allow GL Account Override when Posting Costs box in JC Company Parameters; otherwise, the system disables the field. If the default is blank, the system allows entry, but disables the field when you save the record.

- 2-Inventory – For this type, this field defaults from the Inventory Location file. You can override this default if you checked the Allow GL Account Overrides box in IN Company Parameters; otherwise, the system disables the field. If the default is blank, the system allows entry, but disables the field when you save the record.

- 3-Expense – Defaults from the AP Vendors. You can override the default as necessary.

- 4-Equipment / 5-EM Work Order – For these types, the field defaults from the EM Department file, based on cost type, and cost code (if applicable). You can override this default if you checked the Allow GL Account Override box in EM Company Parameters; otherwise, the system disables the field. If the default is blank, the system allows entry, but disables the field when you save the record.

- 6-SM Work Order - Defaults the WIP account from the SM department assigned to the service center or division specified on the SM work order. The system determines the default as follows:

- If you specified a division on the work order scope and an alternate department is assigned to the division, the system will first look for an override WIP account for parts based on the call type assigned to the work order scope. If an override account is found for the call type, it will default here.

- If no override WIP account is found for the call type, the system will use the standard WIP account for parts defined at the department level (in SM Departments, Info tab).

- If no alternate department is assigned to the division, the system will then use the department assigned to the service center to determine the default WIP account.

Note: This field is disabled if there is activity posted to the PO Item (for example, if you posted a receipt to the item).

## Required Date

Enter the date that this item is required.
This field will default to the value entered
 in the Expected
 Date field on the Info tab in the upper portion of the form.

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Pay Category

This field is enabled only if using pay categories (flag in AP Company Parameters) and allowing entry of pay types with purchase orders (flag in PO Company Parameters).
Specify a valid pay category for this purchase
 order item. The pay category specified here, along with the line type (Type field),
 will determine the default pay type.
Initially defaults a pay category as follows:

- If you have set up a standard or user pay category override in F3 Properties (not recommended), defaults the F3 pay category.

- If no F3 override exists, defaults the pay category specified for the current user in VA User Profile.

- If no override pay category is specified for the user, defaults the pay category defined in AP Company Parameters.

- If no default pay category is defined for the company, default will be null. (In this case, the pay type will default from AP Company Parameters based on the line's type.)

May be left blank or overridden with any valid pay category.
Note: The pay category specified here will override any
 defaults set by F3, VA User Profile, or AP Company Parameters when the purchase order is
 invoiced in AP Transaction Entry.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Pay Type

The Pay Type field on the PO Purchase Order Entry form,
 items Info tab.
This field is only enabled if the Specify Pay Type during PO
 Entry checkbox is selected in PO Company Parameters.
Enter the pay type for this purchase order item or accept the default. Default is determined as follows:

- If you are using pay categories (the Use Payable Category checkbox is seleted in AP
 Company Parameters), this field defaults the pay type from this line's pay category
 based on the line type:

- Job - Uses the Job pay type.

- Inv / Exp / Equip / EM Work Order - Uses the Expense pay type.

- SM Work Order - Uses the SM Work Order pay type.

You may override the default as needed; however, the pay type must be either
 assigned to the specified pay category (in AP Pay Category) or an 'unassigned' pay
 type (a pay type that has not been restricted to a pay category in AP Payable
 Types).

- If you are not using pay categories, default will be the standard pay type from AP
 Company based on the line type. May be overridden.

Note: The pay type specified here
 will override any defaults set by F3, VA User Profile, or AP Company Parameters when the
 purchase order is invoiced in AP Transaction Entry.

## UM

The UM field on the PO Purchase Order Entry form, items Info tab.

Enter a valid unit of measure for this purchase order item or accept the defaulted value.
If you entered a valid material in the Material field, this field defaults the purchase unit of measure from HQ Materials. If you specified a non-valid material (not applicable for Inventory lines), this field defaults as EA.
Other factors (line type and material chosen) affect how this field defaults. The following discusses the default settings for each line type.

- Job, Inv, Exp, and SM Work Order - If overrides exist for the specified material/vendor in PO Vendor Materials (POVM), defaults the vendor material UM matching the Purchase UM in HQ Material; if no match is found, it will default the lowest UM for the vendor/material group/material.

- Equip lines - If the specified material exists in EM Equipment Parts for the equipment, this field defaults the UM from EM Equipment Parts if it matches the Purchase UM in HQ Materials; otherwise, default will be the HQ Materials Purchase UM.If you specified a vendor material that does not also exist in EM Equipment Parts, defaults the vendor material UM if it matches the Purchase UM in HQ Materials; otherwise, defaults the lowest UM (in PO Vendor Materials) for the vendor/material group/material.
 If material does not exist in EM Equipment Parts or PO Vendor Materials, defaults the Purchase UM from HQ Materials.

- EM Work Order lines - If the specified material exists in EM Work Order Parts for the work order, this field will default the UM from EM Equipment Parts, regardless of whether it matches the Purchase UM in HQ Materials.If the specified material exists in EM Equipment Parts and does not also exist in EM Work Order Parts for the work order, it will default the UM from EM Equipment Parts if it matches the HQ Materials Purchase UM; otherwise, it will default the Purchase UM from HQ Materials.
If you specified a vendor material that does not also exist in EM Work Order Parts and/or EM Equipment Parts, defaults the vendor material UM if it matches the Purchase UM in HQ Materials; otherwise, defaults the lowest UM (in PO Vendor Materials) for the vendor/material group/material.
If the material does not exist in EM Work Order Parts, EM Equipment Parts, or PO Vendor Materials, will default the Purchase UM from HQ Materials.

If you did not enter a material for the purchase order item, this field defaults as follows:

- Job - Defaults the UM from JC Job Phases based on the cost type entered for the PO item.

- Inventory - Not applicable; you must specify a material for this line type.

- Exp / SM Work Order - If the purchase order item is the first item in a new batch, defaults the UM as null. Otherwise, defaults the UM from the previous record.

- Equip / EM Work Order - Defaults the UM from EM Cost Codes based on the cost type entered for the PO item.

Note: This field is disabled once you distribute the PO item (in PO Item Distribution), receive the PO item (in PO Receipts Entry), or invoice the item (in AP Transaction Entry).

## Units

The Units field on the PO Purchase Order Entry form, items Info tab.
This field is enabled only if you specified a unit of measure other than LS (lump sum).
Enter the number of units ordered for this item.
If this is a blanket/standing PO, you may leave this field set to 0.00. If you modify the original units/cost for a PO (regular or standing), it will cause the backordered units/cost to go negative (that is, original units/cost minus the invoiced units/cost is less than 0.00), and a warning is displayed; however, the entry is allowed.
Note: If the unit of measure is not LS and you enter zero units, the total cost must be zero.
If you change a standing PO to a regular PO (that is, you modify the original units/cost), the system updates JCCD and JCCP with the total committed costs/units and remaining committed costs/units adjusted by the amount of received units/costs.
Note: This field is disabled when any of the following conditions exist:

- The UM for the purchase order item is LS (Lump Sum)

- When the purchase order item has been distributed (via PO Item Distribution)

- When a change order has been applied against the purchase order item (in PO Change Order Entry)

## UC

The UC field on the PO Purchase Order Entry field, items Info tab.

Enter the unit cost for this purchase order item or accept the defaulted value.
 The following discusses how the system defaults this value.
Job / Exp / Equip / EM Work Order / SM Work Order Lines

- If the material's Purchase UM is equal to the Standard UM, defaults the standard unit cost defined in HQ Materials.

- If the Purchase UM is not equal to the Standard UM, defaults the unit cost defined on the Additional Units of Measure tab (in HQ Materials) for the Purchase UM.

- If pricing overrides exist in PO Category Discounts or PO Vendor Materials, defaults the unit cost as defined in the [Category/Vendor Pricing](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-00030c7a--en__Category_Vendor_Price_Overrides) section below.

- If you entered a non-valid material or did not enter a material, the unit cost defaults as 0.00.

Inventory LinesDefaults the Last Unit Cost for the material from IN Location Materials, unless pricing overrides exist in PO Category Discounts or PO Vendor Materials. In which case, the unit cost defaults as described in the [Category/Vendor Pricing](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form/field-definitions-po-purchase-order-entry-form#ID-00030c7a--en__Category_Vendor_Price_Overrides) section below.

### Category / Vendor Pricing Overrides

If you have set up vendor pricing overrides in either PO Category Discounts or PO Vendor Materials, the system uses the overrides to default the unit cost for purchase order items (all line types).
 If a discount exists for the vendor and material category in PO Category Discounts, the system applies the discount to the standard unit price in HQ Materials to determine the default unit cost.
 If an override exists for the vendor/material group/material/UM in PO Vendor Materials, the unit cost defaults based on the specified Cost Option (Standard Unit Cost, Vendor's Unit Cost, Standard Book Price less discount, or Vendor's Book Price less discount). For job lines, if job overrides exist, the unit cost defaults from the job, if a unit cost is specified; otherwise, it defaults the unit cost based on the Cost Option.

- If the unit of measure is other than LS, and you enter a zero unit cost, the total cost must be zero. In addition, you will need to invoice the items to ensure that JCCD (Cost Detail) and POIT (PO Items) are in balance before you close the PO.

- If overrides exist for the vendor/material in both PO Category Discounts and PO Vendor Materials, the system pulls the unit cost from PO Vendor Materials.

The system disables this field if any of the following conditions exist:

- The UM for the purchase order item is LS (Lump Sum)

- You distribute the purchase order item in PO Item Distribution

- The total costs are not equal

- You receive the purchase order item in PO Receipts Entry

- You invoice the purchase order item in AP Transaction Entry

- You selected to "Initialize Receipt Expenses" in PO Company Parameters

## ECM

 The ECM drop-down on the PO Purchase Order Entry form, items Info tab.
This field is disabled if the UM is LS (Lump
 Sum).
Specify which quantity the unit cost represents, or accept the default.

- E - Per Each

- C - Per Hundred

- M - Per Thousand

This field is also disabled if any of the following conditions exist:

- You distribute the purchase order item in PO Item Distribution

- The total costs are not equal

- You receive the purchase order item in PO Receipts Entry

- You invoice the purchase order item in AP Transaction Entry

- You selected to 'initialize receipt expenses' in PO Company
 Parameters (File > Initialize Expenses on Receipt)

If you change this value, the system automatically updates the Total for the purchase order item. In addition, if you have already posted the purchase order, the system also updates the related cost and billing values on the work completed purchase line (Cost Subtotal, Cost Tax Basis, Cost Tax Amt, Bill Rate, etc.) for the related work order in SM Work Orders.

## Total

If the unit of measure is LS (Lump Sum), enter the total cost for this purchase order item.
If the UM is not Lump Sum, this field defaults an amount based on Units x (Unit Cost / ECM). Accept the default total or enter the new total. If you override the default, the unit cost will be recalculated.
 If you entered zero units and/or unit cost, the total cost must also be zero.
Note: This field is disabled if any of the following conditions exist:

- The UM for the purchase order item is not LS (Lump Sum)

- You distribute the purchase order item in PO Item Distribution

- You selected to "Initialize Receipt Expenses" in PO Company Parameters

[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry

## Tax Type

The Tax Type field on the PO Purchase Order Entry form, Info tab in Items section.

Entry in this field is required if entering a tax code.
Specify the tax type for this purchase order item.

- 1-Sales – Tax amounts are payable to the vendor and
 are added to the purchase order total. This tax amount is directly charged to Job
 Cost, Equipment, and GL. This type is the default for U.S. companies.

- 2-Use - Tax amounts are accrued and paid at
 a later date to the appropriate State or Local taxing authority. Calculated tax
 amounts do not affect the gross or net balance due to the vendor. Instead, the
transaction's gross amount and tax amount are charged to Job Cost, Equipment, and GL
 account with an offsetting liability account as defined in HQ Tax Codes. Use the AP
 Tax Report to obtain an itemization of use tax amounts.

- 3-VAT (Value Added Tax) – This tax is paid on goods
 and services at each stage of production or distribution, and is based on the value
 added at each stage. It is tracked in the GL and reduces the payment to a
 taxing authority through an Input Tax Credit (ITC). This tax is not directly
 expensed. This type is the default for Canadian and Australian companies.Note: You can use the AP Value Added Tax Report to obtain an
 itemization of VAT amounts.

### SM Work Completed Lines

For purchase order items posted to an SM Work Order (line type 6),
 the system defaults the tax information based on the SM Cost Type entered on the
 purchase order item, and the Matl Tax Override and Tax Option Override options
 selected on the associated work order scope. You may override the defaults as
 needed.
SM Cost TypeMaterialTax Option OverrideMatl Tax OverrideDefault
Note: If the PO
 vendor is not assigned a tax code and the work order scope's
 tax source (service site or service center) is not assigned
 a tax code, all tax fields default as blank, but may be
 overridden.

Not TaxableBlankAllAllBlank
Not Taxable
Taxable
TaxableNot TaxableAllAllBlank
TaxableAllN - No TaxBlank
P - Taxable at Purchase
 Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at
 Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at
 Billing OnlyAllBlank
BlankP - Taxable at Purchase
 Only, M - Taxable at Purchase/Markup at Billing, F - Full Tax at
 Purchase and BillingIf Blank or 1-Sales1-Sales (US) or 3-VAT (AU/CA)
If 2-Use (US only)2-Use (US only)
N - Not Taxable, B - Taxable at
 Billing OnlyAllBlank

When you post the purchase order, the system auto-generates a work completed Purchase line on the specified work order (in SM Work Orders) for each SM Work Order line. The Tax Type specified here for each line updates the Cost Tax Type field on the generated work completed line.

Once you specify a Tax Type and Tax Code, the system displays the tax rate in the Tax Rate display field, but does not display the tax amount. However, the tax amount does display on the Purchase Order when printed, and also displays when invoicing the purchase order in AP Transaction Entry.
Note: Once you post any activity to the purchase order item (such as a receipt), this field is disabled.

[PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Tax Code

The Tax Code field on the PO Purchase Order Entry form, Info tab in the Items section.

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

Note: If the SM work order is a job work order, the default behavior is the same as described above for Job Lines.

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

Related information

- [PO Purchase Order Entry Form](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)

## Supplier

Enter the supplier number for this purchase order. Press F4 for a list
 of vendors from [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form).
Note: You will only need to use this field for purchase
 order items where a second party, other than the vendor, is involved.
[](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-purchase-order-entry-form)PO Purchase Order Entry
