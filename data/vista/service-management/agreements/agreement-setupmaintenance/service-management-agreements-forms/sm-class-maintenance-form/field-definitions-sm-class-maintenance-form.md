---
title: "Field Definitions: SM Class Maintenance Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form/field-definitions-sm-class-maintenance-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-class-maintenance-form/field-definitions-sm-class-maintenance-form"
---

# Field Definitions: SM Class Maintenance Form

The following is a list of field descriptions for the SM
 Class Maintenance form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Maintenance

Enter a maintenance code for this serviceable item class maintenance task, up to 30 characters.

## Description

Enter a description of this serviceable item class maintenance task, up to 60 characters.

## Type

Enter the classification type for this
 serviceable item class maintenance task. Press F4 to select from a list of valid class
 types for the specified class.
Leave this field blank if the maintenance task is not specific to a classification type (i.e. applies to all equipment of the selected class).

## Frequency

Enter the scheduling frequency for this
 serviceable item class/type maintenance task. Press F4 to select from a list of valid SM
 frequencies.

## Average Person Hours

Enter the average person hours for this serviceable item class/type maintenance task.

## Task

The Task field on the SM Work Orders form, scope Tasks tab.
Enter N or + to add a new task. The system
 automatically assigns the next available sequence number.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or work order quote (in SM Work Order Quotes), this field defaults from the agreement service or work order quote task and is disabled.

## Standard Task

The Standard Task field on the SM Work Orders form, scope Tasks tab.
Enter the standard task associated with this
 task sequence. Press F4 for a list of valid standard
 tasks.
Leave this field blank if this task is not associated with a standard task.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or work order quote (in SM Work Order Quotes), this field defaults from the agreement service or work order quote task and is disabled.

## Task Name

The Task Name field on the SM Work Orders form, scope Tasks tab.
Required.
Enter a name for the task, up to 60 characters. If you specified a standard task for this task, the field defaults the task name from SM Standard Tasks. Overriding the task name here will not affect the standard task name.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or quote (in SM Work Order Quotes), this field defaults from the service or quote task and is disabled.

## Task Description

The Task Description field on the SM Work Orders form, scope Tasks tab.
Enter a description of this task (character allowance is virtually unlimited). If you specified a standard task for this task, the field defaults the description from SM Standard Tasks.
Note: For work orders generated from an agreement (via SM Generate PM Work Orders) or quote (in SM Work Order Quotes), this field defaults from the service or quote task and is disabled.

## Recommended

This field displays only for required tasks set up in SM Class Maintenance.
Select this checkbox if this task is recommended for this maintenance task. When selecting serviceable items for equipment tasking on an agreement (in SM Maintenance Item Selection), the system automatically creates a service for each class maintenance task matching the serviceable item class/type and adds tasks with this checkbox selected.
Do not select this checkbox if this is not a recommended task. Tasks with this checkbox unselected will not be auto-added to agreement services during equipment tasking.
