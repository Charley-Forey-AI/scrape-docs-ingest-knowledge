---
title: "Set up a Periodic Service Billing Schedule Manually | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-a-periodic-service-billing-schedule-manually"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-a-periodic-service-billing-schedule-manually"
---

# Set up a Periodic Service Billing Schedule Manually

All agreement services that are flagged as Periodic, Billed Separately require that you set up a billing schedule before you activate the related agreement.
The system uses the billing schedule during the periodic billing process to determine which services defined for the work schedule are due for billing, as well as the amount to bill.
 You can set up billing schedules manually using the Billing Schedule grid of [SM Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form) or using the [SM Work Schedule Billings](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-work-schedule-billings-form) form (accessed by double-clicking in the Billing Schedule grid).
Note: You will typically use this form to set up a billing schedule when billing dates and amounts differ or when you only have a few billings to schedule. If you typically schedule billings for the same date and amount, you can use the [SM Automatic Scheduling](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-automatic-scheduling-form) form to [set up billing schedules automatically](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup/set-up-an-agreement-billing-schedule-automatically).
You can set up a single billing sequence for the total service price or set up multiple billing sequences with equal or varying amounts. For example, if you bill once a year, you will need to set up one billing sequence for each year the service is performed, based on the agreement term (e.g., if the agreement term is 2 years, you would set up two billing sequences).
The Total Remaining field (above the tab pages) displays the remaining amount to be scheduled for billing. Initially, this amount will show the total service price (for the term of the agreement). As you enter billing sequences, the Total Remaining amount will decrease until the full amount is dispersed.
The following steps will guide you through setting up billing schedules for services on a work schedule using the Billing Schedule tab.
Note: If you have not set up the service work schedule, you must do so before you can continue here. See [SM Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form) for more information.

1. From the Programs menu of Service Management, double-click on the SM Agreements icon. The SM Agreements form displays.

1. In the Agreement field, select the agreement for which you are setting up a work schedule billing schedule.

1. Click on the Work Schedule tab and then double-click in the grid to open the SM Service form.

1. In the Service Seq field, enter the service for which to define a billing schedule.

1. Click on the Billing Schedule tab.

1. In the Billing Seq field, enter N, New, or +. The system automatically assigns the next sequential number available.

1. Enter the billing date for this sequence in the Date field. The system uses this date to determine which services are due for billing.

1.  In the Billing Amount field, enter the amount to bill for this sequence.

1. From the Tax Type drop-down, select 1-Sales, 2-Use, or 3-VAT to identify the type of tax for this line, or accept the default (if applicable).The system enables the Tax Code and Basis fields.
Note: The tax type will automatically default to 3-VAT for Australian and Canadian companies (i.e. where the Default Country field in HQ Company Setup is AU or CA).

1. Enter a tax code in the Tax Code field or press F4 for a list of codes.Note: If the Tax Type is 3-VAT, you must enter a VAT tax code (i.e., tax code with the Value Added Tax (VAT) box checked in HQ Tax Codes).

1. Enter the tax basis in the Basis field. Note: The Amount field will be updated with the tax amount after invoicing has occurred.

1. Enter any pertinent information about this billing sequence in the Notes field.

1. Save the record.

1. Repeat steps 6-10 for any additional billing sequences needed for this service.

1. Repeat steps 4-11 to set up billing schedules for other applicable services on the work schedule.
