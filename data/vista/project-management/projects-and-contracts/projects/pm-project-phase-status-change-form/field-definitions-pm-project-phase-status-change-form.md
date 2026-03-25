---
title: "Field Definitions: PM Project Phase Status Change Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phase-status-change-form/field-definitions-pm-project-phase-status-change-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phase-status-change-form/field-definitions-pm-project-phase-status-change-form"
---

# Field Definitions: PM Project Phase Status Change Form

The following is a list of field descriptions for the PM
 Project Phase Status Change form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project (from PM Projects) for which to globally change phase status. Initially defaults the currently active project.

## Phase: Change For

- All Phases – Select this option to change the status of all phases on the project.

- Phase Range– Select this option to change the status of all phases within a specified range. Phase range is specified to the right.

##  Phase: Beginning/Ending Phase

 Enabled only if Change For Phase Range selected above.
 Specify the beginning and ending in a range of phases for which to change the 'active' status. All phases within this range will have their status changed to 'Inactive' or 'Active', depending on the Phase Status option selected below.

##  Phase: Phase Status

 Specify the status to which all selected phases will be changed.

- Inactive – Select this option to change the status of all specified phases to 'Inactive'. All phases within the specified range that are currently flagged as 'Active' will be changed to 'Inactive' (i.e. "Active Phase" option unchecked). Phases already flagged as 'Inactive' will be skipped.

- Active – Select this option to change the status of all specified phases to 'Active'. All phases within the specified range that are currently flagged as 'Inactive' will be changed to 'Active' (i.e. Active Phase option checked). Phases already flagged as 'Active' will be skipped.

## Cost Type: Change For (Phase)

- All Phases – Select this option to change cost type Update flags for all phases on the project.

- Phase Range– Select this option to change cost type Update flags for phases within a specified range. Phase range is specified to the right.

## Cost Type: Change For (Cost Type)

- All Cost Types – Select this option to change the Update flag for all cost types on the project.

- CostType Range – Select this option to change the Update flag for cost types within a specified range. Cost type range is specified to the right.

Note:Specified cost types will be updated for all phases or phases within a range, depending on the Change For Phase option selected (above).

##  Cost Type: Beginning/Ending Phase

 Enabled only if Change For Phase Range selected above.
 Specify the beginning and ending in a range of phases for which to change cost type Update flags. Cost types (all or those within the cost type range specified below) assigned to phases within this range will have their Update flag changed to ‘Y-Ready to Update’ or ‘N-Not Ready to Update’, depending on the Cost Type Interface option selected below.

##  Cost Type: Beginning/Ending Cost Type

 Enabled only if Change For Cost Type Range selected above.
 Specify the beginning and ending in a range of cost types for which to change the Update flag. Cost types within this range (for all phases or those within the phase range specified above) will have their Update flag changed to ‘Y-Ready to Update’ or ‘N-Not Ready to Update’, depending on the Cost Type Interface option selected below.

##  Cost Type: Cost Type Interface

 Specify the Update status to which all selected cost types will be changed.

- Ready to Interface – Select this option to set the Update flag ‘Y-Ready to Update’ for all specified cost types (in PM Project Phases, Cost Types tab).

- Not Ready to Interface – Select this option to set the Update flag to ‘N-Not Ready to Update’ for all specified cost types (in PM Project Phases, Cost Types tab).

Note:Cost types already set as indicated here will be skipped, as will cost types with the Update flag set to I (Interfaced) or J (Set up in Job Cost).
