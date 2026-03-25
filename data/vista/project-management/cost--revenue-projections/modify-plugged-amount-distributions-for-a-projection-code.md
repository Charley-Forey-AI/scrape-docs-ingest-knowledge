---
title: "Modify Plugged Amount Distributions for a Projection Code | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/modify-plugged-amount-distributions-for-a-projection-code"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/modify-plugged-amount-distributions-for-a-projection-code"
---

# Modify Plugged Amount Distributions for a Projection Code

Enter plugged amounts on the projection codes using the Grid tab on the [PM Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form) form. The plugged values are distributed to the phases/cost types based on how you configured the spread.
You can modify how the plugged amount is distributed
Once you enter a plugged amount on the projection code, you can also change how it is distributed, for example if you need to change how a variance is spread to the phase/cost types when the projections are being entered.

1. Enter a plugged amount on the Grid tab of the PM Cost Projections form.

1. Move the cursor into the
 field that you want to redistribute. For example if you entered a plugged value in
 the Projected
 Final Hours field, move the cursor into that field.

1. Select Tasks > Adjust
 Projection in the toolbar at the top of the form. This will open the PM Adjust Cost
 Projection form.

Why does the "cannot be spread into phase/cost type" message display?
You can only select the
 Adjust Projection
 option when the cursor is in a field that can contain a plugged value. For example if the cursor is in the
 Remaining Unit Cost
 field when you select the
 Adjust Projection
 option, the error message will display since you cannot enter a plugged value in this field.

1. The plugged amount displays in the
 Original Value
 field.

1. Optional:
 If you need to change the plugged amount, change the
 Adjusted Value
 field.

1. Change the value in the
 Spread Percent
 or
 Spread Value
 field to change the distribution.

Prorate
If you make a change to the Spread Percent
 field, the Spread
 Value amount is increased but the value that displays in the Adjusted Value
 field is not recalculated. For example if you enter 200% in the  Spread Percent
 field, 200% of the plugged amount will be distributed to the selected phase/cost type. The
 Adjusted
 Value field will not recalculate to reflect this change, but when you click
 Apply the system will use the total Spread Value as the new plugged
 value.
Defined at Projection
System will automatically recalculate the other fields
If you change a value in the
 Spread Percent
 or
 Spread Value
 field, the system will automatically recalculate the other fields.
Changing the Spread Percentage will not change the spread on the projection code
When using the Defined at Projection option, the changes
 to the Spread
 Percentage field only impact the current projection. The changes will not
 update the spread that was configured on the PM Projection Code form (PM Projection
 CodePhase/Cost Type tab Spread % field).

1. Click Apply when
 complete to apply the new distribution. This will close the PM Adjust Cost Projection
 form.

Related information

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [PM Projection Codes Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form)
