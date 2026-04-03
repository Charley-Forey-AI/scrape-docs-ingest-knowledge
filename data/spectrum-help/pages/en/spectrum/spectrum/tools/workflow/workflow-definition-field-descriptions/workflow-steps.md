---
title: "Workflow Steps | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/workflow-steps"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/workflow-steps"
---

# Workflow Steps

Use this window to define, edit, and/or insert steps to the workflow.
Field
Description

Step #
The step # will be automatically calculated by the system. The number is calculated from the prior step, and based on the step type above.

- If the Step type = THEN, the step # is one more than the prior step.

- If the Step type = AND, the step # is the same as the prior step, plus the next alphabetic letter.

Step type
Select a type for this step:

- THEN = Process sequentially

- AND = Process in parallel

- UPDATE = Certain fields will be hidden

If this is the first step, the type must be THEN and the user is not allowed to change this field.
If the Step type is UPDATE, select a Data field to update and Set to option.
When adding a new vendor, customer, or job workflow, you can update the 'Status' to any valid setting for that particular workflow.

Conditional upon
This field will display any conditions that must be met to complete this step. Click the hyperlink to open the Modify Conditions for this Step window to add new conditions.

Assign to
If the Step type is THEN or AND, select who to assign the step to:

- Contact

- Group

- Role

- Originator

Depending on your selection, conditional fields will display below to enter Contact name, Workflow group, or select a Role.
Note: If the Step type is UPDATE, this field will be
 hidden.

For
Select what this step requires:

- Completion: Step needs to be performed and checked off.

- Approval: User must approve the step to continue.

Due by
Select a due by option:

- Immediate

- Hours

- Days

- Respond by days

- No limit

If Hours is selected, enter the number of hours allowed to the right of this field.
If Days is selected, enter the number of days allowed to the right of this field.
If Respond by days is selected, the Days to respond specified on the Project Log Defaults screen will default here. If this option is selected but no default was specified, the date will revert to the current system date.

Function
Select the screen function related to this workflow step. The primary screen function will default.

Instructional text
Enter any optional instructional text for the workflow step.
