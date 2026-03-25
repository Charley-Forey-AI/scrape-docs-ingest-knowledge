---
title: "Field Definitions: JC Cost Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form/field-definitions-jc-cost-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form/field-definitions-jc-cost-projections-form"
---

# Field Definitions: JC Cost Projections Form

The following is a list of field descriptions for the JC Cost
 Projections form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Date

 Specify the date for which projections will be calculated.
Important: Changing projections for a prior month after you have calculated projections for a later month may cause the later projections to be incorrect. If you must recalculate projections for a prior month, make sure you recalculate all subsequent months. Date field shortcuts
T ort
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Job

Enter the job that you want to calculate projections on or press F4 to select it from a list.
Once a job is selected, the grid will display
 the phases and cost types on the selected job based on the options set up using the [JC Projection Options ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-projection-options-form) form. You can open this form by selecting File > Projection
 Options from the top of the form.
You can only select a soft- or hard-closed job
 if the Allow
 Posting to Soft-Closed Jobs/ Allow Posting to Hard-Closed Jobs  boxes
 on the Info tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form) are checked.
Note: Although not recommended, the system will allow the
 same job to be opened in multiple projection batches in the same month without affecting
 another user’s work - for example if you have large jobs where project managers need to do
 projections within their area of work at the same time. If you wish to use this feature,
 you need to check the Allow Jobs to be in Multiple Open Batches in the Same
 Month box on the Projections tab of [JC Company Parameters ](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form). However, when using this feature,
 be aware that if more than one user posts to the same phase/cost type, the last batch
 posted will determine the final values for the phase/cost type.
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections
Projection Options

## Item

This field is only accessible if sorting by contract item (i.e. Order By is set to ‘C-Contract Item’ in JC Projection Options).
Enter the contract item for which to review or update projections. The projections grid (above) will display all phases/cost types assigned to the specified contract item (based on the phase range specified in JC Projection Options). The Phase and Cost Type fields below will default the first phase/cost type for the contract item.
Note: The ‘Cycle Through Items or Phases One at a Time’ option (JC Projection Options) determines how you will cycle through records. If checked, the grid will show only phases/cost types assigned to this contract item. If unchecked, all phases/cost types for all contract items are included in the grid (in numeric order).
Tip: To cycle through each phase/cost type for the contract item, use the Page Down key (from either this field or the Phase field below). To move to the next contract item, use the left/right arrow buttons (/) to the left.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Phase

This field is only accessible if sorting by phase (i.e. Order By is set to ‘P-Phase’ in JC Projection Options).
Enter the phase for which to review or update projections. The projections grid (above) will display phases/cost types in numeric order and this field will default the first phase in the grid. The Cost Type field to the right will default the first cost type for the phase. The phases/cost types displayed are based on the phase range and cost types specified in JC Projection Options.
Note: The ‘Cycle Through Items or Phases One at a Time’ option (JC Projection Options) determines how you will cycle through records. If checked, the grid will show only cost types assigned to this phase. If unchecked, all cost types for all phases are included in the grid (in numeric order).
Tip: To cycle through each phase/cost type for the contract item, use the Page Down key (from either this field or the Phase field below). To move to the next contract item, use the left/right arrow buttons (/) to the left.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## % Complete

Disabled for U/C and U/HR, HR/U, ManDays, and CST/HR.
Use this column to override (plug) the percent complete for Units, Hours, and/or Costs for each phase/cost type on the job (up to 4 digits and 6 decimals; however, value must be less than 10000.)

- If hours are not being tracked for the selected cost type (flag in JC Cost Types), this field is disabled and values cannot be plugged.

- If you enter a value in this field for a phase/cost
 type with estimate values for units, hours, or costs, and no actual values, the
 system will compute the Over/Under, Remaining, and Final fields as 0.00.

Once you plug a value, all other values on that line (as well as all lines below it) will be recalculated by the system. In addition, an asterisk is placed in the P column (upper grid) to indicate plugged amounts and the line color changes to light yellow. If the Buy Out flag is checked for the phase and the plugged value does not equal the buy out value, the line color changes to blue. If a line’s remaining committed cost plus actual cost exceeds the projected cost, the line color changes to peach (only if using Actual projection method). (Tip: Right clicking the mouse will display an explanation of what the row colors represent.)
Note: You can use the Page Down/Page Up keys to plug amounts
 for remaining phase/cost types without having to select the phase/cost type first. For
 example, if you select a phase/cost type to work on and enter % Complete Units, you can
 then press the Page Down key to enter % complete units for the next phase/cost type. The
 cursor will remain in the % Complete Units field, allowing you to quickly plug amounts for
 all phase/cost types on the job.
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Over/Under

Disabled for U/C and U/HR, HR/U, ManDays, and CST/HR.
Use this column to override (plug) the amount your project will be over or under the current estimate amount. Enter amounts that are under the current estimate as a negative value (e.g. -2,500.00).
Note: If hours are not being tracked for the selected cost type (flag in JC Cost Types), this field is disabled and values cannot be plugged.
Once you plug a value, all other values on that line (as well as all lines below it) will be recalculated by the system. In addition, an asterisk is placed in the P column (upper grid) to indicate plugged amounts, and the line color changes to light yellow. If the Buy Out flag is checked for the phase and the plugged value does not equal the buy out value, the line color changes to blue. If a line’s remaining committed cost plus actual cost exceeds the projected cost, the line color changes to peach (only if using Actual projection method).
Tip: Right clicking the mouse will display an explanation of what the row colors represent.
Note: You can use the Page Down/Page Up keys to plug amounts for remaining phase/cost types without having to select the phase/cost type first. For example, if you select a phase/cost type to work on and enter Over/Under Units, you can then press the Page Down key to enter over/under units for the next phase/cost type. The cursor will remain in the Over/Under Units field, allowing you to quickly plug amounts for all phase/cost types on the job.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Remaining

 Use this field to override (plug) projected remaining amounts.
 If using the ManDays option (last line), the value entered here will be multiplied by the Hrs/ManDay (shown above the entry grid) to determine the remaining hours. For example, if Hrs/ManDay is set to ‘8’, and you change the remaining man-days from ‘10’ to ‘15’, the remaining hours will be increased to 120 (15 x 8). All other man-day and hours values (i.e. over/under and final) are recalculated accordingly.
 Once you plug a value, all other values on that line (as well as the lines below it) will be recalculated by the system. When you update the line, an asterisk is placed in the P column (upper grid) to indicate plugged amounts, and the line color changes to light yellow. If the Buy Out flag is checked for the phase and the plugged value does not equal the buy out value, the line color changes to blue. If a line’s remaining committed cost plus actual cost exceeds the projected cost, the line color changes to peach (only if using Actual projection method). (Tip: Right clicking the mouse will display an explanation of what the row colors represent.)
Note: The Hours and ManDays lines will be disabled for any cost type that is not tracking hours (defined in JC Cost Types). Also, you can use the Page Down/Page Up keys to plug amounts for remaining phase/cost types without having to select the phase/cost type first. For example, if you select a phase/cost type to work on and enter Remaining Units, you can then press the Page Down key to enter remaining units for the next phase/cost type. The cursor will remain in the Remaining Units field, allowing you to quickly plug amounts for all phase/cost types on the job. Set Remain UC
 Click this button to have the system automatically set the Remaining U/C for this phase/cost type to the current estimated or actual unit cost based on how you set the Select Which Unit Cost to Use for Remaining option selected in JC Company Parameters (Projections tab). If you selected ‘E-Current Estimate’, the system sets the Remaining U/C column equal to the Current Est’d U/C column. If you selected ‘A-Actual’, the system sets the Remaining U/C column equal to the Actual U/C column.
Note: In order for this feature to work, the current estimated unit cost or actual unit cost must not be zero, depending on which JC Company option applies. If there are no existing values, then clicking the Set Remain UC button will not change the remaining unit cost from its current value.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Final

 Use this field to override (plug) projected final amounts.
 If using the ManDays option (last line), the value entered here will be multiplied by the Hrs/ManDay (shown above the entry grid) to determine the final hours. For example, if Hrs/ManDay is set to ‘8’, and you change the final man-days from ‘100’ to ‘130’, the remaining hours will be increased to 1040 (130 x 8). All other man-day and hours values (i.e. over/under and remaining) are recalculated accordingly.
 Once you plug a value, all other values on that line (as well as all lines below it) will be recalculated by the system. When you update the line, an asterisk is placed in the P column (upper grid) to indicate plugged amounts, and the line color changes to light yellow. If the Buy Out flag is checked for the phase and the plugged value does not equal the buy out value, the line color changes to blue. If a line’s remaining committed cost plus actual cost exceeds the projected cost, the line color changes to peach (only if using Actual projection method). (Tip: Right clicking the mouse will display an explanation of what the row colors represent.)
Note: The Hours and ManDays lines will be disabled for any cost type that is not tracking hours (defined in JC Cost Types). Also, you can use the Page Down/Page Up keys to plug amounts for remaining phase/cost types without having to select the phase/cost type first. For example, if you select a phase/cost type to work on and enter Final Units, you can then press the Page Down key to enter final units for the next phase/cost type. The cursor will remain in the Final Units field, allowing you to quickly plug amounts for all phase/cost types on the job.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Buy Out

Check this box if the buy out is complete for
 this phase/cost type; that is, total commitments have been made through subcontracts,
 purchase orders, and/or material orders (applies to linked cost types as well). Initially
 defaults based on how you have set the Buy Out checkbox for the phase/cost type
 in JC Job Phases. If checked and the plugged value does not equal the buy out value (e.g.
 in a previous month you plugged a projected final, posted that projection, then later
 checked the buy out box, and now in a current projection batch have a discrepancy between
 the previous plugged value and the sum of Actual + Remaining Committed), the line color
 will change to light blue.
Leave this box unchecked if the buy out is not complete for this phase/cost type.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Seq

Enter a sequence number (1-9999999) for this projection detail line or enter N, New, or + to have the system auto-assign the next available sequential number for the job/phase/cost type.
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Action

 When adding new entries, this field defaults to A (Add) and cannot be changed.
 If this is an existing transaction (i.e., a projection detail line that was pulled into the current batch), specify the action for this entry.

- Change - Use this action to make
 changes to detail lines that have already been processed.

- Delete - Use this action to delete
 the detail line from the JC Projection Transaction Detail table (JCPR). This will
 eliminate the record from all future projection batches.

Note: Using the delete functions in the toolbar and Records menu will only delete the entry from the batch. Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Budget Code

 Enter the budget code (from JC Budget Codes) that applies to this projection detail line. Once entered, this detail line will default values defined for the budget code in JC Budget Codes (e.g. Description, Budget UM and, depending on budget code’s basis, Hrs/Unit, Cost/Hour, and/or Unit Cost/Rate).
Note: Defaults (other than description) only apply if the budget code’s Costing Level is ‘Detail’. Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC
 Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  PRCo

 This field only displays for labor-related cost types (i.e. JB Cost Type Category is ‘Labor’ in JC Cost Types).
 Required if entering craft/class or employee.
 Enter the PR company (set up in PR Company Parameters) that applies to this projection detail line.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Craft

The system only displays this field for labor-related cost types (the
 Cost
 Type field is set to Labor), and is only enabled if a PR company is
 specified for the detail line (PR Co field).
Enter the craft that applies to this
 projection detail line. Press F4 for a list of valid crafts set up in
 PR Crafts.
Once you enter a craft, the system displays a
 warning stating that you must enter a class in the Class field.
Note: Only enter a craft and class if this detail line does
 not apply to a specific employee. Once you enter a craft, the system disables the
 Employee field.
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Class

The system only displays this field for labor-related cost types (the
 Cost Type
 field is set to Labor), and is only enabled if a PR company is specified for the detail line (
 PR Co
 field).
Enter the class that applies to this projection detail line. Press
 F4
 for a list of classes (PR Craft Classes) that are set up for the craft that you specified in the
 Craft
 field.
If you entered a craft in the
 Craft
 field, you must enter a class here.
Note: Only enter a craft and class if this detail line does
 not apply to a specific employee. Once you enter a craft, the system disables the Employee
 field.
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Employee

 This field only displays for labor-related cost types (i.e. JB Cost Type Category is ‘Labor’ in JC Cost Types) and is only enabled if no craft/class is specified for the detail line.
 Enter the employee (from PR Employees) that applies to this projection detail line.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  EMCo

 This field only displays for equipment-related cost types (i.e. JB Cost Type Category is ‘Equipment’ in JC Cost Types).
 Required if entering an equipment code.
 Enter the EM company (set up in EM Company Parameters) that applies to this projection detail line.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Equipment

 This field only displays for equipment-related cost types (i.e. JB Cost Type Category is ‘Equipment’ in JC Cost Types) and is only enabled if an EM company is specified for the detail line.
 Enter the equipment (from EM Equipment) that
 applies to this projection detail line.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Description

Enter the description for this projection detail line, up to 60 characters.
Default value
If a budget code is entered for the detail line, defaults the budget code description.
If no budget code is entered and:

- line’s CT is ‘Labor’ and you specified a craft/class, defaults the class description. If you specified a craft but no class, or if no craft/class is specified, defaults as null.

- line’s CT is ‘Equipment’ and you specified an equipment code, defaults the equipment description. If no equipment is specified, defaults as null.

- line’s CT is not ‘Labor’ or ‘Equipment’, defaults as null.
Why is this field disabled?
The Projection Detail tab is only enabled when the
 Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are enabled
 based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Detail Month

Enter the month that applies to this projection detail line.
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  From Date

 Enter the beginning date in a range of dates to which this projection detail line applies.
Date field shortcuts
T ort
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  To Date

 Enter the ending date in a range of dates to which this projection detail applies.
Date field shortcuts
T ort
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC
 Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Number Of

 This field is enabled only for Labor,
 Equipment, and Burden cost types (i.e. the JB Cost Type Category is ‘Labor’, ‘Equipment’,
 or ‘Burden’ in JC Cost Types).
 If the line’s cost type is Labor and you
 specified a craft or craft/class, enter the number of employees of the specified craft or
 craft/class to which this projection detail line applies. If you specified an employee, you
 should not need to enter a value here; leave the default of 0.00.
 If the line’s cost type is Equipment and you
 specified an equipment code, enter the number of the specified equipment to which this
 projection detail line applies.
 If the line’s cost type is Burden, you should
 not need to enter a value here; leave the default of 0.00.
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Units

 Enter the number of units that apply to this projection detail line.
 For Labor and Equipment lines (those with cost types having a JB Cost Type Category of ‘Labor’ or ‘Equipment’), if you specified a budget code with a Costing Level of ‘Detail’ and a Basis of ‘Hour’, units refers to the number of time units, based on the UM. So, if the UM is Days, enter the number of days; if the UM is WEEK, enter the number of weeks; and so forth.
Note: The system multiplies units x hrs/unit x number of the craft, craft/class, or equipment specified in the Number Of field to determine the total hours for the detail line. Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Budget UM

 Display only, the unit of measure specified for the budget code in JC Budget Codes, depending on the basis. If the basis is ‘Hour’, this will be the Time UM; if basis is ‘Unit’, this will be the Work UM.
Note: If the budget code Costing Level is ‘Subtotal’ or ‘Total’, this field defaults as null, since no unit of measure is specified for these costing levels.
 If you did not specify a budget code, this field displays as null.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## UM

Enter the unit of measure for this projection detail line. Initially defaults the unit of measure as follows:

- If you specified a budget code with a Costing Level of ‘Detail’ and a basis of ‘Hour’, defaults the Time UM specified for the budget code in JC Budget Codes.

- If you specified a budget code with a Costing Level of ‘Detail’ and a basis of ‘Unit’, defaults cost type’s assigned unit of measure.

- If you specified a budget code with a Costing Level of ‘Subtotal’ or ‘Total’, defaults as null.

- If you did not specify a budget code, defaults the cost type’s assigned unit of measure.
Why is this field disabled?
The Projection Detail tab is only enabled when the
 Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are enabled
 based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Hrs/Unit

 This field is enabled only for Labor, Equipment, and Burden cost types (i.e. the JB Cost Type Category is ‘Labor’, ‘Equipment’, or ‘Burden’ in JC Cost Types).
 Enter the number of hours that makes up one unit of the specified UM (e.g. if UM is ‘DAY’, enter 8.00).
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Hours

 This field is enabled only for Labor, Equipment, and Burden cost types (i.e. the JB Cost Type Category is ‘Labor’, ‘Equipment’, or ‘Burden’ in JC Cost Types).
 Enter the number of hours for this projection detail line. Initially defaults a value based on units x hrs/unit x number of the craft, craft/class, or equipment specified in the Number Of field to determine the total hours for the detail line.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Cost/Hour

 Enter the cost per hour for this projection detail line. Initially defaults as follows:

- If an hour-based budget code is specified, defaults the rate specified for the budget code.

- If a unit-based budget code is specified, defaults as null (as no rate is specified for unit-based budget codes).

- If no budget code is specified, defaults as null.
Why is this field disabled?
The Projection Detail tab is only enabled when the
 Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are enabled
 based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Unit Cost

Enter the unit cost for this projection detail line. Initially defaults as follows:

- If you specified an hour-based budget code and:

- Labor or equipment cost type, defaults based on cost/hour x Number Of field

- Burden cost type, defaults from the cost/hour

- Material, Subcontract, or Other cost type, defaults as null

- If you specified a unit-based budget code and:

- Labor or equipment cost type, and you specified a cost/hour, defaults based on cost/hour x Number Of field. If you do not specify a cost/hour, defaults as null

- Burden cost type, defaults from the cost/hour

- Material, Subcontract, or Other cost type, and the Budget UM is equal to cost type UM, defaults the unit cost specified for the budget code in JC Budget Codes. If Budget UM is not equal to cost type UM, defaults as null
Why is this field disabled?
The Projection Detail tab is only enabled when the
 Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are enabled
 based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

##  Amount

 Enter the amount for this projection detail line. Initially defaults based on units x unit cost.
Plug Detail
 Once you have completed entering all detail
 lines for the phase/cost type, click the Plug Detail button below the grid to
 update the values to the projections grid (Info tab).
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections

## Notes

Use this field to enter any miscellaneous notes about this projection detail line. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Why is this field disabled?
The Projection Detail tab is only enabled when
 the Activate
 projection detail feature box is checked (PM Company Parameters form,
 Projections tab).
 The fields on the Projection Detail tab are
 enabled based on the JB cost type category associated with the selected cost type (JC Cost
 Types form, JC Cost
 Type Category field).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)JC Cost Projections
