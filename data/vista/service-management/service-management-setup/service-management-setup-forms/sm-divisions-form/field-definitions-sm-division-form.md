---
title: "Field Definitions: SM Division Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-divisions-form/field-definitions-sm-division-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-divisions-form/field-definitions-sm-division-form"
---

# Field Definitions: SM Division Form

The following is a list of field descriptions for the SM
 Division form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Division

Enter a name for this service center division, up to 10 characters.
Examples:

- Install

- Electrical

- Plumbing

- HVAC

- Special

- Maint

## Description

Enter a description of this service center division, up to 60 characters.

## Alternate Department

Check this box to use an alternate (override) department for determining the GL accounts to update when entering work completed on a work order referencing this division.
Note: You will only need to check this box if you require separate GL accounting by division of work.
Uncheck this box to use the standard department (assigned to the service center) for determining the GL accounts to update when entering work completed on a work order referencing this division.

## Reviewer

Enter a reviewer ID in this field to enable that user to mark work orders as ready to bill.
Press F4 in the Reviewer field
 for a list of active reviewers from which to choose. Press F5 to access
 the HQ Reviewers form.

## Department

This field is only enabled if the Alternate
 Department box is checked.
Enter the alternate (override) department (from SM Departments) to use for determining the GL accounts to update when capturing work completed on a work order that references this service center.
Note: The system will only use this department if the division is referenced on a work order scope.

## Active

Check this box to activate this service center division. Once activated, it will be available for selection when setting up accounting treatments (in SM Advanced Accounting Setup) or on a work order (in SM Work Orders).
Uncheck this box to deactivate this service center division. When inactive, division will not display in F4 lookups, nor can it be referenced when setting up accounting treatments (in SM Advanced Accounting Setup) or on a work order (in SM Work Orders).
