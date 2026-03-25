---
title: "About the PM Import Estimates Upload Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form"
---

# About the PM Import Estimates Upload Form

This form can only be accessed by clicking the ‘Upload into
 PM’ button on the PM Import Menu, and is used to upload the data from the work file into
 Project Management.
When entering the project to which you are
 uploading the data, you can specify either an existing project or a new project. If you
 specify an existing project, the related project and contract fields (i.e. project
 description, liability template, state code, markup/discount rate, contract and
 description, department, customer, tax code, retainage percent and start month) are
 disabled, and the screen will display the following message:
WARNING: Detail on file, duplications will
 have costs accumulated.
If you specify a new project, these fields are
 enabled and you must enter the appropriate data. The project description will automatically
 default the description entered on the Info tab (in PM Edit Import Data form), but it can
 be overridden. The Lock Phases option allows you to specify whether to lock phases for the
 new project. If checked, the upload process will automatically set this option to Y
 (checked) in PM Projects, thereby restricting posting to only those phases set up for the
 project in PM Project Phases.
The contract automatically defaults to a
 number identical to the project number, and the contract description automatically defaults
 the same description entered for the project. Both of these defaults may be overridden. If
 you specify an existing contract (from JC Contracts) for the project, the contract
 description and department fields are disabled, and the following message is displayed:
WARNING: Contract items on file,
 duplications will be ignored.

- Project/Contract Security - If you have implemented data level security at the
 job and/or contract level (in VA Data Security Setup), security group fields
 display in the Project Info and Contract Info sections, allowing you to designate
 the security group who will have access to information about the project and/or
 contract. Note: It is important to note that in
 addition to the security group specified for the project and/or contract,
 access to information about the project and/or contract will automatically be
 granted to the Default Security Group you specified in VA Data Security
 Setup.

- IN Co/Location - If you will be uploading material detail, you can specify the
 default IN Co and Location to which stocked materials will be assigned. When
 uploading stocked materials, records will be flagged as type 'M' (Material Order) and
 assigned the specified IN Co# and Location. If a material is not stocked at the
 specified location, the IN Co# and Location will default as null, but the record will
 remain flagged as a material order.

- Upload as a Pending Change Order - This option is used when the
 import data will be uploaded into PM as a change order. For more information, see
 [About the PM Import Estimates Upload Form](#ID-000289a6--en__ID-000289a6).

- Assign Change Order Issue - This option allows you to specify
 whether an issue will automatically be created in PM when the change order is
 uploaded. If you assign the change order to an issue, you can have the upload create
 a new issue and assign the change order and all its items to the issue, or you can
 assign the change order/change order items to an existing PM issue. Once you have
 entered all the criteria, click the Upload button at the bottom of the form to begin
 the upload process. Once completed, you will receive a message giving you the option
 to purge the import data for the specified import ID. If you answer Yes, all import
 data will be purged from the work file for the specified import ID.

- Cost Type Records - Read about the process used when uploading
 cost type records [here](/en/vista/vista/project-management/import-project-estimates/about-uploading-cost-type-records#concept-5186--en__concept-5186).

[PM Import
 Estimates Template](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-template-form)
[PM Import Estimates - Overview ](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form)
