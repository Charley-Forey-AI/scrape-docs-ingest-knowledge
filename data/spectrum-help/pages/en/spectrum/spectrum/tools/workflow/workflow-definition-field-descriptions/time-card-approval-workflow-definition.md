---
title: "Time Card Approval Workflow Definition | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/time-card-approval-workflow-definition"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/time-card-approval-workflow-definition"
---

# Time Card Approval Workflow Definition

This window displays when the Payroll - Time Card Approval option is selected from the Select Workflow Type window in the [Workflow Definition Field Descriptions](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions) screen.

- You are prompted for which type of approval the current company will use: Employee's supervisor and/or Job contact it will also prompt for whether reviewers may reject time cards--ending them back to a defined group of Payroll staff, for further review and correction.

- If Approve by employee? is selected, workflows will be created by employee code + check sequence and the employee's Supervisor will see a list of employees (by check sequence) assigned to him/her to review. When this option is selected, the workflow starts when a pre-time card line is added. These Reviewers will likely review the employee's time cards as each pay period ends.

- If Approve by job?
 is selected, workflows will be created by job code + phase code + work date and
 the job contact--for example, the Project Manager--will see a list of jobs and
 phases (by day) assigned to him/her to review. These Reviewers will likely
 review the job time cards on a daily basis. When this option is selected, the
 workflow starts when a pre-time card is entered OR when a user enters a
 different 'job code' or 'phase code' or 'work date' into an existing pre-time
 card record. •

- If both Approve by employee? and Approve by job? are selected, the Time Card Approval screen will display a list that includes both record types. A new pre-time card entry for a 'job' will initiate TWO Workflows (one for the employee supervisor and one for job approval).

- If Allow reviewer to 'Reject'? is selected, you will be prompted to select the Workflow group who will be responsible for handling the rejected records.

- If Allow override operator to modify approved time cards? is selected, the workflow will allow approved operators to modify approved time cards.

- Like other Spectrum Workflows, the administrator can use the Override Operators button to define a list of [Override Operators](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/time-card-approval-workflow-definition/override-operators)

- Like other Workflows, an Active/Inactive Status flag is provided for the Administrator to specify whether the particular Workflow impacts operations in the current company.
