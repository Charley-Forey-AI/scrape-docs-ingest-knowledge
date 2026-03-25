---
title: "Setting up a Service Revenue Deferral Schedule Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/setting-up-a-service-revenue-deferral-schedule-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/setting-up-a-service-revenue-deferral-schedule-manually"
---

# Setting up a Service Revenue Deferral Schedule Manually

Set up a service revenue deferral schedule manually.
You can set up revenue deferral schedules for eligible agreement services directly in the Deferral grid of [SM Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form) or using the [SM Agreement Service Deferral](/en/vista/vista/service-management/agreements/revenue-recognition/service-management-revenue-recognition-forms/sm-agreement-service-deferral-form) form (accessed by double-clicking in the Deferral grid). Eligible services are those with the Revenue Recognition drop-down set to S-Amortize for the related agreement and that have a Pricing method of P-Periodic and the Billed Separately box checked.
When setting up deferral schedules for agreement services, you must make sure that the total amount of all deferral sequences equal the total amount of the agreement service. The Total Remaining field above the tab pages will display the total amount to defer and then adjust as each deferral sequence is entered.
The following steps detail how to set up deferral schedules for services using the Deferral grid in SM Service.

1. Launch the SM Agreements form.

1. Select the agreement for which to set up agreement service deferral schedules.

1. Click on the Work Schedule tab.

1. Select the agreement service for which to set up a deferral schedule and then double-click in the grid to open the SM Service form.

1. The Service Seq field automatically defaults to the selected agreement service; accept the defaulted sequence or enter the sequence for which to set up a deferral schedule.

1. Click on the Deferral tab.

1. In the Deferral field, enter N, New, or + to create a new deferral. The system will automatically assign the next sequential number available for the agreement service.

1. In the Date field, enter the deferral date.Note: The system will use this date to determine if the deferral amount should be recognized when running the amortization process (in SM Agreement Amortize Revenue).

1. In the Amount field, enter the deferral amount.Note: The system will 'recognize' this amount as revenue when running the amortization process if the deferral is eligible (i.e. is in the date range specified during amortization and the specified amount is available for recognition).

1. In the Notes field, enter any notes that apply to the deferral.

1. Save the record.

1. Repeat for additional deferrals, making sure that the total amount of all sequences is equal to the total amount of the agreement service (i.e. the Total Remaining is 0.00).

Related information

- [Set up an Agreement Amortization Schedule Automatically](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup/set-up-an-agreement-amortization-schedule-automatically)
