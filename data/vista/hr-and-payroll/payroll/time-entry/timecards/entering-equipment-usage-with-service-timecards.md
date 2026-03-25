---
title: "Entering Equipment Usage with Service Timecards | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-equipment-usage-with-service-timecards"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-equipment-usage-with-service-timecards"
---

# Entering Equipment Usage with Service Timecards

If you have purchased the Equipment Management (EM) module, you can enter usage hours for equipment that was operated by an employee with service timecards in PR Timecard Entry.
Note: This functionality is only available for customer work
 orders; all equipment-related fields will be disabled for job work orders.
To enable this feature:

1. Open the PR Company Parameters form and select the company to work with.

1. Click the on Equipment tab.

1. Select the Enter Equipment Usage with Time Cards checkbox.

1. Save the record.

1. Open a timecard batch in PR Timecard Entry.

1. From the Options menu, select Post Equipment Usage. This should display and enable the equipment usage
 fields (EM company, equipment, revenue code, etc.) and allow
 entry of equipment usage with each service timecard. If you do
 not see these fields in the grid, you will need to set the
 display options in [PR User Grid Options](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-user-grid-options-form)
 (accessed via PR Timecard Entry by selecting Options > Customize
 Grids).
Note: The EM Co and Equip fields display either before or after the Class field, depending on how you have set the Equipment Class Override
 option in PR Timecard Entry (Options menu). For more information, see [Equipment Class Override ](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/equipment-class-override).
When you enter an employee’s time and specify a piece of equipment, the usage hours default the same as the employee’s hours; however, you can override this setting. The revenue code specified for the timecard line determines the Time UM that the usage hours represent.
 Once you save the timecard line, the system generates a work completed labor line and work completed equipment line for the work order in SM Work Orders (Work Completed grid). When you process payroll and run PR Ledger Update, the system updates the equipment usage as revenue to EM and as a cost to the work order in SM.
Note: Work completed equipment lines generated from a timecard
 cannot be edited in SM; all edits must be handled via PR Timecard Entry.
 Additionally, work completed equipment lines entered in SM will not update labor
 entries (on timesheets or timecards) in Payroll.

Related information

- [About the PR Timecard Entry Form](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-the-pr-timecard-entry-form)

- [About Customizing Timecard Entry](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-customizing-timecard-entry)
