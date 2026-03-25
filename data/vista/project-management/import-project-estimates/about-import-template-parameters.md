---
title: "About Import Template Parameters | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-import-template-parameters"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-import-template-parameters"
---

# About Import Template Parameters

For each import template, you must define the import parameters; that is,
 how the system handles raw data when it is imported into the work files from the text file.
The Import Parameters tab in PM Import Estimates Template is used to define the import parameters. Some parameters apply to all import
 templates; others are based on the import routine. Parameters include (but are not
 limited to):

- Create Items (Schedule of Values) –
 Used for imports such as Timberline (where no item data is available) to
 identify how items will be created during the import process. [Click here for more information about creating a
 schedule of values.](/en/vista/vista/project-management/import-project-estimates/schedule-of-values).

- Standard Item Codes – Used for
 imports other than Timberline (where item data is available) to define how
 standard item codes will be used. [Click here for
 more information about standard item codes.](/en/vista/vista/project-management/import-project-estimates/standard-item-codes).

- Create Unique Phases – Determines
 whether unique phases will always be created, never created, only created when
 duplicate phases exist for a project, or only created for phases with
 subcontractor cost types. [Click here for more information about creating unique
 phases.](/en/vista/vista/project-management/import-project-estimates/about-the-create-unique-phase-using-item-or-sequential-number-option).

- Material Codes – Options are
 available that define whether to import all material codes, valid material
 codes, or no material codes, as well as whether to roll up material detail into
 one record when multiple records have matching material detail (i.e. material
 code, phase, cost type, UM, and unit price match).

- Accumulate Phase Costs – Allows you
 to have the upload procedure accumulate the costs for each phase into contract
 items with zero amounts. During the import, contract items with amounts will use
 those amounts; contract items where the amount is 0.00 will be set equal to the
 sum of the associated phase costs. If multiple phases are assigned to a single
 contract item, costs for all phases will be pulled into the contract item.

- Create Subcontract Records –
 Determines whether to automatically create subcontract records when imported
 cost types equal the subcontract cost types defined for the company in PM
 Company Parameters. If checked, a subcontract record will be created for cost
 type detail where the cost type equals one of the subcontract cost types in PM
 Company Parameters. If multiple records exist with the same unit of measure, the
 units and costs will be summed and the record created. However, records will
 only be created if the subcontract record does not already exist.

- Use Phase UM and Units for Cost
 Types – Used for Timberline imports to allow cost types with no UM or Units to
 use the phase’s UM and Units.
