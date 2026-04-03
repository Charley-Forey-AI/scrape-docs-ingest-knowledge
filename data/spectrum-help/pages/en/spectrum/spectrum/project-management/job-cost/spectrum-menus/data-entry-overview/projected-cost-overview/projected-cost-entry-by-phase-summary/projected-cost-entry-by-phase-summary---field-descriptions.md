---
title: "Projected Cost Entry by Phase Summary - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions"
---

# Projected Cost Entry by Phase Summary - Field Descriptions

A reference when completing fields on the Projected Cost Entry screen.
FieldsDescription
JobEnter a valid job code, and the job description will display to the right.
During the Projected Cost Update, if a job is selected for an updated batch while it is also in use by another operator in Projected Cost Entry, the specified job will not be updated at that time. Instead, the job will remain built and will be available for update after the current entry is complete.

BatchThe batch code associated with the specified job displays. This is the batch code assigned when the job was built.
Select the magnifying glass icon adjacent to this field to view the [Projected Cost Batch Inquiry](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-group/projected-cost-entry-by-group---field-descriptions/projected-cost-batch-inquiry)

PhaseEnter a phase to enter projected cost information for. Only phases that were included when the transaction file was built will be available. To display only a portion of the available phases, enter that specific phase (or a portion of a phase code).
Quantity cost typeThe quantity cost type and description for the selected job displays in this field.
Projected profit at completionThe job's projected profit amount displays. Projected profit is defined as Revised contract (or Projected contract for unit price jobs) less Projected costs.
Projected cost at completionThe current projected cost total for the selected transactions display.
Variance since last projectionThis is the variance for the selected phase line based on the variance of the current projection (at completion) and the current estimate and last projection. [Variance Calculations for Projected Costs](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-group/projected-cost-entry-by-group---field-descriptions/variance-calculations-for-projected-costs)
Buttons
More TotalsSelect to view the [Summary Totals](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-group/projected-cost-entry-by-group---field-descriptions/summary-totals) window.
Activity StatusSelect to select the status filter to determine which phases will display:

- Phases with no activity?: Phases that had no costs or changes within the last period.

- Phases with recent cost?: Phases with non-zero costs booked in the last period.

- Edited phases?: Phases for which projections have been entered since the build.

ExpandBy default, the grid window will only display the first three rows of data for the selected phase. Select the Expand button to display all five rows of data for the phase.

VarianceSelect to display the [Variance window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/variance-window) window.
Grid (Columns)
PhaseEnter a phase to enter projected cost information for. Only phases that were included when the transaction file was built will be available. To display only a portion of the available phases, enter that specific phase (or a portion of a phase code).

EstimateThe current estimates for this phase or group display. Select the arrow to open the [Phase Estimates window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/phase-estimates-window), showing current estimates for this phase.

Last projectionThe last projection amount displays (rounded to the nearest dollar). The title of this column is defined in the Description field of the Build Projected Cost Transaction File screen.
Select the arrow to view the [Projection History window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/projection-history-window) window. The Phase Details window will open first to allow you to view all cost types before proceeding to the Projection History, Cost History, or Open Commitments windows.

Week/Month/Year-to-date/ Add'l quantityThe amount for the period type displays. The period type for this column (Week-to-date, Month-to-date, or Year-to-date) is defined during the Build Projected Cost Transaction file build. The amount will be 0 after the build. Select the arrow to open the [Last Period Detail window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/last-period-detail-window) window.
If the Set projected cost to actual if actual is greater checkbox in Job Cost Installation is selected, enter any additional quantities in this field. If this checkbox is not selected, this field will be display only.

JTD + openJTD + open
This field displays if the Include open commitments checkbox in Build Project Cost was selected when the job was built. Select the arrow to view the totals for job-to-date cost and open commitments in the [Job-to-Date Detail window](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-entry-by-phase-summary/projected-cost-entry-by-phase-summary---field-descriptions/job-to-date-detail-window).
JTD actual
This field displays if the Include open commitments checkbox in Build Projected Cost was not selected when the job was built.

% CompleteEnter the new percent complete, as recorded on the project manager's Projected Cost Worksheet. The system will automatically apply this percentage with the job-to-date actual amount to compute the projected total cost and the remaining fields on this line will be recalculated based on the calculations method you have selected in the Projected Cost Calculations window. If the percent complete is 100%, then Cost-to-complete is automatically zero.
Drill-down to view the Dollars Change Since Last Projection window. This window will display 'Last projection', 'Net change', and 'At completion' amounts for this phase.

To completeEnter the dollar amount at completion. The remaining fields on this line will be recalculated based on the calculations method you have selected in the Projected Cost Calculations window.
Drill-down to view the Dollars Change Since Last Projection window. This window will display 'Last projection', 'Net change', and 'At completion' amounts for this phase.

At completionThe remaining fields on this line will be recalculated based on the calculations method you have selected in the Projected Cost Calculations window.
Drill-down to view the Dollars Change Since Last Projection window. This window will display 'Last projection', 'Net change', and 'At completion' amounts for this phase. You can enter a new 'Net change' amount in this window, and the 'At completion' total will recalculate accordingly.

Grid (Rows)
CodeThe phase code and description displays on this line.
The Unit of measure (Um) for the Quantity cost type in the header displays to the right of the phase code.

DollarsThe dollar amounts for all selected cost types for the phase will display on this row.
Enter amounts for % Complete,To complete, or At completion and the other amounts will be recalculated accordingly.

QuantityThe quantity amounts for all selected cost types for the phase will display on this row.
Enter amounts for % Complete,To complete, or At completionand the other amounts will be recalculated accordingly.

$/UnitThe dollar amount per unit for all selected cost types for the phase will display on this row.
Enter the amounts for To complete or At completion and the other amount will be recalculated accordingly.

MemoEnter a brief memo relating to the transaction line (up to 55 characters). Entry in this field is optional. During the update, memo text will be stored in all cost types for the current phase included in the build.
The committed cost as built and projected method, as built or edited, wil also display on this row.

Related information

- [Projected Cost Phase Calculations - Dollars](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---dollars)

- [Projected Cost Phase Calculations - Quantity](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---quantity)

- [Projected Cost Phase Calculations - $/Unit](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/data-entry-overview/projected-cost-overview/projected-cost-calculations-window/projected-cost-phase-calculations---unit)
