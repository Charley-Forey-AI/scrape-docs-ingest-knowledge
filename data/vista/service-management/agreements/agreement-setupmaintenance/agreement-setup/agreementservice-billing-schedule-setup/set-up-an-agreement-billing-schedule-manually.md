---
title: "Set up an Agreement Billing Schedule Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-an-agreement-billing-schedule-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-an-agreement-billing-schedule-manually"
---

# Set up an Agreement Billing Schedule Manually

All agreements require that you set up a billing schedule before you activate the agreement.
You can set up billing schedules manually using the Billing Schedules grid in [SM Agreements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form) or the [SM Agreement Billing Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-billing-schedule-form) form (accessed by double-clicking in the Billing Schedule grid).
Note: You will typically use this form to set up a billing schedule when billing dates and amounts differ or when you only have a few billings to schedule. If you generally schedule billings for the same date and amount, you can use the [SM Automatic Scheduling](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-automatic-scheduling-form) form to [set up billing schedules automatically](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-an-agreement-billing-schedule-automatically).
You can set up a single billing sequence for the entire agreement amount or set up multiple billing sequences with equal or varying amounts. For example, if you bill once a year, you will only need to set up one billing sequence for each year of the agreement. If you bill on a quarterly basis, you will need to set up sequences for each quarter for the life of the agreement.
The Total Remaining field (above the tab pages) displays the remaining amount to be scheduled for billing. As you enter billing sequences, the Total Remaining amount will decrease until the full amount is dispersed.
The following steps will guide you through the process of setting up an agreement billing schedule using the Billing Schedule grid.
Note: If you have not already set up the agreement, you must do so before you can continue here. See [Setting up an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements) for more information.

1. From the Programs menu of Service Management, double-click on the SM Agreements icon. The SM Agreements form displays.

1. In the Agreement field, select the agreement for which to define a billing schedule.

1. Click on the Billing Schedule tab.

1. In the Billing Seq field, enter N, New, or +. The system automatically assigns the next sequential number available.

1. Enter the billing date for this sequence in the Date field. The system uses this date to determine which agreements are due for billing.

1.  In the Billing Amount field, enter the amount to bill for this sequence. Amount must be equal to or greater than 0.00.

1. From the Tax Type drop-down, select 1-Sales, 2-Use, or 3-VAT to identify the type of tax for this line, or accept the default (if applicable).The system enables the Tax Code and Basis fields.
Note: The tax type will automatically default to 3-VAT for Australian and Canadian companies (i.e. where the Default Country field in HQ Company Setup is AU or CA).

1. Enter a tax code in the Tax Code field or press F4 for a list of codes.Note: If the Tax Type is 3-VAT, you must enter a VAT tax code (i.e., tax code with the Value Added Tax (VAT) box checked in HQ Tax Codes).

1. Enter the tax basis in the Basis field. Note: The Amount field will be updated with the tax amount after invoicing has occurred.

1. Enter any pertinent information about this billing sequence in the Notes field.

1. Save the record.

1. Repeat steps 4-8 for any additional billing sequences needed for this agreement. Note: To set up billing schedules for periodic services that are billed separately from agreements, see [Setting up a Periodic Service Billing Schedule Manually](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-a-periodic-service-billing-schedule-manually).

Related information

- [SM Agreement Billing Schedule Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-billing-schedule-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Work Schedule Billings Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-work-schedule-billings-form)
