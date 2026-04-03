---
title: "Workflow Definition Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions"
---

# Workflow Definition Field Descriptions

Workflow definitions are templates that define what triggers the workflow and what happens when it is finished.
To get started, click the New
 button and from the Select Workflow Type window, choose the workflow you want to define
 (for example, select the PO Proposed Purchase Order workflow type). Click OK.
Next, the Workflow Definition window displays (refer to the table
 below when completing this window). Each workflow definition contains steps or tasks
 that are defined by you to meet your organization's needs and objectives. Steps can be
 processed sequentially or in parallel.
Each step is assigned to a user, a group of users, a role or the
 person who initially entered the transaction. It includes instructions, due dates, notes
 and the ability to view the entire workflow assigned to the transaction. The history of
 each step is recorded within the system as well.
Table 1. Field DescriptionsField/Button
Description

Initiated when
This screen will be initiated when the originator adds
 a purchase order with a status of 'Proposed'.

Override Operators button
Click this button to select an operator who is allowed
 to perform any step in the workflow. Operators can be added and removed
 from this list if you have security permissions to do so.

Status
Select a status for the selected purchase order:
 Active or
 Inactive.

Reject to
If a step is rejected in a workflow, select whether to
 return to the Prior
 step or back to the Originator.

New/Edit
Click this button to open the [Workflow Steps](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/workflow-steps) window to add or
 edit steps for this workflow.
If the Payroll (PR) Time Card Approval workflow type
 is selected, the [Time Card Approval Workflow Definition](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/time-card-approval-workflow-definition) window displays.

Insert
Click this button to open the [Workflow Steps](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/workflow-steps) window to insert
 a new step in the selected position.
All subsequent steps will be re-numbered if a THEN or
 UPDATE step is inserted. If an AND step is inserted, other records for
 the current step number may need to be revised.

Delete
Click this button to remove the selected step.

Finished when
When the workflow steps are completed, the workflow
 update switches the purchase order status from 'Proposed' to 'Open'.
