---
title: "SM Work Completed Misc Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-misc-form"
---

# SM Work Completed Misc Form

Use the SM Work Completed Misc form to add, edit, or review work completed Miscellaneous lines for a work order.
Access this form by:

-  Double-clicking any Miscellaneous line on the Work Completed tab of SM Work Orders.

- Selecting Miscellaneous from the Work Completed drop-down in the SM Work Orders toolbar.

Work completed miscellaneous lines are used to capture miscellaneous expenses associated with a work order, such as trip charges, fuel surcharges, waste disposal, and so forth. The system uses the information entered for each line to determine the costs incurred, as well as the charge to the customer or job.
The system automatically generates miscellaneous work completed lines from standard charges or miscellaneous requirements associated with the work order. These lines are assigned a 'Provisional' status and will retain that status until you manually post the batch in SM Work Order Cost Posting.
If you are using the agreements feature and you want the system to automatically generate miscellaneous work completed lines from standard charges associated with an agreement, you must select the Apply Standard Charges to Agreement Work Orders checkbox in SM Company Parameters. If you do not select this checkbox, you must manually add miscellaneous work completed lines for standard charges associated with the agreement. For more information, see [Apply Standard Charges to Agreement Work Orders](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#ID-00042859--en).
Miscellaneous work completed lines are also used to generate invoices for customer work orders. Job invoices, however, can only be billed using the Job Billing or Accounts Receivable module. For information, see [About Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders).
You can access this form as often as needed to edit existing entries before you bill the work completed line. Once you bill the work completed line (i.e., generate and process an invoice), edits will only be allowed via the SM Invoice Review form.

## Miscellaneous Expenses Entered via AP Transaction Entry

You can capture miscellaneous expenses for an SM work order using AP Transaction Entry and AP Unapproved Invoice Entry. When you post an AP invoice batch, the system generates a separate work completed miscellaneous line for each transaction line that references an SM work order (line type S-SM Work Order). The cost values (quantity, rate, tax, and total) are based on the Units, UC, Gross, Misc Amt, and Tax values for the AP transaction. For customer work orders, the billable amount is set equal to the cost total; however, the billable quantity and rate is set as null. For job-related work orders, the billable amount is determined by the costing method specified on the work order.
In addition, the Accounts Payable section shows the AP Co, Vendor, Reference number, and line number associated with the work completed entry. This information is display only and cannot be edited. With the exception of cost values, you can edit all other information entered for the AP transaction; however, the changes are not updated to AP. Edits to the cost values must be handled using AP Transaction Entry.
The following applies to all miscellaneous expenses entered for a work order in AP:

- If you enter a value in the Misc Amt field for the AP transaction line, that amount is included in the cost total for the work completed line. However, neither the quantity or rate is adjusted, so the total will not match the calculation of quantity x rate.

-  Work order scopes referenced on a detail line must be assigned a call type and rate template. If the scope is missing either or both of these values, AP batch validation will generate an error report indicating that these values are needed before work completed can be entered for the scope. You must assign a call type and/or rate template to the work order scope before you can post the batch.

- You cannot use the SM Work Completed Misc form to delete a work completed miscellaneous line that originated in AP; that must also be handled using AP Transaction Entry (by pulling the transaction back into a batch and setting the Action field to Delete). When you post the batch, the transaction is deleted from the AP files and the work completed line deleted from the work order. Note: If you delete an AP transaction and the corresponding work completed miscellaneous line has already been billed, the work completed line is not deleted; however, the cost values are set to 0.00

Select the link below for more information about capturing miscellaneous expenses on a work order.
[Enter Work Completed Miscellaneous for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order/enter-work-completed-miscellaneous-for-a-work-order)

Related concepts

- [About SM Work Order Cost Adjustments](/en/vista/vista/service-management/work-orders/about-sm-work-order-cost-adjustments)

Related tasks

- [Set Up Standard Charges for a Customer or Service Site](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-standard-charges-for-a-customer-or-service-site)

Related information

- [Set Up Standard Charges for a Customer or Service Site](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-standard-charges-for-a-customer-or-service-site)

- [Set Up Miscellaneous Requirements](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/required-resources-for-work-orders/set-up-miscellaneous-requirements)

- [SM Work Completed Equipment Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-equipment-form)

- [SM Work Completed Labor Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-labor-form)

- [SM Work Completed Inventory Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-inventory-form)

- [SM Work Completed Purchase Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
