---
title: "Work Order Tasks | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/in-depth-overview/work-order-tasks"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/in-depth-overview/work-order-tasks"
---

# Work Order Tasks

A work order task is a pre-defined work assignment. It can be comprised of labor, materials, and other costs. It can also be a group of sub-tasks.
Every work order can have an unlimited amount of tasks associated with it. Every task can be billed on a separate basis as a flat rate task or on a time + material basis. Examples of tasks include the installation of a dishwasher or the replacement of a specific filter.
On the Work Order Installation – Defaults tab, select the checkboxes in the Automatically transfer task detail section to automatically transfer details for labor, material, and other costs. If the checkboxes are selected, the subtasks will be listed individually in the Labor Entry, Material Entry, and Other Cost Entry screens.

## Flat Rate Tasks

In the Price type defaults section on the Work Order Installation – Defaults tab, select Flat rate if your invoices are typically billed at one rate, regardless of the amount of labor, materials use, and other costs.
Time + Material Tasks In the Price type defaults section on the Work Order Installation – Defaults tab, select Time + materials to create a "budget" for labor, material, and other costs in the work order.
Tasks and Subtasks You can create a task that is comprised of multiple tasks or subtasks. This option is only available when no labor, material, or other costs are set up on the parent task.

- If the parent task is billed as time + materials, then all subtasks must also be billed as time + materials.

- If the patent task is billed at a flat rate, then the subtasks can be billed as time + materials and/or flat rate.

## Pricing methods for Flat Rate Tasks with Subtasks

- In the Task File Maintenance  >  Add Task window, select the Use flat subtask price option if you want Spectrum to calculate the total charge for a task based on the total prices of the subtasks. Because the price is based on the subtask's prices, you cannot add any overhead or profit. If you need to add overhead or profit, add them in the subtasks instead.

- In the Task File Maintenance  >  Add Task window, select the Use flat subtask cost option if you want Spectrum to calculate the total charge for a task based on the total costs across the subtasks plus any markups. You can add a percentage for overhead and profit at the task and subtask levels.

## Task Completed

When the 'Task completed?' option is cleared in the Edit Labor Hours, Edit Material or Edit Other Charges windows, the respective transactions are included in the unposted costs on the Edit Work Order  >  Financials tab. When determining the basis for other charge calculations, transactions with the 'Task completed' flag cleared would be excluded since the transaction would not be included on the A/R billing if invoiced now.
