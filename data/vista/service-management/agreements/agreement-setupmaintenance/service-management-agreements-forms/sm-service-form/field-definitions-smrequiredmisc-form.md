---
title: "Field Definitions: SMRequiredMisc Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredmisc-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-smrequiredmisc-form"
---

# Field Definitions: SMRequiredMisc Form

The following is a list of field descriptions for the
 SMRequiredMisc form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Misc: Seq

Enter N, New, or +. The system will auto-generate a
 sequence number for the requirements entry.
For agreement services and work order quotes defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Misc: Task

Enter the task associated with this
 requirements entry or leave blank if this requirements entry is not related to a task.
 Press F4 for a list of valid tasks (those set up on the Tasks tab).

## Misc: Standard Item

Enter the standard item associated with this
 miscellaneous requirements entry. Press F4 for a list of valid standard
 items.
Leave this field blank if this miscellaneous requirements entry is not associated with a standard item.

## Misc: Description

Enter a description for this miscellaneous requirements entry, up to 60 characters.
 If you specified a standard item for this requirements entry, this field defaults the description defined for the standard item (in SM Standard Items). May be overridden.

## Misc: Cost Type

Enter the SM cost type for this miscellaneous
 requirements entry. Press F4 for a list of valid SM cost types.
If you specified a standard item for this requirements entry, this field defaults the cost type designated for the standard item (in SM Standard Items). May be overridden.

## Misc: Quantity

Enter the quantity for this miscellaneous requirements entry.

## Misc: Cost Rate

Enter the cost rate for this requirements line. Initially defaults the cost rate specified for the line's standard item in SM Standard Items. If you did not specify a standard item for this line, the cost rate defaults as blank.

## Misc: Cost Total

This field defaults the total cost for this requirements line. You may override the defaulted value. If you override the defaulted value, the system will automatically recalculate the Cost Rate.

## Misc: Billing Rate

This field only displays for work order and work order quote scopes with a Time and Materials pricing method, and agreement services with a Time of Service, Rate Template pricing method.
If you entered a standard item for this requirements line, this field defaults the billable rate from the standard item and cannot be changed.
If you did not enter a standard item for this required miscellaneous sequence, this field defaults as blank. Enter the billable rate for the sequence.

## Misc: Total Billable

Total Billable field on the Misc tab of the SM Service and SM Work Order Quotes forms.
If you entered a Standard Item for this requirements line, this field displays the total billable and cannot be changed.
If you did not enter a Standard Item for this
 required miscellaneous sequence, but you entered a Billing Rate, this field defaults the
 calculated total billable. If you override the default, the system will recalculate the
 Billing Rate. If you did not enter a value in the Billing Rate field, enter the total
 billable amount for this sequence. The system will automatically calculate the Billing
 Rate.
