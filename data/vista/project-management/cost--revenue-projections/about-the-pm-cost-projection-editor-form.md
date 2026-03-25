---
title: "About the PM Cost Projection Editor Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projection-editor-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projection-editor-form"
---

# About the PM Cost Projection Editor Form

Use this form to view detailed projection information and enter plugged values.
Access this form from the PM Cost Projections form by selecting a
 record in the Grid or Phase/Cost Type tab and either double-clicking on the record or
 clicking the Detail Window button (below the grid).
Note: You can make changes using either the PM Cost Projection Editor or PM Cost
 Projections form. If a change is made in one form, the system will automatically
 update the other.

## Info

The Info tab displays projection values for the selected projection code or
 phase/cost type, depending on whether you accessed this form from the Grid tab or
 the Phase/Cost Type tab in PM Cost Projections. You can use this tab to override
 (plug) projected % Complete, Over/Under, Remaining, or Final amounts.
The Producton Type button () displayed in the last line of the projection values
 allows you to toggle between ManDays, CST/HR, U/H, HR/U values. If you opened this
 form from the Phase/Cost Type tab, you can plug the Remaining and Final values for
 the selected option. If using the ManDays option, the value entered in the Remaining
 and Final values are multiplied by the Hrs/ManDay shown above grid to determine the
 remaining or final hours (respectively). For example, if Hrs/ManDay is set to ‘8’,
 and you change the Remaining man-days from ‘10’ to ‘15’, the remaining hours will be
 increased to 120 (15 x 8). All other man-day and hours values (i.e. over/under and
 final) are recalculated accordingly.

## Projection Detail

If you selected the Activate projection detail feature check
 box in PM Company Parameters, this form displays a Projection Detail tab. This tab
 displays a detailed breakdown of the projected costs for the currently selected
 Projection Code and/or Phase/Cost Type. You can add new detail sequences if needed,
 or use the Action field for an existing detail sequence to
 change or delete the detail.

## Costs

The Costs tab displays the cost detail of the currently selected projection code or
 phase/cost type.
Use the Begin Month, End Month,
 Show actual units only, and Costs
 fields to filter the cost information displayed in the lower portion of the tab.
The Phase Costs informational display shows the actual, estimate, total committed,
 and remaining committed costs for all phases; however, as you select phases/cost
 type in the grid the Descriptions section displays information specific to the
 selected phase/cost type. For example, if you select a phase/cost type with a EMRev
 source, the Descriptions section shows the equipment description, EM group, Revenue
 Code, and Equipment associated with that phase/cost type.

## Future COs

The Future COs tab is an informational display showing you the pending change order
 (PCO) items and approved change order (ACO) items that are associated with the
 selected project/phase/cost type in the Project Management module, but have not been
 interfaced with the Job Cost module using the PM Interface form.
Change orders will only display if you selected a phase and cost type. If the tab is
 blank, verify there is a Phase and Cost Type selected in the form. If both of these
 fields are blank, it means you launched the PM Cost Projection Editor form using a
 projection code. Return to the PM Cost Projections form, select on projection code
 on the Grid tab, open the Phase/ Cost Type tab, and then double click on a
 phase/cost type. The change orders for the selected phase/cost type will now display
 on the Future Change Orders tab.
If a pending change order or approved change order that you expect to see is missing
 from the list, verify that the PCO or ACO meets the following conditions.

- The PCO or ACO has not been interfaced.

- The PCO or ACO is associated with a document type that is set up to display
 in projections (that is, the Include in Cost
 Projections checkbox is selected for the document type in
 PM Document Types). Document types are associated with PCOs using the
 PCO Type field in PM Pending Change Orders and
 ACOs using the Document Type field in PM Approved
 Change Orders.

- The PCO item is associated with a status ID that is set up to be included in
 projections (that is, the PM Status ID is set up in PM Status IDs with a
 Projections Option of Display in Projections or
 Display & Calculate in Projections).
 PCO items are assigned a status ID using the Status field in PM Pending
 Change Orders, Items section (either the Grid or Info tabs).

If the PCO does not meet these conditions, it will not display on the Future COs
 tab.

Related concepts

- [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)
