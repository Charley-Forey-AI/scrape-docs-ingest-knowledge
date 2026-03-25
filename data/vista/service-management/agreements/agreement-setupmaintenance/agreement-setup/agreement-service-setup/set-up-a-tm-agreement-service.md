---
title: "Set up a T&M Agreement Service | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-tm-agreement-service"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-tm-agreement-service"
---

# Set up a T&M Agreement Service

You can set up "time and material" (T&M) services for agreements that use a rate template to determine billing amounts for agreement work orders.
If you have not yet [set up the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements), you must do so before you can proceed here.

T&M (rate template) services on an agreement are not billed with the agreement; instead they are billed from the work order or using SM Work Order Billing.Note: You can also set up agreement services directly in the Work Schedule grid; however, to set up work schedules, billing schedules, required resources, and/or amortization schedules for the service, you must use SM Service.

1. From the main menu, select Service Management > Programs > SM Agreements.

1. In the Agreement field, enter the agreement for which you are defining services.

1. Select the Work Schedule tab and double-click in the grid to open SM Service.

1. In the Service Seq field, enter N, New, or +; the system will automatically assign the next available service sequential number.

1. In the Description field, enter a description of the service.

1. In the Service Site field, enter the service site to which this service applies or press F4 to select from a list of valid service sites for the specified customer.

1. In the Assigned Tech field, enter the technician for this agreement service. If the technician is Active in SM Technicians and PR Employees, the system will automatically create a single trip on work orders generated from this agreement service, with this technician designated.If you leave this field blank, the system will not automatically create trips for work orders generated from this agreement service, and will assign the primary technician designated for the service site as the Lead Tech on work orders.

1. In the Call Type field, enter the call type for the service or press F4 to select from a list of valid call types.

1. In the Service Center field, enter the service center that will perform this service if different than the service center defined for the service site (in SM Service Sites) or customer (in SM Customers).

1.  If you entered a service center in the Service Center field, use the Division field to enter the division that applies to the service or press F4 to select from a list of valid divisions for the service center. Leave blank if not applicable.

1. From the Tax Source drop-down, select C-Service Center or S-Service Site to indicate where to default the tax code from for work completed lines entered on a work order for this service.

1. From the Pricing drop-down, select T-Time of Service.

1. Select the Rate Template radio button to the right of the Pricing drop-down.

1. In the Price field, enter the price for the service.

1. In the Rate Template field, enter the rate template to use for the agreement service (required).

1. Select the Separate Work Order checkbox to always generate a separate work order for this agreement service.Leave the Separate Work Order checkbox unselected to combine this agreement service on a single work order with other services when applicable. See the [F1](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form#ID-000414b7--en) help for more information.

1. The Matl Tax Override drop-down defaults the option specified for the agreement (in SM Agreements). Accept the default or select the tax type default to use when entering material-related work completed for a PM work order for this service.

- Blank

- N-No Tax

- S-Sales Tax Only

- Use Tax Only

Note: If you leave this field blank, the system uses the standard tax type defaulting behavior. For more information, see the [F1 Help](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form#ID-000414be--en).

1. The Tax Option
 Override drop-down defaults the option specified for the
 agreement (in SM Agreements). Accept the default or select how to handle taxes
 for materials purchased for a work order associated with this agreement service.
 For more information, see the [F1 Help](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form#concept-hlbyy5r5--en).

- N - Not Taxable

- P - Taxable at Purchase Only

- B - Taxable at Billing Only

- M - Taxable at Purchase/Markup at Billing

- F - Full Tax at Purchase and Billing

1. Save the record.

You can now set up cost estimates, work schedules, and required tasks and resources, as well as billing schedules and amortization schedules (billed separately services only). Select the links below for more information.[Enter Summarized Cost Estimates for Agreement Services](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/enter-summarized-cost-estimates-for-agreement-services)
[Set up Service Work Schedules](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules)
[Set up Required Tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-required-tasks)
[About Setting up Required Resources for an Agreement Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-setting-up-required-resources-for-an-agreement-service)
[Agreement/Service Billing
 Schedule Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup)
[Agreement/Service Amortization Schedule
 Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup)
