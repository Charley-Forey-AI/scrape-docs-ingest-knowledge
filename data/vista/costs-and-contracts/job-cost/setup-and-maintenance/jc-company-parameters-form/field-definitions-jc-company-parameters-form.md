---
title: "Field Definitions: JC Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form/field-definitions-jc-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form/field-definitions-jc-company-parameters-form"
---

# Field Definitions: JC Company Parameters Form

The following is a list of field descriptions for the JC Add
 New Phase form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## JC Company

Enter the Job Cost company. This company must be a valid company from HQ Company Setup.

## Number of Valid Characters in Phase Code

The Number of Valid Characters in Phase Code field on the JC Company Parameters form.
Specify the number of characters that will be used to validate phases.

- Phases on Job Locked – This is the number of characters of the phase that must be valid (that is, set up in JC Phases) when adding phases to a job in JC Job Phases, JC Original Estimates, JC Change Orders, PM Project Phases, PM Change Orders, or PM Import Estimates.
Note: This validation does not apply when posting phases to a 'locked phases' job, as only phases assigned specifically to that job (as indicated above) may be entered.

- Phases on Job Not Locked – This will be the number of characters of the phase that must be valid (i.e. must be set up in JC Phases) when posting to the job.

## Allow Posting to Soft-Closed Jobs

Check this box to allow posting to soft-closed jobs (those with a
 status of ‘2-Soft Close’ in JC Jobs) in Job Cost and other modules (such as AP, EM, PR, SM,
 etc.). During posting, a ‘closed job’ indicator displays (in red) on the form (location and
 message will vary by form), but entry is allowed. Costs are posted to open accounts defined
 in the Department file (JC Departments).
Leave this box unchecked if you do not allow posting to soft-closed jobs.
Note: Checking the Allow Posting to Hard-Closed Jobs box
 automatically sets this box to checked (if not already checked). Likewise, if you uncheck
 this box, the system will automatically uncheck the Allow Posting to Hard-Closed Jobs box.
For more information, see [Closing Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract)Close a contract
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Allow Posting to Hard-Closed Jobs

Check this box to allow posting to hard-closed jobs (those with a
 status of ‘3-Hard Close’ in JC Jobs) in Job Cost and other modules (such as AP, EM, PR, SM,
 etc.). During posting, a ‘closed job’ indicator displays (in red) on the form (location and
 message will vary by form), but entry is allowed. Costs will be posted to closed accounts
 defined in the Department file (JC Departments).
Leave this box unchecked if you do not allow posting to hard-closed jobs.
Note: Checking this box automatically sets the Allow Posting to
 Soft-Closed Jobs box to checked (if not already checked). Likewise, if you
 uncheck the Allow
 Posting to Soft-Closed Jobs box, the system will automatically uncheck this
 box.
For more information, see [Closing Contracts](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract).

[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-contract-close-form/close-a-contract)Close a contract
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Close Subcontracts when Job Hard-Closed

Close Subcontracts when Job Hard-Closed checkbox on the Info tab of the JC Company Parameters form.
Select this checkbox to automatically close open subcontracts when closing a job.

## Close Purchase Orders when Job Hard-Closed

Close Purchase Orders when Job Hard-Closed checkbox on the Info tab of the JC Company Parameters form.
Select this checkbox to automatically close open purchase orders when closing a job.

## Add Standard Item Code to Database if Not on File

If this box is checked, you can create a new item codes when creating or modifying contract items.
If this box is not checked, you can only select item codes that have already been set up using the [JC Standard Item Codes](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) form when creating or modifying contract items.
 Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-standard-item-codes-form) for more information.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Post Crew With Progress Entry

Check this box if you will be posting progress to crews in Progress Entry. When posting progress to crews, units produced are entered by job/phase/cost type/crew code. This information can be used to create crew productivity reports.
Leave this box unchecked if you will not be posting progress to crews. Instead, progress will be posted by job/phase/cost type.
[JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)

## Attach Batch Reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
[](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form)HQ Batch Control

## GL Co#

Specify the GL company to be updated when job costs are entered directly into JC module. You must enter a company here even if you will not actually interface to GL.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## AR Co#

Specify the Accounts Receivable company to which invoices created in JB for this JC company will be interfaced.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## IN Co #

Identify which valid Inventory company will be the company to which all material entries will be posted.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  PR Co #

 Specify the Payroll company that will be used to validate certain payroll-related
 information, such as the craft/class and/or class templates assigned to a job in JC Jobs.
Note: This is also the PR company that will be used for PR-related fields in PM (with the exception of initializing 'our firm' contacts, which uses the PM PR company.)  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Use Job Billing

Check this box if you will be using the Job Billing module for billing jobs.
Leave this box unchecked if jobs will be billed offline and invoices entered in AR.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Next Field Ticket

The Next Field Ticket field on the JC Company Parameters form, Info tab.
Enter the number with which to begin auto-numbering field tickets. The system updates this number automatically each time you add a new field ticket in JC Field Ticket.
 You can change the number in this field at any time. The next time you add a field ticket, the system checks existing field ticket numbers and if the number already exists, the system skips to the next sequential number that is not already in use.
Entry in this field is not required. If left blank, the system automatically assigns field ticket numbers based on the highest existing number in the system.

## Job Billing Options

Only one of the following billing options may be selected.

- P-Progress.Select this option if most contracts are billed on a 'percent complete' basis.

- T-T and M.Select this option if most contracts are billed on a 'time and materials' basis.

- B-Both.Select this option if you will be billing contracts on both a 'percent complete' and 'time and materials' basis.

- N-None.Select this option if you are not using Job Billing for billing jobs.

The bill type option selected here will be
 used as the default bill type when manually setting up new contracts in JC Contracts and PM
 Contracts, as well as when auto-setting up contracts via JC Jobs, PM Projects, and PM
 Import Upload.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following lists and describes the audit options.

- Company Parameters – This audit option is display-only, and is always checked. Any changes made to a company in JC Company Parameters will be tracked in the Master Audit file.

- Department – Check this box to record changes made
 to departments in JC Departments.

- Contracts – Check this box to record changes made to
 contracts in JC Contracts and PM Projects.

- Jobs – Check this box to record changes made to jobs
 in JC Jobs and PM Projects.

- Change Orders – Check this box to record changes made to change orders in JC Change Orders.

- Job Phases – Check this box to record changes made to job phases in JC Job Phases and PM Project Phases.

- Job Phase Cost Types – Check this box to record changes made to cost types on job phases in JC Job Phases, Cost Types and Estimates tabs, and PM Project Phases, Cost Types tab.

- Phase Master – Check this box to record changes made
 to phases and phase cost types in JC Phases (Info and Cost Types tabs).

- Projection Overrides – Check this box to record additions and changes made to the Cost or Revenue tabs in JC Override Projections.

- Liability Templates – Check this box to record additions and changes made to liability templates in JC Liability Template.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Cost Interface Options

 Select one of the options below to indicate how GL is to be updated when cost adjustments are entered.

- No Update - GL entries created when posting cost adjustments will not be interfaced to GL.

- Summary - Cost adjustment entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Create GL transactions for every cost adjustment entry. In the selection box below, highlight each of the details to include in the GL transaction description. As you highlight an item, it is added to the description line to the right. When posting transactions, the system will extract this data to create the transaction description. Available fields are:

- Job

- Phase

- CT

- Trans Type

- Desc

- Trans #

Note: Fields can be selected in any order, and the GL transaction description will appear in the same order in GL.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Cost Interface: Summary GL Description

 Enabled only if GL Cost Interface level is ‘Summary’.
 Enter the description that will be used each time a summarized cost adjustment entry is interfaced to GL.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Cost Interface: Journal

 Enter the GL journal to use for cost adjustment entries.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Cost: Allow GL Account Override

 Check this box to allow overrides to default GL accounts when
 posting job costs throughout the system (JC, AR, AP, etc.). Default accounts are defined in
 the JC Departments program.
 Leave this box unchecked if you do not allow overrides to GL accounts when posting job costs. This is recommended if the GL Close Interface (GL Close tab) level is Summary or Detail.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## GL Revenue Interface Options

Select one of the options below to indicate how GL is to be updated when revenue adjustments are entered.

- No Update - GL entries created when posting revenue adjustments will not be interfaced to GL.

- Summary- Revenue adjustment entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - One entry will be posted to GL for every revenue adjustment entry. In the selection box below, highlight each of the details to include in the GL transaction description. As you highlight an item, it is added to the description line to the right. When posting transactions, the system will extract this data to create the transaction description.

Note: Fields can be selected in any order, and the GL transaction description will appear in the same order in GL.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Revenue Interface: Summary GL Description

 Enabled only if the GL Revenue Interface level is ‘Summary’.
 Enter the description you want used each time a summarized revenue adjustment entry is interfaced to GL.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Revenue Interface: Journal

 Enter the GL journal to use for revenue adjustment entries.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Revenue: Allow GL Account Override

 Check this box if allowing overrides to default GL accounts when
 posting revenue throughout the system (JC,AR, JB, etc.). Default accounts are defined in
 the JC Departments program.
 Leave this box unchecked if you do not allow overrides to GL accounts when posting revenue. This is recommended if the GL Close Interface (GL Close tab) level is Summary or Detail.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Close Interface Options

 Specify whether GL detail will be automatically posted to General
 Ledger when the JC Contract Close program is run.

- No Update - Any necessary GL entries must be
 manually posted. Use this option if your job cost departments in JC Departments have
 the same set of GL accounts in the open and closed columns, in which case no GL
 interface is needed during the contract close process.

- Summary - Update GL and post one entry per GL account for each department. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Update GL, and post one entry per GL account for each contract. In the selection box below, highlight each of the details to include in the GL transaction description. As you highlight an item, it is added to the description line to the right. When posting transactions, the system will extract this data to create the transaction description. Available fields are:

- Dept

- Contract

Note: Fields can be selected in any order, and the GL transaction description will appear in the same order in GL.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Close Interface: Summary GL Description

 Enabled only if the GL Close Interface level is Summary.
 Enter the description to use when a closing entry is interfaced to GL.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Close Interface: Journal

 Enter the GL journal to which GL entries will be posted when you close contracts.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## GL Material Interface

Enter the type of GL update that will occur when posting material use transactions.

- No Update - GL entries created when posting material use will not be interfaced to GL.

- Summary- Material use entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail- For each unique GL account that occurs in a transaction, one GL entry will be posted. In the selection box below, highlight each of the details to include in the GL transaction description. As you highlight an item, it is added to the description line to the right. When posting transactions, the system will extract this data to create the transaction description. Available fields are:

Note: Fields can be selected in any order, and the GL transaction description will appear in the same order in GL.  
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Material Interface: Summary GL Description

 Enabled only if the GL Material Interface level is ‘Summary’.
 Enter the description to use when a material use entry is interfaced to GL.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  GL Material Interface: Journal

 Enter the GL journal to use for material use entries.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  Validate Material

 Check this box to validate materials when posting material usage. If checked, materials entered when posting material usage must be set up in HQ Materials.
 Leave this box unchecked if materials will not be validated when posting material usage. If unchecked, any material can be entered when posting material usage, even if they have not been set up in HQ Materials.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  Use Tax on Material

 Check this box to allow posting use tax with materials.
 Leave this box unchecked if do not post use tax with materials.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  Misc Matl GL Account

Specify the GL account to credit when posting
 miscellaneous (non-stocked) materials in JC Material Use (type ‘MI’).
This account may be used if the
 Validate Material checkbox is selected and the HQ Category
 associated with the HQ Material does not have an assigned GL Account, or if the
 Validate Material checkbox is not selected and, when posting
 material usage, you enter a material that does not exist in HQ Materials.
Note: Regardless of how the Validate
 Material checkbox is set, if you enter a stocked material, the GL account
 specified in Inventory (Location Overrides) is used. If the material is non-stocked, but is
 set up in HQ Materials, the Non-Stocked GL account specified in HQ Material Categories is
 used.
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  Projection Method

 Define how projections will be calculated. Users can override this selection using the projection options form when entering projections.

- Actual Costs - Cost projections are calculated using only actual costs.

- Actual + Committed Costs - Cost projections are calculated using both actual costs and committed costs.

Click [here](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form) for information about the JC Projection Options form.
Note: This option only applies to JC Cost Projections. Although there are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms, changing an option on one form does not impact the other form. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections

##  Minimum Projection %

Use this option to define when cost projections
 should begin. Phases/cost types with percent complete values less than the minimum percent
 will have projected values calculated at the higher of estimated or actual costs.
Projection minimum percentage is set up in several places

- [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) / [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) - This value is only used if a projection minimum percentage has not been set up on the project/job or phases.

- [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form) / [JC Jobs](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) - This value is only used if a projection
 minimum percentage has not been set up on the phases.

- [PM Project Phases ](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form) / [JC Job Phases](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form) - This field defaults based on the
 projection minimum percentage set up using the JC Phases form.

- [JC Phases ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-phases-form) - This is the default value of the
 projection minimum percentage when new phases are added to a project/job.
This option only impacts JC Cost Projections
There are cost projection settings on both the JC
 Company Parameters and PM Company Parameters forms. If you change an option on one
 form, the other form will not be impacted. For example
 if you make a change to the PM Company Parameters form, the JC Company Parameters
 form is not impacted. This allows you to maintain separate configurations for JC Cost
 Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in
 the PM module.
You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.

Click the links below for more information.
[JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)
[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

## Allow Inactive Phases and Cost Types

Check this box if inactive phases and cost types can be included in cost projections.
When this box is checked, the Include Inactive Phases and
 Cost Types box on the [JC Projection Options ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form) form is enabled, which allows users
 to include or exclude inactive phases and cost types when calculating cost projections.
This option only impacts JC Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in
 the PM module. [More](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.

##  Post Projection Forecasts when only Forecast exists

 When this box is checked users can post projections even if only the forecast has changed, for example the projections did not change for the phase/cost type, but the actual costs caused the forecast to change.
This option only impacts JC Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will
 not be impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.

[About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
[JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)

##  Allow Jobs to be in Multiple Open Batches in the Same Month

Although not recommended, checking this option allows the same job to be opened in multiple projection batches in the same month without affecting another user’s work. You should only check this option if you have users (e.g. project managers working on large jobs) that need to do projections within their area of work at the same time. However, if you elect to use this feature, be aware that if more than one user posts to the same phase/cost type, the last batch posted will determine the final values for the phase/cost type.
 Leave this box unchecked to restrict jobs from being added to multiple open projection batches in the same month. Jobs may only be added to a projection batch if they do not already exist in another open projection batch in the same month.
 This option only impacts JC Cost
 Projections
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

[JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)

##  Activate Projection Detail Feature

When this box is checked users can enter projection detail on phases/cost types, for example budget code, detail date range, units, hours, unit cost, etc.
 This will add a Projection Detail tab to the lower portion of the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.
This option only impacts JC Cost Projections
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

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

## Activate Time Stamp Feature for Projection Notes

Check this box to activate the time stamp feature on projection notes. Notes entered on a projection will include the date, time, and user that entered the note, but the note cannot be edited once it has been saved.
 The selection in this box will impact the [JC Cost Projections ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)> Notes tab.
This option only impacts JC Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form will notbe impacted. For example if you make a change to the PM Company
 Parameters form, the JC Company Parameters form is not impacted. This allows you to
 maintain separate configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy - Prior to the version 6.8
 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced - Starting in version 6.8,
 the application also includes an enhanced version of the cost projections process in
 the PM module. [More](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)
You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.

##  Select Which Unit Cost to Use for Remaining

 Select how the system will set the remaining unit cost for a phase/cost type.

- Current Estimate
 – The remaining unit cost will equal the current estimated unit cost.

- Actual
 – The remaining unit cost will equal actual unit cost.

The remaining unit cost is calculated when you click the
 Set Remain UC
 button on the [JC Cost Projections ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)form.
Note: This option only applies to JC Cost Projections. Although there are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms, changing an option on one form does not impact
 the other form. This allows you to maintain separate
 configurations for JC Cost Projections and PM Cost Projections.

##  Columns for Entry

Select which columns are enabled when entering cost projections.

- Percent Complete
 — Percent complete is the actual cost divided by projected cost.

- Over/Under
 — The over or under amount is projected cost minus estimated cost.

- Remaining
 — The remaining cost is projected cost minus actual cost.

When any of these boxes are checked, the related fields are enabled on the Info tab in the lower portion of the JC Cost Projections form.
 This option only impacts JC Cost Projections
There are cost projection settings on both the
 JC Company Parameters and PM Company Parameters forms. If you change an option on one form,
 the other form
 will
 not
 be impacted. For example if you make a change to the PM Company Parameters
 form, the JC Company Parameters form is not impacted. This allows you to maintain separate
 configurations for JC Cost Projections and PM Cost Projections.
There are two versions of the cost projections feature.

- Legacy
 - Prior to the version 6.8 release, all cost projections were processed using the [JC Cost Projections](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) form.

- Enhanced
 - Starting in version 6.8, the application also includes an enhanced version of the cost projections process in the PM module.
You can continue using the JC Cost Projections form, or you can transition to the new PM Cost Projections process.

## Revenue Forecast Method

Specify the method to use when initializing revenue forecasts for contracts using JC Forecast Initialize. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.

- None - Select this method if you are not using the forecasting feature or if you will be entering forecasts manually.

- Linear - Select this option to use the linear method when initializing forecasts. Initialization will spread the contract amount equally over the life of the contract.

- Curve - Select this option to use the curve method when initializing forecasts. Initialization will spread the contract amount in defined increments over the life of the contract. Incremental amounts are based on the forecast intervals and the percent complete expected at the end of each interval.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options)Forecasting Options - Overview

## # of Revenue Forecast Intervals (or periods)

This field is enabled only when the revenue forecast method is 'C-Curve'. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.
Enter the number of intervals or periods to use when initializing revenue forecasts. Must be a minimum of 2, a maximum of 10. Intervals represent times throughout the life of the contract at which revenue complete is expected to reach a defined level.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
Forecasting Options - Overview

## Revenue % Complete at End of Each Interval

This field is enabled only when the revenue forecast method is 'C-Curve'. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.
Enter the percent of revenue (in whole numbers) that is expected to be complete at the end of each interval, inserting a colon between each percent complete value. The number of revenue forecast intervals is assumed to include the final interval (i.e. 100% complete); therefore, the number of percent complete values entered here must be 1 less than the number of intervals (i.e. if 4 intervals, enter 3 percent complete values).

###  Example

# of Revenue Forecast Intervals:  4
Revenue % Complete at end of each interval:   25:50:75

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
Forecasting Options - Overview

## Cost Forecast Method

Specify the method to use when initializing cost forecasts for contracts using JC Forecast Initialize. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.

- None - Select this method if you are not using the forecasting feature or if you will be entering forecasts manually.

- Linear - Select this option to use the linear method when initializing forecasts. Initialization will spread the contract estimate amount equally over the life of the contract.

- Curve - Select this option to use the curve method when initializing forecasts. Initialization will spread the contract estimate amount in defined increments over the life of the contract. Incremental amounts are based on the forecast intervals and the percent complete expected at the end of each interval.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
Forecasting Options - Overview

## # of Cost Forecast Intervals (or periods)

This field is enabled only when the cost forecast method is 'C-Curve'. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.
Enter the number of intervals or periods to use when initializing cost forecasts. Must be a minimum of 2, a maximum of 10. Intervals represent times throughout the life of the contract at which cost complete is expected to reach a defined level.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters
Forecasting Options - Overview

## Cost % Complete at End of Each Interval

This field is enabled only when the cost forecast method is 'C-Curve'. Click [here](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/revenuecost-forecast-options) for an overview on the forecasting options.
Enter the percent of cost (in whole numbers) that is expected to be complete at the end of each interval, inserting a colon between each percent complete value. The number of cost forecast intervals is assumed to include the final interval (i.e. 100% complete); therefore, the number of percent complete values entered here must be 1 less than the number of intervals (i.e. if 4 intervals, enter 3 percent complete values).

###  Example

# of Cost Forecast Intervals:  4
Cost % Complete at end of each interval:   25:50:75

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)JC Company Parameters

##  Document Type

The Document Type field on JC Company Parameters form, Workflow tab.
 Select the type of document to which the workflow applies.

- PO - Purchase Order

- SL - Subcontracts

Note: You can have only one process for each document type.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the JC Company Parameters form, Workflow tab.
Enter the workflow process to perform for the specified document type or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the same document type specified in the Document Type field or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type (Purchase Order or Subcontract). However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). In this case, you may assign it to either or both document types on this tab.

Note: You can override the workflows defined here by job in JC Jobs.

##  Notes

The Notes field on the JC Company Parameters form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

##  Active

The Active checkbox on the JC Company Parameters form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
