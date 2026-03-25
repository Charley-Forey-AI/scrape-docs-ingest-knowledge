---
title: "About Types of SM Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders"
---

# About Types of SM Work Orders

The Service Management module supports Customer, Job, and Preventative Maintenance work
 orders.
All work orders are maintained in the SM Work
 Orders form. Customer and job work orders are entered manually, while preventative maintenance
 work orders are generated using the SM Generate PM Work Orders form.

## Customer Work Orders

Customer work orders are used when service work will be costed and billed to a customer.
 These work orders are created when the service site specified on the work order has a Type
 of C-Customer (in SM Service Sites). Work completed for these work
 orders is billed directly in Service Management to the "Bill To" customer specified on the
 work order scope.

## Job Work Orders

Job work orders are used when service work
 will be costed to a job and billed in the Job Billing or Accounts Receivable modules. These
 work orders are created when the service site specified on the work order has a Type of
 J-Job.
When capturing work completed for job work
 orders, the system uses the phase and cost type associated with the work completed line to
 post the costs to specified job in Job Cost (via the JC Cost Detail table). The Costing Method
 defined for the work order determines how the system sends costs to JC. If the costing
 method is Actual Cost, the system sends actual costs to JC. If the costing method is Markup,
 the system sends revenue (cost pus markup) as cost to JC. For more information, see the
 [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-0004543a--en) help.
Records interfaced to the Job Cost Detail
 table (JCCD) are assigned a JCTransType as follows:

- EM (work completed equipment)

- MI (work completed miscellaneous)

- IN (work completed inventory)

- PR (work completed labor)

- AP (AP transaction lines with SM Work Order type referencing a job
 work order or transaction lines with PO type referencing an SM job work order).

## Preventative Maintenance Work Orders

Preventative maintenance work orders are
 generated using the SM Generate PM Work Orders form, and apply only to customers with which
 you have one or more active agreements (in SM Agreements).
During work order generation, the system uses a combination of filtering
 criteria to determine which services are due and then based on the services you select, will
 generate work orders accordingly. For services with the Separate Work Order box checked (in SM
 Service), the system creates a separate work order. If multiple services are assigned the
 same service site, service center, pricing method (and rate template, if applicable), call
 type, and schedule date, they are grouped together on the same work order/scope.
If you
 manually add a work order scope, the agreement-related fields are enabled, allowing you to
 associate the work order scope with the appropriate agreement. However, these work order
 scopes will be considered "add-ons" and cannot be associated with a specific service on the
 agreement. In addition, the add-ons are billed separately from the agreement (either in SM
 Work Orders or in SM Work Order Billing).

Related concepts

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

Related tasks

- [Enter Customer SM Work Orders](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders)

- [Enter Job SM Work Orders](/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders)

- [Generate Preventative Maintenance Work
 Orders](/en/vista/vista/service-management/work-orders/about-types-of-sm-work-orders/about-preventative-maintenance-work-orders/about-the-work-order-generation-process/generate-preventative-maintenance-work-orders)
