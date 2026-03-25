---
title: "Setting Up Timesheet Entry | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/setting-up-timesheet-entry"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/setting-up-timesheet-entry"
---

# Setting Up Timesheet Entry

In order to take advantage of timesheet entry, you must first configure some system and user settings.
 The tasks that you must complete include: setting timesheet permissions for system users, creating timesheet reviewer groups, assigning employees to a reviewer group, and setting up earnings codes for timesheet entry.
The following steps discuss how to configure the system for remote timesheet entry.

1. In HQ Reviewers, [create a reviewer record](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form) for each user who will be reviewing timesheets.

1. Create timesheet reviewer groups in HQ Reviewer Groups. The reviewer group establishes who can approve submitted timesheets. See [Creating Reviewer Groups for Timesheet Entry](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-timesheet-entry) for more information. Note: You can assign reviewer groups at the employee level or at the job level. If you are reviewing timesheet based on both levels, you might want to create multiple groups.

1. In JC Jobs, enter the appropriate reviewer group for the job in the Timesheet field (Reviewer Groups section). If you are creating the job/project in PM Project Manager, enter the appropriate group in the Timesheet field (Reviewer Groups section).

1. In PR Employees, enter the appropriate reviewer group for the employee in the Timesheet Reviewer Group field. Note: Reviewer groups set at the job (in JC Jobs) take precedence (applies only to Job and Mechanic timecards; SM Work Order timecards are not associated with JC jobs). If an employee enters time for a job, and the job has an assigned reviewer group, and the employee has an assigned reviewer group (in PR Employees), then only the job reviewer group can access the timesheet lines from PR My Timesheet Approval. If there is not a reviewer group assigned to the job, the system uses the reviewer group assigned to the employee.

1. Assign timesheet permissions to system users in VA User Profile. Permissions determine whether a user can only enter their own timesheets or if they can enter timesheets for themselves and other employees. See [Setting Timesheet Permissions for Users](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/setting-up-timesheet-entry/set-timesheet-permissions) for more information.

1. In PR Earnings Codes, check the Include in Remote Timesheet Entry box for each earnings code that employees and foremen can use when entering timesheets in PR My Timesheet.

1. Make sure that your users have proper security access. When entering timesheet data into PR My Timesheet, users will be entering certain pieces of data that may have datatype or group security active (e.g., job, employee, etc.). If either group or datatype security is active, the user will be unable to enter timesheets against the secured item. See [VA Data Security Setup](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-data-security-setup-form) and [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) for more information. You will want to make sure to set appropriate form security for PR My Timesheet Approval. If users are not assigned a reviewer group at the employee or job level, and they have access to PR My Timesheet Approval, they will be able to approve their own timesheets.
Once you have completed these setup procedures, you can begin to have your employees and foreman enter timesheets directly into the system. See [Entering Timesheets](/en/vista/vista/hr-and-payroll/payroll/time-entry/timesheets/entering-timesheets) for more information.

Related information

- [About the HQ Reviewers Form](/en/vista/vista/administration/headquarters/reviewer-setup/about-the-hq-reviewers-form)
