---
title: "Field Definitions: SM Work Completed Misc Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form/field-definitions-sm-work-completed-misc-form"
---

# Field Definitions: SM Work Completed Misc Form

The following is a list of field descriptions for the SM Work Completed Misc form. These fields also apply to work completed Misc lines on the SM Work Order form, Work Completed tab.. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Line #

If you are entering this work completed line using the Work Completed grid, this field is display only. The system auto-assigns a line number once you save the work completed line.
If you are entering this work completed line
 using any of the work completed forms, enter N or + to add a new work completed line; the
 system will automatically assign the next sequential number.

## Has Adj

The Has Adj checkbox on the SM Work Orders form, Work Completed tab.
This field is display only and indicates whether the selected work completed line has been adjusted; that is, a cost adjustment line was applied to the selected work completed line. Cost adjustment lines appear with a Status of Adjustment.

## Create Adjustment

checkbox under the Cost Adjustment Info section of Work Completed Equipment, Labor, Miscellaneous, Inventory, and Purchase forms.
Select this checkbox to create a cost adjustment to an Equipment, Labor, Miscellaneous or Inventory Work Completed line.

## Orig Line #

The

This field also appears on the SM Work Completed form under the Cost Adjustment Info section.
Enter
 the original work completed line to adjust. Press F4 for a list of completed customer work
 order lines.
This
 field is enabled if you have selected either the Adj checkbox on the Work Completed tab
 or the Create
 Adjustment checkbox under the Cost Adjustment Info section of the SM Work
 Completed form.

## Dest SM Co

Dest SM Co # field on the SM Work Orders Work Completed tab.
This field also appears as the SM Co field under the Destination Adjustment section of the Cost Adjustment Info section of the SM Work Completed form.
Defaults to the SM company associated with
 Orig Line #
 field entry.
Enter the company the cost adjustment will be made to. Press
 F4
 for a list of SM companies from which to choose.
This field is enabled if you have selected either the
 Adj
 checkbox on the Work Completed tab or the
 Create Adjustment
 checkbox on the SM Work Completed form, under the Cost Adjustment Info section.

## Dest Work Order

Dest Work Order field on the SM Work Orders Work Completed tab.
This field also appears as the Work Order field under the Cost Adjustment Info drop-down section of the SM Work Completed form.
Enter a
 destination work order for the cost adjustment. Press F4 for a list of customer work orders
 from which to choose.
This
 field is enabled if you have selected either the Adj checkbox on the Work Completed tab
 or the Create
 Adjustment checkbox on the SM Work Completed form, under the Cost
 Adjustment Info section.

## Destination Scope Seq

Defaults to the scope associated with the
 Dest Work Order
 entry.
Enter scope for the cost adjustment will be made to. Press
 F4
 for a list of work order scopes from which to choose.
This field is enabled if you have selected either the
 Adj
 checkbox on the Work Completed tab or the
 Create Adjustment
 checkbox on the SM Work Completed form, under the Cost Adjustment Info section.

## Scope Seq

Required.
Enter the work order scope to which this work
 completed entry applies or press F4 to select from a list of valid scopes
 for the work order.
For work completed purchase lines (type 5-Purchase), this field defaults the scope sequence specified for the purchase order item (in SM Purchase Order Entry, PO Purchase Order Entry, or PO Item Distribution) and cannot be changed.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- If you enter a scope that is closed, a message displays indicating such and you will be unable to save the line. You must either reopen the scope or enter a different (open) scope.

- If you change the scope for a work completed line (labor, equipment, miscellaneous, or inventory lines only) and the new scope has a different rate template, the system will recalculate the Bill Rate and Bill Subtotal values.

- Once you bill this work completed line (i.e., the invoice is sent to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Technician

The Technician field on the SM Work Order form, Work Completed tab, and on the related SM Work Completed forms.
Required for 2-Labor line types only.
Enter the technician who performed the work
 associated with this work completed line or press F4 to select from a list of valid SM
 technicians.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- The technician specified here can be from any Payroll company; however, he/she must be set up in SM Technicians for the active SM company and must be flagged as "Active" in PR Employees. If the technician is flagged as "inactive", a warning displays and you will be unable to save the record.

- If this work completed line is associated with a closed scope (that is, a work order scope that was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field are only allowed via the SM Invoice Review form (accessed by double-clicking the invoice line).

Note: In order to enter work completed labor lines, you must be set up in VA User Profile with a PR Co and Employee designation, as well as the appropriate My Timesheet Permissions setting (1-Enter for Self or 2-Enter for Self and Others). If this is not done, you will receive an error message once you enter a value in this field. The message displayed depends on whether you are entering time for yourself or for another user. You will be unable to proceed until you set up the required information in VA User Profile. For more information, see [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions).

## Date

Required.
Enter the date for this work completed entry; typically the date the work was completed. Defaults the current date.
Work Completed Labor
 For work completed labor lines, the date entered here determines the start date for the timesheet (header) based on the pay period defined for the technician's payroll group. For example, if you have a pay period of 04/01/12 through 04/07/12, and you enter labor hours for 04/02/12, the timesheet created in PR My Timesheet will have a Start Date of 04/01/12, with time posted on 04/02/12.
However, because timesheets are in 7-day increments, if your pay periods span multiple weeks, the system will use the pay period start "day" to determine the start date for labor hours posted in each week of the pay period. For example, say your pay period runs 04/01/12 — 04/15/12. The start date, 04/01/12, falls on Sunday, so this is the "day" the system will use when determining the Start Date for timesheets posted in each week of the pay period. Therefore, labor hours posted on 04/01/12 through 04/07/12 will have a start date of 04/01/12; labor hours posted on 04/08/12 through 04/14/12 will have a start date of 04/08/12; and labor hours posted on 04/15/12 will have a start date of 04/15/12.
This date cannot be edited if you initiated the work completed line in PR Timecard Entry or you initiated the work completed line in SM Work Orders, but the corresponding timesheet has been approved and sent to a timecard batch.
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- You can make changes to this date as long as the new date falls within the specified Post Month. However, once you bill the work completed line (i.e. the invoice is sent to AR), you can only change this date via the SM Invoice Review form (accessed by double-clicking the invoice line).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

## Post Month

This field displays for Equipment, Miscellaneous, and Inventory lines only.
Required.
Enter the posting month (must be an open month) for this work completed line. For Equipment lines, this will become the batch month for equipment usage. For Misc lines, this will become the batch month for posting costs to GL. For Inventory lines, this will be the batch month for material usage (IN). For or purchase order receipts (PO).
For labor and equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.

- This field initially defaults the current month; however, if you change the date (in the Date field), this field will default the month from the newly entered date. Default may be overridden.

- Once you save the work completed line, this field is disabled and cannot be changed.

## Non-Billable

The Non-Billable checkbox on the SM Work Orders form, Work Completed tab.
Select this checkbox if this work completed line is not billable (that is, it will not be used to generate an invoice). The Bill Rate, Bill Subtotal, and and tax-related fields will be disabled and default as blank.
Leave this box unselected if this work completed line is billable and will be used to generate an invoice.
The enabling/disabling and defaulting of this field is as follows:

- If this work completed line is associated with a Flat Price work order scope that was manually added or generated from a work order quote or Time of Service, Flat Price agreement service, this field is disabled and defaults as checked. For these lines, work completed is covered in the flat price amount.

- If this work completed line is associated with a Time and Material work order scope that was manually added or generated from a work order quote or Time of Service, Rate Template agreement service, this field is enabled and defaults as unchecked.

- If this work completed line is associated with a Non-Billable work order scope that was manually added or generated from an Included in Agreement or Periodic agreement service, this field defaults as checked and is disabled. For these lines, work completed is covered by the agreement price (Included in Agreement or Periodic, Not Billed Separately services) or the agreement service price (Periodic, Billed Separately services).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- If this work completed line is associated with an agreement and you have set up spot work coverage for the agreement/service site, this checkbox defaults based on the line type and the spot coverage defined for the agreement/service site. For more information, see [Agreement Covered Spot Work](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-agreement-covered-spot-work).

## Ready To Bill

The Ready to Bill checkbox on the SM Work Orders form, Work Completed tab, and on the
 related SM Work Completed forms (such as SM Work Completed Equipment).
For Customer Work Orders only.
This field only displays if your login is
 associated with a reviewer on the work order; however, it does not display until after you
 have entered and saved the work completed line (either in the Work Completed grid or the
 related Work Completed form).
Select this checkbox to if the work completed
 item is ready to bill.
Note: This field is disabled if:

- The work completed item is marked as Non-Billable.

- The work completed item has already been billed.

## Reference No

Enter a reference number for this work
 completed line, up to 60 characters, if applicable. Initially defaults the reference number
 from existing work completed entries (for the work order) with the same work order scope
 and date, if applicable; otherwise, defaults as null.
You can use the reference number to represent
 any pertinent value; however, reference numbers are primarily intended as a mechanism for
 auto-selecting customer work orders for billing (in SM Work Order Billing) or reporting
 purposes. They are not used anywhere else in the system.Note: Although you cannot bill job
 work orders here in SM, you can use the reference number on job-related equipment lines
 for reporting purposes.If this work completed line is associated with a closed scope
 (i.e. the work order scope was closed after the work completed line was entered),
 this field is disabled and cannot be changed

## Standard Item

The Standard Item field on the SM Work Orders form, Work Completed tab.

This field displays for Miscellaneous lines only.
Enter the standard item for this work completed miscellaneous line or leave blank if no standard item applies to this line. Press F4 for a list of valid standard items.
 You will generally use this field to identify work order charges that are not specific to labor, equipment, or parts on a work order. If you select an existing standard item, it will be used to default the Cost Rate and Bill Rate values for this line.

- If the work order scope specified for this line has a Price Method of Non-Billable or Flat Rate, the Bill Rate will be set to blank (and cannot be changed), regardless of whether the standard item specifies a Bill Rate.

- If the work completed miscellaneous line originated in AP Transaction Entry, the Cost values will default from the AP transaction; the cost rate defined for the standard item will not be used. Changes to the cost rate must be handled directly in AP Transaction Entry.

- For work completed miscellaneous lines that originated in SM Work Orders, if the work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

Note: For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## SM Cost Type

The SM Cost Type field on the SM Work Orders form, Work Completed tab and related work completed forms.
Enter the cost type (from SM Cost Types) that applies to this work completed line. You must specify a cost type that is assigned an SM Cost Type Category that is valid for the work completed line type. For example, if you are entering a work completed Equipment line, you must assign a cost type with a category of E-Equipment. This does not apply to work completed miscellaneous lines, which will allow any SM cost type, regardless of the cost type category.
This field is disabled as follows:

- For Labor and Equip lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and can only be changed via PR Timecard Entry.

- For work completed Misc lines generated from an AP invoice (via AP Transaction Entry or AP Unapproved Invoice Posting), this field defaults from the invoice line and can only be changed via AP Transaction Entry.

- For work completed Purchase lines, this field defaults from the purchase order item and can only be changed via the SM Purchase Order Entry or PO Purchase Order Entry forms.

- For work completed lines associated with a closed scope (where the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- Once you create and process an invoice (send it to AR), this field is disabled; however, you can change the SM Cost Type via the SM Invoice Review form (by double-clicking the invoice line or selecting the invoice line and selecting Edit Record).

## JC Cost Type

The JC Cost Type field on the SM Work Orders form, Work Completed grid and on related Work Completed forms.

This field displays for job work orders only.
Required.
Enter the JC cost type (from JC Cost Types) for this work completed line. Initially defaults based on the work completed line type as follows:

- Equipment - If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type. If no JC cost type is assigned to the SM cost type or you did not enter an SM cost type, defaults the JC cost type assigned to the equipment (in EM Equipment). If no JC cost type is assigned to the equipment, defaults as blank and must be entered manually.

- Labor - If you entered a labor code for the line, defaults the JC cost type assigned to the labor code (in SM Labor Codes). If no JC cost type is assigned to the labor code or you did not enter a labor code, defaults the JC cost type assigned to the line's SM cost type. If no JC cost type is assigned to the SM cost type or you did not enter an SM cost type, defaults the JC cost type assigned to the earnings code associated with the lines SM pay type.

- Miscellaneous - If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type. If no JC cost type is assigned to the SM cost type or you did not enter an SM cost type, defaults as blank and must be entered manually.

- Inventory - If you entered an SM cost type for the line, defaults the JC cost type assigned to the SM cost type. If no JC cost type is assigned to the SM cost type or you did not enter an SM cost type, defaults the JC cost type assigned to the material (in HQ Materials). If no JC cost type is assigned to the material, field defaults as blank and must be entered manually.

- Purchase - This field defaults the JC Cost Type specified for the PO item and cannot be overridden, regardless of whether you specify an SM Cost Type that has a JC Cost Type assigned.

Note: For all line types except Purchase, this field defaults as blank if the cost type that would normally default for the line does not exist for the JC company associated with the work order. You will need to enter a cost type that is valid for the JC company.

The system uses the cost type specified here, in conjunction with the phase specified for the work order sequence, to post the costs to Job Cost (via the JC Cost Detail table).

### Closed Scopes

If the work completed line is associated with a closed scope (that is, the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.
For work completed lines not associated with a closed scope, once you create and process an invoice (send it to AR), edits to this field are only allowed via the SM Invoice Review form (accessed by double-clicking the invoice line or selecting the line and selecting Edit Record).

### GL Account Validation

When you enter a cost type here, the validation process checks that the phase (from the work order scope) or cost type is set up in JC Departments. This validation process is as follows:

- If an override for the phase exists in JC Departments, the GL accounts defined for the phase will be used, regardless of whether the cost type is set up for the department.

- If no phase override exists in JC Departments (Phase Overrides tab), the cost type entered here must be set up with the appropriate GL accounts in JC Departments (Cost Types tab) based on the following:

- If the phase exists on the job (locked and non-locked jobs), the cost type must be set up for the department assigned to the phase's contract item.

- If the phase does not exist for the job (non-locked jobs only), the cost type must be set up for the department assigned to the first contract item associated with the job.

- If the phase does not exist for the job (non-locked jobs only), but the phase matches the "number of valid characters" of a phase that does exist on the job, the cost type must exist for the contract item assigned to the valid job phase.

Note: These conditions apply regardless of how you set the JC interface checkbox in SM Company Parameters.

### Locked Phases vs. Non-Locked Phases

If the job specified for the work order is locked (that is, the Phases on this job are locked checkbox is selected in JC Jobs), the cost type specified here must be set up for the job/phase in JC Job Phases. If the cost type is not set up for the job phase, you can add it by pressing F5 from this field to access JC Job Phases. Once you set up the cost type and exit JC Job Phases, you can enter the cost type here.
If the job is not locked (the Phases on this job are locked box is not selected in JC Jobs), you can use any cost type defined for the phase in JC Job Phases or JC Phases.

## Cost Acct #

Enter the GL account to debit for costs related to this work completed line or accept the default cost account. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
The system determines when to update this account based on whether or not you are tracking WIP for the call type associated with the work completed line (i.e. the call type assigned to the referenced work order scope). For more information, see [SM Departments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form).
 Click on the following links for information about how the system determines the default cost account.
Cost Accounts by Division:
If you assigned a division to the work order scope and the division is assigned an 'alternate department' (in SM Divisions), the system determines the default cost account as follows:

- Uses the override Cost GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Cost GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Cost account for the cost type category (as defined on the Info tab in SM Departments).

- If no alternate department is assigned to the division, the system uses the department assigned to the service center to determine the default cost account (see below).

Cost Accounts by Service Center
If you did not assign a division to the work order scope (or if a division was assigned, but no alternate department is assigned to the division), the system will use the service center department to determine the default cost account as follows:

- Uses the override Cost GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Cost GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Cost account for the cost type category (as defined on the Info tab in SM Departments).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Revenue Acct #

Enter the GL account to credit when billing for this work completed line or accept the default revenue account. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system determines when to update this account based on whether or not you are tracking WIP for the call type associated with the work completed line (i.e. the call type assigned to the referenced work order scope). For more information, see [SM Departments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form).
 Click on the following links for information about how the system determines the default revenue account.
Revenue Accounts by Division:
If you assigned a division to the work order scope and the division is assigned an 'alternate department' (in SM Divisions), the system determines the default Revenue account as follows:

- Uses the override Revenue GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Revenue GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Revenue account for the cost type category (as defined on the Info tab in SM Departments).

- If no alternate department is assigned to the division, the system uses the department assigned to the service center to determine the default Revenue account (see below).

Revenue Accounts by Service Center
If you did not assign a division to the work order scope (or if a division was assigned, but no alternate department is assigned to the division), the system will use the service center department to determine the default Revenue account as follows:

- Uses the override Revenue GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Revenue GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Revenue account for the cost type category (as defined on the Info tab in SM Departments).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Cost WIP Acct #

Enter the GL account to debit for this work completed line or accept the default Cost WIP account. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
For equipment lines generated from a service timecard (in PR Timecard Entry), this field defaults from the timecard line and cannot be changed.
The system determines when to update this account based on whether or not you are tracking WIP for the call type associated with the work completed line (i.e. the call type assigned to the referenced work order scope). For more information, see [SM Departments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form).
 Click on the following links for information about how the system determines the default cost WIP account.
Cost WIP Accounts by Division:
If you assigned a division to the work order scope and the division is assigned an 'alternate department' (in SM Divisions), the system determines the default Cost WIP account as follows:

- Uses the override Cost WIP GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Cost WIP GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Cost WIP account for the cost type category (as defined on the Info tab in SM Departments).

- If no alternate department is assigned to the division, the system uses the department assigned to the service center to determine the default Cost WIP account (see below).

Cost WIP Accounts by Service Center
If you did not assign a division to the work order scope (or if a division was assigned, but no alternate department is assigned to the division), the system will use the service center department to determine the default Cost WIP account as follows:

- Uses the override Cost WIP GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Cost WIP GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Cost WIP account for the cost type category (as defined on the Info tab in SM Departments).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Revenue WIP Acct #

Enter the GL account to credit when billing for this work completed line or accept the default revenue account. Must be a valid account (set up in GL Chart of Accounts) with a subledger code of S-Service or null.
The system determines when to update this account based on whether or not you are tracking WIP for the call type associated with the work completed line (i.e. the call type assigned to the referenced work order scope). For more information, see [SM Departments](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form).
 Click on the following links for information about how the system determines the default revenue WIP account.
Revenue WIP Accounts by Division:
If you assigned a division to the work order scope and the division is assigned an 'alternate department' (in SM Divisions), the system determines the default Revenue WIP account as follows:

- Uses the override Revenue WIP GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Revenue WIP GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Revenue WIP account for the cost type category (as defined on the Info tab in SM Departments).

- If no alternate department is assigned to the division, the system uses the department assigned to the service center to determine the default Revenue WIP account (see below).

Revenue WIP Accounts by Service Center
If you did not assign a division to the work order scope (or if a division was assigned, but no alternate department is assigned to the division), the system will use the service center department to determine the default Revenue WIP account as follows:

- Uses the override Revenue WIP GL Account defined for the specified cost type category/call type/cost type. If no override defined for the cost type category/call type/cost type, will use the override defined for the cost type category/cost type or cost type category/call type, respectively.

- If no override Revenue WIP GL Account is found for the cost type category/call type/cost type, cost type category/cost type, or cost type category/call type, the system will use the standard Revenue WIP account for the cost type category (as defined on the Info tab in SM Departments).

- If this work completed line is associated with a closed scope (i.e. the work order scope was closed after the work completed line was entered), this field is disabled and cannot be changed.

- For work completed lines not associated with a closed scope, once you create and process an invoice (i.e. send it to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Cost Quantity

The Cost Quantity field on the SM Work Completed Misc and Inventory forms.

Enter the cost quantity for this work completed line.
This field defaults as follows:

- If this line was entered on the Work Completed grid in SM Work Orders, this field defaults the value entered in the grid.

- If this line is being added in this form, this field defaults as blank.

- If this is a work completed miscellaneous line that originated in AP Transaction Entry, this field is disabled and cannot be edited.

Note: Once you bill this line (that is, you've sent the invoice to AR), edits to this field are only allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).

## Cost Rate

The Cost Rate field on the SM Work Orders form, Work Completed tab.

Display only.
For lump sum (LS) items, this field is blank. For unit-based items, this field defaults based on the work completed line type as follows:Equipment LinesThe Cost Rate defaults from EM Revenue Rates by Equipment or EM Revenue Rates by Category (if no rate is defined at the equipment level), depending on the equipment and revenue code specified for the line. The system multiplies the Cost Rate by either the Time Units (if hour-based revenue code) or the Work Units (if unit-based revenue code) to derive the cost total (Actual Cost), which cannot be changed.Labor LinesThe Cost Rate defaults based on the technician and pay type specified on the line, as well as the cost method specified for the pay type as follows:

- If the cost method is Multiplier, the Cost Rate is a calculation of the technician's pay rate (from SM Technicians) x the pay type's factor. For example, if the pay rate is $55 and the factor is 1.5, the Cost Rate will be $82.50.

- If the cost method is Dollar Rate, the Cost Rate defaults the rate specified for the pay type in SM Pay Types.

Note: The system calculates the Cost Hrs x Cost Rate and displays the value in the ​Total Projected Cost​ field. Once payroll is processed and the employee paid, the system populates the Total Actual Cost field with the actual amount paid to the employee.
Miscellaneous LinesThese lines default a Cost Rate as follows:

- For Misc lines generated from an AP transaction, this field defaults as follows:

- If you did not apply taxes or a Misc Amt to the AP transaction, this field defaults equal to the Cost UC.

- If you applied taxes and/or a Misc Amt to the AP transaction, this field includes the posted tax and/or Misc Amt (calculated as Total Actual Cost / Cost Qty).For example, say the AP transaction Units=100, the Gross=1,000, the Misc Amt=50, and the Tax Amt=100, resulting in a Total Actual Cost of $1,150. In this case, the Cost Rate for the resulting Misc line will equal $11.50 ($1,150 / 100).

- For Misc lines entered directly in SM (via the Work Completed grid or the SM Work Completed Misc form) with no taxes applied, this field defaults equal to the Cost UC. If you applied cost taxes to the line, this field includes the tax amount (calculated as Total Actual Cost / Cost Qty).

Inventory LinesThe Cost Rate defaults as follows:

- If the work completed line does not include taxes, this field defaults equal to the Cost UC.

- If the work completed line includes taxes, this field includes the tax amount (calculated as Total Actual Cost / Quantity).

Purchase LinesThe Cost Rate defaults the unit cost from the purchase order item. However, if the purchase order item includes tax (Sales or Use), the Cost Rate for the resulting work completed purchase line includes the tax amount. For example, if the PO item is posted with 100.000 units, a unit cost of 5.00000, and tax of 50.00, the Cost Rate for the resulting work completed purchase line would be 5.500 (Total + Tax / Units). For purchase order items with a UM of LS (that is, material is non-valid or no material was specified), this field defaults as 0.00, regardless of whether you post tax to the line or not.

### Value Added Tax (VAT)

If you entered a Provincial Sales Tax (PST) code, the cost rate includes the PST amount. If you entered a Goods and Services Tax (GST) code, the cost rate excludes the GST amount. For multi-level tax codes that include both PST and GST, only the PST portion is included in the tax amount.

## Billable Quantity

The Billable Quantity field on the SM Work Completed Misc and Inventory forms.
Enter the billable quantity for this work completed line.
If you are entering this work completed line here, this field defaults the quantity specified in the Cost Qty field. If you entered this line on the Work Completed grid in SM Work Orders, defaults the value specified in the grid.
Note: This field is disabled if:

- the Non-Billable checkbox is selected for the work completed line. In this case, this field defaults to blank.

- the work completed line is for a job work order with a Costing Method of Actual Cost. The value in this field is set equal to the Cost Quantity.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Rate

The Bill Rate field on the SM Work Order form, Work Completed tab and on the related SM Work Completed forms.
Enter the billable rate for the work completed line or accept the default rate.

### Customer Work Orders

For all work completed lines posted to a Flat Price or Non-Billable work order scope, this field defaults as blank and is disabled.
 If you manually select the Non-Billable checkbox (for a work completed line), this field defaults as blank and is disabled, regardless of the scope's price method.
For work completed lines posted to a Time and Material work order scope, this field defaults as follows:
Equipment, Labor, and Misc LinesIf you entered units for the work completed line, this field defaults as Bill Subtotal / Bill Quantity. If you did not enter units for the work completed line (that is, you entered a lump sum amount), this field defaults as blankInventory LinesIf you entered units for the work completed line, this field defaults based on the Material Rates: Type and Materials Rates: Basis settings as follows:

- For scopes assigned a rate template with a Cost basis (Actual, Standard, Average, or Last):

- If the Type is Markup or Discount and no INCo/Location is specified, the bill rate defaults as Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively)

- If the Type is Markup or Discount and an INCo/Location is specified, the bill rate defaults as the selected Basis +/- (Basis x Markup/Discount %, respectively). For example, if the Basis is Average Cost, the bill rate defaults as Avg Unit Cost (from IN Location Materials) +/- (Avg Unit Cost x Markup/Discount %, respectively).If the Basis is Actual Cost, this field calculates as Total Actual Cost +/- (Total Actual Cost x Markup/Discount %, respectively)

- For scopes assigned a rate template with a Price basis:

- If the Type is Markup or Discount and no INCo/Location is specified, the bill rate defaults as Standard Unit Price (from HQ Materials) +/- (Standard Unit Price x Markup/Discount %, respectively)

- If the Type is Markup or Discount and an INCo/Location is specified, the bill rate defaults as Std Unit Price (from IN Location Materials) +/- (Std Unit Price x Markup/Discount %, respectively)

Purchase LinesIf you entered units for the work completed line, this field defaults as Bill Subtotal / Bill Quantity x ECM (1, 100, 1000). If you did not enter units for the work completed line, this field defaults as blank

### Job Work Orders

For all line types, this field defaults based on the Costing Method (Actual Cost or Markup) specified for the work order.

- Actual Cost - For all work completed line types, if you selected this costing method, the system sets the Bill Rate equal to the Cost Rate and disables this field. The only way to change this value is to change the Cost Rate for the line.

- Markup - If you selected this costing method, the Bill Rate defaults in the same manner as Customer Work orders. See the Customer Work orders section above.

### Agreement Work Orders

If the work completed line is associated with a Flat Price or Non-Billable scope or you have manually selected the Non-Billable checkbox for the line.
If the work completed line is associated with a Time and Material scope and the Agreement Rates checkbox is selected for the work completed line, this field is disabled and defaults a value based on the rate template assigned to the agreement. If the Agreement Rates checkbox is unselected, this field is enabled and defaults a value based on the rate template assigned to the agreement service (generated scopes) or work order scope (manually added scopes). May be overridden.
If the work completed line is associated with a non-agreement scope (manually entered with no agreement assigned), but you entered an agreement at the work completed line level, this field defaults as follows:

- If you selected both the Non-Billable and Agreement Rates checkboxes for the work completed line, this field is enabled and defaults a value from the rate template assigned to the work order scope. May be overridden.

- If you selected the Non-Billable checkbox for the work completed line, this field is disabled and defaults as blank.

- If you selected the Agreement Rates checkbox for the work completed line, this field is disabled and defaults based on the rate template assigned to the agreement.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Subtotal

The Bill Subtotal field on the SM Work Orders form, Work Completed tab and SM Work Completed forms.
For SM Work Completed Equipment and SM Work Completed Labor forms, this field shows as Billable Total.
For work completed lines referencing a Non-Billable or Flat Price scope,or where the Non-Billable checkbox is manually selected for the work completed line, this field defaults as blank and is disabled.
For work completed lines posted to a Time and Material scope, this field defaults as follows:
Equipment / Labor LinesDefaults as Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %).Miscellaneous LinesDefaults are as follows:If the work completed line is posted to a non-material SM Cost Type, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)
If the work completed line is material-related (posted to a material-related SM Cost Type), this field defaults as follows:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %).

For Miscellaneous lines posted in AP Transaction Entry:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively). This applies to transaction lines without a material, with an HQ Material, or with a non-HQ Material.

- If the scope's rate template has a type of Markup or Discount and a Price basis, and a valid HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, but no material is specified or a non-HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)

Inventory LinesFor Inventory lines, the Bill Subtotal is a calculation of the work completed line's Bill Rate x Bill Qty, with the Bill Rate being based on unit rates from HQ Materials or IN Location Materials. Calculations are as follows: Scopes assigned a rate template with a Cost basis (Actual, Std, Avg, Last):

- If you specify an HQ Material (no INCo/Location), this field defaults as the Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively) x Bill Qty.

- If you specify an INCo/Location, this field defaults as Basis +/- (Basis x Markup/Discount %, respectively) x Bill Qty. For example, if the basis is Avg Unit Cost, the calculation will be Avg Unit Cost (from IN Location Materials) +/- (Avg Unit Cost x Markup/Discount %) x Bill Qty.

- If the Cost basis is Actual, this field defaults as Cost Rate +/- (Cost Rate x Markup/Discount %, respectively) x Bill Qty.

Scopes assigned a rate template with a Price basis:

- If you specify an HQ Material (no INCo/Location), this field defaults as the Std Unit Cost (from HQ Materials) +/- (Std Unit Cost x Markup/Discount %, respectively) x Bill Qty.

- If you specify an INCo/Location, this field defaults as Std Unit Price (from IN Location Materials) +/- (Std Unit Prices x Markup/Discount %, respectively) x Bill Qty.

Purchase LinesDefaults are as follows:

- If the scope's rate template has a type of Markup or Discount and a Cost basis (Actual, Std, Avg, Last), this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively). This applies to transaction lines without a material, with an HQ Material, or with a non-HQ Material.

- If the scope's rate template has a type of Markup or Discount and a Price basis, and a valid HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) +/- (Total Actual Cost * Template Markup/Discount %, respectively)

- If the scope's rate template has a type of Markup or Discount and a Price basis, but no material is specified or a non-HQ Material is specified, this field defaults a value of Total Actual Cost (incl tax) + (Total Actual Cost * Template Markup %)

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Type

The Bill Tax Type field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.

### Customer Work Orders

For work completed lines posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.
For work completed lines posted to a T-Time and Material work order scope, accept the default value or enter the billing tax type for this work completed line.

- 1-Sales

- 3-VAT

For Equip and Labor lines, if the SM Cost Type is taxable, this field defaults the Bill Tax Type from the work order scope or as blank if the work order scope Tax Type is blank. The tax type also defaults as blank if you did not enter a cost type for the work completed line or if the cost type is not taxable.
For Misc, Inventory, and Purchase lines, this field defaults as indicated in the table below. The Tax Option Override options are defined as follows:

- blank

- N=Not Taxable

- P=Taxable at Purchase Only

- B=Taxable at Billing Only

- M=Taxable at Purchase/Markup at Billing

- F=Full Tax at Purchase and Billing

Work Completed SM Cost TypeWO Scope Tax Option OverrideBill Tax TypeCan Override?
blankblank, N, P, B, M, F Defaults as blankYes
Non-Taxableblank, N, P, B, M, FDefaults as blankYes
TaxableblankSystem uses the scope's Call Type Tax Option to determine taxability. If the call type's Tax Option is blank, N, or P, this field defaults as blank.If the call type's Tax Option is B, M, or F, this field defaults the Tax Type from the work order scope.
If the work order scope Tax Type is blank, this field defaults as blank.
Yes
N or PDefaults as blankYes
B, M, F Defaults the Tax Type from the work order scope. If the work order scope Tax Type is blank, this field defaults as blank.Yes

### Agreement-Related Work Orders

When you generate an agreement work order, the Price Method for the resulting work order scopes are set as follows:
Agreement Service Pricing Method: Work Order Scope Price Method
I - Included in AgreementNon-Billable
P - Periodic, Billed SeparatelyNon-Billable
P - Periodic, Not Billed SeparatelyNon-Billable
T - Time of Service, Flat RateFlat Price
T - Time of Service, Rate TemplateTime and Materials

For work completed lines posted to the Non-Billable and Flat Price scopes, the Bill Tax Type field defaults as blank and cannot be changed.
For work completed lines posted to a Time and Materials scope, the Bill Tax Type defaults as shown in the Customer Work Orders table above.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, the Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Code

The Bill Tax Code field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.

### Customer Work Orders

For work completed lines posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.
For work completed lines posted to a T-Time and Material work order scope, accept the default value or enter the tax code for this work completed line. Must be a valid tax code for the specified tax type.
For Equip and Labor lines, this field defaults the Bill Tax Code from the work order scope or as blank if the work order scope Tax Code is blank. The tax type also defaults as blank if you did not enter a cost type for the work completed line or if the cost type is not taxable.
For Misc, Inventory, and Purchase lines, this field defaults as indicated in the table below. The Tax Option Override options are defined as follows:

- blank

- N=Not Taxable

- P=Taxable at Purchase Only

- B=Taxable at Billing Only

- M=Taxable at Purchase/Markup at Billing

- F=Full Tax at Purchase and Billing

Work Completed SM Cost TypeWO Scope Tax Option OverrideBill Tax CodeCan Override?
blankblank, N, P, B, M, F Defaults as blankYes
Non-Taxableblank, N, P, B, M, FDefaults as blankYes
TaxableblankSystem uses the scope's Call Type Tax Option to determine taxability. If the call type's Tax Option is blank, N, or P, this field defaults as blank.If the call type's Tax Option is B, M, or F, this field defaults the Tax Code from the work order scope.
If the work order scope Tax Code is blank, this field defaults as blank.
Yes
N or PDefaults as blankYes
B, M, F Defaults the Tax Code from the work order scope. If the work order scope Tax Code is blank, this field defaults as blank.Yes

Note: Although work completed purchase lines are generated from purchase orders entered in SM Purchase Order Entry or PO Purchase Order Entry, the billable tax code does not default from the related purchase order item. Therefore, the tax code for the work completed line may differ from the tax code on the purchase order item.

Note: If you enter a tax basis of 0.00 or if the tax code's rate is set to 0.00, the system sets the Tax Amount to 0.00; however, the Tax Type, Tax Code, and Tax Basis designations are left intact.

### Agreement-Related Work Orders

When you generate an agreement work order, the Price Method for the resulting work order scopes are set as follows:
Agreement Service Pricing Method: Work Order Scope Price Method
I - Included in AgreementNon-Billable
P - Periodic, Billed SeparatelyNon-Billable
P - Periodic, Not Billed SeparatelyNon-Billable
T - Time of Service, Flat RateFlat Price
T - Time of Service, Rate TemplateTime and Materials

For work completed lines posted to the Non-Billable and Flat Price scopes, the Bill Tax Code field defaults as blank and cannot be changed.
For work completed lines posted to a Time and Materials scope, the Bill Tax Code defaults as shown in the Customer Work Orders table above.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Basis

The Bill Tax Basis field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.
Applies only to lines with a Tax Type and Tax Code specified.
Enter the tax basis amount for this work completed line or accept the defaulted amount.
Note: If you enter a bill tax basis of 0.00, the system sets the bill tax amount to 0.00; however, the Billing Tax Type, Tax Code, and Tax Basis designations are left intact.

The following describes the default behavior for this field:

- If the work completed line is posted to a N - Non Billable or F - Flat Price work order scope, this field defaults as blank and cannot be changed.

- If the work completed line is posted to a Time and Material work order scope and the Tax Type and Tax Code are blank, this field defaults as blank.

- If the work completed line is posted to a Time and Material work order scope and you entered a Tax Type and Tax Code, this field defaults as shown below.

Equipment and Labor LinesDefaults the Bill Qty x Bill Rate.
Miscellaneous, Inventory, and Purchase LinesFor these work completed lines, this field defaults based on the Tax Option Override specified for the work order scope and whether you entered units or a lump sum amount for the work completed line.
 If the work order scope's Tax Option Override is blank, the system uses the Tax Option specified for the scope's assigned call type. If the call type's Tax Option is blank, this field defaults as blank.
Tax Option Override/Tax OptionUnit-based?Default
Note: Inventory lines do not allow entering lump sum amounts. Therefore, the non-unit based descriptions apply only to work completed Misc and Purchase lines.

N=Not TaxableP=Taxable at Purchase Only
Yblank
Nblank
B=Taxable at Billing OnlyF=Full Tax at Purchase and Billing
YBill Quantity x Bill Rate
N (Misc)Total Actual Cost (incl tax) + (Total Actual Cost x Template Markup/Discount %)*

N (Purchase)Total Projected Cost (incl tax) + (Total Projected Cost x Template Markup/Discount %)*
M=Taxable at Purchase/Markup at BillingYIf Bill Qty is >= Cost Qty, the Bill Tax Basis is calculated as:Bill Subtotal - (Cost Tax Basis + Cost Tax Amt)
If Bill Qty is < Cost Qty, the Bill Tax Basis is calculated as:
Bill Subtotal - ((Cost Tax Basis + Cost Tax Amt) * (Bill Qty / Cost Qty))
Note: If you did not capture taxes when recording costs, there is no credit to apply to the transaction at billing; therefore, the bill tax basis is calculated using the full billing subtotal, not just the markup.

N (Misc)If the Bill Qty is blank and the Bill Subtotal <= 0, then the Bill Tax Basis is set to 0.00If the Bill Qty is blank and the Bill Subtotal > 0, then the Bill Tax Basis is set equal to the Bill Subtotal.

N (Purchase)
* If the work completed line is posted to a non-material SM Cost Type, the system uses the Non-Material Purchases: Markup Percent specified for the rate template. If the work completed line is posted to a material-related SM Cost Type, the system uses the material rate type and basis defined for the template to determine the template markup or discount percent to use. For more information, see [Material Rates: Type](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form/field-definitions-sm-rate-template-form#ID-00043a13--en) and [Material Rates: Basis](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form/field-definitions-sm-rate-template-form#ID-00043a23--en).

Note: The system uses the Tax Option Override assigned to the work order scope to determine the taxability/default behavior for work completed lines. If the work order scope's Tax Option Override is blank, the system uses the Tax Option specified for the scope's assigned call type to determine taxability/tax defaults. If the call type's Tax Option is blank, all bill tax fields default as null and must be entered manually.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## Bill Tax Amt

The Bill Tax Amt field on the SM Work Orders form, Work Completed tab, and on the related work completed forms.
This field defaults as blank and is disabled if the Non-Billable checkbox is selected for the work completed line.
If you entered a bill tax type and tax code for the work completed line, this field defaults the Bill Tax Amt as follows:

- If the bill tax basis is not 0.00, the system defaults the bill tax amount as a calculation of the tax basis times the tax rate defined for the tax code.

- If the bill tax basis is not 0.00, but the bill tax code has a rate of 0.00, the bill tax amount is set to 0.00; however, the system leaves the specified Bill Tax Type, Bill Tax Code, and Bill Tax Basis designations intact.

- If the bill tax basis is 0.00, the system sets the tax amount to 0.00, but leaves the specified Bill Tax Type, Bill Tax Code, and Bill Tax Basis designations intact.

For Misc, Inventory, and Purchase lines, you can override the default if needed; however, if you change the bill tax amount, the Bill Tax Basis is not recalculated.
For Equipment and Labor lines, this field is disabled.
Note: When you generate an invoice that includes this work completed line (T&M scopes only), the system recalculates the bill tax amount based on the tax rate applicable at the time of bill, if the date on the work completed line is falls before the tax rate Effective Date and the rate has changed for the specified tax code. If it differs from the amount calculated for the work completed line at the time of posting, the amount in this field is updated accordingly.

### Job Work Orders

You can only enter cost taxes for work completed lines associated with a Job work order. Therefore, all Bill Tax fields default as blank and are disabled.

Once you bill a work completed line, edits to this field are only allowed using the Edit Record option in SM Invoice Review or SM Agreement Invoice Review (agreement work orders). Edits are updated to the invoice and the related work completed line.

## No Charge

Select this checkbox if the customer/service site will not be charged for the work associated with this work completed entry.
Note: Checking this box does not clear the cost/price information; although the customer/service site will not be charged for the work, the cost/price information will be included on the invoice.
Do not select this checkbox if the customer/service site will be charged for the work associated with this work completed entry. (Default setting).
Once you bill this work completed line (i.e., the invoice is sent to AR), edits to this field will only be allowed via the SM Invoice Review form (by double-clicking the invoice line or selecting the line and clicking Edit Record).
