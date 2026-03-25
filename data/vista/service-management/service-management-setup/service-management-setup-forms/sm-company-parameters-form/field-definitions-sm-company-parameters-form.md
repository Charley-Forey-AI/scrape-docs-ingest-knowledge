---
title: "Field Definitions: SM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form"
---

# Field Definitions: SM Company Parameters Form

The following is a list of field descriptions for the SM
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Agreement Mask

Agreement Mask field in SM Company Parameters, Info tab.
Enter the mask to use for selecting agreements to include when rebuilding the materials list for agreement services.

-  To update a selected agreement, enter the full agreement number (e.g. 21000).

- To update multiple agreements in the same number range, enter the number of characters to include, followed by the percent sign (%). For example, if you want to update all agreements that start with SM10, enter SM10%.

When you click the Rebuild button, the system will update the material lists for agreement services associated with the specified agreement(s) as follows:

- Updates with the current materials specified for the class maintenance task associated with the serviceable item referenced on the agreement service

- Updates with the current parts defined for the serviceable item (in SM Serviceable Items, Parts tab), where the part type matches the part type

Only agreements with a status of Active or Quote will be updated.
Note:You will typically only need to run the Rebuild before you begin using serviceable item parts, class maintenance, and/or PM work order parts syncing.

## Auto Generate Agreement Work Order Trips

Auto Generate Agreement Work Order Trips checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to automatically set up trips when generating work orders from agreements. The system will set up a single trip for each work order and assign the technician designated as the Primary Tech on the agreement service or the service site (if one is not assigned to the agreement service). No description, details, date, time, or duration will be defined for the trip.
Do not select this checkbox if you do not want trips set up automatically for work orders generated from agreements.

## Post Anticipated Costs to Job Cost

Post Anticipated Costs to Job Cost field on the SM Company Parameters form, Info tab.
This setting applies to work completed labor and purchased material lines on job work orders only.
Select this checkbox to post anticipated costs on a job work order to Job Cost. When capturing labor or purchased materials on a work order, the system will update the Proj Cost (anticipated cost) to Job Cost once you enter and save the work completed line. When the Actual Cost is updated for the work completed line from PR (Labor lines) or AP (Purchase lines), the system will then update Job Cost accordingly.
Clear this checkbox to post actual costs on a job work order to Job Cost. When capturing labor or purchased materials on a work order, no updates to Job Cost will occur when entering and saving the work completed lines. Instead, the system will update Job Cost once the actual costs are available. For payroll, this will be when payroll is processed. For purchased materials, this will be when the PO is invoiced in Accounts Payable.

## SM Co

SM Co field on the SM Company Parameters form.
Enter a valid company number (from HQ Company Setup) for Service Management processing.

## GL Co

GL Co field on the SM Company Parameters form, Info tab.
Enter the GL company (set up in GL Company Parameters) to update when processing transactions in this SM company. This company will also be used to validate GL accounts.

## AR Co

AR Co field on the SM Company Parameters form, Info tab.
Enter the AR company to update when billing work completed on work orders. In addition, this AR company's customer master will be linked to the customer master for this SM company; any customer set up in SM Customers must first exist in AR Customers for this AR company.

## AP Co

AP Co field on the SM Company Parameters form, Info tab,
Enter the AP company to update when entering/receiving purchase orders for SM work orders.
Note: Because AP and PO have a one-to-one relationship, the company specified here will also be your PO company; therefore, the PO company must be set up in PO Company Parameters.

## PR Co

PR Co field on the SM Company Parameters form, Info tab, Default Companies section.
Enter the PR company (set up in PR Company Parameters) for this SM company. This company will be used as the default PR company when setting up technicians (in SM Technicians); default may be overridden as necessary.

## IN Co

IN Co field on the SM Company Parameters form, Info tab.
Enter the IN company (set up in IN Company Parameters) for this SM company. This company will be used as the default IN company when capturing stocked materials on a work order (in SM Work Orders); default may be overridden as necessary.

## EM Co

EM Co field on the SM Company Parameters form, Info tab.
Enter the EM company (set up in EM Company Parameters) for this SM company. This company will be used as the default EM company when entering equipment on a work order (in SM Work Orders); default may be overridden as necessary.

## JC Co

JC Co field on the SM Company Parameters form, Info tab.
Enter the JC company (set up in JC Company Parameters) to update when capturing work completed (labor, equipment, materials, and miscellaneous) for a job-related SM work order.
Note: This company will also be used to validate cost types entered for work completed lines and SM purchase orders.

## Auto Post New Work Completed

Auto Post New Work Completed checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to have the system automatically create and process a cost posting batch when entering work completed in SM Work Orders (Work Completed tab). When you enter and save a work completed line, the system automatically creates the cost posting batch. Once you click Refresh or move off the work order, it will then automatically post the batch.
Do not select this checkbox if you want to manually create and process cost posting batches for new work completed lines. When you enter work completed for a work order, the system saves the work completed lines and sets their status to Provisional. You can then create and process cost posting batches for these lines using the SM Work Order Cost Posting form.
When this checkbox is not used:
There are specific circumstances in which the system ignores this checkbox. They are as follows:

- Work Completed Labor / Purchase lines - Costs for these lines are posted in other modules; therefore, the system will save the work completed line, but not create and post a batch. For work completed labor lines, costs will be posted when running PR Ledger Update. For work completed purchase lines, costs will be posted when invoicing the purchase orders in AP Transaction Entry.

- Imported / Auto-Added Work Completed lines - For imported lines, these will be added to a work order during the upload process in IM Upload. Auto-added lines are those added to a work order from miscellaneous requirements or standard charges (defined for a customer or service site). Imported and auto-added lines are flagged as Provisional and must be manually batched and processed using SM Work Order Cost Posting.

- Changing Posted Work Completed lines - If you change work completed lines that have already been batched and posted, the system will automatically create and post a batch for the changes, regardless of how you set this checkbox.

## Apply Standard Charges to Agreement Work Orders

Apply Standard Charges to Agreement Work Orders checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to add standard charges to work orders generated from an agreement (in SM Generate PM Work Orders). If you set up standard charges for customers and/or services sites (in SM Standard Charges), the system will generate a work completed miscellaneous line for each standard charge defined for the service site or customer associated with the agreement.
Do not select this checkbox if you do not want standard charges applied to work orders generated from agreements. Standard charges may still be applied manually on the Work Completed tab of SM Work Orders.

## Attach Batch Reports to HQ Batch Control

Attach Batch Reports to HQ Batch Control checkbox on the SM Company Parameters form, Info tab.
Select this checkbox (recommended) to have batch audit reports saved and attached to the batch record when a batch is posted. During batch processing, the system will export the related batch reports (except error reports) to a PDF file and attach them to the HQ Batch Control record. Reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options. You can retrieve the reports later using HQ Batch Control. For more information, see [Retrieving SM Batch Reports](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/about-attaching-sm-batch-reports-to-hq-batch-control/retrieve-sm-batch-reports).

- The system exports batch reports before posting the batch. If errors occur for any batch report, the system displays an error message and aborts the posting process. You will need to correct the error before you can re-validate and post the batch.

- If you secure audit reports, access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, only users with access will be able to access the batch reports. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

Do not select this checkbox if you do not want batch reports saved and attached to HQ Batch Control records.
Service Management batches are processed behind the scenes; that is, the batches are created and posted without ever exposing the batch processing form. For more information about batch processing as it relates to this option, see [Attaching Batch Reports to HQ Batch Control](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/about-attaching-sm-batch-reports-to-hq-batch-control).

## Default Agreement Number on Work Order Scopes

Default Agreement Number on Work Order Scopes checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to default the agreement number on manually entered customer work order scopes when the work order service site is included in Spot Coverage for a single active agreement (in SM Agreements, Spot Coverage tab). If the service site is included in Spot Coverage on multiple agreements, no agreement number will default on the work order scope; however, you can manually enter or select the agreement number.
Leave
 this checkbox unselected to have the Agreement field in SM Work Orders always
 default as blank.
Do not
 select this checkbox if you want the Agreement field in SM Work Orders to
 always default as blank on manually entered work order scopes, regardless of whether an
 agreement exists for the customer/service site.

## Next Work Order Number

Next Work Order Number field on the SM Company Parameters form, Info tab.
Enter the number with which to begin auto-numbering work orders. The system will automatically update this number each time you add a new work order using auto-numbering. You can change the number in this field at any time. The next time a work order is added, the system will check existing work order numbers, and if the specified number already exists, the system will skip to the next sequential number that is not already in use.
Entry in this field is not required. If left blank, the system will automatically assign work order numbers based on the highest existing number in the system.

## Use Review Process

The Use Review Process checkbox on the SM Company Parameters form, Info
 tab.
Use Review checkbox on the SM Company Parameters form, Info tab.
Defaults to unchecked.
Select this box to active the SM billing review process for Work Order Billing.
This Reviewer field appears in the following
 forms:

- SM Work Orders

- SM Service Sites

- SM Customers

- SM Service Center

- SM Divisions

Clear this checkbox to the standard billing method of billing all work completed lines when billing a work order.

## Show Customer/Site Attachments in Invoicing

The Show Customer/Site Attachments in Invoicing checkbox in SM Company Parameters, Info tab.
This checkbox works in conjunction with the Deliver To option for the customer in SM Customers as follows:

- If you select this checkbox and the Deliver To option is set to either AR Customer or Service Site, attachment types from both the customer and service site are shown. If the Deliver To option is set to None, no attachments will show.

- If you leave this checkbox unselected and the Deliver To option is set to AR Customer, only attachment types assigned to the Customer are shown. If the Deliver To option is set to Service Site, only attachment types assigned to the Service Site are shown. If the Deliver To option is set to None, no attachments are shown.

Once you process an invoice (in SM Invoice Review or SM Agreement Invoice Review), any applicable attachments associated with the customer and/or service site (depending on the settings described above) will display on the Attachments tab and can be selected for inclusion when delivering the invoice via email.
Applicable attachments are those matching the attachment types defined in SM Customer & Site Attch Types. For example, if you assign an attachment type of AP Invoice to the customer and service site (in SM Customer & Site Attch Types), invoices generated for the customer will include only attachments with a type of AP Invoice on the Attachments tab. Attachments assigned any other attachment type are not included.

Note: If the Bill To customer on the work order scope differs from the customer on the work order header, the system includes all applicable attachments from the bill to customer. However, it uses the Include Attachments settings for the work order customer to determine the attachments to include; the Include Attachments settings for the bill to customer are ignored.

## Auto Close Work Order on Final Bill

Auto Close Work Order on Final Bill checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to have the WO billing process automatically close the work order when fully billed.
When you select this checkbox, the Prevent Scope Auto Close when Billing checkboxes in SM Call Types and in SM Work Scopes are enabled, allowing you to prevent work order scopes referencing the call type or work scope from being auto-closed when fully billed.
Leave this checkbox unselected if you do not want work orders automatically closed when fully billed. If you do not select this checkbox, the Prevent Scope Auto Close when Billing checkboxes in both SM Call Types and SM Work Scopes are cleared and disabled.

## Auto Delete Open Trips

Auto Delete Open Trips checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to automatically delete open trips when closing work
 orders on final billing or from the SM Work Order Close form.

## Use Closest Open Month

Use Closest Open Month checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to use the closest open month for closing entries when
 closing work orders on final billing of from the SM Work Order Close form.

## Credit Hold

Credit Hold drop-down list on the SM Company
 Parameters form, Info tab.

Select for soft or hard credit hold:

- S - Soft Credit Hold - (default) Select this option to alert users that
 they are on credit hold

- H - Hard Credit Hold - Select this
 option to prohibit users on credit hold from creating new work orders, and work
 orders cannot be imported

## Recognize Revenue as Costs Incurred

The Recognize Revenue as Costs Incurred checkbox on the SM Company Parameters form, Info tab.
Select this checkbox to have revenue recognized as costs are incurred when posting customer and agreement work orders.
If you leave this checkbox unselected, work order/agreement revenue will be recognized during the billing process.

## Minimum WO Quote ID

Minimum WO Quote ID field on the SM Company Parameters form, Info tab.
Enter the number with which to begin auto-numbering work order quote IDs (e.g. 100). The system will automatically update this number each time you add a new work order quote. However, if you override a system-generated quote number, it will not update this field.
If you leave this field blank, the system will automatically start with '0'. If you do not want to use 0 as a quote ID, make sure you enter a number here.
Note: You can change the starting quote number at any time. The next time you add a work order quote, the system will check existing quote numbers and use the next sequential number that is not already in use.

## Default Use Tax on Purchases

Default Use Tax on Purchases checkbox under the Tax Options section of the SM Company Parameters form Info tab.
This checkbox controls use tax defaulting on material-related miscellaneous and purchase work completed lines once you post an AP invoice or purchase order.
Select this checkbox to default use tax on material-related miscellaneous and purchase work completed lines when posting AP invoices or purchase orders. If you post an invoice or purchase order that does not include tax, but the work order scope is set up to allow use tax, use tax will default for the generated work completed miscellaneous or purchase line. If the work order is not set up for use tax, no use tax will default on the work completed line.
Clear this checkbox if you do not want to default use tax on material-related miscellaneous and purchase work completed lines when posting AP invoices or purchase orders. Use tax will only default for work completed if you specify Use tax on the invoice or purchase order and you have set up the work completed line to allow use tax.

## Default Trip Duration

Default Trip Duration field on the SM Company Parameters form, Info tab.
Enter the number of hours to use as a default when creating trips in SM Dispatch Board using the drag and drop functionality. May be overridden in SM Trips or by grabbing the left or right side of the trip icon on the Dispatch Board and dragging it to the desired time.
If you leave this field blank, the default duration will be 1 hour.

## Default Receivable Type

Default Receivable Type on the SM Company Parameters form, Info tab.
Enter the receivable type to use when billing
 work orders for this SM company. Press F4 for a list of valid receivable
 types.
The system will assign this receivable type to all invoices created via SM Work Orders, SM Agreement Billings Due, or SM Work Order Billing. If you leave this field blank, the system will use the receivable type assigned to the invoice's Bill To customer (in AR Customers) or the receivable type defined in AR Company Parameters (if no receivable type is defined for the Bill To customer).

## Default WO Invoice Report

Default WO Invoice Report field on the SM Company Parameters form, Info tab.
Enter the custom invoice report ID to use when
 printing work order invoices for this SM company. Press F4 for a list
 of valid custom invoice report IDs.
The system will assign this report ID to all
 work order invoices created via SM Work Orders or SM Work Order Billing. You can override
 this default by customer (in the Custom Invoice Report field of SM
 Customers) or by service site ( in the Custom Invoice Report field of SM Service
 Sites).
Leave this field blank to use the standard SM Invoice report.
Note: The system will only use the invoice report specified here if no overrides are defined at the customer or service site levels.

## Def. Agreement Inv. Report

Def. Agreement Inv. Report field on the SM Company Parameters form, Info tab.
Enter the custom invoice report ID to use when
 printing agreement invoices for this SM company. Press F4 for a list of valid custom invoice
 report IDs.
The system will assign this report ID to all
 agreement invoices created via SM Agreement Billings Due. You can override this default by
 specifying a report ID in the Invoice Format field of SM Agreements.
Leave this field blank to use the standard SM Agreement Invoice report.
Note: The system will only use the invoice report specified here if no overrides are defined at the agreement level.

## Generate Agreement WO Time

The Generate Agreement WO Time field on the SM Company Parameters form, Info tab.
If you want to schedule agreement work order process runs for a specific time (such as outside normal work hours), enter the time (in 24-hour format). For example, to run the work order process at 6:00 p.m., enter 18:00.
 At the scheduled time, the system checks to see if there are work order process requests in the queue (shown in SM Generate Work Order Summary). If there are, the system begins the process starting with the earliest request and continuing with the remaining requests in the order they were requested (based on the Requested Time).
Leave this field blank to have the system process work order runs as soon as they are requested. As with scheduled runs, the system first checks to see if there are requests already in the queue. If not, the system begins the process for the new request one minute after it is requested. If there are requests already in the queue, the system will run the new request as soon as it has completed all previous requests.
Note: You can see the status of work order process requests in the upper grid of the SM Generate Work Order Summary form.

## Audit Options

Audit Options section on the SM Company Parameters form, Info tab.
Audit options control updates to the HQ Master Audit (HQMA) file when changes are made in the company and/or account files.
The HQMA file stores audit information for all modules on the system. When you elect to track changes to any of the files specified in the company file, HQMA will store updated information, including who made the changes and the date and time that the changes were made. If you want to access any of this information, you can create reports that reference the HQMA file.

- Company Parameters – This audit option is disabled and is always checked. Any changes made to the company information in SM Company Parameters will be tracked in the Master Audit file.

- Company Settings - Check this box to record additions, changes, and deletions made in SM Call Types, SM Cost Types, SM Labor Codes, SM Part Types, SM Pay Types, SM Serviceable Item Class, and SMTypes (Types tab in SM Serviceable Item Class).

- Service Centers - Check this box to record additions, changes, and deletions made in SM Service Centers and SM Divisions.

- Technicians - Check this box to record additions, changes, and deletions made in SM Technicians and SM Technician Preferences.

- Rate Templates - Check this box to record additions, changes, and deletions made in SM Rate Templates, SM Advanced Labor Overrides, SM Rate Equipment Overrides, SM Rate Override Base, SM Rate Override Material, SM RO Material Breakpoint, SM Rate Template Effective Dates, SM Override Category Material, SM RO Cat Matl Rate Breakpoint, and SM Standard Item Overrides.

- Departments -Check this box to record additions, changes, and deletions made in SM Departments and SM Department Overrides.

- Work Scopes - Check this box to record additions, changes, and deletions made in SM Work Scopes.

- Standard Tasks - Check this box to record additions, changes, and deletions made in SM Standard Task.

- Standard Items - Check this box to record additions, changes, and deletions made in SM Standard Items and SM Standard Charges.

- Customers - Check this box to record additions, changes, and deletions made in SM Customers, SM Customer Contact, SM Service Sites, SM Serviceable Items, SM Serviceable Item Parts, SM Service Site Contacts, and SM Invoice Review.

- Work Orders - Check this box to record additions, changes, and deletions made in SM Work Orders, SM Work Order Scopes, SM Trips, and SM Work Completed.

- Agreements - Check this box to record additions, changes, and deletions made in SM Agreements, SM Service, SM Work Schedule Tasks, SM Agreement Billing Schedule, and SM Work Order Scope Tasks.

- Work Order Quotes - Check this box to record additions, changes, and deletions made in SM Work Orders Quotes.

- Calls - Check this box to record additions, changes, and deletions made in SM Call Handler.

## Work Order Invoices

Work Order Invoices checkbox on the SM Company Parameters form, Default Invoice Print Options section of Info tab.
This checkbox defaults as selected.
Leave this checkbox selected to always
 default the Print
 Invoice checkbox in SM Invoice Review as selected. You will typically use
 this default setting if you want to automatically print work order invoices once they are
 posted.
Clear this checkbox to always default the
 Print
 Invoice checkbox in SM Invoice Review as unselected. You will typically use
 this default setting if you do not want work order invoices printed automatically once they
 are posted.
Note: You may override the default in SM Invoice Review as needed prior to posting an invoice batch.

## Agreement Invoices

Agreement Invoices checkbox on the SM Company Parameters form, Info tab.
This checkbox defaults as selected.
Leave this checkbox selected to always
 default the Print
 Invoice checkbox in SM Agreement Invoice Review as selected. You will
 typically use this default setting if you want to automatically print agreement invoices
 once they are posted.
Clear this checkbox to always default the
 Print
 Invoice checkbox in SM Agreement Invoice Review as unselected. You will
 typically use this default setting if you do not want agreement invoices printed
 automatically once they are posted.
Note: You may override the default in SM Agreement Invoice Review as needed prior to posting an invoice batch.

## Agreement Sync Options

The Agreement Sync Options section on the SM Company Parameters form, Info tab.
The Agreement Sync options are only applicable if you are using the Tasking feature to generate agreement services. They control whether the system automatically updates agreement services and/or preventative maintenance work orders (those generated from agreements) when making changes to serviceable item parts and/or class maintenance tasks. For more information about the Tasking feature, see [Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking).
Service Item Parts SyncSelect this checkbox to have the system automatically update corresponding material entries for Active or Quote agreement services when changes are made to serviceable item parts in SM Serviceable Items. Update will only occur if the agreement service and serviceable item part types match.
 For example, you have a serviceable item of FURNACE with a parts entry that is assigned a Part Type of 'Filter' and Material of 'AF100'. The serviceable item is associated with an agreement service that you generated from a class maintenance task. The agreement service has a material entry referencing part type 'Filter' and Material 'AF100'. You then change the material for the serviceable item (in SM Serviceable Items) to 'AF6500'. When you save the change, the system updates the agreement service material to 'AF6500'.
Class Maintenance SyncSelect this checkbox to have the system automatically update Active or Quote agreement services when making additions, deletions, or changes to the tasks, equipment, labor, and/or materials for a class maintenance (in SM Class Maintenance).
 If you add a labor, equipment, or material requirement, the system will add a corresponding requirement entry to each agreement service associated with the class maintenance. If you add a new task requirement, the system only adds it to the Tasks list in SM Agreement Maintenance. You will need to select the new task in SM Agreement Maintenance to add it to the Tasks tab for the agreement service.
 If you delete or change an existing class maintenance requirement, the agreement service requirement will only be updated if it matches the requirement being changed or deleted on the class maintenance.
For example, say you have a class maintenance for which you have set up a required labor entry with a Craft of 'Electrician' and a Class of 'Jrny 1'. The class maintenance is associated with multiple agreement services. You then change the Class for the class maintenance labor entry to 'Jrny 2'. When you save the change, the system looks for labor entries on the associated agreement services where the Craft is 'Electrician' and Class is 'Jrny 1', and updates them to show the new class (Jrny 2).
PM Work Order Parts SyncSelect this checkbox to have the system automatically update corresponding material entries for work order scopes when making changes to associated serviceable item parts (in SM Serviceable Items).
For example, you have a serviceable item of FURNACE with a parts entry that is assigned a Part Type of 'Filter' and Material of 'AF100'. The serviceable item is referenced on a work order scope that is associated with an agreement service generated from a class maintenance task (using the Tasking feature). You then change the material for the serviceable item (in SM Serviceable Items) to 'AF6500'. When you save the change, the system updates the material for the related work order scope to 'AF6500'.
Do not select this checkbox if you do not want to automatically update related material entries on work order scopes when making changes to related serviceable item parts.
Agreement MaskYou will only need to enter a value in this field if you want to rebuild the material lists for agreement services before you begin using serviceable item parts, class maintenance, and/or PM work order parts syncing.
Enter the mask to use for selecting agreements to include when rebuilding the materials list for agreement services.

-  To update a selected agreement, enter the full agreement number (e.g. 21000).

- To update multiple agreements in the same number range, enter the number of characters to include, followed by the percent sign (%). For example, if you want to update all agreements that start with SM10, enter SM10%.

- To update all agreements, enter %.

To initiate the rebuild process, click the Rebuild button. The system will update the material lists for agreement services on the specified agreement(s) with the current material lists for all associated class maintenance and serviceable item parts. Agreements must have a status of Active or Quote; those with a status of Terminated or Expired will be ignored.

## Auto-Number

Auto-Number section on the SM Company Parameters form, Info tab.
The Auto-Number options are applicable if you are using the SM Service Sites, SM Serviceable Items, or the SM Serviceable Item Parts forms, and you want the next sequential number auto-generated when you create a new service site, serviceable item, or serviceable item part.
By leaving these checkboxes unchecked (their default), the next sequential number will not be automatically generated when you create a new service site, serviceable item, or serviceable item part.

- Service Sites - Select this checkbox to have the system generate service site number based on the next sequential number available.

- Serviceable Items - Select this checkbox to have the system generate a serviceable item number based on the next sequential number available.

- Serviceable Item Parts - Select this checkbox to have the system generate a serviceable item part number based on the next sequential number available.

## GL Usage Interface

GL Usage Interface section on the SM Company Parameters form, Interfaces tab.
Select one of the options below to indicate how GL is to be updated when posting work completed miscellaneous lines (type 3-Misc) in SM Batches/SM Batch Process.

- No Update - No GL update will occur.
Note: If you select this option, the system will still create the batch reports with the same information that would be included if you were updating GL.

- Summary - Enter Description text directly (max 60 char) - Work completed miscellaneous entries will be summarized and one entry posted to GL for each unique Cost and WIP account (as defined in SM Departments). Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the GL Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail- Select from following options: - Create GL transactions for every work completed miscellaneous entry. If you select this option, use the selection box below to indicate which fields you want included in the GL transaction description. Available fields are:

- SM Company

- Work Order

- Scope

- Line Type

- Line Sequence

As you select each field, it is added to the Detail GL Description field. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: The GL transaction description appears in the same order as the order in which these fields are selected.

## Summary GL Description

Summary GL Description field on the SM Company Parameters form, Interface tab.
This field is enabled when the GL Usage Interface option is Summary.
Enter a summary description to be used when interfacing work completed miscellaneous information to GL. Up to 60 characters allowed.

## Journal

Journal field on the SM Company Parameters form, Interfaces tab.
Enter the journal (from GL Journals) to update when posting miscellaneous work completed lines (via SM Batch Processing).

## Other Interfaces: EM

EM checkbox on the SM Company Parameters form, Interfaces tab.
Select this checkbox to interface equipment usage to the Equipment Management (EM) module when capturing equipment on an SM work order. When a work completed equipment line is entered and saved (in SM Work Orders, Work Completed tab), the system will create and post an equipment usage batch to update the usage to EM. In addition, the system will update the appropriate Cost and WIP GL accounts (defined in SM Departments). The level of update to GL will be based on the GL Usage Interface level specified in EM Company Parameters for the SM company's assigned EM company.
Note: Equipment usage and General Ledger updates will also occur each time you modify or delete a work completed equipment line.
Do not select this checkbox if equipment usage will not be interfaced to EM when capturing equipment on an SM work order. When adding, modifying, or deleting work completed equipment lines, the system will not update equipment usage to EM, nor will any GL updates occur.
Important: Typically, you will only leave this checkbox unselected if you do not have the EM module or during implementation to prevent duplication of data.

## Other Interfaces: IN

The IN checkbox on the SM Company Parameters form, Interfaces tab.
Select this checkbox to update material use to the Inventory (IN) module when capturing materials pulled from inventory on an SM work order. When you enter a work completed inventory line for a stocked material, the system creates an inventory batch. Once the batch is posted (whether automatically or manually), the system relieves inventory for the specified IN Co and Location. The system will also update the appropriate GL accounts (as defined in SM Departments) based on the GL Adjustment Interface level specified in IN Company Parameters.
Do not select this checkbox if you are not updating material usage to the Inventory module when capturing stocked materials on an SM work order. When you add, modify, or delete work completed inventory lines for a stocked material, the system will not update GL, nor will it relieve on-hand amounts for the specified IN Co and Location.
Note: You will typically only leave this checkbox unselected if you do not have the IN module or to prevent duplication of data during implementation.

### Interface to Inventory

If you selected to interface material usage to
 Inventory (the IN interface box is checked in SM Company Parameters), upon saving a work
 completed inventory line, the system will automatically create and post a material usage
 batch and update Inventory as applicable. If you make any changes to the material line, the
 system will automatically create and post adjusting entries in IN.
If you did not select to interface material
 usage (the IN interface box is not checked in SM Company Parameters), upon saving the
 material line, the system will the system will create and post a batch, but no update to
 Inventory will occur.

## Other Interfaces: PR

AR Co field on the SM Company Parameters form, Info tab.
Select this checkbox to interface labor hours to the Payroll module when capturing labor on an SM work order. When you save a work completed labor line in SM Work Orders (Work Completed tab), the system will automatically generate a timesheet record (in PR My Timesheet) for the specified employee. You can edit the labor record via the timesheet or work completed line until you approve the timesheet and send it to a timecard batch. At that point, you can only make changes to the work completed line in PR Timecard Entry.
Do not select this checkbox if labor hours captured on an SM work order will not be interfaced to PR. The system will not generate timesheet entries when entering and saving work completed labor lines on an SM work order.
Note: Labor entries added directly in PR My Timesheets or PR Timecard Entry will generate work completed labor lines in SM for the specified work order, regardless of how you set this checkbox. In addition, edits to the timesheet or timecard will update the corresponding labor entries in SM. However, if this checkbox is not selected, updates to the work completed line will not update the timesheet or timecard.

## Other Interfaces: JC

JC checkbox on the SM Company Parameters form, Interface tab.
Select this checkbox to interface costs to Job Cost when capturing work completed on a job-related SM work order. When you enter and save a work completed line in SM Work Orders (Work Completed tab), the system will automatically update the costs to Job Cost.
 In addition, the system will update the appropriate Cost and WIP GL accounts (defined in SM Departments). The level of update to GL will be based on the GL Cost Interface level specified in JC Company Parameters for the SM company's JC company. The GL accounts updated will come from JC Departments based on the phase/cost type specified on the work order. For more information about the updates to GL, see Updates to GL.
Note: The system will only update actual costs to Job Cost. When capturing labor and purchased materials on a job work order, actual costs are not initially available. For work completed labor lines, the system will update Job Cost once payroll is processed and the actual costs are available. For work completed purchase lines, the system will update Job Cost once the PO is invoiced in AP Transaction Entry. 
Do not select this checkbox if costs will not be interfaced to Job Cost when capturing work completed on a job-related SM work order.

## From Address

From Address field on the SM Company Parameters form, Email Settings tab.
Enter the from address, up to 60 characters. This will typically be the reply address.

## Subject

Subject field on the SM Company Parameters form, Email Settings tab.
Enter the text that should appear in the Subject line of the email. Up to 60 characters allowed.

## Body

Body field on the SM Company Parameters form, Email Settings tab.
Enter the text that will appear in the body of the email, up to 255 characters, using Ctrl + Enter to move to the next line in your text.
 To apply carriage returns and formatting to your email text (e.g. bold, italics, etc.), use HTML tags.
For example, say you want the body text to read as follows:
Dear Customer,
Please find attached, a copy of the invoice for the service work you requested. If you have any questions, please call Account Services at ###-###-####.

Sincerely,
John Smith
You might enter it like this:
<p>Please find attached, a copy of the invoice for the service work you requested. If you have any questions, please call Account Services at <b>###-###-####.</b></p> <p></p> <p>SIncerely,</p> <p></p> <p>John Smith</p>
