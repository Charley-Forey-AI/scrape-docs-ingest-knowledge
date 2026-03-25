---
title: "Field Definitions: PM Import Estimates Upload Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form/field-definitions-pm-import-estimates-upload-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form/field-definitions-pm-import-estimates-upload-form"
---

# Field Definitions: PM Import Estimates Upload Form

The following is a list of field descriptions for the PM
 Import Estimates Upload form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  ImportID

 Enter the import ID of the data you want to upload into Project Management. Press F4 for a list of valid import IDs.
 If there are any errors existing in the import data work file, you will receive a message notifying you what errors were found (e.g. “Phase errors found”). Once you click OK, cursor returns to this field and you will need to specify another import ID to upload. You also have the option to correct the indicated errors in the work file (via PM Import Edit) and then return to this form to retry the upload.

## Project

Indicate to which project the import data will be uploaded. If entering a new project, enter a project code as defined when your system was installed. If you entered an existing project (from PM Projects), the project and contract information (project description, liability template, PR state, markup/disc rate, and the contract description, department, customer, tax code, and retainage) is displayed and the corresponding fields are disabled. (Note: The contract’s Start Month will remain enabled, allowing you to specify the start date for the new data.)
In addition, you will receive the following project and contract warnings:
WARNING: Detail on file, duplications will have costs accumulated.
WARNING: Contract Items on file, duplications will be ignored.

## Description

Enabled for new projects only.
Enter the description for this project, up to 30 characters. Initially defaults the description specified for the estimate in the work file (PM Import Edit, Info tab).
If uploading to an existing project, the project’s description defaults from PM Projects and cannot be changed.

## Liab Template

Enabled for new projects only.
Required.
Enter the liability template (as defined in JC Liability Template) to use when processing payroll for this project.
If uploading to an existing project, the project’s liability template defaults from PM Projects and cannot be changed.

## PR State

Enabled for new projects only.
Required.
Enter the 2-character state code (from HQ
 States) that identifies the state in which this project is located. If the Use Job, SM Work Order or
 Office State for Tax State box in the PR Company Parameters form is checked,
 this code will be used as the default when posting timecards (PR Timecard Entry) that
 reference this project.
If uploading to an existing project, the
 project’s state defaults from PM Projects and cannot be changed.

## Lock Phases

Enabled for new projects only.
Check this box to lock phases for this
 project. During the upload, the Phases on this Job are Locked checkbox in
 PM Projects is checked and you will only be allowed to post to phases/cost types assigned
 to this project in PM Project Phases.
Uncheck this box if not locking phases for
 this project. During the upload, the Phases on this Job are Locked checkbox in
 PM Projects is unchecked and you will be allowed to post to any valid phase/cost type in
 the phase master.
Note:If uploading to an existing project, the Phases on this Job are
 Locked checkbox defaults as defined for the project in PM Projects and
 cannot be changed.

## Project Security Group

This field only displays when data security is in effect for the ‘bJob’ datatype (in VA Data Security Setup) and a new project is specified.
Enter the security group (from VA Security Groups) for this project. Users assigned to this security group will be allowed access to information about this project.
Note:It is important to note that in addition to the security group specified here, access to information about this project will automatically be granted to the Default Security Group you specified in VA Data Security Setup.

## Markup/Disc Rate

Enabled for new projects only.
Enter the markup/discount rate that will be used in determining material pricing for stocked materials (posted to this project) with no estimated unit price.
If uploading to an existing project, the project’s markup/discount rate defaults from PM Projects and cannot be changed.

## Contract

Enabled for new projects only.
Enter the contract for this project, up to 9 characters (including dashes). Initially defaults the project number. If you enter an existing contract, the remaining contract inputs (except for Start Month) default as defined for the contract and are disabled.
If you are uploading to an existing project, defaults the contract as defined in PM Projects and cannot be changed.

##  Description

 Enabled for new contracts only.
 Enter a description for this contract, up to 30 characters. Initially defaults the project’s description.
 If you are uploading to an existing contract,
 defaults the contract’s description (from JC Contracts) and cannot be changed.

##  Department

 Enabled for new contracts only.
 Required.
 Enter a valid JC department (from JC
 Departments) for the specified contract.
 If you are uploading to an existing contract,
 defaults the contract’s department (from JC Contracts) and cannot be changed.

##  Customer

 Enabled for new contracts only.
 Enter the customer (from AR Customers) for this contract, if applicable. This is the customer to whom billing invoices for this contract will be posted.
 If you are uploading to an existing contract,
 defaults the contract’s customer (from JC Contracts) and cannot be changed.

##  Tax Code

 Enabled for new contracts only.
 Enter the tax code (from HQ Tax Codes) for this contract. This tax code will be assigned to the contract and each contract item.
 If you are uploading to an existing contract,
 defaults the contract’s tax code (from JC Contracts) and cannot be changed.

## Retainage %

Enabled for new contracts only.
Specify the retainage percent to use as the default for this contract.
Note:The value entered here will not be used as the default for the contract items being uploaded with this contract; rather, the value specified for each contract item in the work file will be used.

If you are uploading to an existing contract,
 defaults the contract’s retainage (from JC Contracts) and cannot be changed.

##  Start Month

 Enter the starting month for this contract. Initially defaults the current month. This month specified here will be used to store original estimates.

## Contract Security Group

This field only displays when data security is in effect for the ‘bContract’ datatype (in VA Data Security Setup) and a new contract is specified.
Enter the security group (from VA Security Groups) for this contract. Users assigned to this security group will be allowed access to information about this contract.
Note:It is important to note that in addition to the security group specified here, access to information about this contract will automatically be granted to the Default Security Group you specified in VA Data Security Setup.

## IN Co#

Enter the IN company for material detail. During the upload, the system will assign this company to all material detail records where the IN Co is blank.
Note:The system automatically sets the Material
 Type to M-Material Order for all records assigned to the IN Co and
 Location specified during the upload; if a materials is not set up for the specified IN
 Co and Location, these values will default as null.

## Location

Enter the IN location (from IN Locations) for
 material detail. During the upload, the system will assign this location to all material
 detail records where the Location is blank.
Note:The system automatically sets the Material
 Type to M-Material Order for all records assigned to the IN Co and
 Location specified during the upload; if a materials is not set up for the specified IN
 Co and Location, these values will default as null.

## Upload As A Pending Change Order

Check this box if the import data will be uploaded as a pending change order. When checked, related change order fields are enabled, allowing you to specify the pending change order/change order items to which data will be uploaded, as well as the issue to which the change order is associated (if applicable).
Do not check this box if imported data should be uploaded as standard project data.

## PCO Type

Enabled only if theUpload as a Pending Change
 Order box is checked.
Specify the pending change order type (from PM Document Types) to which the data will be uploaded.

## PCO

Enabled only if Upload as a Pending Change
 Order box is checked.
Enter the pending change order number, up to 10 characters. If uploading data to a new project, must be a new pending change order.
If uploading data to an existing project, you
 may specify a new or existing pending change order. (Note: If the change order number
 exists as an approved change order in PM, this change order can only be uploaded as a
 pending change order and the Approve this Pending Change Order
 checkbox is disabled. Change order will need to be approved manually in PM.)

## Description

Enabled only if Upload as a Pending Change
 Order box is checked.
Enter a description of the change order, up to 60 characters. Initially defaults the project description.
If you are uploading data into an existing change order, defaults the change order description and cannot be changed.

## PCO Item

This field only displays when a single
 contract item exists in the work file, and is only enabled when you are not uploading
 contract items as change order items (option in PM Import Templates). 
Enter the pending change order item, up to 10 characters.
Note:If you are uploading contract items as change order items, this field is disabled and the contract item will become the change order item; however, if the contract item cannot be formatted as a change order item, the system will assign a sequential number.

## Starting PCO Item

This field only displays when multiple contract items exist in the work file. Enabled only if:

- You are uploading data to a new pending change order
 and you are not uploading contract items as change order items (option in PM
 Import Templates).

- You are uploading data to an existing pending change order, regardless of whether you are uploading contract items as change order items.

Enter the number with which to begin numbering CO items, up to 6 digits.
Note:If you are uploading data to a new pending change order and you are uploading contract items as change order items, this field is disabled and contract items will become change order items; however, if contract items cannot be formatted as change order items, the system will assign sequential numbers.

## Increment By

This field only displays when multiple contract items exist in the work file. Enabled only if:

- You are uploading data to a new pending change order
 and you are not uploading contract items as change order items (option in PM Import
 Templates).

- You are uploading data to an existing pending change order, regardless of whether you are uploading contract items as change order items.

Enter the number by which to increment change order item numbers. For example, if you specify ‘500’ as the Starting PCO Item and set the increment value to ‘5’, change order items will be numbered as follows: 500, 505, 510, etc.

## PCO Item Description

Enabled only if the Upload as a Pending Change
 Order box is checked.
Enter a description of the change order, up to 60 characters.

## Approve This Pending Change Order

Enabled only if the ‘Upload as a Pending Change Order’ option is checked.
Check this box to set the status of this pending change order as ‘approved’ when uploaded to PM.
Uncheck this box to upload this change order as a pending change order.

## Assign Change Order Issue

Enabled only if the Upload as a Pending Change
 Order box is checked.

- None – Select this option if no issue will be assigned to the pending change order when uploaded to PM.

- Create New – Select this option to create a new issue when the pending change order is uploaded. The issue will be assigned to the pending change order and its items.

- Use Existing – Select this option to assign an existing issue to this change order and its items. Issue is entered to the right of this field. (Note: This option only applies if you are uploading to an existing project and there are existing issues assigned to the project.)
