---
title: "About the HR Leave Request Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/leave/about-the-hr-leave-request-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/leave/about-the-hr-leave-request-form"
---

# About the HR Leave Request Form

Use this form to enter leave requests.
Once you enter a request, the approver assigned to your approval group is responsible for approving or denying the request. The system sends an email notification to you when the approver sets an approval status.
Note: The system sends an email notification based on the preferences set for you in VA User Profile or in the User Options form. For more information, see [VA User Profile ](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) or [User Options ](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form) for more information.
You can also use this form to monitor all scheduled leave requests and their approval status.
Note: To ensure that the correct information displays for an employee in the Leave Totals by Code display fields, do not apply bEmployee datatype security to the PRLH and PREL tables. For more information on datatype security, see [Setting Datatype Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes).

## Requesting Leave

When you first access this form, it
 automatically defaults to your resource number in the upper, left-hand corner of the
 screen. The Grid Hours field displays the total number of hours in the grid for
 requests with a status of New or Approved. If there are requests in the grid, the
 system displays information based on leave code in the Leave Totals by Code section.
 Depending on the selected grid record, this section displays the leave code,
 available leave total for the code, pending leave (scheduled leave that has not been
 taken yet), balance leave (available leave minus pending leave), and the last date
 that leave information was posted from the Payroll (PR) module.

- If the system does not display
 any records based on your filtering criteria, but you have leave associated
 with the code that you enter in the Leave Code filtering field, the system
 displays leave totals for that code in the Leave Totals by Code section.


- Leave totals may not be accurate
 if information has not been posted recently from PR. If the date in the Last
 PR Post Date is more than a few weeks old, you may want to double-check
 leave totals with your organization’s payroll department. The PR Auto Leave
 Accrual/Usage form is used to post PR leave information to HR.

To enter a leave request for a single
 day, enter the date, leave code, hours, and any additional comments in the grid.
 Repeat this for any other single day requests and save the record as usual.
To enter a leave request for multiple
 days, click Add. The system displays the HR Multi-Day Leave Request form. Use
 that form to enter multiple, consecutive leave days. You can also use that form to
 enter single-day leave requests. For more information, refer to HR Multi-Day Leave
 Request in Related Topics below.
Once you enter your request, the
 approver assigned to your approval group will review your request using HR Leave
 Approval. When the approver updates the status, the system sends you an email
 notification via your notification preference.

## Viewing Scheduled Leave

You can use this form to view the status
 of all your scheduled leave requests. Once the approver sets a status for your
 requests in HR Leave Approval, the system updates the status field in the grid,
 along with the name of the approver (Approver field), and any comments
 from the approver (Approver Comments field).
If there are a number of requests in the
 grid, you can use the fields in the Scheduled Leave Filter section of the form to
 search for requests within a specific date range and/or requests with specific leave
 codes. Enter the filtering criteria in the fields and click Refresh. The grid displays all requests meeting the criteria.

## Deleting Leave Requests

You can delete leave requests from this form that have a New
 status. To delete, select the request record in the grid and click the Delete
 button or select Records  > Delete. Leave requests with all other statuses remain in the grid and you
 cannot delete them.
[ About the HR Multi-Day Leave Request Form](/en/vista/vista/hr-and-payroll/human-resources/leave/about-the-hr-multi-day-leave-request-form)
[PR Auto Leave Accrual/Usage Form](/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-auto-leave-accrualusage-form)
