---
title: "Field Definitions: SM Advanced Labor Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-labor-overrides-form/field-definitions-sm-advanced-labor-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-labor-overrides-form/field-definitions-sm-advanced-labor-overrides-form"
---

# Field Definitions: SM Advanced Labor Overrides Form

The following is a list of field descriptions for the SM
 Advanced Labor Overrides form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

Enter N, New, or + to add a new sequence; the system will
 automatically assign the next available sequential number.

## Technician

Enter the technician to which this labor
 override rate applies. Press F4 for a list of valid technicians.
When capturing labor on a work order (in SM Work Orders), the system will apply the rate specified to the right to any work completed labor line assigned this technician and matching all other criteria specified for this override sequence.
Leave blank if this override rate applies to all pay types.
Note: Must be flagged as "Active" in PR Employees. If you enter a technician that is flagged as "inactive" in PR Employees, a warning displays and you will be unable to save the record.

## PR Co

Required.
Enter the PR company to which this override rate applies. The system will use this company to validate technician, craft, and class values.

## Craft

Enter the craft to which this labor override
 rate applies. Press F4 for a list of valid crafts.
When capturing labor on a work order (in SM Work Orders), the system will apply the rate specified to the right to any work completed labor line assigned this craft and matching all other criteria specified for this override sequence.
Leave blank if this override rate applies to all crafts.
Note: Entry in this field is required if you will also be restricting the override rate by class.

## Class

Note: Entry in this field requires that you first enter a
 craft in the Craft field.
Enter the craft class to which this labor
 override rate applies. Press F4 for a list of valid classes for the
 specified craft.
When capturing labor on a work order (in SM Work Orders), the system will apply the rate specified to the right to any work completed labor line assigned this class and matching all other criteria specified for this override sequence.
Leave blank if this override rate applies to all classes for the specified craft.
Note: If you did not specify a craft, the specified rate will apply to all craft classes.

## Call Type

Enter the call type to which this labor
 override rate applies. Press F4 for a list of valid call types.
When capturing labor on a work order (in SM Work Orders), the system will apply the rate specified to the right to any work completed labor line associated with this call type and matching all other criteria specified for this override sequence.
Leave blank if this override rate applies to all call types.

## Pay Type

Enter the pay type to which this labor
 override rate applies. Press F4 for a list of valid pay types.
When capturing labor on a work order (in SM Work Orders), the system will apply the rate specified to the right to any work completed labor line assigned this pay type and matching all other criteria specified for this override sequence.
Leave blank if this override rate applies to all pay types.

## Rate

Enter the labor rate for this sequence.
This labor rate will default as the Billable Rate
 on work completed labor lines entered for a work order (in SM Work Orders, Work Completed
 tab) that match all criteria specified for this override sequence.

-  The system will only use the rate defined here if all criteria specified for this line matches the data entered on the work completed line.

-  Because labor rate overrides can be defined at the rate template, effective date, customer, and service site levels, the system will use a specific hierarchy to determine which labor rates to use. For more information, see [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy).
