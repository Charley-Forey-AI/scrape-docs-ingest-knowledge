---
title: "Field Definitions: PM Cost Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form/field-definitions-pm-cost-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form/field-definitions-pm-cost-projections-form"
---

# Field Definitions: PM Cost Projections Form

The following is a list of field descriptions for the PM Cost
 Projections form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Projection Date

 Enter the date of the cost projections. The date entered in this field determines the batch month that will be used when the projections are posted.
Select an existing batch
The PM Cost Projections form uses a batch process. Only one project can be included in each batch.
Press F4 in the Projection Date field to see a list of the existing projection batches. This allows you to select an existing batch that you have created, or a batch that has been created by another user.
There can only be one user in each batch.
Delete an existing batch
To delete an existing batch, open the batch and then select Tasks >  Clear Projections from the toolbar at the top of the PM Cost Projection form.
Date field shortcuts
T or t
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
Just like with +, you can enter any value after the -, for example you can enter -7 to set the date to the previous week.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related information

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Project

 Enter a job/project number or press
 F4
 to select one from a list.
Once the Projection Date and Project fields
 are complete, all of the projection codes set up on the selected project will populate in
 the lower portion of the form.
Cost projections is a batch process
The PM Cost Projections form uses a batch process. Only one project can be included in each batch.
Press F4 in the Projection Date
 field to see a list of the existing projection batches. This allows you to select an
 existing batch that you have created, or a batch that has been created by another user.
Only interfaced projects can be selected
Only projects that have been interfaced with
 the JC module can be selected in the Project field.
Delete an existing batch
To delete an existing batch, open the batch
 and then select Tasks > Clear
 Projections from the toolbar at the top of the PM Cost Projection form.
Single project in multiple batches
If the Allow projects to be in multiple open projections in
 the same month box is checked (PM Company Parameters> Projections tab), a
 project can be in multiple open cost projection batches.
When this box is not checked, you won't be able to select a project if another user has the project in an open PM Cost Projections batch for the same date.

Related information

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Projection Code - Projection Code

 You cannot change the value in this field.
Once the Projection Date and Project fields are complete, all of the projection codes set up on the selected job will populate in the lower portion of the form.
Projection codes are set up on a project using the [PM Projection Codes](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form) form.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

Related information

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

## Projection Code - Percent Complete Hours

 Use this field to override (plug) the percent complete for hours.

Actual HoursProjected Final Hours
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in the Actual and Actual + Committed Cost column. One of these columns will display depending on the projection method selected in the PM Cost Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form
When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Over / Under Hours

Use this column to override (plug) the amount your project will be over or under the current estimate amount. Enter a negative value if the amount is under the current estimate, for example -2,500.00.
Projected Final Hours
- (Current Estimate + Included Cost)

When this field displays on the Grid tab of the PM Cost Projection form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
Green or red?
If the Display Positive/Negative Values in Color box is checked (PM Cost Projection Options form), NEGATIVE numbers are in green (these are values that are under) and POSITIVE numbers are in red (these are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projection tabs> Spread Option field):

- Protated- The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code- The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is
 not checked (Projections tab> Columns For Entry section). For more information, see
 [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Projected Final Hours

Use this field to override (plug) projected final hours.
This field is the difference between the projected hours at completion and the previously projected hours at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Remaining Hours

Use this field to override (plug) projected remaining hours.
This field is the difference between the projected final hours and the actual hours (invoiced in the AP module).
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are
 distributed in one of the following ways (PM Company Parameters> Projections
 tab> Spread Option
 field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based
 on the spread percentage set up on each phase/cost type (PM Projection
 Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
 Why is this field disabled?
This field is disabled if the Remaining box on the PM Company Parameters form is not checked
 (Projections tab > Columns For Entry section). For more information, see the [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en) F1 help.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Percent Complete Units

 Use this field to override (plug) the percent complete for units. This is the actual units incurred divided by the projected final units.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in
 theActual and  Actual + Committed Cost column. One
 of these columns will display depending on the projection method selected in the PM Cost
 Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form
When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see[Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Over / Under Units

Use this column to override (plug) the amount your project will be over or
 under the current estimate amount.
Projected final units - (Current estimate + included units)
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the spread percentage set
 up on each phase/cost type (PM Projection Codes>Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en)
 field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or red?
If the Display Positive/Negative Values in Color box is checked(PM Cost Projection Options form), NEGATIVE numbers are in green (these are values that are under) and POSITIVE numbers are in red (these are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is not checked (Projections
 tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

## Projection Code - Projected Final Units

Use this field to override (plug) projected final units.
 This is the projected units to completion, and it is the difference between the projected units at completion and the previously projected units at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?

The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
If you entered units on the projection code
If you entered units on the projection code (PM Projection Code> Info tab> Units field), they will populate in this field.
Click here for information about using a common unit of measure.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Remaining Units

 Use this field to override (plug) projected remaining units.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed
 based on the spread percentage set up on each phase/cost type
 (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Why is this field disabled?
This field is disabled if the Remaining box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see the
 [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en) F1 help.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Percent Complete Cost

 Use this field to override (plug) the percent complete for costs.
Actual Costs
Projected Final Costs
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
 You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in the Actual and Actual + Committed Cost column. One of these columns will display depending on the projection method selected in the PM Cost Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form

When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Over / Under Cost

Use this column to override (plug) the amount your project will be over or under the current estimate amount. Enter a negative value if the amount is under the current estimate, for example -2,500,00.
Projected Final Cost - (Current Estimate + Included Cost)
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters>Projections tab>Spread Option field):

- Prorated- The plugged amount will be distributed based on
 the a weighted average of the percent complete units on the phases/cost
 types associated with the selected projection code.

- Defined at projection code- The plugged amount will be
 distributed based on the spread percentrage set up on each phase/cost type
 (PM Projection Codes>Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or Red?
If the Display Positive/Negative Values in Color is checked (PM Cost
 Projection Options form), NEGATIVE  numbers are in green (these
 are values that are under) and POSITIVE numbers are in red (these
 are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is
 not checked (Projections tab>Columns For Entry section). For more information, see
 [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en)

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Projected Final Cost

Use this field to override (plug) projected cost to completion. This field is the difference between the projected cost at completion and the previously projected cost at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Remaining Cost

Use this field to override (plug) projected remaining costs. This is the difference between the projected final costs and actual costs (invoiced in the AP module).
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based
 on the spread percentage set up on each phase/cost type (PM Projection
 Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Why is this field disabled?
This field is disabled if the Remaining box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see the [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en) F1 help.

Related concepts

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Production Type

On the Grid tab of the PM Cost Projections form, use this field to select how production is calculated.
On the Info tab of the PM Cost Projection Editor form, this is the icon.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Percent Complete Unit Cost

This is the actual cost divided by the projected final cost.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Over / Under Unit Cost

 Use this column to override (plug) the amount your project will be over or
 under the current estimate amount
Over/Under CostOver/Under Units.

When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the spread percentage set
 up on each phase/cost type (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or red?
If the Display Positive/Negative Values in Color box is checked(PM Cost
 Projection Options form), NEGATIVE numbers are in green (these are values
 that are under) and POSITIVE numbers are in red (these are numbers that
 are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is
 not checked (Projections tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Remaining Unit Cost

Use this field to override (plug) projected remaining amounts.
If using the ManDays option (last line), the value entered here will be
 multiplied by the Hrs/ManDay (shown above the entry grid) to determine
 the remaining hours. For example, if Hrs/ManDay is set to ‘8’, and you
 change the remaining man-days from ‘10’ to ‘15’, the remaining hours will
 be increased to 120 (15 x 8). All other man-day and hours values (i.e.
 over/under and final) are recalculated accordingly.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Why is this field disabled?
This field is disabled if the Remaining box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see the [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en) F1 help.

Related concepts

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Projected Final Unit Cost

Use this field to override (plug) projected final unit cost. This is the projected final cost divided by the number of projected final units.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 How will the plugged values entered on the Grid tab be distributed to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Buyout

Check the Buyout box
 if the buy out is complete on a projection code, or phase/cost type. This means the total
 commitments have been made through subcontracts, purchase orders, and/or material orders. The
 system automatically calculates the final values based on your projection method (>  Actual Cost or Actual + Committed Cost fields).
If you check this box on a projection code, the system will also automatically check Buyout box on all of the phases/cost types associated with the projection code.
The selection in this field also applies to any linked cost types. For more
 information about linked cross types, see [Types of Cost Information](/en/vista/vista/costs-and-contracts/job-cost/types-of-cost-information).
Why is the row highlighted in blue?
If you check the Buyout box and a plugged value on a projection code or phase/cost type does not equal the calculated buyout value, the row will be highlighted in blue.

Related concepts

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Projection Code - Notes

Enter any notes on the projection code. You can also enter notes on the Notes tab on the PM Cost Projection Editor form, or the Notes field on the Phase/Cost Type tab of the PM Cost Projections form.

Time stamped notes
If the Activate time stamp feature for projection notes box is checked (PM Company Parameters>Projections tab), double click on the Notes field.

1. Double click on the field. The Time Stamp Notes form will display.

1. Enter a note in the lower portion of the form and then click Add to save the note.

1. The new note will display in the upper portion of the form and it will include the time, date, and your user name.

1. Click the Close button when complete to close the Time Stamp Form.

Projection detail notes
If the Activate projection detail feature  box is checked (PM Company Parameters>Projection tab), you can also enter notes on the projection detail using the Notes field on the Projection Detail tab of the PM Cost Projection Editor form.
Spelling Check
Click the Spelling icon on the toolbar or select Tools > Spelling to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in
 the application. This text is created and maintained using the HQ Standard Note form.
 For more information, see [Create a Standard Note](/en/vista/vista/administration/headquarters/standard-notes/create-a-standard-note).
To insert a standard note into the field, right click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard note to copy (or select from F4 lookup) and click OK. The system inserts the selected note into the field.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

Related reference

- [About Calculated Fields in Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-calculated-fields-in-cost-projections)

## Phase / Cost Type - Phase

The Phase and Code Type fields display the phases and cost types associated with the projection code selected on the Grid tab.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Cost Type

The Phase and Code Type fields display the phases and cost types associated with the projection code selected on the Grid tab.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Percent Complete Hours

 Use this field to override (plug) the percent complete for hours.
Actual HoursProjected Final Hours
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in the Actual and Actual + Committed Cost column. One of these columns will display depending on the projection method selected in the PM Cost Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form
When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.

If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Over / Under Hours

Use this column to override (plug) the amount your project will be over or
 under the current estimate amount. Enter a negative value if the amount is under the
 current estimate, for example -2,500.00.
Projected Final Hours - (Current Estimate + Included Cost)
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the spread percentage set
 up on each phase/cost type (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en)
 field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or red?
If the Display Positive/Negative Values in Color box is checked(PM Cost Projection Options form), NEGATIVE numbers are in green (these are values that are under) and POSITIVE numbers are in red (these are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is not checked (Projections
 tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Projected Final Hours

Use this field to override (plug) projected final hours.
This field is the difference between the projected hours at completion and the previously projected hours at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Remaining Hours

 Use this field to override (plug) projected remaining hours.
This field is the difference between the projected final hours and the actual hours (invoiced in the AP module).
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed
 based on the spread percentage set up on each phase/cost type
 (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Percent Complete Units

 Use this field to override (plug) the percent complete for units. This is the actual units incurred divided by the projected final units.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in the Actual and Actual + Committed Cost column. One of these columns will display depending on the projection method selected in the PM Cost Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form
When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Over / Under Units

Use this column to override (plug) the amount your project will be over or
 under the current estimate amount.
Projected final units - (Current estimate + included units)
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection code - The
 plugged amount will be distributed based on the spread percentage set up on each phase/cost
 type (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en)
 field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or red?
If the Display Positive/Negative Values in Color box is checked(PM Cost Projection Options form), NEGATIVE numbers are in green (these are values that are under) and POSITIVE numbers are in red (these are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is not checked (Projections
 tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Projected Final Units

Use this field to override (plug) projected final units.
 This is the projected units to completion, and it is the difference between the projected units at completion and the previously projected units at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are
 distributed in one of the following ways (PM Company Parameters> Projections
 tab> Spread Option
 field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Remaining Units

Use this field to override (plug) projected remaining units.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Percent Complete Cost

 Use this field to override (plug) the percent complete for costs.
Actual Costs
Projected Final Costs
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.

What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).
 You can only make a change to this field if there are actuals
You can only make a change to this field if there are actuals posted to the selected phase/cost type.
Using the PM Cost Projection Editor form
When using the PM Cost Projection Editor form, the actuals display in the Actual and Actual + Committed Cost column. One of these columns will display depending on the projection method selected in the PM Cost Projection Options form.

- The Actual column will display if you selected Actual Cost in the Projection Method field.

- The Actual + Committed Cost column will display if you selected Actual + Committed Cost in the Projection Method field.

Using the Phase/Cost Type tab on the JC Cost Projections form
When using the Phase / Cost Type tab on the JC Cost Projections form, the actuals display in the applicable columns: Actual Hours, Actual Units, Actual + Committed Units, Actual Unit Cost, Actual Cost, Actual + Committed Cost, Actual Production.
Why is this field disabled?
This field is disabled if the Percent Complete box on the PM Company Parameters form is not checked
 (Projections tab> Columns For Entry section). For more information, see[Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Over / Under Cost

Use this column to override (plug) the amount your project will be over or
 under the current estimate amount. Enter a negative value if the amount is under the
 current estimate, for example -2,500.00.
 
Projected Final Cost - (Current Estimate + Included Cost)
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the spread percentage set
 up on each phase/cost type (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en)
 field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Green or red?
If the Display Positive/Negative Values in Color box is checked(PM Cost Projection Options form), NEGATIVE numbers are in green (these are values that are under) and POSITIVE numbers are in red (these are numbers that are over).
This only applies to the Grid and Phase/Cost Type tab on the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
Why is this field disabled?
This field is disabled if Over/Under box on the PM Company Parameters form is not checked (Projections
 tab> Columns For Entry section). For more information, see [Columns for Entry](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f96--en).
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Projected Final Cost

Use this field to override (plug) projected cost to completion. This field is the difference between the projected cost at completion and the previously projected cost at completion.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Remaining Cost

 Use this field to override (plug) projected remaining costs. This is the difference between the projected final costs and actual costs (invoiced in the AP module).
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
 What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed
 based on the spread percentage set up on each phase/cost type
 (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code

All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Percent Complete Unit Cost

This is the actual cost divided by the projected final cost.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Projected Final Unit Cost

Use this field to override (plug) projected final unit cost. This is the projected final cost divided by the number of projected final units.
When this field displays on the Grid tab of the PM Cost Projections form, the calculation includes all of the phase/cost types associated with the projection code. You can see these phases and cost types using the Phase/Cost Types tab.
What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Projected Final Production

This field is calculated based on the selected production type.
 What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed based on the
 spread percentage set up on each phase/cost type (PM Projection Codes>
 Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).
Here's another reason why this field might be disabled
This field will also be disabled if Track Hours box is not checked on the
 selected cost type (JC Cost Types> Info tab> [ Track Hours](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-cost-types-form/field-definitions-jc-cost-types-form#ID-0001863e--en)
 field).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Remaining Unit Cost

 Use this field to override (plug) projected remaining amounts.

 If using the ManDays option (last line), the value entered here will be
 multiplied by the Hrs/ManDay (shown above the entry grid) to determine
 the remaining hours. For example, if Hrs/ManDay is set to ‘8’, and you
 change the remaining man-days from ‘10’ to ‘15’, the remaining hours will
 be increased to 120 (15 x 8). All other man-day and hours values (i.e.
 over/under and final) are recalculated accordingly.
 What if the plugged value entered on the Grid tab isn't distributed correctly to the associated phases/cost types?
The plugged values entered on the Grid tab of the PM Cost Projections form are distributed in one of the following ways (PM Company Parameters> Projections tab> Spread Option field):

- Prorated - The plugged amount will be distributed based on a weighted average of the percent complete units on the phases/cost types associated with the selected projection code.

- Defined at projection
 code - The plugged amount will be distributed
 based on the spread percentage set up on each phase/cost type
 (PM Projection Codes> Phase/Cost Type tab> [Spread %](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form/field-definitions-pm-projection-codes-form#ID-00019db1--en) field).

Click [ Spread Option](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#ID-00023f71--en) for more detailed information about using the spread option.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Production Type

On the Grid tab of the PM Cost Projections form, use this field to select how production is calculated.
On the Info tab of the PM Cost Projection Editor form, this is the icon.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - CO Calculation Included

Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Buy Out

Check the Buyout box if the buy out is complete on a projection code, or phase/cost type. This means the total commitments have been made through subcontracts, purchase orders,
 and/or material orders. The system automatically calculates the final values based on your projection method ( Actual Cost or Actual + Committed Cost fields).
If you check this box on a projection code, the system will also automatically check Buyout box on all of the phases/cost types associated with the projection code.
The selection in this field also applies to any linked cost types. For more
 information about linked cross types, see [Types of Cost Information](/en/vista/vista/costs-and-contracts/job-cost/types-of-cost-information).
Why is the row highlighted in blue?
If you check the Buyout box and a plugged value on a projection code or phase/cost type does not equal the calculated buyout value, the row will be highlighted in blue.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

## Phase / Cost Type - Notes

Enter any notes on the detail projection.
You can also enter a note on a phase/cost type using the Notes tab on the PM Cost Projection Editor form, which you can open by double clicking on the projection detail.
Add a phase/cost type to a projection code
All of the phases and cost types associated with the projection code selected on the Grid tab will display on the Phase/Cost Types tab.
Use the Phase / Cost Type tab on the PM Projection Codes form to associate a projection code with multiple phases / cost types.
If the phase/cost type that you want doesn't display, you need to clear the current projection (PM Cost Projections> Tasks> Clear Projections), add the new phase/cost type to the projection code (PM Projection Codes), and then create a new cost projections batch (PM Cost Projections).

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)
