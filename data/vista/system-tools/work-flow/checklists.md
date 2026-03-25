---
title: "Checklists | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/checklists"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/checklists"
---

# Checklists

Checklists consist of a series of tasks, which in turn, can be broken down into a
 series of steps, if necessary.
You can assign each checklist task and step to
 system users. Assigned tasks and steps display on the user's task list (WF Tasklist) when
 the task or step is ready to have work performed. Whether a task or step is ready depends
 on a variety of factors.

- If you do not enforce order for the
 checklist, and no tasks (or steps) are required, all tasks and steps display on the
 respectively assigned user's task list.

- If you enforce checklist order, and no
 tasks (or steps) are required, the first task displays on the assigned user's task
 list. The next task on the checklist will not display until a user assigns a final
 status to the first task. Additionally, the first step associated with the first
 task, if any, displays on the assigned user's task list. The next step associated
 with the first task will not display until a user assigns a final status to the first
 step.

- If you enforce checklist order, and all
 tasks are required, the first task displays on the assigned user's task list. All
 non-required steps associated with that task will display on the assigned user's task list.

- If you assign a final status to a task,
 and there are still incomplete steps associated with it, the system warns that the
 steps are incomplete. You can then choose to apply the same status to all associated
 steps, regardless of the assigned user for each step. Otherwise, you must complete
 each step prior to completing the task.

- If you change the status of a step from
 a new status to an in progress or final status, the system updates the task to the
 default in progress status (determined on WF Checklist Status Codes; for more
 information, refer to Related Topics below). After all steps have been assigned a
 final status, the task remains at an in progress status. You must change the task
 status manually.

## Understanding Status Types

Checklists statuses determine the progress
 for a checklist, task, or step. The assigned user can update the status of a checklist
 item (task or step) using [WF
 Tasklist](/en/vista/vista/system-tools/work-flow/checklists/wf-tasklist). Supervisors can monitor or update checklist item statuses using
 [WF Checklist Tasks](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-tasks)
There are three types of status types
 available:

- New – This status indicates that work
 has not begun for the checklist or checklist item.

- In Progress – This status indicates
 that someone is currently working on the checklist or checklist item.

- Final – This status indicates that
 work on the checklist or checklist item is complete.

For each status code you create, there can
 only be one assigned status type. However, you can create numerous codes for each type
 to help customize the module to fit your organization's own workflow and processes. For
 example, you might create ‘In Progress' codes with descriptions of "On Hold" or "Waiting: and create 'final' codes with descriptions of "Complete" or "Canceled".
You can designate a single, default status
 code for each status type. Each time the system automatically uses a status type, it
 will automatically use the code that you designate as the default.
Note: If you do not designate a default status code, the
 system uses a hard-coded default (i.e., New, In Progress, or Final).

Related information

- [WF Checklist Status Codes](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-status-codes)

- [WF Checklist Template](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-template)

- [WF Checklist Maintenance](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-maintenance)

- [WF Checklist Initialization](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-initialization)

- [WF Checklist Tasks](/en/vista/vista/system-tools/work-flow/checklists/wf-checklist-tasks)

- [WF Tasklist](/en/vista/vista/system-tools/work-flow/checklists/wf-tasklist)
