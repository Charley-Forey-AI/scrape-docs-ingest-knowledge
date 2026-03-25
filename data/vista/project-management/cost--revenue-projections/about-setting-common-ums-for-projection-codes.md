---
title: "About Setting Common UMs for Projection Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-setting-common-ums-for-projection-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-setting-common-ums-for-projection-codes"
---

# About Setting Common UMs for Projection Codes

 You can specify a common unit of measure for a projection code which will be used to determine the how the units are summarized and adjustments are spread back through the phase/cost types.
There are multiple ways that you can specify the unit of measure for the projection code. For information about how hours and costs on a projection code are spread to the associated phases/cost types, see [About Using the Spread Option for Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-using-the-spread-option-for-cost-projections).
From the PM Projection Codes form, you can do one of the following:

- Enter a UM for the projection code - On the projection code setup form, you can enter the unit of measure to use for accumulating units. Any phase cost/types with the same UM will automatically be selected as a ‘Proj Code Unit’.

- Select Proj Code Unit flag for phase/cost type - You can set the ‘Proj Code Unit’ flag for the units you want to summarize for the projection code. You can only select like units. The UM for the selected phase/cost types will automatically populate for the projection code.

If creating projection codes automatically using the "Create projection codes from..." options in the Tasks menu, the system automatically sets the UM for the projection codes as follows:

- If you elect to creating projection codes from phases, and the Phase Unit Flag checkbox is selected for phase's cost type, that UM defaults as the projection code's unit of measure (UM).

- If you elect to create projection codes from phases/cost type, the UM for each projection code will be set equal to the cost type UM.

- If you elect to creating projection codes from contract items, and the Item Unit Flag checkbox is selected for a phase's cost type, that UM defaults as the projection code's unit of measure (UM).

Note: Creating projection codes from cost types does not automatically set a UM for the projection code.

Related information

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [PM Projection Codes Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form)
