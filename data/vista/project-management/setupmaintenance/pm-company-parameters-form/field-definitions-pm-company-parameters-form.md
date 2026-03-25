---
title: "Field Definitions: PM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form"
---

# Field Definitions: PM Company Parameters Form

The following is a list of field descriptions for the PR
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PM Company

 Enter the PM Company in which processing will occur. Must be a valid company set up in HQ Companies.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  AP In Use

 Check this box if the Accounts Payable module is currently in use.
 Leave this box unchecked if you are not using the AP module.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  AP Co#

 Indicate the AP company to be updated when the PM interface is run. This AP company is also used to validate vendors.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  SL In Use

 Check this if the Subcontract Ledger module is currently in use. The SL company updated by PM will be the same as the AP company you specified above.
 Leave this box unchecked if you are not using SL.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## PO In Use

Check this box if the Purchase Orders module is currently in use. The PO company updated by PM will be the same as the AP company you specified above.
Leave this box unchecked if you are not using PO.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## PO Requisitions In Use

Check this box if using the Requisitions feature in the Purchase Order module.
Note:Checking this box enables the ‘R-Requisition’ option in the Material Type column (Non-Interfaced tab).

Leave this box unchecked if you are not using the Requisitions feature in the Purchase Order module.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  IN In Use

 Check this if the Inventory module is currently in use.
 Leave this box unchecked if you are not using IN.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  IN Co#

 Specify the Inventory company to be updated by the PM interface. Also used to validate inventory locations and materials by location.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  MS In Use

 Check this if the Material Sales module is currently in use.
 Leave this box unchecked if you are not using MS.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  MS Co#

 Specify the Material Sales company to be updated by the [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) form.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  PR In Use

 Check this if the Payroll module is currently in use.
 Leave this box unchecked if you are not using PR.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  PR Co#

 Specify the Payroll company to use for employee validation. This is the payroll company that will be used when initializing contacts for "Our Firm" (in PM Firm Contacts).
Note:All other PR company related fields and/or defaults throughout PM will use the JC company's PR company.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  EM In Use

 Check this if the Equipment Management module is currently in use.
 Leave this box unchecked if you are not using EM.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## EM Co#

Enter the EM company to be updated by the PM
 interface or press F4 to select it from a list.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Our Firm #

 Enter the PM module firm number that
 represents your company or press F4 to select it from a list.
Firms are created and maintained using the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Default Beginning Status

Enter the status code that should be used as the default status when creating new pending change orders, pending change order items, submittals, change order requests(CORs), and other records in the application. You can also press F4 to select a status from a list.
Note:The status selected in this field is only the default. It can be changed if it does not apply when the records are created. If you leave this field blank, it will default to the first Beginning Status Code for whichever document type is in use.

Status codes are created and maintained using [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form). You can press F5 while in this field to open PM Status IDs.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Default Final Status

Enter the status code that will be used as the default final status when:

-  Approving pending change order items using [PM Change Order Approval](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form)

- Adding approved change order items using [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form)

Status IDs are created and maintained using [PM Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form).
Note:Only status codes with a code type of Final can be
 selected. If you have categorized status codes by document category in PM Status Codes,
 you can only select a status code with the Active for All Forms box checked, or
 status codes that have the Active for All Forms box unchecked and
 are assigned a Document Category of PCO.

This field is also used by the [PM Subcontract Change Orders](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form) and [PM PO Change Orders ](/en/vista/vista/project-management/materials/pm-po-change-orders-form) forms. Click [here](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form/field-definitions-pm-subcontract-change-orders-form#ID-0002d559--en) for information about SubCOs, and click [here](/en/vista/vista/project-management/materials/pm-po-change-orders-form/field-definitions-pm-po-change-orders-form#ID-0002aafa--en) for information about POCOs.
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Default RFI Beginning Status

Enter the status that should be used as the default status when creating new RFIs. The status selected in this field is only the default and it can be changed if it does not apply when the RFI is created. You can only select a status that is associated with the RFI document type and is set up as a beginning status. Press F4 to select a status from a list.
Status codes are created and maintained using
 [PM
 Status IDs](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form). A status code is associated with the RFI document type by unchecking
 the Active for All
 Forms box and then selecting RFI in the Document Category field. You can press F5
 while in this field to open PM Status IDs.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Submittal Days for Review Responsible Firm / Approving Firm / Requesting Firm

Enter the default number of review days for each party that is involved in the submittal process. This allows you to set the default submittal schedule.
When a new project is created, the values entered in these fields will populate on the PM Info tab of the [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) form.
Click [here](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-submittals) for an overview of submittal schedules.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Document Tracking View

Enter the default document tracking view for this PM company. Must be a valid view set up in PM Document Tracking Views. This view will be used each time you access the PM Document Tracking form, and will determine the document tabs and columns displayed. Default view may be overridden via the Change Document Tracking View option in PM Document Tracking (Options menu).
Note: If this field is left blank, the standard document tracking view will be used.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Fax Server Name

Enter the fax server name to use for distributing documents or correspondence using the Fax via Server option in PM Document Create and Send. For example, enter ‘faxmaker.com’ for GFI Fax. The fax server name specified here will be used in conjunction with the fax number to create the fax address (e.g. 1234567890@faxmaker.com).

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Default VFE Estimate Template

Default VFE Estimate Template field in the PM Company Parameters form
Applies to users of MEP Estimating and PC Estimating only.
Use this field to indicate the default PM
 Import template that will be used by the automated estimating import. This can be
 overridden when doing the import but will default to this selection so that step is not
 required. Press F4 to select from a list of valid templates.

Related information

- [About the PM VFE Auto Import Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-vfe-auto-import-form)

- [Auto Importing Estimates from Third-Party Applications](/en/vista/vista/project-management/import-project-estimates/auto-importing-estimates-from-third-party-applications)

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Allow Update from AP

Check
 this box if changes made in the PM Firms form should update the AP Vendors form. This
 only applies to firms that are associated with an AP vendor using the Vendor  field
 on the [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) form.
When changes are made to a vendor in AP Vendors, a
 message will appear. Click Yes  and the PM firm is updated. Click
 No
 and you will have to manually update the PM firm.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form) for more information.
Note: If you check this box, generally you should also
 check the Allow Add
 from PM  and Allow Update from AP  boxes on the Audit
 Options tab of AP Company Parameters. This will ensure that records are kept in
 sync.
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Lock down ACO Items after Interface

Two things occur when this box is checked:

- An ACO item cannot be edited in [PM Approved Change Orders](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form) after it has been interfaced (PM Interface).

- You cannot create new items on an ACO that has been interfaced using the PM Approved Change Orders form.
Why would you check this box?

When a PM module change order is interfaced ([PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form)), a record is created in [JC Change Orders ](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-change-orders-form). If you change an interfaced ACO item using [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form), this change does not automatically update the record in JC Change Orders, which means the accounting data and PM module data will be out of sync. You will have to run PM Interface again to update the record in JC Change Orders and bring the PM module and accounting back in sync.
If you check the Lock Down ACO Items after
 Interface box, the Info tab in the details section of PM Approved Change Orders will be disabled on all ACO items that have been interfaced. This means that users will not be able to change interfaced ACO items and the PM module and accounting data will stay in sync.
What if this box is checked and you need to change an interfaced ACO?
If you check the Lock Down ACO Items after
 Interface box and need to change the amounts on an interfaced ACO, you can create a new ACO.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Using Review Workflow Notifier Queries

The Using Review Workflow Notifier Queries checkbox on the PM Company Parameters form, Info tab.

This checkbox is for use with the PO/SL Process Workflow feature.
Select this checkbox to suppress the standard system notifications sent during the PO/SL review/approval workflow process. You should only select this checkbox if you are using Notifier queries to send review/approval workflow notifications.
Note: If you select this checkbox and are not using Notifier queries for review/approval notifications, no notifications will be sent to reviewers/approvers or submitters during the review/approval workflow process.

If you leave this checkbox unselected and you are using Notifier queries to send review/approval workflow notifications, reviewers/approvers and submitters will receive the standard system notifications, along with the notifications sent via the Notifier queries.
In order to send notifications using Notifier queries, you must [set up Notifier jobs](/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job) (in WF Notifier Job Manager) and associate them with the queries listed below.

- PMDocumentApprovalList - Notifier jobs using this query will send email notifications to approvers with a list of all purchase orders, pending purchase orders, and/or subcontracts submitted for approval that they are assigned to review/approve.

- PMReviewedDocumentList - Notifier jobs using this query will send email notifications to submitters with a list of purchase orders, pending purchase orders, and/or subcontracts that have been approved, rejected, or are still waiting review/approval.

For more information about using review notifier queries, see [Use Notifier Queries for Workflow Notifications](/en/vista/vista/project-management/setupmaintenance/use-notifier-queries-for-workflow-notifications).

##  Default SL Item Description from Phase Description

 Check this box if the phase description will be used as the default description for subcontract items.
 Leave this box unchecked if you do not want the phase description used as the default when creating subcontract items. Instead, the description for the contract item to which the phase is assigned will be used.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  SL Cost Type 1/2

 Enter the cost types that will be associated with subcontracts. SL Cost Type 1 will be used as the default cost type when entering subcontract detail in PM Subcontract Detail.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Auto-Add Cost Type From Subcontract

Specify how to handle the addition of new phases/cost types when entering subcontracts.

- No - Do not allow addition of new
 phases/cost types. Phases and cost types must first be set up for the project in PM
 Project Phases.

- With Estimates - Allow adding new
 phases/cost types, and automatically update project detail and original estimate.

- With No Estimates - Allow adding
 new phases/cost types and automatically update project detail, but do not update
 original estimate.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Create single Subcontract Change Orders per Vendor when generating
 ACOs

This box determines the default value of the
 Create a single
 Sub Change Order per Vendor box on the [PM Approve
 PCOs](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form) form.
When this box is checked, by default the
 Create a single
 Sub Change Order per Vendor box will also be checked when the PM Approve
 PCOs form is opened.
Click [here](/en/vista/vista/project-management/change-orders/about-the-pm-approve-pcos-form/field-definitions-pm-approve-pcos-form#ID-0005b12c--en) for more information about the Create a single Sub Change
 Order per Vendor box.
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Allow adding new subcontract item during subcontract change order
 entry

This option is intended for Australian customers, and it allows pre-billing of subcontract change orders. Generally US and Canadian customers will not check this box.
Check this box if users should be able to add
 new subcontract items to existing subcontracts in [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form). When the subcontract is added, the
 system enters the item with 0.00 values. This allows you to invoice
 against the item, even before it has been interfaced to SL.
In order to enter a new item, you must be
 assigning detail to a pending or approved change order, the subcontract must have a status
 of Open, the subcontract type must be 1-Regular or 2-Change Order,
 and the item must not exist.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Disable Initialize button for change order subcontract detail

Check this box if the Initialize
 button on [PM Subcontract Detail](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form) should be disabled when entering
 "Change" subcontract item types. This means that users will be forced to manually select an
 existing subcontract and subcontract item using the SL and SL Item field
 rather than being able to create a new subcontract.
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  Copy PCO Detail Notes to Subcontract CO Header

Appears on the Subcontract Parameters tab of the Company Parameters form.
Check to copy PCO Detail Notes to Subcontract Header.

Related information

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

- [About the Add Items to Approved MOs/POs Options](/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options)

- [Copy PCO Detail Notes to Purchase Order CO Header](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023b5b--en)

## SL Number Type

Indicate the format to use for subcontract numbers.

- Project/Sequence – Select this option to use a specified number of characters of the project and a sequence number to generate the subcontract number.

- Project/Vendor – Select this option to use a specified number of characters of the project and vendor numbers to generate the subcontract number.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Significant Part of SL Job

Check this box to use the significant part of job characters for validation when initializing subcontracts in PM (Subcontract Detail). When checked, the system will validate the job number specified for the subcontract detail line and if the number matches the Significant SL Job Characters (specified below) for any job on an existing subcontract, the subcontract detail line will be added as an item on the existing subcontract (provided the vendors are the same). If the significant characters do not match or the vendor differs, a new subcontract number will be generated for the subcontract detail line.
Uncheck this box to validate the entire job number when initializing subcontracts. If job matches in its entirety to any job on an existing subcontract and the vendors are the same, it will be added as an item on that subcontract. If it does not match or the vendors differ, a new subcontract number will be generated for the subcontract line.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Significant SL Job Characters

This field is only used when the Significant Part of
 SL Job box (above) is checked.
Indicate the number of job characters (1-10) to use for validation when initializing subcontract numbers. During subcontract initialization, if a project number matches the number of characters specified here for any project/job on an existing subcontract, the subcontract detail line will be added as an item on the existing subcontract (provided the vendors are the same). If the significant characters do not match or the vendor differs, a new subcontract number will be generated for the subcontract detail line.
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## SL Project Characters

Enter the project number characters that should be included in the subcontract number. The system will use numbers beginning from left to right, and any dashes included in the project number will be included in the subcontract number.
This field cannot be greater than 10.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Maximum of 30 characters
The subcontract number cannot exceed 30
 characters, that is, the sum of the SL Project Characters and SL Sequence
 Characters fields must be 30 or less.
Defining Subcontract/PO/MO Numbers
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## SL Sequence Characters

Enter the number of sequence characters that should be included in the subcontract number. The system will use zeros to fill in unused characters. For example, if you specify 10 characters and the sequence number is 11, the resulting number will be 0000000011.
 This field is only enabled when
 Project/Sequenceis selected in the SL Number Type field.
 Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Maximum of 30 characters
The subcontract number cannot exceed 30
 characters. That means that the sum of the SL Project Characters and SL Sequence
 Characters fields must be 30 or less.
Defining Subcontract/PO/MO Numbers
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## SL Vendor Characters

Enabled only when the SL Number Type
 is set to Project/Vendor.
Enter the number of characters of the vendor number (1-8) to use in combination with the project number when initializing subcontract numbers.
Note: The sum of project characters and vendor characters
 cannot exceed 18 characters.
 Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Defining Subcontract/PO/MO Numbers
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## SL Starting Sequence

Enabled only when the SL Number Type
 is Project/Sequence.
Enter the sequence number with which to begin sequence number assignment. When initializing subcontract numbers for a project (new or existing project with no existing subcontracts), the system will start with this sequence number, then assign the next available sequence from that point forward.

### Example

Starting sequence is by project, not by company. Therefore, each project will start with the same starting sequence.
SL Project Characters: 6
SL Sequence Characters: 10
Starting Sequence: 5500

Project
Subcontract #

Record 1:
11000-
11000-0000005500

Record 2:
11000-
11000-0000005501

Record 3:
22000-
22000-0000005500

Record 4:
22000-
22000-0000005501

Record 5:
33000-
33000-0000005500

Record 6:
33000-
33000-0000005501

Note: The above example assumes a different vendor for each record. Records with the same project and vendor will be assigned as items on the same subcontract.

 Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Defining Subcontract/PO/MO Numbers
[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Default Material Descriptions from Phase Description

Check this box to use the phase description as the material description when entering/initializing material detail lines (in PM Material Detail, PM PO Header, or PM MO Header) where the material description is blank, or when auto-adding material detail lines via PM Project Phases for cost types designated as material cost types (in PM Company Parameters, Material Cost Types section).
Leave this box unchecked if you do not want material descriptions to default from the phase description when blank. Instead, the system will use the description for the contract item assigned to the phase.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Material Cost Type 1

Enter the primary cost type to associate with
 material detail. This cost type will be used as the default when entering material detail
 lines in PM Material Detail.

- If this cost type is specified when adding phases to projects (PM
 Project Phases) or pending/approved change orders (PM Change Orders, PM Pending Change
 Orders, and/or PM Approved Change Orders), the system will automatically create a single
 material detail line for the phase/cost type in PM Material Detail with a Material Type
 of P-Purchase Order.

- If you do not specify a material cost type here or in the
 Material Cost
 Type 2 field, the system will not automatically create material detail
 lines when adding phases to projects or change orders, regardless of whether a material
 cost type is specified for the phase. You will need to enter material detail lines
 manually.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Material Cost Type 2

Enter the second cost type to associate with material detail.

- If this cost type is specified when adding phases to projects (PM
 Project Phases) or pending/approved change orders (PM Change Orders, PM Pending Change
 Orders, and/or PM Approved Change Orders), the system will automatically create a single
 material detail line for the phase/cost type in PM Material Detail with a Material Type
 of P-Purchase Order.

- If you do not specify a material cost type here or in the
 Material Cost
 Type 1 field, the system will not automatically create material detail
 lines when adding phases to projects or change orders, regardless of whether a material
 cost type is specified for the phase. You will need to enter material detail lines
 manually.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Auto-add cost type from material

Specify how to handle the addition of new phases/cost types when entering material detail.
1 = No. Do not allow addition of new phases/cost types. Phases and cost types must first be set up for the project in PM Project Phases.
2 = With Estimates. Allow adding new phases/cost types and automatically update project detail and original estimates.
3 = With No Estimates. Allow adding new phases/cost types and automatically update project detail, but do not update original estimates.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## PO Number Type

Indicate the format to use for purchase order numbers.

- Project/Seq – Select this option to use a specified number of characters of the project and a sequence number to generate the purchase order number.

- Project/Vendor – Select this option to use a specified number of characters of the project and vendor numbers to generate the purchase order number.

- Auto-Number – Select this option to have the system
 generate a purchase order number based solely on the next sequential number
 available. If this option is used, in PO Company Parameters, you must check the
 Automatically Generate PO #'s box and enter a value in the Last Used PO
 # field (cannot be null).

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## Significant Part of PO Job

Check this box if PM will use the significant part of job for validation when initializing purchase orders. This allows a single purchase order to include items for multiple jobs.
Leave this box unchecked if the entire destination job will be used for validation when initializing purchase orders.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## Significant PO Job Characters

Indicate the number of job characters (1-10) to use for validation when initializing purchase order numbers.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## PO Project Characters

Enter the project number characters that
 should be included in the PO number. The system will use numbers beginning from left to
 right, and any dashes included in the project number will be included in the PO number.
This field cannot be greater than 10.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Maximum of 30 characters
The subcontract number cannot exceed 30
 characters. That means that the sum of the SL Project Characters and SL Sequence
 Characters fields must be 30 or less.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## PO Sequence Characters

Enter the number number of sequence characters
 that should be included in the PO number. The system will use zeros to fill in unused
 characters. For example, if you specify 10 characters and the sequence number is 11, the
 resulting number will be 0000000011.
This field is only enabled when Project/Sequence is selected in the PO Number Type drop down.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.
Maximum of 30 characters
The PO number cannot exceed 30 characters.
 That means that the sum of the PO Project Characters and PO Sequence
 Characters fields must be 30 or less.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## PO Vendor Characters

Enabled only when number format is ‘Project/Vendor’.
Specify the number of characters of the vendor number (1-9) that you want used in combination with the project number when initializing purchase order numbers. The system will use numbers beginning from right to left.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## PO Starting Sequence

This field is only enabled when using Project/Seq number format.
Enter the sequence number with which to begin sequence number assignment. When initializing PO numbers for a project (new or existing project with no existing POs), the system will start with this sequence number, then assign the next available sequence from that point forward.
Starting sequence is by project, not by company. Therefore, each project will start with the same starting sequence. For example:
PO Project Characters: 6
PO Sequence Characters: 4
Starting Sequence: 6000

Project
Purchase Order #

Record 1:
11000-
11000-6000

Record 2:
11000-
11000-6001

Record 3:
21000-
21000-6000

Record 4:
21000-
21000-6001

Record 5:
31000-
31000-6000

Record 6:
31000-
31000-6001

Note:The above example assumes a different vendor for each record. Records with the same project and vendor will be assigned as items on the same purchase order.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
Defining Subcontract/PO/MO Numbers

## Add items to approved purchase orders not interfaced

Specify how initialization will handle PO material detail lines (those with a Material Type of P-Purchase Order).
Select this checkbox to add materials as new items on approved purchase orders for the vendor that have not been interfaced. If no approved, non-interfaced purchase orders are found, initialization will create a new purchase order for the material.
Clear this checkbox if only allowing materials to be added to non-interfaced purchase orders that have not been approved.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
Defining Subcontract/PO/MO Numbers

## Add original items to valid open purchase order for vendor

Check this box to assign material detail with
 a Material
 Type of P-Purchase Order to the highest valid open purchase order for the
 vendor. In PM Material Detail, when initializing purchase order numbers (via Initialize
 button), the initialize process will add material detail lines as items on the highest
 existing purchase order with the latest date for the specified vendor. If one does not
 exist, a new purchase order will be created.
Note:The Add items to approved purchase orders not
 interfaced box (above), when checked, takes precedence over this option.
 Initialization will add material detail lines to approved, non-interfaced purchase
 orders first. If none exist, material detail lines will then be added to open purchase
 orders (as indicated above).

Leave this box unchecked to always create a new purchase order for each material.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## Add change order items to valid open purchase order for
 vendor

Check this box to assign purchase order material detail set up for an approved or pending change order (in PM Approved Change Orders or PM Pending Change Orders) to the highest valid open purchase order for the vendor. In PM Material Detail, when initializing purchase order numbers (via Initialize button) for approved or pending change orders, initialization will add material detail lines as items on the highest existing purchase order with the latest date for the specified vendor. If one does not exist, a new purchase order will be created.
Note:The Add items to approved purchase orders not
 interfaced box (above), when checked, takes precedence over this option.
 Initialization will add material detail lines to approved, non-interfaced purchase
 orders first. If none exist, material detail lines will then be added to open purchase
 orders (as indicated above).

Leave this box unchecked to always create a new purchase order for each material.
Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
Defining Subcontract/PO/MO Numbers

##  Copy PCO Detail Notes to Purchase Order CO Header

Appears on the Material Parameters tab of the Company Parameters form.
Check to copy PCO Detail Notes to Purchase Order CO Header.

Related information

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

- [About the Add Items to Approved MOs/POs Options](/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options)

- [Copy PCO Detail Notes to Subcontract CO Header](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-0002394e--en)

## MO Number Type

Indicate the format to use for material order numbers.

- Project/Seq– Select this option to use a specified number of characters of the project and a sequence number to generate the material order number.

- Auto-Number– Select this option to have the system generate a material order number based solely on the next sequential number available. If this option is used, in IN Company Parameters, the “Auto Generate MO#s” option must be checked, and a value specified in the “Last Used MO#” (cannot be null).

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
Defining Subcontract/PO/MO Numbers

##  Group materials by location when initializing

 Check this box to group materials by location when initializing material orders. If checked, materials will be grouped together by location and a separate material order created for each location. Materials assigned to a location already existing on a material order will be added as new items on that material order.
 Leave this box unchecked if you do not want to group materials by location when initializing material orders. Materials will be added as items on a single material order, regardless of location.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Add items to approved material orders not interfaced

Specify how initialization will handle MO material detail lines (those with a Material Type of M-Material Order).
Check this box to add materials as a new items on approved material orders that have not been interfaced. If no approved, non-interfaced material orders are found, initialization will create a new material order for the material.
Leave this box unchecked if only allowing
 materials to be added to non-interfaced material orders that have not been approved (i.e.
 do not have the Approved box checked in PM MO Header, Info tab).
Note:If the Group materials by location when
 initializing box is checked, materials will be added to material orders
 based on location. If unchecked, they will be added to material orders regardless of
 location.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## MO Project Characters

Specify the number of characters of the project number (1-9) to use when initializing material order numbers. (The system will use numbers beginning from left to right).
Note:The sum of project characters and sequence characters cannot exceed 10 characters.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## MO Sequence Characters

Indicate the number of characters (1-9) in length for sequence numbers when initializing material order numbers. Leading zeros will be used with the sequence number to fill in where necessary. For example, if you specify 4 characters, and the next available sequence number is 11, the resulting number will be 0011.
Note:The sum of project characters and sequence characters cannot exceed 10 characters.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## MO Starting Sequence

Enabled only when using Project/Seq number format.
Enter the sequence number with which to begin sequence number assignment. When initializing material order numbers for a project (new or existing project with no existing MOs), the system will start with this sequence number, then assign the next available sequence from that point forward. (Note: Starting sequence is by project, not by company. Therefore, each project will start with the same starting sequence.)For example:
MO Project Characters: 6
MO Sequence Characters: 4
Starting Sequence: 7000

Project
Purchase Order #

Record 1:
11000-
11000-7000

Record 2:
11000-
11000-7001

Record 3:
21000-
21000-7000

Record 4:
21000-
21000-7001

Record 5:
31000-
31000-7000

Record 6:
31000-
31000-7001

Note:The above example assumes a different location for each record. Records with the same project and location will be assigned as items on the same material order.

Click [here](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats) for information on defining subcontract/PO/MO numbers.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters
[](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)Defining Subcontract/PO/MO Numbers

## Show CT Column 1-10

Specify the cost types (from JC Cost Types) that will display as grid columns in PM Project Phases. Show CT Column 1 and 2 will default as 1 and 2, respectively, but may be overridden.
Note:You should consider screen size and system performance when determining how many cost types you want displayed in PM Project Phases. You may typically want to specify only those cost types for which you standardly set up estimate information when adding phases to a project.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following lists and describes the audit options.

- Company Parameters – This option is always checked and is disabled. Changes made to the PM Company Parameters program will be tracked in the Master Audit file.

- Daily Logs – Check this box to record changes made to daily logs in PM Daily Logs.

- Company Add-ons – Check this box to record changes made in PM Company Add-Ons.

- Project Locations – Check this box to record changes made in PM Project Locations.

- Project Markups – Check this box to record changes made in PM Project Markups (Markups tab, PM Projects).

- Project Add-ons – Check this box to record changes made in PM Project Add-Ons.

- Project Firms – Check this box to record changes made in PM Project Firms.

- Project Notes – Check this box to record changes made in PM Notes.

- Project Notes Review – Check this box to record changes made in PM Project Notes Reviewers (Reviewers tab, PM Notes).

- Template Phases – Check this box to record changes made in PM Template Phases.

- Firms – Check this box to record changes made in PM Firms.

- Firm Contacts – Check this box to record changes
 made in PM Firm Contacts.

- Meeting Minutes – Check this box to record changes made in PM Meeting Minutes.

- Subcontract Detail – Check this box to record changes made in PM Subcontract Detail.

- Material Detail – Check this box to record changes made in PM Material Detail.

- Project Issues – Check this box to record changes made in PM Issues.

- Budget Codes – Check this box to record changes made in PM Billing and Cost Rate IDs.

- Project Budgets – Check this box to record changes made in PM Project Budgets

Note: When setting up a company, the entry of invalid data
 in certain fields will cause a warning; however, entries will be allowed and you will be
 able to save the record. This primarily applies to (but is not limited to) required data
 such as the ‘interface to’ companies and journals, since it is sometimes necessary to set
 up the company information before you can set up the data being requested.

## Document History Options

This section determines if a history record is created when a record is added, changed, or deleted records.

- Approved Change Orders – Check this box to generate history records when adding, changing, or deleting approved change orders.

- Drawing Logs – Check this box to generate history records when adding, changing, or deleting drawing logs.

- Inspection Logs – Check this box to generate history records when adding, changing, or deleting inspection logs.

- Other Documents – Check this box to generate history records when adding, changing, or deleting other documents.

- Pending Change Orders – Check this box to generate history records when adding, changing, or deleting pending change orders.

- Punch Lists – Check this box to generate history records when adding, changing, or deleting punch lists.

- Requests for Information – Check this box to generate history records when adding, changing, or deleting RFI’s.

- Request for Quotes – Check this box to generate history records when adding, changing, or deleting RFQ’s.

- Submittals – Check this box to generate history records when adding, changing, or deleting submittals.

- Test Logs – Check this box to generate history records when adding, changing, or deleting test logs.

- Transmittals – Check this box to generate history records when adding, changing, or deleting transmittals.

Note:Checking or unchecking an option does not affect the ability to track the specified document category in PM Document Tracking; it only determines whether history records will be generated for the document category.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

## Document Type

Enter a document type or press F4 to select
 one from a list.
Document types are created and maintained using [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form).
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

## Default Template

Press F4 to select a document template from a
 list. Only document templates of the document type selected in the Document Type
 field will display in the list.
Document templates are created and maintained using [PM Create & Send Templates ](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form).
Using the Document Templates tab
You can set up default document templates at both the company and project level.
On the company
Use the Document Templates tab on the PM Company Parameters form to assign document templates to the company.
For example if all RFI documents generated in a company should use a specific RFI document template, add that template to the Document Templates tab on the PM Company Parameters form. When the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature is used to generate an RFI document for any project in that company, by default the RFI document will be generated using the selected template.
On the project
Click the Distribution Templates () icon to set up the default document templates on a project, and/or configure which document templates can be used to generate project documents. [More](/en/vista/vista/project-management/create-and-send/assign-a-project-template)
What if a document template is set up on both the company and project?
If there are document templates set up on both
 the company and project, the templates set up on the project will always override
 any templates set up on the company.

[](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)PM Company Parameters

##  Projection Method

 Define how projections will be calculated. Users can override this selection using the projection options form when entering projections.

- Actual Costs - Cost projections are calculated using only actual costs.

- Actual + Committed Costs - Cost projections are calculated using both actual costs and committed costs.

This will only impact PM Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the JC Cost Projections form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in the
 PM module.

You
 can continue using the JC Cost Projections form, or you can transition to the new PM
 Cost Projections process.
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

##  Minimum Projection %

Use this option to define when cost projections
 should begin. Phases/cost types with percent complete values less than the minimum percent
 will have projected values calculated at the higher of estimated or actual costs.
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a projection minimum percentage has not been set up on the project/job or phases.

- [PM
 Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a projection
 minimum percentage has not been set up on the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the
 projection minimum percentage when new phases are added to a project/job.
 This will only impact PM Cost Projections
There are cost projection settings on both the JC
 Company Parameters and PM Company Parameters forms. If you change an option on one
 form, the other form will not be impacted. For example
 if you make a change to the PM Company Parameters form, the JC Company Parameters
 form is not impacted. This allows you to maintain separate configurations for
 JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in the
 PM module. You
 can continue using the JC Cost Projections form, or you can transition to the new PM
 Cost Projections process.

[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

## Allow inactive phases and cost types

Check this box if inactive phases and cost types can be included in cost projections.
When this box is checked, the
 Include Inactive Phases and Cost Types
 box on the PM Cost Projection Options form is enabled, which allows users to include or exclude inactive phases and cost types when calculating cost projections.
When is a phase or cost type active
A phase is active if the
 Active Phase
 box on the Info tab of the JC Job Phases form is checked.
A cost type is active if the
 Active
 box on the Cost Types tab of the JC Job Phases form is checked.
 This option impacts only PM Cost Projections
There are cost projection settings on both the JC Company Parameters and PM Company Parameters forms. If you change an option on one form, the other form
 will not
 be impacted. For example if you make a change to the PM Company Parameters form, the JC Company Parameters form is not impacted. This allows you to maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy
 - Prior to the version 6.8 release, all cost projections were processed using the JC Cost Projections form.

- Enhanced
 - Starting in version 6.8, the application also includes an enhanced version of the cost projections process in the PM module.

You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

##  Post projection forecasts when only forecast exists

 When this box is checked users can post projections even if only the forecast has changed, for example the projections did not change for the phase/cost type, but the actual costs caused the forecast to change.
 This will only impact PM Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in the
 PM module. You
 can continue using the JC Cost Projections form, or you can transition to the new PM
 Cost Projections process.

##  Allow projects to be in multiple open projections in the same month

When this box is checked the same project can be opened in multiple cost projection batches.
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in the
 PM module. You
 can continue using the JC Cost Projections form, or you can transition to the new PM
 Cost Projections process.

[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

##  Activate projection detail feature

When this box is checked users can enter projection detail on phases/cost types, for example budget code, detail date range, units, hours, unit cost, etc.
 This will add a Projection Detail tab to the PM Cost Projection Editor form.
This option only impacts PM Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the JC Cost Projections form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in
 the PM module.

You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

##  Activate revenue projection feature

Check this box to display the Revenue Projections button in PM Cost Projections, to enable users to view revenue-projection details.
There are cost projection settings on both the JC Company Parameters and PM Company Parameters forms. If you change an option on one form, the other form will
 not be impacted. For example if you make a change to the PM Company Parameters form, the JC Company Parameters form is not impacted. This allows you to maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8, the application also includes an enhanced version of the cost projections process in the PM module.

You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

## Activate time stamp feature for projection notes

Check this box to activate the time stamp feature on projection notes. Notes entered on a projection will include the date, time, and user that entered the note, but the note cannot be edited once it has been saved.
 The selection in this box will impact the [PM Cost Projections ](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)> Notes tab.
This option only impacts PM Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in
 the PM module. [More](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.

## Use Projection Detail Units as Default for Remaining Units

Use Projection Detail Units as Default for Remaining Units checkbox on the Projections tab of the PM Company Parameters form.
Deselect this checkbox to have the following cost projections fields appear on the Projection Detail tab of PM Cost Projection Editor.

- To Date Units

- To Date Unit Cost

- To Date Costs

- Remaining Units

- Remaining Unit Cost

- Remaining Costs

- Final Units

- Final Unit Cost

- Final Costs

Select the Use Projection Detail Units as Default for Remaining Units checkbox to have these cost projections field not appear on the Projection Detail tab of PM Cost Projection Editor.

Related information

- [PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

##  Select which unit cost to use for remaining

 Select how the system will set the remaining unit cost for a phase/cost type.

- Current Estimate – The remaining
 unit cost will equal the current estimated unit cost.

- Actual – The remaining unit cost
 will equal actual unit cost.

 The remaining unit cost is calculated when
 you click the Update Projections button on the [PM
 Cost Projections ](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form) form.
This only impacts PM Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in the
 PM module. [More](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)You
 can continue using the JC Cost Projections form, or you can transition to the new PM
 Cost Projections process.

[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

## Columns for Entry

Select which columns are enabled when entering cost projections.

- Percent Complete — Percent complete is the actual cost divided by projected cost.

- Over/Under — The over or under amount is projected cost minus estimated cost.

- Remaining — The remaining cost is projected cost minus actual cost.

When any of these boxes are selected, the related fields are enabled on the Phase/Cost Type tab on the PM Cost Projections and PM Cost Projection Editor forms.
There are cost projection settings on both the JC Company Parameters and PM Company Parameters forms. If you change an option on one form, the other form will
 not be impacted. For example if you make a change to the PM Company Parameters form, the JC Company Parameters form is not impacted. This allows you to maintain separate configurations for JC Cost Projections and PM Cost Projections.
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)

##  Spread Option

Select how plugged values entered on the projection code will be distributed to the associated phases/cost types.

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection code - The plugged amount will be distributed to the phases/cost types based on the spread percentage set up on the projection code (PM Projection CodesPhase/Cost Type tab[Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field). If you select this option, you will have to
 manually set up the spread on each phase/cost type on every projection code on a
 project. This means more data entry and additional set up time.

Click [here](/en/vista/vista/project-management/cost--revenue-projections/about-using-the-spread-option-for-cost-projections) for detailed information about using spread.
There are cost projection settings on both the JC Company Parameters and PM Company Parameters forms. If you change an option on one form, the other form will
 not be impacted. For example if you make a change to the PM Company Parameters form, the JC Company Parameters form is not impacted. This allows you to maintain separate configurations for JC Cost Projections and PM Cost Projections.

##  Document Type

The Document Type field on PM Company Parameters form, Workflow tab.
 Select the type of document to which the workflow applies.

- PO - Purchase Order

- SL - Subcontracts

Note: You can have only one process for each document type.

Note: You can override the workflows defined here by project in PM Projects.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the PM Company Parameters form, Workflow tab.
Enter the workflow process to perform for the specified document type or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the same document type specified in the Document Type field or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type (Purchase Order or Subcontract). However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). In this case, you may assign it to either or both document types on this tab.

Note: You can override the workflows defined here by project in PM Projects.

##  Active

The Active checkbox on the PM Company Parameters form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Notes

The Notes field on the PM Company Parameters form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
