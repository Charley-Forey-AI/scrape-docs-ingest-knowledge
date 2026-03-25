---
title: "SM Agreements Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form"
---

# SM Agreements Form

Use the SM Agreements form to set up agreements with customers for services you perform.
For each agreement, you will specify the agreement type, customer, effective and expiration dates, rate template, and pricing, as well as the services that will be included in the agreement and the agreement billing schedule. The services you define for an agreement can be included in the agreement price or can be priced and billed separate from the agreement.

## Separate Scope Per Service Item

If you are using the [Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling) feature for agreements, you can use the Separate Scope Per Service Item checkbox to have the system create separate work order scopes for each service item on an agreement during work order generation (in SM Generate PM Work Orders). This allows you to track all costs captured on a work order scope to a specific serviceable item.
 Using this feature requires the following:

- At least one maintenance must be set up for each serviceable item class (in SM Serviceable Item Class, Maintenance tab) that you assign to serviceable items.

- You must set up one or more tasks (in SM Class Maintenance, Tasks tab) for a maintenance, each with the Recommended checkbox selected.

- Add serviceable items/maintenances to your agreement using the Tasking button (in SM Agreements) and then schedule the maintenance tasks using the Task Scheduling button (also in SM Agreements).

During work order generation, the system generates a work order with separate scopes for each applicable service item (those with the same price method, call type, service site, service center, and division, if applicable). If the service item's criteria does not match, the system generates a separate work order for that service. The system also generates a separate work order for any service with the Separate Work Order checkbox selected in SM Service.
Note: You can select the Separate Scopes Per Service Item for existing agreements, as long as the agreement is in quote status. If the agreement is active and no work orders have been generated, you can either deactivate the agreement or create an amendment to make that change. If the agreement is active and you have already generated work orders, you must first delete the work orders before deactivating the agreement or creating an amendment.

## Posted Detail

The Posted Detail tab displays posted revenue details for agreements revenue posted via SM Agreement Amortize Revenue or SM Invoices. For each posted agreement line, the grid shows a debit or credit entry. Posted revenue details include service, source company, post month, batch ID, source (SM Agreement Amortize Revenue or SM Invoices), transaction type, GL company, GL account, and the debit or credit amount.

Select the following links for related tasks:
[Set up an Agreement in SM Agreements](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements)
[Set up an Agreement Budget](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-budget)
[Agreement Service Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup)
[Agreement/Service Billing
 Schedule Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-billing-schedule-setup)
[Agreement/Service Amortization Schedule
 Setup](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreementservice-amortization-schedule-setup)
[Set up Labor Allocations](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-labor-allocations)
[Set up an Agreement Task Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/set-up-an-agreement-task-schedule)
[Define Spot Work Coverage on an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/define-spot-work-coverage-on-an-agreement)
[Add Maintenance Tasks to an Active Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/add-maintenance-tasks-to-an-active-agreement)
[Add Serviceable Items/Tasks to an Active Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/add-serviceable-itemstasks-to-an-active-agreement)
[Modify the Remaining Amount to Bill for an
 Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-the-remaining-amount-to-bill-for-an-agreement)
[Modify an Agreement Billing Schedule](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/modify-an-agreement-billing-schedule)
[Amend an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments/amend-an-agreement)
[Terminate an Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination/terminate-an-agreement)
[Reactivate a Terminated Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-termination/reactivate-a-terminated-agreement)
[About Agreement Notes / Attachments](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-notes--attachments)
[About Removing Maintenance Tasks from an Active Agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling/about-removing-maintenance-tasks-from-an-active-agreement)
[About Agreement Renewals](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-renewals)

Related information

- [About Agreement Versions / Terms](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-versions--terms)

- [About the Agreement Status](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-the-agreement-status)

- [About Estimated Profit Margin / Markup Percent](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-estimated-profit-margin--markup-percent)

- [About Estimated Service Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-estimated-service-revenue)

- [About Revenue Distributions by Department](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/about-revenue-distributions-by-department)

- [About Tasking / Task Scheduling](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/about-tasking--task-scheduling)

- [Service Schedules](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/service-schedules)

- [About Agreement Amendments](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-amendments)

- [About Changing Agreements / Services After Activation](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-modifying-agreements--services/about-changing-agreements--services-after-activation)

- [About Canceling / Deleting Agreement Quotes](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-canceling--deleting-agreement-quotes)

- [SM Agreement Adjustment Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-adjustment-form)
