---
title: "Field Definitions: PM Cost Projection Options Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projection-options-form/field-definitions-pm-cost-projection-options-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projection-options-form/field-definitions-pm-cost-projection-options-form"
---

# Field Definitions: PM Cost Projection Options Form

The following is a list of field descriptions for the PM Cost
 Projection Options form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Show only changed since last projection

The Show only changed since last projection checkbox on the PM Cost Projection Options form.
Check this box if only the phases where the current calculated
 forecast does not equal the previous calculated forecast should display.

 The forecast is the system generated
 projection that is calculated when you add the job to the PM Cost Projections form. It is
 compared to the previous calculated forecast. The previous projection may
 be either the last time projections were posted in the current month or
 the last time in the previous month, depending on whether the Previous
 Projected Through Prior Month box is checked.
Do not check this box if all phases should display.

## Show only item unit cost types

The Show only item unit cost types checkbox on the PM Cost
 Projection Options form.
Check this box if only cost types with the Item Units box checked on either JC
 Phases or JC Job Phases (Cost Types tab) should display.

## Show only phase unit cost types

The Show only phase unit cost types checkbox on the PM Cost
 Projection Options form.
Check this box if only cost types with the Phase Units box checked on the JC Job Phases
 (Cost Types tab) or JC Phases forms should display.

## Show linked cost types

The Show linked cost types checkbox on the PM Cost Projection Options form.
Check this box if both the primary and linked cost types should display on the Phase/Cost Type tab of the PM Cost Projections form.
You can link cost types using the Link Progress Cost Type field on the JC Cost Types
 form.
Click [Types of Cost Information](/en/vista/vista/costs-and-contracts/job-cost/types-of-cost-information) for
 detailed information about linking cost types.
If you do not check this box
If you do not check this box, the linked cost type will not display on the Phase/Cost Type tab of the PM Cost Projections form even if you have associated it with a projection code using the PM Projection Codes form.

## Show this window on form open

The Show this window on form open checkbox on the PM Cost Projection Options form.
Check this box if the PM Cost Projection Options form should display
 each time the PM Cost Projections form is opened.
This allows you to set the projection options before entering the projections.

## Load last opened Projection

The Load last opened Projection checkbox on the PM Cost Projection Options form.
Check this box if the PM Cost Projections form should automatically open to the most recent unposted projection. If the box is checked, but no unposted projections exist, the blank form will open.

## Show projections with remaining units only

The Show projections with remaining units only checkbox on the PM Cost Projection Options form.

 Check this box if only projections with remaining units should display.

## Show projections with remaining cost only

The Show projections with remaining cost only checkbox on the PM Cost Projection Options form.

 Check this box if only projections with remaining costs
 (dollars) should display.

## Projection Code Options - Begin Projection Code / End Projection Code

The Begin Projection Code / End Projection Code fields on the PM Cost Projection Options form.
Enter a beginning and ending projection code to filter the projection codes that display in the PM Cost Projections form. Press F4 to select a projection code from a list.
If you leave these fields blank, all projection codes set up on the selected job will display on the Grid tab of the PM Cost Projections form.
Cost projections are created and maintained using the PM Projection Codes form.

## Cost Type Options

The Cost Type Options section of the PM Cost Projection Options form.
Use this field to filter the cost types that are included on the Phase / Cost Type tab of the PM Cost Projections form. Check the Select Cost Types Only box and then select the cost types that should be included in the list.

## Projection Method

The Projection Method radio buttons on the PM Cost Projection Options form.
Use this field to select the override projection method that will be used to calculate cost
 projections. This field defaults based on the selection on the PM Company Parameters form (Projections tab> Projection Method field).

- Actual -
 Cost projections are calculated using only actual costs.

- Actual
 + Committed Costs - Cost projections are calculated using both
 actual costs and committed costs.

## Show inactive phases and cost types

The Show inactive phases and cost types checkbox on the PM Cost Projection Options form.
Check this box if inactive phases and cost types should display on the PM Cost Projections form.
This box is enabled only when the Allow Inactive Phases and Cost Types box on
 PM Company Parameters is checked. More.
When is a phase or cost type active

A phase is active if the Active Phase box on the Info tab of the JC Job Phases
 form is checked.

A cost type is active if the Active box on the Cost Types tab of the JC Job Phases form is checked.

## Previous Projected Through Prior Month

The Previous Projected Through Prior Month checkbox on the PM Cost Projection Options form.

 Check this box if the Previous column on the Info tab of the PM Cost Projection Editor form should include amounts
 through the previous month, but not the current month. The current batch month is determined by the date entered in the Projection Date field at the top of the PM Cost Projections form
The selection in this box also affects the Previously Projected Hours, Previously Projected Units, Previous Projected Cost, Previously Projected Unit Cost, and Previous Production fields on the Grid tab and Phase / Cost Type tab on the PM Cost Projections form.
Example
For example if you enter 7/15/2014 in the Projection Date field (PM Cost Projections) and check the Previous projected through prior month box, the previous projections include amounts through June but not any projections made in the month of July.
If you enter 7/15/2014 in the Projection Date field and do not check the Previous projected through prior month box, the previous projections include amounts through July.
Previous projections are not date sensitive

The previous projection amounts are not date
 sensitive. For example a cost projection with a projection date of 07/15/13 will be included in
 the previous amount on cost projection with a projection date of 07/10/13.

## Display Positive / Negative Values in Color

The Display Positive / Negative Values in Color checkbox on the PM Cost Projection Options form.
Check this box if NEGATIVE numbers should display in green (these are values that are under) and POSITIVE numbers should display in red (these are values that are over).
This only applies to the Over/Under columns (Hours, Units, Cost, Unit Cost, Production) that display on the Grid tab and Phase/Cost Type tab of the PM Cost Projections form. This does not apply to the PM Cost Projection Editor form.
