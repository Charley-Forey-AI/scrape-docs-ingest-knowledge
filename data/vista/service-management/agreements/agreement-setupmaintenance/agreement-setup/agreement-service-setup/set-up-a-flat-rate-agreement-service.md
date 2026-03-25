---
title: "Set up a Flat Rate Agreement Service | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service"
---

# Set up a Flat Rate Agreement Service

Set up Flat Rate services for agreements that will charge a flat price for all work covered on an agreement work order.
If you have not yet [set up the agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements), you must do so before you can proceed here.

You will use the Time of Service pricing method to set up Flat Rate services on an agreement. These services are not billed with the agreement; instead they are billed from the work order or using SM Work Order Billing.Note: You can also set up agreement services directly in the Work Schedule grid; however, to set up work schedules, billing schedules, required resources, and/or amortization schedules for the service, you must use SM Service.

1.  Open the SM Agreements form.

1. In the Agreement field, enter the agreement for which you are defining services.

1. Select the Work Schedule tab and double-click in the grid to open SM Service.

1. In the Service Seq field, enter N, New, or +; the system will automatically assign the next available service sequential number.

1. In the Description field, enter a description of the service.

1. In the Service Site field, enter the service site to which this service applies or press F4 to select from a list of valid service sites for the specified customer.

1. In the Assigned Tech field, enter an (active) technician for this agreement service. If the technician is 'active' in both SM Technicians and PR Employees, the system automatically creates a single trip on work orders generated from this agreement service, with this technician designated.
Leave this field blank if you do not want the system to auto-create trips for work orders generated from this agreement service.

1. In the Call Type field, enter the call type for the service or press F4 to select from a list of valid call types.

1. In the Service Center field, enter the service center that will perform this service if different than the service center defined for the service site (in SM Service Sites) or customer (in SM Customers).

1. If you entered a service center in the Service Center field, use the Division field to enter the division that applies to the service or press F4 to select from a list of valid divisions for the service center. Leave blank if not applicable.

1. From the Tax Source  drop-down, select where to default the tax code from for work completed lines entered on a work order for this service.

- C - Service Center

- S - Service Site

1. From the Pricing drop-down, select T-Time of Service.

1. Select the Flat Rate radio button to the right of the Pricing drop-down.

1. In the Price field, enter the price for the service. The Split button is enabled.

1. Select the Split button to [enter flat price revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue) by cost type category (required).

1. If you want to always generate a separate work for this agreement service, select the Separate Work Order checkbox.If you leave this checkbox unselected, the system includes this agreement service on a single work order with other services when applicable. See the [F1](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form/field-definitions-sm-service-form#ID-000414b7--en) help for more information.

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

1. In the Cost Revenue Margin, enter the expected margin percentage to apply when recognizing revenue for work orders generated from this flat price service.

1. Save the record.

Once you have completed setting up the agreement service, you can set up summarized cost estimates, work schedules, required tasks and resources, and billing schedules (billed separately services only). If you are deferring revenue, you can also set up amortization schedules (billed separately services only). Select the links below for more information.[Entering Summarized Cost Estimates for Agreement Services](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/enter-summarized-cost-estimates-for-agreement-services)
[Setting up Service Work Schedules](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules/about-service-work-schedules/set-up-service-work-schedules)
[Setting up Required Tasks ](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes/set-up-required-tasks)
[Setting up Required Resources for an Agreement Service](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-setting-up-required-resources-for-an-agreement-service)
