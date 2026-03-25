---
title: "Field Definitions: EM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form"
---

# Field Definitions: EM Company Parameters Form

The following is a list of field descriptions for the EM
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## EM Company

Enter the EM company in which equipment processing will occur. Must be a valid company set up in HQ Company Setup.

##  GL Co#

 Specify the GL company to be updated when equipment costs and revenue are entered in EM. Entry is required even if you will not be interfacing to GL.

##  IN Co#

 Enter the IN company to use when posting materials to equipment cost (in EM Usage Posting or EM WO Parts Posting). Default may be overridden at time of entry.

##  JC Co#

 Enter the JC company to which all equipment usage will be posted (EM Usage Posting). Default may be overridden at time of entry.

##  PR Co#

 Enter the PR company that will be used to validate all employees when posting usage. Default may be overridden at time of entry.

##  Fuel Cost Code

 Specify the cost code to be used as the default when posting fuel usage (EM Fuel Posting). Default may be overridden at time of entry.

##  Fuel Cost Type

 Specify the EM cost type to be used as the default when posting fuel usage (EM Fuel Posting). Default may be overridden at time of entry.

## Last Month Calculated

Specify the last month through which all depreciated costs have been processed. You will only need to make an entry here during the initial setup. Once you begin using the EM Depreciation Processing program, the system updates this field automatically and manual updates are not required or recommended.
Note: The system will only update this field if you post depreciation for all assets (i.e., you leave the ‘Post Depreciation for Select Assets’ option unchecked when running EM Depreciation Processing).

##  Last Year Budgeted

 Specify the last fiscal year through which you have calculated depreciation budgets. You will only need to make an entry here during the initial setup. Once you begin using EM Depreciation Processing, the system updates this field automatically. Manual updates are not required or recommended (as it may cause existing depreciation budgets to be incorrectly updated).

##  Depreciation Cost Code

 Specify the cost code the system will assign to all depreciation cost-adjusting entries created when running the Deprecation Processing program.
Note: Be aware that if you change this code, the system will not reassign previously posted costs to the new cost code.

##  Depreciation Cost Type

 Specify the EM cost type the system will assign to all depreciation cost-adjusting entries created when running the Deprecation Processing program.
Note: Be aware that if you change this code, the system will not reassign previously posted costs to the new cost type.

##  Calculations Required

 Indicate whether you will be allowed to close a period if depreciation has not been posted.

- Monthly – Depreciation must be posted for each month before you can close that month in GL.

- Annual – Depreciation must be posted annually before you can close the year in GL.

- None – No depreciation posting is required.

##  Post Costs to Components

 Check this box to allow equipment costs to be posted at the component level.
 Leave this box unchecked if equipment costs will not be posted at the component level.
Note: This flag only controls the default setting of the
 ‘Post Costs to Components’ option in EM Equipment. Overrides to this default must be set
 individually by equipment.

##  Allow GL Account Override

 Check this box to allow overrides to default GL accounts (as defined in EM Departments) when posting equipment costs and usage.
 Leave this box unchecked if not allowing overrides to GL accounts during posting.

##  Labor Cost Type

 Specify the EM cost type to which labor costs entered in EM Work Order Time Cards will be posted.

##  Allow Cost Code Change

 Check this box to allow overrides to the cost code for a work order when entering timecards (EM Maintenance Timecard Entry and PR Timecard Entry).
 Leave this box unchecked if not allowing overrides to the work order cost code when entering timecards.

##  Unattached Component Equipment No

 Specify the equipment number to be used when a component is not attached to a primary piece of equipment. Because the system will not allow a component to exist independently, this equipment number is used as a 'dummy' until the component is assigned to a primary piece of equipment.

##  Default Warranty Start Date

 Specify the date to use as the default Start Date when entering new warranties in EM Warranties.

- I-Installed Date – Use the warranty’s installation date (Date Installed) as the default.

- P-Purchase Date – Use the warranty’s purchase date (Date Purchased) as the default.

Note: If left blank, warranty Start Date defaults as null.

##  GL Adjustments Interface

 Select one of the options below to indicate how GL is to be updated when adjustment entries are posted.

- No Update - GL entries created when posting adjustment transactions will not be interfaced to GL.

- Summary - Enter Description text directly (max 60 char) - Adjustment entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Select from following options: - Create GL transactions for every adjustment entry.

 If you select this option, use the option box provided with this option to select the fields you want included as part of the GL transaction description. Available fields are:

- Co

- CostType

- Equip

- AdjDesc

- CostCode

- EMTrans

As you select each field, it is added to the Detail GL Description field below. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: Fields can be selected in any order and the GL transaction description will appear in the same order in GL.

##  Beginning WO Status

 Specify the status code (from EM Work Order Status Codes) that you want initially assigned to all work orders created using the EM Work Order Initialization or EM Work Order Edit programs.

##  Beginning Parts Status

 Specify the status code (from EM Work Order Parts Status) that you want initially assigned to all parts set up on work orders created in the EM Work Order Initialization or EM Work Order Edit programs.

##  Default Repair Type

 Specify the repair type (as defined in EM Work Order Repair Types) that you want initially assigned to all work orders created automatically using EM Work Order Initialization (e.g. “Scheduled Maintenance”).

##  Parts Cost Type

 Specify the EM cost type to which costs for parts (materials) on work orders will be posted.

##  Outside Repair Cost Type

 Specify the EM cost type to use for costs from work order items that are sent out for repair.

##  Allow Cost Posting to Items w/Status Flagged as Final

 Check this box to allow costs to be posted to work order items that are flagged with a 'Final' status (i.e. a status code assigned ‘Final’ type).
 Leave this box unchecked if not allowing costs to be posted to work order items with a 'Final' status.

##  Allow Cost Code Change

 Check this box to allow overrides to the cost code for a work order when entering timecards (EM Maintenance Timecard Entry and PR Timecard Entry).
 Leave this box unchecked if not allowing overrides to the work order cost code when entering timecards.

## Auto Sequence Work Order #

Check this box to have the system automatically generate work order numbers using the last company or shop work order number.

-  If using EM Company as the last work order option,
 the system will generate work order numbers based on the value specified in the
 Last
 Company W.O. # field.

- If using Shop as the last work order option, the
 system will generate work order numbers based on the Last WO#
 specified in EM Shops.

Note: The auto-sequence function is used during
 initialization (in EM Work Order Initialize) and when entering work orders manually (in EM
 Work Order Edit).
Leave this box unchecked if assigning work
 order numbers manually (in EM Work Order Edit and EM Work Order Initialize).

## Last Work Order Options

Indicate which option to use for automatically generating work order numbers.

- EM Company – Select this option to have the system automatically generate work order numbers based on the Last Company W.O. # specified for this company below.

- Shop – Select this option to have the system automatically generate work order numbers by shop. When selected, work order numbers will be assigned based on the Last WO# specified for the shop (in EM Shops) to which the work order is assigned.

Note: If multiple companies share the same shop group and are using this option, the system will search all of the companies for the highest work order number in existence for the specified shop, then assign the next sequential work order number.
Companies sharing the same shop group, but not using the auto-sequence by shop (i.e. are auto-sequencing by company), will be excluded when searching for the highest work order number for the shop. Auto-numbering for those companies will be based on the highest work order number for the company; this may result in multiple companies having the same work order numbers.

##  Last Company WO #

This field is only accessible if you selected
 the Auto Sequence
 Work Order # checkbox and the EM Company work order option.
 Enter the last work order number used for
 this EM company, up to 10 digits. For example, if you want numbering to start with 100,
 then enter 99 here. Once the initial number is entered, this field will be updated
 automatically each time a new work order number is assigned.

## Initialize all Standard Maintenance Group Items

Select this checkbox to initialize all items in a standard maintenance group not currently on an open work order, regardless of whether they are due for maintenance. When selecting equipment due for maintenance (in EM Work Order Initialize), the system will initialize all maintenance groups meeting the selection criteria and days / variances in advance, along with all associated maintenance items, regardless of whether they are due for maintenance.
Note: When selecting maintenance groups for initialization, the system will pull only those maintenance groups where at least one item is due for maintenance. Then when creating work orders, the system will initialize all SMG items, even if they are not due for maintenance.
Do not select this checkbox if you want to initialize only those maintenance items not currently on an open work order that are 'due' for maintenance.

## Always Initialize Linked Standard Maintenance Groups

Select this checkbox to initialize all linked standard maintenance groups not currently on an open work order, regardless of whether they are due for maintenance. When selecting equipment due for maintenance (in EM Work Order Initialize), the system will initialize all maintenance groups meeting the selection criteria, along with their child (linked) maintenance groups, regardless of whether the child groups meet the selection criteria or are due for maintenance.
Note: Initialization will exclude any child maintenance group already on an open work order.
Do not select this checkbox if you want to initialize only linked maintenance groups not currently on an open work order that are 'due' for maintenance.

##  Show All Work Orders

 Check this box to set the load/display default in EM Work Order Edit to show all work orders. If checked, all work orders (open and closed) will be loaded and available for display when using the scroll buttons at the bottom of the screen.
 Leave this box unchecked to set the load/display default in EM Work Order Edit to show only open work orders. If unchecked, only work orders with a status of Open will be loaded and available for display when using the scroll buttons.
Note: The default setting here can be overridden by
 checking/unchecking the Show All Work Orders option in the Options menu of EM Work Order
 Edit.

##  Liability Type

 Specify the liability type to which labor burden will be posted.

##  Burden Type

- A – Actual Burden. Select this option to update employee’s actual labor and burden to EM from Payroll.

- R – Override Rate. Select this option to calculate labor burden as a rate of the employee’s gross pay and add to labor costs when updating EM from Payroll. Specify the burden rate to the right.

##  Burden Rate

 Used only when burden type is ‘R - Override Rate’.
 Specify the rate to use when calculating burden for a mechanic when updating EM costs from Payroll.

##  Addon Rate

 Used only when burden type is ‘A – Actual Burden’.
 Specify the rate to use when calculating the additional mark-up to add on top of burden labor.

##  Liability Type

 Specify the liability type to which labor burden will be posted.

##  Burden Type

- A – Actual Burden. Select this option to update employee’s actual labor and burden to EM from Payroll.

- R – Override Rate. Select this option to calculate labor burden as a rate of the employee’s gross pay and add to labor costs when updating EM from Payroll. Specify the burden rate to the right.

##  Burden Rate

 Used only when burden type is ‘R - Override Rate’.
 Specify the rate to use when calculating burden for a mechanic when updating EM costs from Payroll.

##  Addon Rate

 Used only when burden type is ‘A – Actual Burden’.
 Specify the rate to use when calculating the additional mark-up to add on top of burden labor.

## GL Usage Interface

Select one of the options below to indicate how GL is to be updated when usage entries are posted.

- No Update - GL entries created when posting usage transactions will not be interfaced to GL.

- Summary - Enter Description text directly (max 60 char) - Usage entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail- Select from following options: - Create GL transactions for every usage entry. If you select this option, use the option box provided with this option to select the fields you want included as part of the GL transaction description. Available fields are:

- Co

- Equipment

- Rev Code

- Usg Type

- Job

- Date

- EMTrans

As you select each field, it is added to the Detail GL Description field below. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: The GL transaction description will appear in the same order as the order in which these fields are selected.
Note: The interface level selected here will also be used
 when updating Cost and WIP accounts for work completed equipment lines in SM Work Orders
 (Work Completed tab); however, the update will only occur if the EM interface box is checked in SM Company Parameters.

##  Usage: Summary GL Description

 Enter the transaction description that will be used when usage data is sent to GL at the summary level.

##  Usage: Journal

 Specify the GL journal to which usage entries will be posted.

## Allow Rate Change

Check this box to allow overrides to usage
 rates when entering usage transactions in EM Usage Posting. When checked, the Allow Posting
 Override checkbox is enabled in the rate setup forms (EM Revenue Rates by
 Category, EM Revenue Rates by Equipment, and EM Revenue Template), allowing you to specify
 at the category, equipment, and/or revenue template level whether to allow overriding usage
 rates.
Leave this box unchecked if not allowing rate
 changes when entering usage transactions. The Allow Posting Override option in EM
 Revenue Rates by Category, EM Revenue Rates by Equipment, and EM Revenue Template will be
 disabled, and the usage rate specified in these programs (based on hierarchy) will be used.

##  Revenue Breakdown Code

 Specify the revenue breakdown code to use as the default when setting up rates for revenue codes by category (in EM Revenue Rates by Category), or when overriding rates by equipment (in EM Revenue Rates by Equipment) or template (in EM Revenue Template).
Note: A code must be entered here even if you do not plan to use the Revenue Breakdown feature. This code is needed because each time a revenue code is established, the revenue breakdown must also be established. Whenever a revenue rate is entered (in any of the forms indicated above), the whole amount will automatically be assigned to this code.

##  UM for Hrs on Unit-Based Rev Code

 Enter the unit of measure that represents hours, as specified in HQ Units of Measure. This is the unit of measure to which the Time Units specified when entering usage for unit-based revenue codes will be posted.

##  GL Adjustments Interface

 Select one of the options below to indicate how GL is to be updated when adjustment entries are posted.

- No Update - GL entries created when posting adjustment transactions will not be interfaced to GL.

- Summary - Enter Description text directly (max 60 char) - Adjustment entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Select from following options: - Create GL transactions for every adjustment entry.

 If you select this option, use the option box provided with this option to select the fields you want included as part of the GL transaction description. Available fields are:

- Co

- CostType

- Equip

- AdjDesc

- CostCode

- EMTrans

As you select each field, it is added to the Detail GL Description field below. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: Fields can be selected in any order and the GL transaction description will appear in the same order in GL.

##  Adjustments: Summary GL Description

 Enter the transaction description that will be used when adjustment data is sent to GL at the summary level.

##  Adjustments: Journal

 Specify the GL journal to which adjustment entries will be posted.

##  GL Adjustments Interface

 Select one of the options below to indicate how GL is to be updated when adjustment entries are posted.

- No Update - GL entries created when posting adjustment transactions will not be interfaced to GL.

- Summary - Enter Description text directly (max 60 char) - Adjustment entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Select from following options: - Create GL transactions for every adjustment entry.

 If you select this option, use the option box provided with this option to select the fields you want included as part of the GL transaction description. Available fields are:

- Co

- CostType

- Equip

- AdjDesc

- CostCode

- EMTrans

As you select each field, it is added to the Detail GL Description field below. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: Fields can be selected in any order and the GL transaction description will appear in the same order in GL.

##  Adjustments: Summary GL Description

 Enter the transaction description that will be used when adjustment data is sent to GL at the summary level.

##  Adjustments: Journal

 Specify the GL journal to which adjustment entries will be posted.

##  GL Parts Interface

 Select one of the options below to indicate how GL is to be updated when parts (materials) are posted to work orders.

- No Update - GL entries created when posting parts/materials to work orders will not be interfaced to GL.

- Summary - Enter Description text directly (max 60 char) – Parts/materials entries will be summarized and one entry will be posted to GL for each unique GL account. Enter the description that will be used for each of these transactions in the Summary GL Transaction field below. Also, select items for the detail description. Even though the summary is chosen here, if an account is set up in the Chart of Accounts for interface detail, then that account will receive detail entries.

- Detail - Select from following options: - Create GL transactions for every parts/materials entry.

 If you select this option, use the option box provided with this option to select the fields you want included as part of the GL transaction description. Available fields are:

- Co

- CostType

- Equip

- WO

- PartCode

- WOItem

- PartDesc

- INLoc

- CostCode

- EMTrans

 As you select each field, it is added to the Detail GL Description field below. When the GL entry is made, the system pulls the data from each of the fields and creates the description from the information.
Note: Fields can be selected in any order and the GL transaction description will appear in the same order in GL.

##  Parts: Summary GL Description

 Enter the transaction description that will be used when parts/materials data is sent to GL at the summary level.

##  Parts: Journal

 Specify the GL journal to which parts/material entries will be posted.

## Misc Parts GL Acct

Required.
Specify the GL account to credit when posting
 miscellaneous parts/materials (in EM Work Order Parts Posting, EM Fuel Usage, or EM Cost
 Adjustments). This account will only be used when not validating materials (Validate
 Parts/Materials box is unchecked) and you are posting parts or materials not
 set up in HQ Materials. The subledger code for this GL account must be blank (null).

##  Display Last Used Date for Parts in AP/PO/EM

 Check this box to display the ‘last used date’ for parts on the AP Transaction Entry, PO Purchase Order Entry, and EM Work Order Parts Posting forms. When checked, transactions posted in the forms indicated above where the line type is ‘Equip’ or ‘Work Order’ will display the “Last Used Date of Part” label above the tab pages.
 Leave this box unchecked if you do not want the last used date of part information displayed on the AP Transaction Entry, PO Purchase Order Entry, and EM Work Order Parts Posting forms.

##  Validate Parts/Materials

 Check this box to validate all parts and/or materials against the HQ Materials file. When checked, parts and/or materials entered for a work order or cost adjustment must exist and be active in HQ Materials, PO Vendor Materials (vendor parts), or be cross-referenced to a valid and active HQ Material (in EM Equipment Parts).
 Leave this box unchecked to allow using non-valid parts and/or materials (those not set up in HQ Materials) on work orders or cost adjustment entries.

##  Use Tax on Parts/Materials

 Check this box to allow use tax on transactions posted to parts and/or materials (e.g. work orders, fuel posting, and cost adjustments).
 Leave this box unchecked if not allowing use tax on transactions posted to parts and/or materials.

##  Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following is a detailed list of the audit options.

- Company Parameters - This audit option is display only, and is always checked. Changes made to the EM Company Parameters program will be tracked in the Master Audit file.

- Equipment Master – Check this box to record changes
 made to equipment information (category/department assignments, meter readings,
 ownership info, components/attachments, equipment status, etc.) in EM Equipment.

- Equipment Warranty – Check this box to record changes made to warranty information in EM Warranties.

- Department GL - Check this box to record changes made to the GL accounts defined for departments in EM Departments.

- Asset Master – Check this box to record changes made to assets in EM Asset Setup, including asset life and value, deprecation method, and depreciation schedule calculations.

- Revenue Rates by Category – Check this box to record changes to revenue rates set up by category in EM Revenue Rates by Category. This includes changes to the revenue breakdown for each revenue code.

- Revenue Rates by Equipment – Check this box to record changes to revenue rates set up by equipment in EM Revenue Rates by Equipment. This includes changes to the revenue breakdown for each revenue code.

- Location Transfers – Check this box to record transfers of equipment from one location/job to another location/job in EM Location Transfers or EM Mass Location Transfers.

- Component Transfers – Check this box to record transfers of components from one piece of equipment to another in EM Component Transfers.

## Attach batch reports to HQ Batch Control

Check this box if the batch reports should be attached to the batch record that displays in the [HQ Batch Control](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form) form.
 The reports are stored using the Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment Options.

- The system will attempt to export batch reports before posting the batch. If the export is successful, it will then post the batch. However, if errors occur for any batch report, the system will display an error message and abort the posting process. You will need to correct the error before you can revalidate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users will only be able to access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

## Meter Updates: Equipment Usage

Specify the option to use for updating meters and reading dates when posting equipment usage in EM, MS, and/or PR.

- Update meters and reading date when new reading
 date is greater than last reading date — Select this option to update
 both the meter reading and the reading date for odometers and/or hour meters during
 usage posting when the new reading date (i.e. transaction date) is greater than the
 last reading date.

- Always update Meters. Never update Meter
 Reading Date — Select this option to always update odometers and/or
 hour meters when posting usage, regardless of the transaction date, and to never
 update reading dates. Updates to reading dates must be done manually in EM Meter
 Readings.

- Always update Meters. Update Reading Date when
 post date is greater than last reading date — Select this option to
 always update odometers and hour meters when posting usage, regardless of the
 transaction date, and to only update reading dates if the transaction date is greater
 than the last reading date.

Note: Regardless of which option you select, updates to hour
 meters will only occur if the Update Hour Meter box is checked for the
 posted revenue code (in EM Revenue Code, EM Revenue Rates by Category, or EM Revenue Rates
 by Equipment).
The update from EM Usage Posting will occur upon the creation of a batch record; however, updates from PR Timecard Entry and MS Ticket Entry will not occur until you post the batch.

## Meter Updates: Costs Adj and Parts Posting

Specify the option to use for updating meters and reading dates when posting cost adjustments and parts in EM.

- Update meters and reading date when new reading
 date is greater than last reading date - Select this option to update
 both the meter reading and the reading date for odometers and hour meters during cost
 adjustment and parts posting when the new reading date (i.e. transaction date) is
 greater than the last reading date.

- Always update Meters. Never update Meter
 Reading Date - Select this option to always update odometers and hour
 meters when posting cost adjustments and parts, regardless of the transaction date,
 and to never update reading dates. Updates to reading dates must be done manually in
 EM Meter Readings.

- Always update Meters. Update Reading Date when
 post date is greater than last reading date - Select this option to
 always update odometers and hour meters when posting cost adjustments and parts,
 regardless of the transaction date, and to only update reading dates if the
 transaction date is greater than the last reading date.

## Meter Updates: Fuel Posting

Specify the option to use for updating meters and reading dates when posting fuel usage in EM.

- Update meters and reading date when new reading
 date is greater than last reading date - Select this option to update
 both the meter reading and the reading date for odometers and hour meters during fuel
 posting when the new reading date (i.e. transaction date) is greater than the last
 reading date.

- Always update Meters. Never update Meter
 Reading Date - Select this option to always update odometers and hour
 meters when posting fuel usage, regardless of the transaction date, and to never
 update reading dates. Updates to reading dates must be done manually in EM Meter
 Readings.

- Always update Meters. Update Reading Date when
 post date is greater than last reading date - Select this option to
 always update odometers and hour meters when posting fuel usage, regardless of the
 transaction date, and to only update reading dates if the transaction date is greater
 than the last reading date.

## Job & Location Updates: Equipment Usage

Specify the option to use for updating jobs and locations (in EM Equipment) when posting equipment usage in EM, MS, and/or PR.

- Update Job. Remove Location when Job
 changes - When posting equipment usage, if the posted job does not
 match the job currently assigned to the equipment, the job will be updated for the
 equipment and the location cleared. If the job is the same, the location will be left
 intact.

- Update Job. Save Location even if Job
 changes - When posting equipment usage, if the posted job does not
 match the job currently assigned to the equipment, the job will be updated for the
 equipment. The location will always be left intact, regardless of whether the
 assigned job changes.

- Do not update Job or Location -
 When posting equipment usage, the job and location assigned to the equipment will
 always be left intact, regardless of whether the posting job is different.

## Document Type

The Document Type field on EM Company Parameters form, Workflow tab.

 Specify the type of document to which the workflow applies. Currently, PO-Purchase Order is the only option available.Note: You can have only one process for each document type.

Note: The workflow defined here overrides those defined in HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the EM Company Parameters form, Workflow tab.
Enter the workflow process to perform on purchase orders or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the PO-Purchase Order document type or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type. However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). You can assign these generic workflows to PO document types if applicable.

Note: The workflows defined here override those defined in HQ Company Setup.

##  Active

The Active checkbox on the EM Company Parameters form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Notes

The Notes field on the EM Company Parameters form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

##  Work Orders: Allow Cost Code Change

 Check this box to allow overrides to the default cost code when posting costs to a work order.
 Leave this box unchecked if allowing overrides to the cost code when posting costs to a work order.
Note: This option does not apply to entry of mechanics timecards (in PR Timecard Entry and EM Maintenance Timecard Entry). Changes to cost codes when entering mechanics timecards is determined by the ‘Allow Cost Code Overrides’ option designated for labor on the Info tab in EM Company Parameters.
