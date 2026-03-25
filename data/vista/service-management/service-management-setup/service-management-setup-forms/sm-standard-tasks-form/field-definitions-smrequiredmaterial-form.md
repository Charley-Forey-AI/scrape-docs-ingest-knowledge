---
title: "Field Definitions: SMRequiredMaterial Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-standard-tasks-form/field-definitions-smrequiredmaterial-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-standard-tasks-form/field-definitions-smrequiredmaterial-form"
---

# Field Definitions: SMRequiredMaterial Form

The following is a list of field descriptions for the
 SMRequiredMaterial form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Material: Seq

Enter N, New, or +. The system will auto-generate a
 sequence number for the requirements entry.
Note: For class maintenance tasks, agreement services, work order quotes, or work orders defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Material: Part Type

Enter a part type for this material
 requirements line. Press F4 for a list of valid part types.
If you accessed this grid from SM Standard Tasks or SM Class Maintenance:
Leave this field blank to enter a material
 number in the Material field; you cannot enter both a part type and a material.
Note: You will only enter a value in this field when the task requires a material, but you either do not know the material number or the material number differs based on the equipment being serviced (e.g. the task requires changing a filter, but you don't know which filter will be needed).
If you accessed this grid from SM Service, SM Work Order Quotes, or SM Work Orders:
This field is only enabled if you entered a
 task in the Task field.

- If you are manually entering material requirements,
 you can only enter a part type here if you specified a serviceable item on the task
 and part types have been defined for the serviceable item. Press F4 for a
 list of part types defined for the serviceable item.

- For material requirements that defaulted from a standard task (assigned to the task on the Tasks tab), this field defaults the part type defined in SM Standard Tasks. The system will allow part types assigned in this manner, even if the part type has not been defined for the serviceable item or no serviceable item was specified on the task. Default may be overridden.

## Material: UM

This field is enabled only when a material is entered for the material requirements line.
Required.
If you accessed this grid from SM Standard Tasks.
Enter the unit of measure for the material. Defaults the standard UM defined for the material in HQ Materials.
Press F4 for a list of valid UMs.
If you accessed this grid from SM Class Maintenance:
This field defaults as follows:

- If you did not specify task for this material line or you specified a task not assigned a standard task, this field defaults the standard UM specified for the material in HQ Materials.

- If you specified a task that is assigned a standard task, this field defaults the UM defined for the material in SM Standard Tasks. Default may be overridden.

If you accessed this grid from SM Service, SM Work Order Quotes, or SM Work Orders:
This field defaults as follows:

- If you did not specify task for this material line or you specified a task not assigned a standard task, this field defaults the standard UM specified for the material in HQ Materials.

- If you specified a task that is assigned a standard task, but not a serviceable item, this field defaults the standard UM specified for the material in SM Standard Tasks.

- If you specified a task that is assigned a serviceable item, and you set up parts/materials for the serviceable item, this field defaults the UM defined for the part type/material or material in SM Serviceable Items (Parts tab).

- If you specified a task that is assigned a serviceable item, and you did not set up parts/materials for the serviceable item, this field defaults the standard UM specified for the material in HQ Materials.

Note: Material requirement records that defaulted from a standard task (assigned to the task on the Tasks tab) will automatically default the UM defined for the material in SM Standard Tasks. Default may be overridden.

## Material: Matl Qty

If you accessed this grid from SM Standard Tasks or SM Class Maintenance:
This field is enabled only when a material is entered for the material requirements line.
Enter the quantity of the material required for this standard task.
If you accessed this grid from SM Service, SM Work Order Quotes, or SM Work Orders:
For material lines not associated with a standard task (i.e. no task is specified or specified task is not assigned a standard task), enter the quantity for the specified material.
For material lines associated with a standard task where no serviceable item is specified:

- If only a part type is specified for the material line, this field defaults as blank. You may override the default, but you will be required to enter a material.

- If only a material is specified for the material line, this field defaults the quantity defined for the material in SM Standard Tasks.

For material lines associated with a standard task where a serviceable item is specified:

- If only a part type is specified for the material line, this field defaults the quantity specified for the serviceable item/part type (in SM Serviceable Items). If the part type is not set up for the serviceable item, this field defaults as blank. You may override the default, but you will be required to enter a material.

- If only a material is specified for the material line, this field defaults the quantity specified for the serviceable item/material. If the material is not set up for the serviceable item, this field defaults the quantity defined for the material in SM Standard Tasks. Default may be overridden.

- If both a part type and material are specified for the material line, this field defaults the quantity defined for the serviceable item/part type/material. If the part type/material combination is not set up for the serviceable item, this field defaults as blank. Default may be overridden.
