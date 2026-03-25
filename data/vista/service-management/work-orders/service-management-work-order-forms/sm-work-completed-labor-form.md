---
title: "SM Work Completed Labor Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form"
---

# SM Work Completed Labor Form

Use the SM Work Completed Labor form to add, edit, or review work completed Labor lines for a work order.
Access this form by:

- double-clicking any Labor line on the Work Completed tab of SM Work Orders.

- selecting Labor from the Work Completed drop-down in the SM Work Orders toolbar.

Work completed labor lines are entered once the work requested by a service site (customer or job) is complete, and are used to record the hours a technician worked on a work order. The system uses this information to determine the costs incurred, as well as the charge to the customer or job. Labor lines will generate timesheets in PR (if you elected to update PR in SM Company Parameters) and update costs to jobs in JC (job work orders).
Labor lines are also used to generate invoices for customer work orders; job work orders can only be billed using the Job Billing or Accounts Receivable module.
 For more information about billing customer work orders, see [SM Invoice Review Form](/en/vista/vista/service-management/sm-invoices/service-management-invoice-forms/sm-invoice-review-form). For information about billing job work orders, see [About Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders).
You can access this form as often as needed to edit existing entries before you bill the work completed line. Once you bill the work completed line (i.e., generate and process an invoice), edits will only be allowed via the SM Invoice Review form.

## Updates to PR Timesheets

If the PR interface checkbox is selected in SM Company Parameters, the hours entered for a technician on a work completed labor line automatically generate a timesheet entry in PR My Timesheet. In addition to the employee name and number, each timesheet includes the work order and scope, as well as the pay type, earnings code, shift, and craft/class (if specified). Based on the date specified on the work completed line, the technician's hours will appear in the appropriate day/date column on the timesheet.
You can also capture labor hours for an SM work order directly in PR My Timesheet or PR Timecard Entry. The system generates corresponding work completed labor entries on the work order in SM Work Orders.
Important: In order to capture labor hours for work orders in PR My Timesheet or PR Timecard Entry, you must be set up in VA User Profile with a PR Co and Employee designation, as well as the appropriate My Timesheet Permissions setting. If this is not done, you will be unable to enter timesheets or timecards until the appropriate information is entered in VA User Profile. For more information, see [Set Timesheet Permissions](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/set-timesheet-permissions).

You can edit the labor information for a technician in either this form or the PR My Timesheet form as often as necessary until the timesheet is approved and sent to a timecard batch. Further edits must then be made via PR Timecard Entry. If you edit work completed labor lines for a timesheet that has been approved but not sent to a timecard batch, the system automatically "unapproves" the timesheet. You will need to approve the timesheet with the changes before sending to a timecard batch.
Important: Because timesheet data updates work completed labor and vice-versa, it is highly recommended that you use either PR My Timesheet or SM Work Orders to record labor hours for a technician, not both. This will ensure accuracy and prevent duplication of information.

## Labor Hours Entered in PR Timecard Entry

If you use PR Timecard Entry to capture labor hours for a work order, the system generates a work completed labor line once you save the timecard line. When you process payroll and run PR Ledger Update, the system updates the actual hours and cost to the work order in SM.
Note: If you entered equipment usage with the service timecard, the system will also generate a work completed equipment line. During the PR Ledger Update, the system updates the equipment usage as revenue to EM and as a cost to the work order in SM.

Edits to work completed labor lines generated from a service timecard are limited to the agreement/revision, reference number, serviceable item, billable information, tax information, and the revenue accounts. All other changes must be made in PR Timecard Entry. Additionally, all updates to SM and GL for these lines are done using PR Ledger Update.
A Work Completed Labor record that has not been invoiced is automatically deleted from the Work Order when the corresponding PR Timecard record is deleted or the SM Work Order or Scope assignment is changed. If the work completed labor line was generated from a service timecard (in PR Timecard Entry) and you included equipment usage with the timecard, the related equipment work completed record is also deleted.
If the Work Completed Labor record has been invoiced, the cost total is set to zero and the link to the PR Timecard record removed. If the work completed labor line was generated from a service timecard that included equipment usage, the cost total is set to zero for the equipment work completed line as well, and the link to the PR Timecard record removed.

Select the following link for more information about capturing labor on a work order.
[Enter Work Completed Labor for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-labor-for-a-work-order)

Related information

- [Enter Cost Adjustments for Work Completed Lines](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments/enter-cost-adjustments-for-work-completed-lines)

- [GL Updates: Work Completed Labor](/en/vista/vista/service-management/work-orders/updates-to-gl/gl-updates-work-completed/gl-updates-work-completed-labor)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [SM Technicians Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form)

- [SM Pay Types Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-pay-types-form)

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Misc Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Completed Purchase Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form)
