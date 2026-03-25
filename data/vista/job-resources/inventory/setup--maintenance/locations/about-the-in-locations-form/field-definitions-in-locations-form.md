---
title: "Field Definitions: IN Locations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form/field-definitions-in-locations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form/field-definitions-in-locations-form"
---

# Field Definitions: IN Locations Form

The following is a list of field descriptions for the IN
 Locations form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Enter a code, up to 10 characters, to identify this inventory location.

##  Description

 Enter a description of this location, up to 60 characters.

##  Active

 Check this box to indicate that this is a currently active location. Location will be valid for purchases, sales, transfers, and production posting.
 Do not check this box if this location is not currently active. Purchase, sale, transfer, and production transactions cannot be posted to this location. However, inactive locations and their associated materials can be deleted using the IN Purge program.

##  Purchase Reviewer

 Specify a reviewer (from HQ Reviewer) for this inventory location. The reviewer specified here will be assigned automatically to all Inventory requisition lines (in PO Requisition Entry) that specify this inventory location. This field may be overridden manually in PO Requisition Reviewer.
Press F4 for a list of active Reviewers from
 which to choose.
Press F5 in the Reviewer field
 to access HQ Reviewers.

##  Invoice Reviewer

 Specify a reviewer (from HQ Reviewer) for this inventory location. The reviewer specified here will be assigned automatically to all unapproved invoice lines (in AP Unapproved Invoice Entry) that specify this inventory location. This field may be overridden manually in AP Invoice Line Reviewers.
Press F4 for a list of active Reviewers from
 which to choose.
Press F5 in the Reviewer field
 to access HQ Reviewers.

## Invoice Reviewer Group

Optional field.
Enter the reviewer group that defaults for each line referencing this location in AP Unapproved Invoice Entry.
Press F4 for a list of active reviewer groups.
Press F5 to access HQ Reviewer Group
For more information on reviewer groups, refer to Related Topics below.

Related information

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)

##  Mailing Address: Address

 Enter the mailing address for this location, up to 60 characters. This field is informational only.

##  Mailing Address: City

 Enter the city for this mailing address, up to 30 characters. This field is informational only.

##  Mailing Address: State

 Enter the state (from HQ States) for this mailing address. The system validates the state based on the Default Country specified in HQ Company Parameters for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Mailing Address: Zip

 Enter the zip code for this mailing address, up to 10 characters. This field is informational only.

## Mailing Address: Country

Enter the 2-character country code for this mailing address. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Mailing Address: Add'l Address

 Use this field to enter additional address information for this location (up to 60 characters). For example, if the location receives mail at a P.O. Box, then you might enter the P.O. Box in the Mailing Address field above, and use this field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.

##  Shipping Address: Address

 Enter the shipping address for this location, up to 60 characters. (Initially defaults the Mailing Address specified above.) This address will be used as the default when setting up purchase orders referencing this location.

##  Shipping Address: City

 Enter the city for this shipping address, up to 30 characters. (Initially defaults the MailingCity specified above.) This will be the default city for purchase orders set up referencing this location.

## Shipping Address: State

Enter a valid state (as defined in HQ States) for this shipping address. (Initially defaults the MailingState specified above.) The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
This will be the default state for purchase orders set up referencing this location.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Shipping Address: Zip

 Enter the zip code for this shipping address, up to 10 characters. (Initially defaults the Mailing Zip specified above.) This will be the default zip code for purchase orders set up referencing this location.

## Shipping Address: Country

Enter the 2-character country code for this shipping address. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

##  Shipping Address: Add'l Address

 Use this field to enter additional address information for this location (up to 60 characters). For example, if the location receives mail at a P.O. Box, then you might enter the P.O. Box in the Shipping Address field above, and use this field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.

##  Location Group

 Specify the location group (from IN Location Groups) to which this location is associated. This group is used by Material Sales to set standard pricing, haul, and vendor payment rates. Will also be used by Bill of Materials to determine which locations will use the Bill of Materials when posting production of finished goods.

##  Cost Method

 Indicate which method will be used to control how costs are calculated to relieve inventory when materials are sold, produced, adjusted, or transferred from this location. If you set this option ‘No Override’, the company Cost Method will be used.
Note: Override is not allowed if the valuation method defined in IN Company Parameters is Standard Cost.

- 0-No Override

- 1-Average Cost

- 2-Last Cost

- 3-Standard Cost

Note: The Cost Method specified here will only be used if there is no override defined by location/category in IN Location Category Overrides.

##  Tax Code

 Enter the tax code (from HQ Tax Codes) to be used as a default when purchasing materials for, or selling materials to, this location.

##  Haul Tax Option

 Specify the tax option to use for haul charges.

- 0-Non Taxable – Haul charges are not taxable.

- 1-Taxable/Haul Vendor – Haul charges are only taxable when using an outside vendor to haul materials.

- 2-Taxable – Haul charges are always taxable, regardless of whether using company vehicle or outside haul vendor.

##  JC Co#

 Specify the Job Cost company to which this location will be linked for the purpose of tracking operational costs for a plant. This field is optional.
Note: If a Job Cost company is entered here, you must also specify the associated job.

##  Job

 Enter the job that will be used to track operational costs for a plant, and to which this location will be linked for reporting purposes. This link allows you to pull together job costs from JC with sales revenue tracked in Inventory.

##  EM Co#

 Specify the Equipment Management company to which this location will be linked for the purpose of tracking operational and/or maintenance costs for a plant.
Note: If an EM company is entered here, you must also specify the associated equipment.

##  Equipment

 Enter the equipment that will be used to track operational and/or maintenance costs for a plant, and to which this location will be linked for reporting purposes. This link allows you to pull together equipment costs from EM with sales revenue tracked in Inventory.

##  Receivable Type

 Enter the receivable type (from AR Receivable Types) to use when entering Material Sales invoices. The receivable type identifies the AR account that will be updated when selling materials to customers from this location.

##  CM Co#

 Optional field.
 Specify the CM company to use when auto applying payments in AR to cash sale invoices interfaced from MS. The company specified here overrides the default CM Co# assigned in AR Company Parameters; however, it will only be used if creating separate invoices by location (in MS).

##  CM Account

 Optional field.
 Specify the CM Account to use when auto applying payments in AR to cash sale invoices interfaced from MS. The account specified here will override the default CM Account assigned in AR Company Parameters; however, it will only be used if creating separate invoices by location (in MS).

##  MS Price Template

 Specify the pricing template (from MS Price Templates) for this location. This template will be used to default prices when selling materials to this location in Material Sales (Ticket Entry)

## Weight Option

Indicate in what unit of measure weight values entered on tickets in Material Sales will be expressed. The option selected here will be used when calculating a default value for units sold.

- Tons

- Lbs

- Kilograms

- None (Select this option if not entering weights.)

##  Inventory

 Enter the GL account that will be updated when materials are bought for or sold from this Inventory location. This account cannot be a Memo or Heading type account, and will be the primary asset account for stocked materials at this location.

##  Adjustments

 Enter the GL account that will be updated when posting manual, physical, or month-end reconciliation adjustments to materials at this location. This cannot be a Memo or Heading type account.

##  Cost of Goods

 Enter the GL account that will be used to track the costs of goods sold. This account is used to offset the credit to Inventory when materials are sold from this location. This cannot be a Memo or Heading type account.

## Cost Variance

Enter the GL account that will be used to
 record the difference between the standard and actual cost of a material when materials are
 posted to Inventory through PO receipts and/or AP invoices. It will also be updated when
 posting materials via MS Ticket Entry if you are using standard costing (that is, the
 Cost
 Method in IN Location Category Override or IN Company Parameters is
 3-Standard Cost).
Note: The account specified here cannot be a Memo or Heading account.

##  Misc Expense

 Enter the GL account for miscellaneous expenses; must be an active GL account with a subledger type of 'I' (Inventory) or null. Account entered here will override the Misc GL Account specified in IN Company Parameters.
 If not using burdened cost, this is the account that will be debited with miscellaneous amounts posted to this location in AP.
 If using burdened cost, and you enter freight amounts with the "Inc" flag set to N for the transaction, freight amounts will be credited to this account to offset the charge to inventory.

##  Tax Expense

 Enter the GL account that will be debited with tax amounts posted in AP.Cannot be a Memo or Heading type account. Account entered here will override the Tax GL Account specified in IN Company Parameters.

##  Cost of Production

 Enter the GL account that will be debited for the sum of the raw materials when finished goods are produced at this location (via IN Production Entry or MS Ticket Entry). This cannot be a Memo or Heading type account.

##  Value of Production

 Enter the GL account that will be credited with the value of finished goods produced at this location (via IN Production Entry or MS Ticket Entry). This cannot be a Memo or Heading type account.

##  Production Qty

 Enter the GL account that will be used to record units produced and sold at this location. Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Revenue: Customer Sales

 Enter the GL account used to record revenue when selling materials to customers from this location. If using intercompany invoicing (option in MS), the revenue from sales to other companies will also be credited to this account. This cannot be a Memo or Heading type account.

##  Revenue: Job Sales

 Enter the GL account used to record revenue when selling materials to jobs from this location. This cannot be a Memo or Heading type account.

##  Revenue: Inventory Sales

 Enter the GL account used to record revenue when selling materials to other Inventory locations from this location. This cannot be a Memo or Heading type account.

## Revenue: Equipment Sales

Enter the GL account used to record revenue when selling materials to equipment from this location. This cannot be a Memo or Heading type account, and the subledger code must be 'I-Inventory' or blank (Null).

## Revenue: Service Sales

Enter the GL account used to record revenue when selling materials to SM work orders from this location. This cannot be a Memo or Heading type account, and the subledger code must be 'I-Inventory' or blank (Null).

##  Quantity: Customer Sales

 Enter the GL account used to record units sold to a customer from this location. If using intercompany invoicing (option in MS), the units sold to other companies will also be credited to this account.Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Quantity: Job Sales

 Enter the GL account used to record units sold to a job from this location.Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Quantity: Inventory Sales

 Enter the GL account used to record units sold to another Inventory location from this location. This may include component materials used in production if their source location differs from the production location, and if the Usage Option (IN Company Parameters) is set to Sales.Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  AR Discount

 Enter the GL account used to record discounts taken when materials are sold from this location. If left blank, discounts taken will be posted to the Discount account assigned to the transaction’s specified receivable type (in AR Receivable Types).

## Haul - Own Equipment: Customer Sales

Enter the GL account to credit with haul revenue when materials sold to customers from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Haul - Own Equipment: Job Sales

Enter the GL account to credit with haul revenue when materials sold to jobs from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Haul - Own Equipment: Inventory Sales

Enter the GL account to credit with haul revenue when materials sold to other Inventory locations from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Haul - Outside Haulers: Customer Sales

Enter the GL account to credit with haul revenue when materials sold to customers from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Haul - Outside Haulers: Job Sales

Enter the GL account to credit with haul revenue when materials sold to jobs from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Haul - Outside Haulers: Inventory Sales

Enter the GL account to credit with haul revenue when materials sold to other Inventory locations from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Surcharge - Own Equipment: Customer Sales

Enter the GL account to credit with surcharge revenue when materials sold to customers from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Surcharge - Own Equipment: Job Sales

Enter the GL account to credit with surcharge revenue when materials sold to jobs from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Surcharge - Own Equipment: Inventory Sales

Enter the GL account to credit with surcharge revenue when materials sold to other Inventory locations from this location are delivered using your own equipment. This cannot be a Memo or Heading type account.

## Surcharge - Outside Haulers: Customer Sales

Enter the GL account to credit with surcharge revenue when materials sold to customers from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Surcharge - Outside Haulers: Job Sales

Enter the GL account to credit with surcharge revenue when materials sold to jobs from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Surcharge - Outside Haulers: Inventory Sales

Enter the GL account to credit with surcharge revenue when materials sold to other Inventory locations from this location are delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

## Haul - Own Equipment: Customer Sales

Enter the GL account to debit with haul expense when materials sold to customers from this location are delivered using your own equipment. This field offsets the equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the customer $50, $40 dollars will be debited to this account, and $50 will be credited to the Haul Revenue account for customer sales.
This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Haul - Own Equipment: Job Sales

Enter the GL account to debit with haul expense when materials sold to jobs from this location are delivered using your own equipment. This field offsets the equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the job $50, $40 dollars will be debited to this account, and $50 will be credited to the Haul Revenue account for job sales.
This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Haul - Own Equipment: Inventory Sales

Enter the GL account to debit with haul expense when materials sold to other Inventory locations from this location are delivered using your own equipment. This field offsets the equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the inventory location $50, $40 dollars will be debited to this account, and $50 will be credited to the Haul Revenue account for inventory sales.
This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Haul - Outside Haulers: Customer Sales

Enter the GL account to debit when an AP transaction is created for the haul expense of materials (sold to customers) delivered using an outside haul vendor. This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Haul - Outside Haulers: Job Sales

Enter the GL account to debit when an AP transaction is created for the haul expense of materials (sold to jobs) delivered using an outside haul vendor. This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Haul - Outside Haulers: Inventory Sales

Enter the GL account to debit when an AP transaction is created for the haul expense of materials (sold to other Inventory locations) delivered using an outside haul vendor. This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

## Material Expense: Customer Sales

Enter the GL account to debit when an AP transaction is created for the expense of purchased materials sold to a customer.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
This cannot be a Memo or Heading type account, and subledger type must be 'I' or null. Overrides may be set up by material category, company, or category/company.

##  Material Expense: Job Sales

 Enter the GL account to debit when an AP transaction is created for the expense of purchased materials sold to a job.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
 This cannot be a Memo or Heading type account, and subledger type must be 'I' or null. Overrides may be set up by material category, company, or category/company.

## Material Expense: Inventory Sales

Enter the GL account to debit when an AP transaction is created for the expense of purchased materials sold to inventory locations.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
This cannot be a Memo or Heading type account, and subledger type must be 'I' or null. Overrides may be set up by material category, company, or category/company.

## Surcharge Expense: Customer Sales

Enter the GL account to debit with expenses incurred when surcharges assessed on a ticket for materials sold to a customer and delivered using an outside hauler are partially or fully paid to the haul vendor. This account will be updated when processing haul vendor payments (in MS Haul Payment Worksheet) and only applies to surcharges referencing a pay code (in MS Surcharge Codes).
This cannot be a Memo or Heading type account, and subledger type must be null.

## Surcharge Expense: Job Sales

Enter the GL account to debit with expenses incurred when surcharges assessed on a ticket for materials sold to a job and delivered using an outside hauler are partially or fully paid to the haul vendor. This account will be updated when processing haul vendor payments (in MS Haul Payment Worksheet ) and only applies to surcharges referencing a pay code (in MS Surcharge Codes).
This cannot be a Memo or Heading type account, and subledger type must be null.

## Surcharge Expense: Inventory Sales

Enter the GL account to debit with expenses incurred when surcharges assessed on a ticket for materials sold to another inventory location and delivered using an outside hauler are partially or fully paid to the haul vendor. This account will be updated when processing haul vendor payments (in MS Haul Payment Worksheet) and only applies to surcharges referencing a pay code (in MS Surcharge Codes).
This cannot be a Memo or Heading type account, and subledger type must be null.

## Role

The Role field on the IN Locations form, Roles tab.
 Use this field to select a role. Press
 F4 to select one from a list. Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for more information about how roles work in the Process Workflow
 feature.
Roles are created and maintained using the
 [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form. You can launch this form by pressing
 F5
 in this field.

Related information

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## User Name

The User Name field on the IN Locations form, Roles tab.
 Use this field to select a user account. You
 can only select a user that is associated with the role selected in the Role field.
Roles are created and maintained using the HQ Roles form, and users are associated with roles using either of the following forms:

- Users tab on the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) form - You can access this form by pressing
 F5 in the Job
 Role field.

- Roles tab on the [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form - You can access this form by
 pressing F5 in the User Name field.

Related information

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Lead

The Lead checkbox on the IN Locations form, Roles tab.
Select this checkbox if this user is the lead for the selected role.
Currently the selection in this box has no affect on how which workflow is applied. This box is informational only.

Related information

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Active

The Active checkbox on the IN Locations form, Roles tab.
Select this checkbox to activate this role and user. The system will use this role/user when calculating workflows to apply to purchase orders that reference this location.
Deselect this checkbox to deactivate this role and user. The system will not use this role/user when calculating workflows for purchase orders.

Related information

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

## Notes

Use this field to enter notes on the role/user.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

Related information

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

##  Document Type

The Document Type drop-down on the IN Locations form, Workflows tab.
This field relates to the Process Workflow feature.
 Specify the type of document to which the workflow applies. Currently, PO-Purchase Order is the only option available.Note: You can have only one process for each document type.

 For more information about the workflow process, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the IN Locations form, Workflow tab.
Enter the workflow process to perform on purchase orders or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the PO-Purchase Order document type or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type. However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). You can assign these generic workflows to PO document types if applicable.

For more information about the workflow process, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Active

The Active checkbox on the IN Locations form, Workflow tab.
Check this box if the workflow should be applied when new POs are created.
This field applies to the Process Workflow feature. Click [here](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) for an overview.

## Notes

The Notes field on the IN Locations form, Workflow tab.
 Enter any notes about the workflow process.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
