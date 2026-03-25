---
title: "SM Work Completed Equipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form"
---

# SM Work Completed Equipment Form

Use the SM Work Completed Equipment form to add, edit, or review work completed Equipment lines for a work order.
Access this form by:

-  Double-clicking any Equipment line on the Work Completed tab of SM Work Orders.

- Selecting Equipment from the Work Completed drop-down in the SM Work Orders toolbar.

Work completed equipment lines are entered once the work requested by a service site (customer or job) is complete. The system uses the information entered for each line to determine the costs incurred, as well as the charge to the customer or job. Equipment lines are also used to generate equipment usage entries in EM (if you elected to update EM in SM Company Parameters), update costs to JC (job work orders), and generate invoices (customer work orders).
Note: You can only bill Job work orders using the Job Billing or Accounts Receivable modules; you cannot generate invoices for job work orders using Service Management. For more information, see [About Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders).
You can access this form as often as needed to edit existing entries before you bill the work completed line. Once you bill the work completed line (that is, you generate and process an invoice), edits will only be allowed via the SM Invoice Review form.

## Updates to Equipment Management

You can specify to update Equipment Management (EM) when capturing equipment used on an SM work order by selecting the EM interface checkbox in SM Company Parameters. Then, when you enter and save a work completed equipment line in SM Work Orders, the system automatically creates and posts an equipment usage batch. This updates the equipment usage to EM, creating entries in the EM Revenue Detail table (EMRD) and updating the EM Equipment (EMEM) table.
Note: If you change the information for an equipment line, the system automatically creates and posts adjusting entries in Equipment Management and General Ledger.
 If you specified an hour-based revenue code for the equipment line and the Update Hour Meters checkbox is selected for the revenue code (in EM Revenue Rates by Equipment or EM Revenue Rates by Category), the system updates the equipment's hour meter based on the time units entered for the line. If the Time Units are expressed in a unit of measure other than hours, the system uses the Hours/Time Unit (specified in EM Revenue Codes) to convert the Time Units into hours.
If you also specified to allow posting work units with usage (checkbox in EM Revenue Rates by Category or EM Revenue Rates by Equipment), and you entered work units for the equipment line, the system updates the work units to EMRD.

## Entering Equipment Usage in PR Timecard Entry

If you allow entering equipment usage with timecards (that is, you selected the Enter Equipment Usage With Time Cards checkbox in PR Company Parameters), you can capture equipment usage for a work order when entering service timecards in PR Timecard Entry.
As soon as you save the service timecard, the system generates both a work completed labor line and a work completed equipment line for work order. Once you post the batch, process payroll, and run PR Ledger Update, the system updates the equipment usage as revenue to EM and as a cost to the work order in SM.
You cannot edit work completed equipment lines generated from a timecard in SM; all edits must be handled via PR Timecard Entry. Additionally, all updates to EM, SM, and GL for these lines are done using PR Ledger Update.

## Deleting Timecards with Equipment Usage

If you delete a previously posted service timecard that includes equipment usage, the system deletes the related work completed labor and equipment lines from the work order. If the work order has already been invoiced, it will set the cost total for both work completed lines to zero and remove the link to the PR Timecard record.

Select the link below for more information about capturing equipment usage on a work order.
[Enter Work Completed Equipment for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-equipment-for-a-work-order)
[Entering Equipment Usage with Service Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-equipment-usage-with-service-timecards)

Related information

- [Enter Cost Adjustments for Work Completed Lines](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines)

- [GL Updates: Work Completed Equipment](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-equipment)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Completed Purchase Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form)
