---
title: "Set up an Agreement Amortization Schedule Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-manually"
---

# Set up an Agreement Amortization Schedule
 Manually

You can set up amortization schedules for eligible agreements directly in the Amortization Schedule grid of SM Agreements or using the SM Agreement Amortization Sched form (accessed by double-clicking in the Amortization Schedule grid).
Eligible agreements are those with the Revenue Recognition drop-down set to S-Amortize.
When setting up amortization schedules for agreements, you must make sure that the total amount of all deferral sequences equal the total amount of the agreement. The Total Remaining field above the tab pages will display the total amount to defer and then adjust as each deferral sequence is entered.
The following steps detail how to set up amortization schedules using the Amortization Schedule grid in SM Agreements.

1. Launch the SM Agreements form.

1. Select the agreement for which to set up the revenue amortization schedule.Note: You can only set up an amortization schedule for agreements with the Recognize Revenue drop-down set to S-Amortize.

1. Click on the Amortize Schedule tab.

1. In
 the
 Deferral field, enter N,
 New,
 or + to create a new deferral. The system
 will automatically assign the next sequential number
 available for the agreement.

1. In the Date field, enter the deferral date.Note: The system will use this date to determine if the deferral amount should be recognized when running the amortization process (in SM Agreement Amortize Revenue).

1. In the Amount field, enter the deferral amount.Note: The system will 'recognize' this amount as revenue when running the amortization process if the deferral is eligible (i.e. is in the date range specified during amortization and the specified amount is available for recognition).

1. In the Notes field, enter any notes that apply to the deferral.

1. Save the record.

1. Repeat Steps 4-8 for additional deferrals, making sure that the total amount of all sequences is equal to the total amount of the agreement (i.e. the Total Remaining is 0.00).

Related information

- [Set up an Agreement Amortization Schedule Automatically](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-automatically)
