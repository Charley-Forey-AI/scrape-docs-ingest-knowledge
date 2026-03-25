---
title: "Field Definitions: PM Phase Cost Type Settings Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-phase-cost-type-settings-form/field-definitions-pm-phase-cost-type-settings-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-phase-cost-type-settings-form/field-definitions-pm-phase-cost-type-settings-form"
---

# Field Definitions: PM Phase Cost Type Settings Form

The following is a list of field descriptions for the PM
 Phase Cost Types Settings form.Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project for which to set the phase/cost type flags. Once entered, the project’s contract defaults and the first contract item and its assigned phases and cost types are displayed in the grid.

## Contract Item

Specify the contract item for which to set phase/cost type flags. Initially defaults the first item for the specified contract. Once entered, all phases/cost types assigned to the contract item are displayed in the grid.

## Bill Flag

Specify whether units and/or costs for this cost type on this phase are to be used in calculating progress complete. Used only for Job Billing.
 Y = Both units and dollars posted to this cost type will be used to calculate progress complete.
 C = Only dollars will be used in calculating percent complete for this phase/cost type.
 N = Neither units nor dollars posted to this cost type will be used when calculating progress complete.

## Item Flag

Check this box if this cost type will be used to accumulate units complete for specified contract item. When summarizing job costs, the costs are all totaled, but only the units posted to the specified cost type are counted.
Only check this box if you are using this cost type to accumulate units complete for the specified contract item.
Note:Generally, this flag is checked for only one cost type on one phase, and the phase selected would be the one most closely related to the contract item.

## Phase Flag

Check this box if this cost type will be used to accumulate units complete for this phase. Typically, this flag is checked for the main cost type, and only units posted to that cost type for that phase would be accumulated.
Leave this box unchecked if not using this cost type to accumulate units complete for this phase.

## Buy Out

Check this box if buy out is complete (total commitments have been made through subcontracts, purchase orders, and/or material orders) for this phase and cost type.
Do not check this box if buy out is not complete for this phase and cost type.
Note:This flag may be used in reporting and will be used in JC Cost Projections if commitments are being included with actual costs (flag setting in JC Company Parameters). If buy out is complete for a phase/cost type (box checked), projected costs will be calculated as the actual cost plus total remaining committed cost.

## Active

Check this box to activate this cost type for this phase. Must be checked to allow posting activity.
Leave this box unchecked to deactivate this cost type. Posting activity will not be allowed.
