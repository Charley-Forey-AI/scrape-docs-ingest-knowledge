---
title: "Field Definitions: PM Purchase Orders Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/materials/pm-purchase-orders-form/field-definitions-pm-purchase-orders-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/materials/pm-purchase-orders-form/field-definitions-pm-purchase-orders-form"
---

# Field Definitions: PM Purchase Orders Form

The following is a list of field descriptions for the PM
 Purchase Orders form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter a project or press F4 to select a project from a list.
Note: If you enter a project with a closed status (hard or soft), the status displays in red to the right of the project description. You will only be able to add or modify purchase orders for the project if you allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters checked).

## Purchase Order

The Purchase Order field on the PM Purchase Order form.
Press F4 to select an existing purchase order or enter a new purchase order using one of the following methods:

- Enter + or N and tab off the field or select New Record () from the toolbar. The system automatically creates a new purchase order and assigns it the next available PO number based on the Purchase Order Number setup in PM Company Parameters (Material Parameters tab).

-  Enter a PO number that has not already been used (for any project/job in the current company). The PO number can be up to 30 characters long and can be in any format, but we recommend that you use the Purchase Order Number format defined in PM Company Parameters.Note: If you enter a purchase order number that is associated with another project/job, a message displays indicating that the PO already exists for another JC/Job.

Note: If you do not allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters are unselected), you can only view existing purchase orders; you cannot not add new purchase orders or modify existing ones (all inputs will be disabled).

## Description

Enter a description for this purchase order. The value in this field can be up to 30 characters long.

## Vendor

Enter the vendor that the materials are being purchased from or press
 F4
 to select a vendor from a list. If the vendor is not on the list, press F5 to open
 [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) and create a new vendor.

##  Document Type

 Use this field to categorize the purchase
 order that you are creating. Press F4 to select a document type from a
 list.
Note: Document types are created and maintained
 using the PM Document Types form.

If you select  > Send with
 transmittal, a document type must be selected in this field.

## Date Ordered

Enter the date the material was ordered.

## Prevent Auto Close of PO

Prevent Auto Close of PO checkbox on the Info tab of the PM Purchase Orders form.
Select this checkbox to prevent the purchase order from being auto-closed on final invoice.

## Ordered By

Enter the person who ordered this material. The value in this field can be up 10 characters long.

## Expected Date

Enter the date you expect to receive the material.
Date field shortcuts
T or tSet the date to the current date.
MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.
+The system will automatically set the date to tomorrow.
+5The system will automatically set the date to 5 days in the future. You can actually enter any value after the +, for example you can enter +7 to set the date to next week.

-The system will automatically set the date to the previous day.

-5The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the -, for example you can enter -7 to set the date to the previous week.

## Pay Terms

 Enter the payment terms (from HQ Payment Terms) that will apply when posting invoices to this purchase order. Initially defaults the payment terms specified for the selected vendor in AP Vendors. Accept the default, or enter the payment terms.

## Hold Code

Enter the hold code that applies to this purchase order. Leave this field blank if no hold code applies.
Hold codes are created and maintained using [HQ Hold Codes ](/en/vista/vista/administration/headquarters/company-setup/hq-hold-codes-form).

## Comp Group

The Comp Group field on the PM Purchase Orders form, Info tab.
If tracking compliance for this purchase order, enter the compliance group that will be used to initialize compliance codes for this purchase order in PO.
If you change the compliance group, you must first delete the current compliance group and save the purchase order. Then add the new compliance group and save. All previously assigned compliance codes are left intact, and compliance codes not already existing for the purchase order are added.
 To delete unwanted compliance codes, select File > PO Compliance. This will bring up the PO Compliance form, allowing you to delete, modify, or add compliance codes as necessary.

## Approved

The Approved checkbox in the PM Purchase Orders form, Info tab.

This checkbox is enabled:

- If you are not using the Process Workflow feature.

- If you are using the Process Workflow feature and the PO is fully approved (Workflow Status of Approved) or if the PO does not require approval (Workflow Status is Approval Not Required).

Select this checkbox to approve this PO. When selected, the By field displays the approver's username.
Note: This checkbox must be selected in order to interface the PO (via PM Interface). In addition, the Send checkbox (on the Non-Interfaced tab) must be selected for any PO items that you want included in the interface.

Leave this checkbox unselected if the purchase order has not been approved or should not be interfaced with the accounting modules using PM Interface.

### Review/Approval Process

If you are using the Process Workflow feature, this checkbox is disabled for purchase orders with a Workflow Status of Approval Required, Submitted for Approval,Partial Approval, or Rejected. You can see the progress of a purchase order's review/approval process by selecting the Workflow button.
Once the purchase order is fully approved (all assigned reviewers have reviewed and approved it), the system sets the Approved checkbox to selected, populates the Approved By field with the username of the final approver, and sets the Workflow Status to Approved.
Note: This checkbox is enabled if the Workflow Status is Approved or Approval Not Required.

For more information about the review/approval process, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

### Unapprove a PO

You can unapprove a PO, as long as it is not associated with a PO change order (POCO). If you attempt to unapprove a PO that is linked to a POCO, the system displays an error and prevents you from saving the record.
If you are using the Process Workflow feature, you can unapprove a PO in one of two ways:

- You can change, delete, or add non-interfaced items. Once you make changes, the system automatically deselects the Approved checkbox and changes the Workflow Status to Approval Required.

- Reviewers can unapprove a PO via the PM Work Center by selecting the purchase order from the Purchase Order query (in the Procurement folder) and then selecting Tasks > Approve/Unapprove. When a purchase order is unapproved with this method, the system deselects the Approved checkbox and sets the Workflow Status to Submitted for Approval.

Note: You can manually deselect this checkbox, but the Workflow Status is only updated if you make changes to the PO. Additionally, the 'approved by' field is only cleared if the final approver deselects this checkbox; for all other users, it is left intact.

## Ship To Job

Check this box to ship the materials on this purchase order to the shipping address specified for the project. Uncheck this box if the materials should be shipped to a different location.
Note:Note: Checking this box will disable the Shipping Location field.

##  Shipping Location

 This field is only accessible if the ‘Ship to Job’ option is unchecked.
 Enter the location (from PO Shipping Locations) to which the materials on this purchase order will be shipped.

## Address/City/State/Zip Code

If the Ship to Job option is checked, these fields default the shipping address, city, state, and zip code specified for the project in PM Projects.
If a Shipping Location is entered, these fields default the address, city, state, and zip code specified for the shipping location in PO Shipping Locations.
If overriding the defaulted address, enter the shipping address, city, state, and zip code to use for this purchase order. This address will print in the Ship To section of the purchase order.
Note: The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Ship Country field.

Note: If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Ship Country

If the ‘Ship to Job’ option is checked, this field defaults the ship country specified for the project in PM Projects.
If you enter a Shipping Location, this field defaults the ship country specified for the shipping location in PO Shipping Locations.
If overriding the default address, enter the 2-character country code. Initially defaults country code from the import data file if specified; otherwise, defaults as null.
Note: Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Add'l Address

The Add'l Address field on the PM Purchase Orders form, Shipping tab.
If the Ship to Job checkbox is selected, this field defaults the additional shipping address specified for the project in PM Projects.
If you entered a Shipping Location, this field defaults the additional address specified for the shipping location in PO Shipping Locations.
 If overriding the defaulted address, enter the additional shipping address to use for this purchase order. This address will print in the Ship To section of the purchase order.
Note: If you have Internet access, you can select the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Shipping Instructions

 Enter shipping instructions for this purchase order, up to 60 characters. These instructions will print on the purchase order form.

## Attention

Enter the person or department to whose attention this PO should be addressed. Up to 30 characters allowed. May be used when creating reports or PO's in Crystal Reports.

## PO Address Seq#

The PO Address Seq#field on the PO Purchase Order Entry form, Address Overrides tab.
If needed, you can use this field to override the vendor's standard purchasing address using an additional address set up on the vendor using AP Vendors. Press F4 to select an additional address from a list.
Additional addresses are set up on vendor records using the Additional Addresses tab of AP Vendors. Only additional addresses set up as purchase addresses, or both purchase and payment addresses, can be assigned using this field.
For more information about assigning additional addresses to vendors, see [About Additional Vendor Addresses](/en/vista/vista/accounting/accounts-payable/vendors/about-additional-vendor-addresses).

## Payment Address Seq

The Payment Address Seq field on the PM Purchase Orders form, Address Overrides tab.
This field is used to override the vendor's standard payment address using an additional address set up on the vendor using AP Vendors. Press F4 to select an additional address from a list.
Additional addresses are set up on vendor records using the Additional Addresses tab of AP Vendors. Only additional addresses set up as payment addresses, or both purchase and payment addresses can be assigned using this field.
For more information about assigning additional addresses to a vendor, see [About Additional Vendor Addresses](/en/vista/vista/accounting/accounts-payable/vendors/about-additional-vendor-addresses).
Note:This address sequence will only be used if no override address or address sequence is specified in the invoice header (AP) and it is the first PO line for the invoice.

Note: This address sequence will only be used if no override address or address sequence is specified in the invoice header (AP) and it is the first PO line for the invoice.

## Item

This is the PO item number assigned to the PO item when the PO was created using PM Material Details.
If you are creating a new PO item, enter a purchase order item (1-9999) number or enter N or + to assign the next available sequential number.

## Project

Display only, the project to which this purchase order item applies. This will typically be the same as the project specified in the PO header; however, it may differ if multiple projects share the same purchase order.
Note: If adding new items, default will always be the current project and cannot be changed. Items where the project differs from the PO header project can only be added via PM Material Detail.

## Material

Enter the material for this purchase order item or press F4 to select a material from a list.
Materials are created and maintained using [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form). Press F5 in this field to access this form.

## Item Description

Initially defaults the description of the selected material, as defined in HQ Materials. May be overridden, up to 60 characters.
Note: If the material description is blank and you checked the Default Material Descriptions from Phase Description box in PM Company Parameters, the phase description will be used as the material description. If the Default Material Descriptions from Phase Description box is unchecked, the system will default the material description from the contract item assigned to the phase.

##  Receiving

 Check this box to receive this item using PO Initialize Receipts or PO Receipts Entry. Using either of these programs to receive purchased items updates the Backordered, Received, and Invoiced quantities, allowing you to track Received not Invoiced units and costs.
 Leave this box unchecked to receive this item using AP Transaction Entry to receive this item. Received and Backordered quantities are updated as Invoiced.

## Phase

 Enter the phase to which the specified material applies. Initially defaults the material phase specified in HQ Materials or as null if no material phase specified.

## Cost Type

Enter the cost type for the selected phase or press F4 to select a cost type from a list.
If you did not select a material in the Material field, the cost type will default based on the default material cost type. This is defined using the Material Cost Type 1 field on the Material Parameters tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).
If you selected a material in the Material field, this field will default with the cost type associated with the material using [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form).

## Ticket

The Ticket field on the PM Purchase Orders form, Non-Interfaced Items tab.

Enter the field ticket number for this purchase order item or press F4 to select from a list of valid open field tickets for the associated contract.
Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to job lines is only useful if the project's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

##  Units

 Enter the number of units of the specified material being purchased.

##  U/M

 Enter the unit of measure by which this material is being purchased (must be a valid unit of measure defined for the material in HQ Materials or HQ Material Units of Measure). Initially defaults the Purchase UM specified for this material in HQ Materials.

## Unit Cost

Enter the unit cost for this material. Initially defaults the unit cost specified for the purchase UM (in HQ Materials) unless overrides exist in PO Category Discounts or PO Vendor Materials. In which case, the unit cost will default as indicated below:

- PO Category Discounts - If a discount exists for the vendor/material category or the vendor/material category/job in PO Category Discounts, it will apply the discount to the standard unit price in HQMT to determine the default unit cost.

- PO Vendor Materials - If an override exists for the material and vendor in PO Vendor Materials, it will default a unit cost based on the cost option (std unit cost, vendor unit cost, std book price less discount, or vendor book price less discount) or the job override (if one exists).

## ECM

The ECM field on the PM Purchase Orders form, Non-Interfaced tab.

Indicate which quantity the unit cost represents.

- E = Unit cost is per each

- C = Unit cost is per 100

- M = Unit cost is per 1000

## Amount

The Amount field on the PM Purchase Orders form, Non-Interfaced tab.
This field defaults a calculated amount based on the Units and Unit Cost fields.
If you change the value in this field the value in the Unit Cost field will be recalculated.

## POCO Number

You can use this field to create a new PO change order (POCO) or associate the PO item with an existing POCO. If the PO item is already associated with a POCO, it will display in this field.
Enter a new PO change order(POCO) number to create a new POCO and associate the PO with it. You can press F4 to see the POCOs that have already been created for the selected purchase order.
Once the record is saved, you can view the new POCO using [PM PO Change Orders ](/en/vista/vista/project-management/materials/pm-po-change-orders-form). Click [here](/en/vista/vista/project-management/materials/po-change-orders-overview) for an overview on PO change orders.
To select an existing PO change order, press F4 and select the desired POCO from the list.

## Required Date

Enter the date the material is required.

## Send

Select this checkbox if this purchase order item should be interfaced with the accounting modules using PM Interface. Only PO items on an approved purchase order and with this box checked will be included in the interface.
Leave this box unchecked if this purchase order item is not ready to be interfaced and the PO item will be skipped when the purchase order is interfaced.

## Tax Code

If the specified material is flagged as taxable, the default for this field is determined by the setting of the Base Tax On drop-down field in PM Projects. If the field is set to J-Job, the tax code defaults from PM Projects (Tax Code field). If the field is set to V-Vendor, the tax code defaults from AP Vendor Master (Tax Code field). If the field is set to O-Vendor Override, the tax cod defaults from AP Vendors. If a tax code is not specified there, the tax code will default from PM Projects. You can override the default as necessary.
If this material is not flagged as taxable, default is null. Tax code may still be entered.

## Tax Type

Specify the tax type for this purchase order item.

- 1-Sales – Select this option for tax amounts that are payable to the vendor.

- 2-Use – Select this option for tax amounts that are accrued and paid later to the appropriate State or Local taxing authority.

- 3-VAT (Value Added Tax) – Select this option for taxes paid on goods and services.

Tax Type will default as follows:

- If the ‘Default Country’ defined for this company (in HQ Company Setup) is ‘US’, tax type defaults as ‘Sales’.

- If ‘Default Country’ is other than US(e.g. Canada, Australia, etc.), tax type defaults as ‘VAT’.

## Requisition #

This is an optional field.
Enter the requisition number of this purchase order item. The value in this field can be up to 20 characters long.

## ACO

This field displays the approved change order that applies to the purchase order item.
This field only applies to items that have not been interfaced.

## ACO Item

This field displays the approved change order item that applies to the purchase order item.
This field only applies to items that have not been interfaced.

## Supplier

The Supplier field on the PM Purchase Orders form, Non-Interfaced tab.
Enter the supplier for this purchase order, if applicable.
Note:You will typically only enter a value in this field if a second party other than the vendor is involved.

If a supplier is specified here, a two-party check will be printed when paying this purchase order in AP Payment Posting.

## Notes

Use this tab to enter any miscellaneous notes about this item. The space allowance is virtually unlimited.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
