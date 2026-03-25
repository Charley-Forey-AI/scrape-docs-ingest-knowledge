---
title: "Field Definitions: SM Agreement Site Coverage Dtl Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-site-coverage-dtl-form/field-definitions-sm-agreement-site-coverage-dtl-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-site-coverage-dtl-form/field-definitions-sm-agreement-site-coverage-dtl-form"
---

# Field Definitions: SM Agreement Site Coverage Dtl Form

The following is a list of field descriptions for the SM
 Agreement Site coverage Dtl form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

Seq field on the SM Agreement Site Coverage Dtl form.
Enter
 +, N, or
 New.
 The system automatically assigns the next sequential number.

## Call Type

Call Type field on the SM Agreement Site Coverage Dtl form.
If this
 agreement covers spot work for the specified service by call type, enter the call type to
 cover or press F4 to select from a list of valid call types.

## Labor Covered

Labor Covered checkbox on the SM Agreement Site Coverage Dtl form.
Select this checkbox if this agreement fully covers labor costs for spot work associated with the selected service site. When you enter labor-related work completed lines on an unscheduled work order for this agreement and service site, the system will automatically flag the line as Non-Billable. Labor-related work completed lines include:

- Work completed Labor lines

- Work completed Purchase lines referencing a labor-related SM cost type

- Work completed Miscellaneous lines referencing a labor-related SM cost type
Note: If you specified a call type for this coverage sequence, work completed lines will only be flagged as Non-Billable if they also reference a work order scope with the same call type.

Do not select this checkbox if labor costs are not covered under this agreement for spot work associated with the selected service site.

## Material Covered

Material Covered checkbox on the SM Agreement Site Coverage Dtl form.
Select this checkbox if this agreement fully covers material costs for spot work associated with the selected service site. When you enter material-related work completed lines on an unscheduled work order for this agreement and service site, the system will automatically flag the line as Non-Billable. Material-related work completed lines include:

- Work completed Inventory lines

- Work completed Purchase lines referencing a material and/or material-related SM cost type

- Work completed Miscellaneous lines referencing a material-related SM cost type
Note: If you specified a call type for this coverage sequence, work completed lines will only be flagged as Non-Billable if they also reference a work order scope with the same call type.

Do not select this checkbox if material costs are not covered under this agreement for spot work associated with the selected service site.

## Equipment Covered

Equipment Covered checkbox on the SM Agreement Site Coverage Dtl form.
Select this checkbox if this agreement fully covers equipment costs for spot work associated with the selected service site. When you enter equipment-related work completed lines on an unscheduled work order for this agreement and service site, the system will automatically flag the line as Non-Billable. Equipment-related work completed lines include:

- Work completed Equipment lines

- Work completed Purchase lines referencing an equipment-related SM cost type

- Work completed Miscellaneous lines referencing an equipment-related SM cost type
Note: If you specified a call type for this coverage sequence, work completed lines will only be flagged as Non-Billable if they also reference a work order scope with the same call type.

Do not select this checkbox if equipment costs are not covered under this agreement for spot work associated with the selected service site.

## Subcontract Covered

Subcontract Covered checkbox on the SM Agreement Site Coverage Dtl form.
Select this checkbox if this agreement fully covers subcontract costs for spot work associated with the selected service site. When you enter subcontract-related work completed lines on an unscheduled work order for this agreement and service site, the system will automatically flag the line as Non-Billable. Subcontract-related work completed lines include:

- Work completed Purchase lines referencing a subcontract-related SM cost type

- Work completed Miscellaneous lines referencing a subcontract-related SM cost type
Note: If you specified a call type for this coverage sequence, work completed lines will only be flagged as Non-Billable if they also reference a work order scope with the same call type.

Do not select this checkbox if subcontract costs are not covered under this agreement for spot work associated with the selected service site.

## Misc Covered

Misc Covered checkbox on the SM Agreement Site Coverage Dtl form.
Select this checkbox if this agreement fully covers "other" miscellaneous costs for spot work associated with the selected service site. When you enter work completed miscellaneous lines on an unscheduled work order for this agreement and service site, if you specify a cost type with a cost type category of Other, the system will automatically flag the line as Non-Billable.
Note: If you specified a call type for this coverage sequence, work completed lines will only be flagged as Non-Billable if they also reference a work order scope with the same call type.
Note: Miscellaneous lines referencing labor, material, equipment, or subcontract-related SM cost types are only flagged as Non-Billable if the corresponding cost type category is selected for coverage on the agreement.
Do not select this checkbox if "other" miscellaneous costs are not covered under this agreement for spot work associated with the selected service site.
