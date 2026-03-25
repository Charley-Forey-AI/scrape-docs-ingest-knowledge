---
title: "Set up an Agreement Task Schedule | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule"
---

# Set up an Agreement Task Schedule

Task schedules allow you to specify the months within an agreement term in which maintenance or other service tasks will occur.
You will use the [SM Agreement Task Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-task-schedule-form) form to set up task schedules for agreements. When you activate the agreement, the system uses the task schedule to create a list of service dates.
When generating service dates for an agreement from a task schedule, the system uses the first of each selected month, since no dates are selected during task scheduling. Therefore, when setting up the task schedule, the months available for scheduling depend on the agreement term.
For example, if your agreement term is 6/1/22 - 5/31/23, the months of June through December will be available for year 2022 and months January through May will be available for year 2023. However, if your agreement term is 6/15/22 - 6/14/23, the month of June 2022 would be disabled; only July 2022 through June 2023 would be enabled. This is because the system would generate a service date of 6/1/22 for June, which falls before the Effective Date of 6/15/22.
Note: You can only set up task schedules for agreement services with the Task Scheduled recurring pattern selected in SM Service (Schedule tab).
To set up an agreement task schedule:

1. In SM Agreements, select the agreement for which to set up a task schedule. The agreement must have a minimum of one agreement service flagged for task scheduling.

1. Click the Task Scheduling button.

1. From the Year drop-down, select the year for which to set up a task schedule. The number of years available will depend on the agreement term.

1. In each of the applicable month columns, enter the task group or press F4 in the Task Group field to select from a list of valid task groups.You may also use the Task Group field to apply the task group to selected cells, instead of entering the group into each cell separately. To do this:

1. Enter the Task Group code for this agreement task schedule or press F4 to select from a list SM Task Groups.

1. Highlight cells to apply the task group to.

1. Click the Update Selected button to apply the task group to the selected cells. From here, you can click Clear Selected to remove the task group from selected cells.

Note: When assigning a task group to a month, the system may highlight the month if certain discrepancies occur. For more information, see [What Do the Colors Mean?](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board) in the SM Agreement Task Schedule help.
For information about task groups, see [SM Task Group Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-task-group-form).

1. Click Save.

1. Repeat Steps 3-4 as applicable for each year in the agreement term.

Once you activate the agreement, the system automatically generates a service schedule based on the data entered here and displays it on the Work Orders tab in SM Agreements.

Related information

- [Set Up Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking)
