---
title: "Enter Equipment Usage with Job Timecards | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-equipment-usage-with-job-timecards"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/enter-equipment-usage-with-job-timecards"
---

# Enter Equipment Usage with Job Timecards

If you have purchased the Equipment Management (EM) module, the charge-out of equipment that was operated by an employee may be entered with job timecard lines in PR Timecard Entry.
This provides a one-step entry that:

- Posts the employee’s time to the job at their pay rate plus burden.

- Charges the equipment to the job at a usage rate.

- Credits the equipment with revenue earned at the usage rate.

If not entered in Payroll, the equipment usage may be directly entered in the Equipment Management module.
To enable this feature:

1. Open the PR Company Parameters form and select the company to work with.

1. Click the on Equipment tab.

1. Select the Enter Equipment
 Usage with Time Cards checkbox.


1. Save the record.

1. Open a timecard batch in PR Timecard Entry.

1. From the Options
 menu, select Post Equipment
 Usage. This should display and enable the equipment usage fields (EM company,
 equipment, revenue code, etc.) and allow entry of equipment usage with each
 job timecard. If you do not see these fields in the grid, you will need to
 set the display options in [PR User Grid Options](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form) (accessed by selecting
 Options  > Customize Grids).
When you enter an employee’s time and specify a
 piece of equipment, the usage hours default the
 same as the employee’s hours, although you can
 override this setting.
Although you might typically post labor and
 equipment usage to the same phase, you do have the
 option to post labor and equipment usage to
 different phases. If you set the Equip Phase
 drop-down field (in PR User Grid Options) to allow
 input, you can override the default (which is the
 job phase) and specify the phase for posting
 equipment usage.
Note: If you
 override the equipment phase, the timecard audit list report (PR Timecard
 Entry Audit List) will show the equipment phase below the job phase line.
 However, if you do not override the equipment phase, it will be excluded
 from the report since it is the same as the job phase.
You can also override the cost type to which equipment usage is posted by
 setting the Cost Type drop-down field
 (in PR User Grid Options) to allow input. This allows you to override the
 equipment's default usage cost type (as specified in EM Equipment) and
 specify the cost type for posting equipment usage. However, the override
 cost type must be valid for the specified equipment phase.
Note: If
 attachments exist for the equipment you are posting usage to, the override
 equipment phase and cost type are also updated for the attachment.

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [About Customizing Timecard Entry](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-customizing-timecard-entry)
