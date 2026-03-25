---
title: "Create Reviewer Groups for Timesheet Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-timesheet-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-timesheet-entry"
---

# Create Reviewer Groups for Timesheet Entry

Create reviewer groups for timesheet entry.

When implementing [timesheet functionality](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets), you will need to create
 reviewer groups in HQ Reviewer Groups. All users associated with a reviewer group
 will be able to approve timesheets using PR My Timesheet Approval.
Once you create a reviewer group, you can assign the
 reviewer group to the job (in JC Jobs), the
 project (in PM Projects), or to an employee (in PR
 Employees). The system uses a hierarchy to
 determine which reviewer group can approve a
 timesheet. Reviewer groups set at the job/project
 take precedence over any employee reviewer groups
 (applies to job and mechanic timesheets only; SM
 work order timesheets are not associated with JC
 jobs).
For example, if an employee enters time for a job with an assigned reviewer group, and the employee has an assigned reviewer group, only the job reviewer group can access and approve the timesheet lines in PR My Timesheet Approval. In the same example, if a reviewer group is not assigned to the job, only the employee reviewer group can access and approve the timesheet lines. This also means that the same employee can enter multiple timesheet lines, and depending on the reviewer group set up, have more than one group reviewing the timesheet lines.
Note:Even if a timesheet line references a job and/or employee that is not assigned a reviewer group, that timesheet can still be reviewed and approved by users who have access to PR My Timesheet Approval. Make sure that you have set appropriate security permissions to [PR My Timesheet Approval](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-approval-form).

The following instructions detail how to create reviewer groups for timesheet entry.

1. In the Records tab, select New.

1. Enter a name for the group in the Reviewer Group field.

1. Enter a description of the group in the Description field.

1. Select the Active checkbox to indicate the Reviewer Group is "active" and able to approve or deny unapproved invoices or timesheets.

1. Specify the responsible person in the Responsible Person field. Press F4 for a list of available reviewers. The responsible person must be a reviewer in the system (in HQ Reviewers).

1. Select 2-Timesheet from the Reviewer Group Type drop-down field.

1. Use the Reviewers tab to add reviewers to the group. See [Adding Reviewers to Reviewer Groups](/en/vista/vista/administration/headquarters/reviewer-setup/adding-reviewers-to-reviewer-groups) for more information.

1. Save the record as normal.

Related information

- [Activating and Deactivating Reviewers](/en/vista/vista/administration/headquarters/reviewer-setup/activating-and-deactivating-reviewers)

- [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets)

- [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions)

- [Adding Reviewers to Reviewer Groups](/en/vista/vista/administration/headquarters/reviewer-setup/adding-reviewers-to-reviewer-groups)

- [About the PR My Timesheet Approval Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/about-the-pr-my-timesheet-approval-form)

- [About the HQ Reviewer Group Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewer-group-form)
