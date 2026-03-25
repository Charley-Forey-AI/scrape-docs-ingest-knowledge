---
title: "Enter Job SM Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders"
---

# Enter Job SM Work Orders

You can enter job-related work orders using the SM Work Orders form.
It is not uncommon for work orders to be entered on the fly. Therefore, only a minimal amount of data is required to get the work order in the system. Remaining data can be entered later when more information is available.
The following steps guide you through the process of manually setting up a job work order. Steps prefaced with "Required" are needed in order to save the work order. All other steps can be done later.

1. Open the SM Work Orders form.

1. Required. In the Work Order field, accept the system defaulted work order number or enter a new work order number.

1. In the Description field, enter a description of the service request.

1. In the Site field, enter the service site requesting the service work or press F4 to select from a list of valid service sites. The Job field automatically defaults the job associated with the service site.Note: If the job is closed and you do not allow posting to closed jobs (that is, the Allow Posting to Hard-Closed Jobs and/or Allow Posting to Soft-Closed Jobs checkboxes are not selected in JC Company Parameters), you will be unable to save the record.

1. The Costing Method drop-down automatically defaults the costing method defined for the service site (in SM Service Sites). Accept the default or select Actual Cost or Markup to indicate how to send costs to Job Cost for this work order. See the [F1](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-0004543a--en) help for additional information about this field.

1. the Lead Tech field, enter the lead technician for this work order or press F4 to select from a list of valide technicians.Leave this field blank to have the system auto-assign a lead technician for you. See the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000454d2--en) for more information.

1. In the Reviewer field, enter a reviewer’s ID in this field to enable that user to mark work orders as ready to bill. Press F4 for a list of active reviewers.

1. Required. In the Center field, enter the service center that will be performing the requested work. Defaults the service center assigned to the service site.

1. In the Site Contact section, use the Name and Phone fields to enter the name and phone number of the service site contact for this work order.

1. In the Requested By section, use the Name and Phone fields to enter the name and phone number of the person who requested the service work.

1. In the Date and Time fields, enter the date and time of the service request.

1. Save the record. The system automatically generates a single work order scope, defaulting standard information (such as the rate template and 'bill to' customer). You are not required to fill out the remainder of the information to save the scope; it can be filled out later if needed.
Note: If you have set up F3 overrides at the scope level for default behaviors or added "required value" validation, this may impact the system's ability to auto-add and save the work order scope. If the defaults are invalid or you require entry in a field and do not auto-default a value, the system will display an error indicating the problem. Although it will create the scope, you will be unable to save the record until the correct information has been entered.

Enter remaining/additional information for the work order and scopes as needed. For more information, click on the links below.[Enter Job Work Order Scopes](/en/vista/vista/service-management/work-orders/enter-job-sm-work-orders/enter-job-work-order-scopes)
[Set up a Trip via SM Work Orders](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/about-trips/set-up-a-trip-via-sm-work-orders)
[About Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order)
[About Capturing Work Completed for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order)
[About Billing SM Job Work Orders](/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders)

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
