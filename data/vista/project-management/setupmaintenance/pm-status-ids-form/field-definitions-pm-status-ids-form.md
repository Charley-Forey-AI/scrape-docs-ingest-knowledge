---
title: "Field Definitions: PM Status IDs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form/field-definitions-pm-status-ids-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form/field-definitions-pm-status-ids-form"
---

# Field Definitions: PM Status IDs Form

The following is a list of field descriptions for the PM
 Status IDs form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Status Code

The status code will be used to identify and select the status ID. Enter a code that is up to 6 characters long.

[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

##  Description

 Enter the description for this status code, up to 30 characters.

[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

## Projections Option

Select how change order items assigned this status ID should be handled in [JC Cost Projections ](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form) and [JC Revenue Projections ](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form).

- (none)
 – Select this option to exclude pending change order items assigned
 this status code from cost and revenue projections. Change order items will be
 excluded from cost and revenue projection calculations and will not display in the JC
 Projection Future CO or JC Revenue Future CO forms. Change order amounts will also be
 excluded from ‘future CO’ and ‘included CO’ amounts in JC Cost Projections, JC
 Revenue Projections, and JC Override Projections.

- Display in Projections
 – Select this option to display pending change order items assigned this status code in cost and revenue projections. Change order items will be excluded from cost and revenue projection calculations, but will display in the JC Projection Future CO and JC Revenue Future CO forms. Change order amounts will be included in the ‘Future CO’ amount columns, but excluded from ‘IncludedCO’ amount columns in JC Cost Projections, JC Revenue Projections, and JC Override Projections.

- Display & Calculate in
 Projections – Select this option to display pending change orders
 assigned this status code in cost and revenue projections, and include them in cost
 and revenue projection calculations. Change orders will display in JC Projection
 Future CO and JC Revenue Future CO forms, and change order amounts included in the
 ‘Future CO’ and ‘IncludedCO’ amount columns in JC Cost Projections, JC Revenue
 Projections, and JC Override Projections.

The system also considers the
  Include in Projections
 checkbox in PM Document Types when determining whether to include the PCO in cost and/or revenue projections:

- The
 Include in Projections
 option must be checked for the PCO’s document type in order for the pending change order to be included in cost and revenue projections, regardless of whether this option is set to ‘Display in Projections’ or ‘Display & Calculate in Projections’ for the status code assigned to the PCO.

- If the
 Include in Projections
 option is checked for the PCO’s document type, but the status code assigned to the PCO has a Projections Option of ‘None’, the PCO will not display in the JC Projection Future CO or JC Revenue Future CO forms, nor will the change order amounts be included in ‘Future CO’ or ‘IncludedCO’ amounts.

[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

## Type of Code

The type of code designation is used in the following:

- Reporting

- If using the automatic approval of a pending change order, it will assign the first status code that is a “Final” type.

- When copying meeting minutes, you can include or exclude items or item details that have a status code that is a “Final” type.
Code Types

Beginning – Select this option if the ID
 represents the beginning stage of a change order’s or document’s process.
Intermediate – Select this option if this
 code is to represent the intermediate stage of a change order’s or document’s process.
Final – Select this option if this code
 is to represent the final stage of a change order’s or document’s process.
Note:Pending change orders can be assigned a 'final' type status code, even if they are not approved. For example, you can assign a status code of 'Rejected' that has a type of 'final'. When printing pending change orders (PM Pending Change Order Form), those with a 'final' type status code will be included as long as the status code is not the 'Default Final Status' designated in PM Company Parameters.
Examples of status IDs and code types:

Type of Code
Status Code

Beginning
New

Submitted for Approval

Sent

Initial Change Request

Intermediate
In Progress

On Hold

Damaged

Pending

Final
Done

Approved

Completed

Rejected

[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

## Exclude From Lookups

Check this box to exclude this status code
 from status code lookups. When checked, the status code will not display when you press
 F4
 in a status code field.
This option allows you to exclude selected
 status codes from F4 lookups. You might use this option for status codes that you no longer
 use but do not want removed from the system. When checked the status code will not display
 in lookup lists, but users can still manually enter it.
Status codes with this option checked will not
 be excluded from the ‘All Status Codes’ lookup available when F4 is pressed
 in the Status Code field in this form.
[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

## Document Category

This field is disabled when the Active for All
 Forms box is checked.
Enter the document category that applies to
 this status code or press F4 to select a one from a list. Only
 records associated with this document category can use this status code. For example, if
 you select 'PCO', the status code can only be used on pending change orders.
Status codes restricted to a specific document
 category will be excluded from any F4 lookup not matching the document
 category. For example the status code lookup in PM Test Logs will exclude any status code
 with a document category of PCO.
Note:The Submittal - OLD document category only applies to submittals created and maintained using the [PM Submittals - 6.5](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittals---6.5-form) form.

Note:The Submittals document category applies to submittal packages in the [PM Submittal Package](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-package-form) form, and submittal revisions in the [PM Submittal Register](/en/vista/vista/project-management/issuessubmittalsother-documents/submittals/about-the-pm-submittal-register-form) form.

[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples

## Active for All Forms

Check this box if the status ID applies to all document categories - for example project issues, pending change orders, drawing logs, etc.
Leave this box unchecked if the status id only
 applies to a specific document category - for example if the status ID only applies to
 RFIs. This will enable the Document Category field to select it.
Note: When this box is not checked, you will only be able to
 assign the status ID to records of the selected document category.
[](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form)PM Status IDs - Create a status ID and examples
