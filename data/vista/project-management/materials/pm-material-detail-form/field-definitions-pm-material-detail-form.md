---
title: "Field Definitions: PM Material Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/pm-material-detail-form/field-definitions-pm-material-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/pm-material-detail-form/field-definitions-pm-material-detail-form"
---

# Field Definitions: PM Material Detail Form

The following is a list of field descriptions for the PM
 Material Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter a project number or press F4 to select a
 project from a list.
Note:If you enter a project with a closed status (hard or soft), the status displays in red to the right of the project description. You will only be able to add or modify material detail for the project if you allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters checked).

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Record Type

Use this field to filter the material items that display in the form. This field is disabled when you access this form from [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form), [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form), or [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form).

- Original – Select this option to enter/modify material detail for an Original Estimate.

- Approved – Select this option to enter/modify material detail for an Approved Change Order.

- Pending – Select this option to enter/modify material detail for a Pending Change Order.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## ACO

This field only displays when this form is accessed from the main menu and the Record Type is ‘A-Approved CO’s’.
 Enter the approved change order item to which this material detail applies. Approved change order must already exist for the project.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## ACO Item

This field only displays when this form is accessed from the main menu and the Record Type is ‘A-Approved CO’s’.
Enter the approved change order item to which this material detail applies. Must be a valid item for the specified change order.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## PCO Type

This field only displays when this form is accessed from the main menu and the Record Type is ‘P-Pending CO’s’.
Enter the pending change order type. Must be a document type (set up in PM Document Types) assigned a Document Category of ‘Pending Change Order’.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## PCO

This field only displays when this form is accessed from the main menu and the Record Type is ‘P-Pending CO’s’.
Enter the pending change order to which this material detail applies. Pending change order must already exist for the project.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## PCO Item

This field only displays when this form is accessed from the main menu and the Record Type is ‘P-Pending CO’s’.
Enter the pending change order item to which this material detail applies. Must be a valid item for the specified change order.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Material Code

 Enter the material to be ordered for this item or press F4 to select a material code from a list. Material codes are created and maintained using [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form).
This is an optional field. If you haven't set
 up material codes, you can enter a description of the material in the Material
 Description field.
Once the material line has been interfaced with accounting, it displays on the Interfaced tab and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Material Description

Initially defaults the material’s description as defined in HQ Materials. If a non-HQ material was entered, description defaults as “Not a valid material”. May be overridden; up to 60 characters allowed.
Note:If the material description is blank and you checked
 the Default
 Material Descriptions from Phase Description box in PM Company
 Parameters, the phase description will be used as the material description. If the
 Default
 Material Descriptions from Phase Description box is unchecked, the system
 will default the material description from the contract item assigned to the phase.

Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Material Type

Specify the material type.

- P - Purchase Order. Material is to be purchased from a vendor/supplier and will be set up on a purchase order. This will be the standard default for all non-stocked materials.

- M - Material Order. This option is only available if
 the IN in
 Use box is checked in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form), and indicates that this
 material will be allocated to the project from available inventory in the Inventory
 module and set up on a material order. This will be the standard default for all
 stocked materials.

- Q - Quote. This option is only available if the
 MS in
 Use box is checked in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form), and indicates that this
 material will be set up on a quote.

- R - Requisition. This option is only available if
 the PO
 Requisitions in Use box is checked in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form), and indicates that this
 material will be set up on a requisition for routing to a quote or purchase
 order.

Note:Once you initialize a requisition line, it is
 automatically updated to PO and moved to the Interfaced tab, and cannot be changed or
 deleted here. Changes/deletions must be handled via PO.

Once you interface material lines to
 accounting (except for requisition lines—see above), they are moved to the Interfaced tab
 and cannot be change or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Phase

Enter a phase or press F4 to select
 one from a list.
This field defaults based on the phase
 associated with the material selected in the Material field. A phase is associated
 with a material using the Material Phase field on the Info tab of
 the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.
If you enter a phase that does not exist for
 the project, the Auto-Add Cost Type from Material option in PM Company Parameters determines
 whether the phase will be allowed or not. If set to ‘1-No’, entry will not be allowed.
 Phase/cost type must be set up for the project in PM Project Phases before it can be
 entered here. If the option is set to ‘2-With No Estimates’, entry is allowed and the
 phase/cost type will be added to the project automatically. However, estimate detail will
 not be updated.
Note: This option overrides the 'Locked Phases" option for
 the project in PM Projects.
[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Cost Type

Specify the cost type for this material detail
 line. Initially defaults the cost type for the specified material from HQ Materials. If a
 cost type is not specified in HQ Materials, the field defaults from the Material Cost Type
 1 field in PM Company Parameters. Otherwise, the field defaults blank.
If you entered a phase (in the previous field)
 that does not already exist for the project and the Auto-add cost type from material option
 (in PM Company Parameters) is set to 2-With Estimates or 3-With No Estimates, the cost type
 entered here will be added to the project detail along with the phase. Otherwise, the cost
 type must be set up with phase in PM Project Phases first before it can be entered here.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Vendor

This field only applies to purchase orders.
Enter the vendor supplying the material or
 press F4to select it from a list. You need to select a vendor before you can
 enter or initialize a purchase order number. Vendors are created and maintained using [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form). If the vendor isn't on the list, press F5 to
 open AP Vendors and create a new vendor.
Note:If the vendor is not already set up in PM Firms or PM Project Firms, it will be added automatically when this line is initialized.

Once the material line has been interfaced to
 accounting using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form),
 it will displays on the Interfaced tab, and this field cannot be
 changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## PO

This field only applies to purchase orders -
 Purchase Order is selected in the Material Type field.
Enter the purchase order number. The value in this field can be up to thirty characters long.
Tip:You should use the same PO number format set up using the Material Parameters section in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

Leave this field blank if you will be
 generating the PO/PO Items numbers using the Initialize button. During initialization,
 materials will be handled as follows:

- If the Add items to approved purchase orders not
 interfaced box is checked, materials with the same vendor will be
 added as items on approved purchase orders for the vendor that have not been
 interfaced. If no approved, non-interfaced purchase orders are found for the vendor
 or this box is unchecked, how materials are initialized will depend on the Add Original Items to
 Valid Open Purchase Order for Vendor and Add Change Order
 Items to Valid Open Purchase Order for Vendor checkboxes. See below
 for more information.

- Add Original Items to Valid Open Purchase Order
 for Vendor - If this option is checked, initialization will assign
 materials to the highest existing purchase order with the latest date for the vendor.
 If no approved, non-interfaced purchase orders are found, initialization will create
 a new purchase order for the material.

- Add Change Order Items to Valid Open Purchase
 Order for Vendor - If purchase order material detail is set up on an
 approved or pending change order, and this box is checked, initialization will add
 the material detail lines as items on the highest existing purchase order with the
 latest date for the specified vendor. If one does not exist, a new purchase order
 will be created.

If none of these options is checked,
 initialization will always generate a new purchase order for each material.
 Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## PO Item

This field only applies to purchase orders.
If you entered a purchase order number in the previous field, enter the purchase order item number, up to 5 digits. If initializing PO/PO Item numbers, leave this field blank.
Note: Materials with the same vendor may be assigned the same purchase order number, depending on how you have set the Add Items to Approved Purchase Orders Not Interfaced option in PM Company Parameters. If checked and the PO has been approved (in PM Purchase Orders) but not interfaced, the material will be added as a new item on the PO. If unchecked, a new PO will be generated for the material.

If a purchase order already exists in the PO module and the vendor is the same, the material will be added as a new item on the purchase order. If the vendor does not match, a message displays indicating that one or more POs are already set up under a different vendor, and initialization will not occur. In this situation, you will need to assign the item number manually.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Receiving

This field only applies to purchase orders.
Check this box if you will be receiving this item in [PO Initialize Receipts ](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-initialize-receipts-form)or [PO Receipts Entry ](/en/vista/vista/costs-and-contracts/purchase-order/receiving/po-receiving-forms/po-receipts-entry-form). Using either of these programs to receive purchased items updates the Backordered, Received, and Invoiced quantities, allowing you to track Received not Invoiced units and costs.
Leave this box unchecked if you will be using AP Transaction Entry to receive this item. Received and Backordered quantities are updated as Invoiced.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## IN Co

This field is only for material orders and quotes.
Specify the Inventory company supplying this material.
 Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## MO

This field only applies to material orders.
Enter the material order number, up to 10 characters. It is suggested you use the same format specified for MO numbers in PM Company Parameters.
 If you will be initializing MO/MO Item numbers (Initialize button), leave this field blank. During initialization, materials will be handled as follows:

- If the Group materials by location when
 initializing box is checked (PM Company Parameters), materials will be
 grouped together by location and a separate material order created for each location.
 Materials assigned to a location already existing on a material order will be added
 as new items on that material order.

If the Group materials by location when
 initializing box is unchecked, Materials will be added as items on a single
 material order, regardless of location.

- If the Add items to approved material orders not
 interfaced box is checked, materials will be added as items on
 approved materials orders that have not been interfaced (based on 'group materials
 by' flag). If no approved, non-interfaced material orders are found, initialization
 will create a new material order for the material.

If the Add items to approved material orders not
 interfaced box is unchecked, initialization will add the material to an
 existing non-approved material order (based on 'group materials by' flag) or will create a
 new material order for the material.
 Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## MO Item

This field on applies to material orders.
Enter the number for this material order item or leave blank if you are using the Initialize feature.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## MS Co

This field only applies to quotes.
Specify the MS module company where the quote will be set up. Must be a valid company set up in [MS Company Parameters ](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form).
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Quote

For quotes only.
Enter a number for this quote, up to 10 characters, or leave blank if using the Initialize feature. If a quote has already been set up for this project, the quote number will default to the existing quote number. Only one quote can exist per project.
Note: The Initialize feature can only be used if the
 Auto-Generate
 Quote #'s option (MS Company Parameters) is checked. Otherwise, quote
 numbers must be entered manually.
If you are using the 'auto-generate' feature
 for quote numbers (option in MS Company Parameters), you can enter a "+" in this field, and
 the system will automatically generate a number for you based on the number specified in
 the Last Used Quote
 # field in MS Company Parameters.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Location

This field only applies to material orders and quotes.
Specify the IN location supplying this
 material. Location must be set up in IN Locations and must be a valid location for the
 material (i.e. set up in IN Location Materials). Entry is required in order to enter or
 initialize material order or quote numbers.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Units

Enter the number of units needed of this material.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## UM

Enter the unit of measure that applies to the material being purchase. This field initially defaults the unit of measure specified for this material in HQ Materials.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Unit Cost

Enter
 the unit cost for the material. If the field does not populate with a default value, the
 value in this field will be 0.000.
Purchase Orders
This field defaults the standard unit cost set up on the material in HQ Materials unless overrides exist in PO Category Discounts or PO Vendor Materials. In which case, the unit cost will default as indicated below:

- PO Category Discounts - If a discount exists for the vendor/material category or the vendor/material category/job in PO Category Discounts, it will apply the discount to the standard unit price in HQMT to determine the default unit cost.

- PO Vendor Materials - If an override exists for the material and vendor in PO Vendor Materials, it will default a unit cost based on the cost option (std unit cost, vendor unit cost, std book price less discount, or vendor book price less discount) or the job override (if one exists).
Material Orders / Quotes

Default will be based on the Pricing Option
 for Jobs in IN Company, the unit cost/unit price values specified in IN Location Materials,
 and the markup/discount rate specified for the job in JC Jobs. If no markup/discount rate
 specified for the job, the markup/discount rate specified for Jobs in IN Location Materials
 will be used.
Requisitions
 Default will be the standard unit cost specified for the material in HQ Materials.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

##  ECM

Indicate which quantity the unit cost represents.
E = Unit cost is per each.
C = Unit cost is per 100.
M = Unit cost is per 1000.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Amount

This field initially defaults an amount based on the Units x Unit Cost. Overriding the calculated amount will cause the unit cost to be recalculated.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## POCO Number

The POCO Number field on the PM Material Details form, Non-Interfaced tab.

This field is disabled unless there is a PO associated with the material detail. You can associate a PO with a material item using the PO field.
If creating a new PO Change Order, enter a new PO change order (POCO) number. Press F4 to see which PO change order numbers have already been created for the selected PO. Once you save the change to the material detail, the new PO change order that you just created displays in PM PO Change Orders. Click [here](/en/vista/vista/project-management/materials/po-change-orders-overview) for an overview on PO change orders.
If not creating a new PO Change order, enter an existing PO change order to associate with the material detail item. Press F4 to select an existing PO change order from a list.
If the material detail item is already associated with a PO change order, that PO change order displays in this field.
Note: PO change orders are created and maintained using [PM PO Change Orders ](/en/vista/vista/project-management/materials/pm-po-change-orders-form).

[Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)
[PM Material Detail Form](/en/vista/vista/project-management/materials/pm-material-detail-form)

## Tax Type

This field is disabled for lines with a Material Type of Q-Quote.
 Select the tax type.

- 1-Sales – Select this option for tax amounts that are payable to the vendor.

- 2-Use – Select this option for tax amounts that are accrued and paid later to the appropriate State or Local taxing authority.

- 3-VAT (Value Added Tax) – Select this option for taxes paid on goods and services.

Tax Type will default as follows:Material TypeTax Type if TaxableTax Type if Non-Taxable
P-Purchase Order
 Non-StockedSales (US) / VAT (AU or CA)Blank
 StockedSales (US) / VAT (AU or CA)Blank
M-Material Order
 Non-StockedN/AN/A
 StockedUse (US, AU, CA)Blank
R-Requisition
 Non-StockedBlankBlank
 StockedBlankBlank

Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.
[Material Buyout Overview](/en/vista/vista/project-management/materials/material-buyout-overview)
[PM Material Detail Form](/en/vista/vista/project-management/materials/pm-material-detail-form)

## Tax Code

This field is disabled for ‘Quote’ material lines.
Specify the tax code for this material. Initially defaults a tax code as follows:

- Purchase Orders - Tax code default is determined by
 the setting of the Base Tax On drop-down field in PM
 Projects. If the field is set to J-Job, the tax code defaults from
 PM Projects ( Tax Code field). If the field is set to V-Vendor,
 the tax code defaults from AP Vendors ( Tax Code field). If the field is
 set to O-Vendor Override, the tax code defaults from AP Vendors. If a tax
 code is not specified there, the tax code will default from PM Projects.

- Material Orders - Defaults the tax code specified
 for the job in PM Projects.

- Requisitions - Inherits the tax code defaulted for the line’s initial Material Type (Purchase Order or Material Order). In other words, if you enter a stocked material, the default material type will be ‘Material Order’ and the tax code will default from the project. If you then change the Material Type to ‘Requisition’, it will retain the originally defaulted tax code. Default may be overridden.

Note:If a material is flagged as ‘not taxable’, the tax code will default as ‘null’; however, it can be overridden.

Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Send

Only material items with this box checked can be interfaced with the accounting modules using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
Note:If this item has a material type of P-Purchase Order
 or M-Material Order, it can be interfaced with the accounting modules using PM Interface
 if the Send box is checked and the item is grouped onto a PO or material order
 that has been approved. This box allows you to define which items on an approved PO or
 material order are ready to be interfaced with the accounting modules because only items
 with this box checked will be sent over to the accounting modules.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Intfc Date

The Intfc Date field on the PM Material Detail form, Interfaced tab.

Display only, the date the selected purchase order/item or material order/item was interfaced.
Note: This date is populated by the system when an interface occurs for the selected item and cannot be edited, even when using the Correct Item option (Tasks > Correct Item).

## Intfc Month

The Intfc Month field on the PM Material Detail form, Interfaced tab.

Display only, the original interface month for the selected purchase order/item or material order/item.
 If you make corrections to a purchase order/item or material order/item (via Tasks > Correct Item), you must interface the changes in this month.
Note: This date is populated by the system when you first interface the selected item and cannot be edited, even when using the Correct Item option (Tasks > Correct Item).

## Requisition

This field only applies to Purchase Order types.
Enter the requisition number of this purchase order item. The requisition number can be up to 20 characters long.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Req'd Date

Specify the date this material is required.
Once the material line has been interfaced to accounting, it displays on the Interfaced tab, and this field cannot be changed or deleted.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

##  Supplier

This field is only accessible for items with a Material Type of ‘P-Purchase Order’.
 Enter the supplier for this purchase order, if applicable.
You will typically only enter a value in this field if a second party other than the vendor is involved.
If a supplier is specified here, a two-party check will be printed when paying this purchase order in AP Payment Posting.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details

## Notes

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools >  Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/materials/material-buyout-overview)Overview of the Material Buyout Process
[](/en/vista/vista/project-management/materials/pm-material-detail-form)PM Material Details
