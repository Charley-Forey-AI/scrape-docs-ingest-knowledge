---
title: "Task File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/task-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/task-file-maintenance---field-descriptions"
---

# Task File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field/Button
Description

Work task
Enter the code for the new task. If you
 are editing an existing task, no change can be made to this field.
Description
Enter a description of the task you are
 adding.
Flat rate?
Select this checkbox if this is a flat
 rate task. If you select this checkbox, the selected task will be billed at
 one rate regardless of the amount of labor, material and other costs used. If
 you are editing an existing task or subtask, this selection cannot be changed.
 Note: If you do want to bill for a certain component
 or task, simply enter the billing rate or item price during data entry.


Recalculate components?
If the selected task is flagged as flat
 rate, select this checkbox to automatically recalculate the pricing of a flat
 rate task if any of the components (Labor, Material, Other, or Subtasks) incur
 changes that will have an effect on the task pricing. This checkbox is not
 available for non-flat rate tasks, and if any costs exist (labor, material, or
 other).

- If this checkbox is selected, automatic
 recalculations will apply to both tasks and subtasks as well as any flat
 rate tasks that are assigned labor, material, or other.

- If this checkbox is selected and the task has
 labor, material, or other items assigned and no subtasks, the Sell price will
 recalculate based on the cost detail and any Overhead or Profit percentages
 entered in this window.

Price method
This field displays only for flat rate
 tasks. Select from the following pricing methods:

- Use flat subtask price

- Use flat subtask cost

Select the Use flat subtask price
 option if you want the software to calculate the total charge for a task
 based on the total prices of the subtasks. As the total price is based on
 the subtask's prices, you cannot add any overhead or profit in the Totals
 section of the screen. If this is needed, you simply add it to the subtasks
 instead.
Select the Use flat subtask cost
 option if you want the software to calculate the total charge for a task
 based on the total costs across the subtasks plus any markup. Here you can
 add a percentage for overhead and profit at the both the task and subtask
 level.
 If the selected task has a flat rate
 status and is assigned Labor, Material, or Other items, this option will not
 be applicable.
Note: If the main task
 is billed as T+M, then all subtasks must also be T+M. However, if the main
 task is billed using a flat rate, then the subtasks can be T+M and/or Flat
 Rate.

Sell price
The system-calculated flat-rate selling
 price displays. During initial entry, this figure will be zero, but will change
 as labor, materials, and other costs are entered. If desired, the calculated
 amount can be overridden simply by entering a dollar amount in this field.
Labor category
Enter the default labor category code
 for use in the Labor detail window, double-click in this field to select from a
 list of available labor category codes, or press Enter to leave this field
 blank.
Notes
Enter any desired notes for this task.
 Task and subtask notes will appear on the Crystal-Link Work Order Form. Note: Service contract task-related notes that
 are updated in the Service Contracts > Data Entry > Contract Work Order Processing screen or the Service Contracts > Utilities > Contract Work Order Processing screen display in the Work Ordered section of the Work Order
 form. Task-related notes not entered in these screens display in the Work
 Notes section of the Work Order form.

Cost detail

Labor total
This figure displays based on entry of
 data in the window that opens when the Labor button is
 clicked.
Material total
This figure displays based on entry of
 data in the window that opens when the Material button
 is clicked.
Other total
The sum of all budget lines
 displays.
Subtask total
The total cost of the subtasks
 displays.
Total budget cost
This figure is the sum of the labor,
 material, other costs, and subtasks displayed above.
Totals

Overhead
If overhead is to be added to the sum
 of labor, materials, and other costs, the amount can be entered here. If
 overhead on this task is a flat dollar amount, enter that dollar amount to the
 right of the Overhead prompt. If overhead on this task is a percentage, enter
 that percentage to the left of the Overhead prompt. The dollar amount will then
 be calculated automatically. Note: The fields
 in this section only display when the Flat rate checkbox on this window is
 selected.

Profit
If profit is to be added to the sum of
 labor, materials, and other costs, the amount can be entered here. If profit on
 this task is a flat dollar amount, enter that dollar amount to the right of the
 Profit prompt. If profit on this task is a percentage, enter that percentage to
 the left of the Profit prompt. The dollar amount will then be calculated
 automatically.
Subtotal
The cost detail subtotal displays.
Flat price
The total of the flat rate subtask
 prices displays. Note: If you do want to bill
 for a certain component or task, simply enter the billing rate or item price
 during data entry.

Sell price
The sell price displayed here is
 calculated as the sum of total budget cost, overhead, and profit. No entry is
 allowed. This calculated amount matches the sell price at the top of the screen
 unless that amount has been overridden.
Buttons

Labor
Click this button to open the [Task Labor](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/task-labor) window to enter labor hours
 allocated for this task.
Material
Click this button to open the [Task Materials](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/task-materials) window to enter the
 materials allocated for this task and their corresponding costs.
Other
Click this button to open the [Task Other Charges](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/task-other-charges) window to enter
 other costs pertaining to this task.
Subtasks
Click this button to open the [Subtasks](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/maintenance-overview/task-file-maintenance/subtasks) window to view, add, and edit
 subtasks associated with the selected task.
