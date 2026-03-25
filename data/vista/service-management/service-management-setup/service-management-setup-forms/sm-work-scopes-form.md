---
title: "SM Work Scopes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-work-scopes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-work-scopes-form"
---

# SM Work Scopes Form

Use the SM Work Scopes form to set up the different scopes of service work performed by your company.
You can use work scopes to identify common problems reported by customers, maintenance work, or services you provide, such as installations, or other small jobs. Whatever needs you meet for your customers, you can define as work scopes.
For example:
General / Small Job
Problems
Maintenance

Installation
No Heat
Electrical

Roof Replacement
No Power
Chillers

Roof Repair
Leaking Pipes
Plumbing

Furnace Replacement
Blown Circuit
HVAC

Re-route Duct work
No Cooling
Roof Re-tar

## Priority

For each work scope you set up, you must assign a priority. Generally, the priority of a work scope drives the priority of a work order; therefore, if a work scope represents an item that does not require immediate action, you would assign it a low priority. Work scopes that represent items needing immediate action (e.g. leaking pipes, power outage, etc.) will generally be a higher priority.

## Default Phase

If you will be assigning a work scope to job-related work orders, you can assign a default phase. When you assign the work scope to a job work order scope, the phase defaults in automatically. When capturing work completed for the work order, the system uses this phase and the cost type specified on the work completed line to post the costs to Job Cost (via the JC Cost Detail table).

- The Default Phase is only used when the work scope is assigned to a job work order. If you add the work scope to a customer work order, the phase is ignored.

- You can override the Default Phase once you add the work scope to a work order sequence (in SM Work Orders).

- You can assign any phase to a work scope; however, when you add the work scope to a job work order, if the job is locked (that is, the Phases on this job are locked checkbox is selected in JC Jobs) and the phase specified here is not set up for the job, a message displays indicating that the phase is not set up for the job. You must either enter a valid job phase or add the phase to the job 'on-the-fly' using the F5 key.

## Revenue Split Setup

 If you use the Flat Price feature for quotes and work orders, you can set up default split revenue entries for each work scope that you will assign to flat price quote and work order scope. Clicking the Revenue Split Setup button accesses the SM Flat Price Revenue form to allow setting up split revenue entries by cost type category or cost type category/cost type. For more information, see [SM Flat Price Revenue Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-flat-price-revenue-form).
Click on one of the following links for more information on using this form.
[Set up a Work Scope](/en/vista/vista/service-management/service-management-setup/set-up-a-work-scope)
[Enter Flat Price Revenue](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/set-up-a-flat-rate-agreement-service/enter-flat-price-revenue)

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
