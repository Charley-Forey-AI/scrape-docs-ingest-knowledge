---
title: "Enter Customer SM Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders"
---

# Enter Customer SM Work Orders

You can use the SM Work Orders form to enter customer work orders.
It is not uncommon for work orders to be entered on the fly. Therefore, only a minimal amount of data is required to get the work order in the system. Remaining data can be entered later when more information is available.
Note: To view a brief video about creating work orders, click [here.](http://cdnedge.viewpointcs.com/lms/ServiceManagement/eLearning/Create%20a%20Work%20Order%20output/story.html)
The following steps guide you through the process of manually setting up a customer work order. Steps prefaced with "Required" are needed in order to save the work order. All other steps can be done later.

1. Open the SM Work Orders form.

1. Required. In the Work Order field, accept the system defaulted work order number or enter a new work order number.

1. In the Description field, enter a description of the service request.

1. Required. In the Site field, enter the service site requesting the service work. The customer associated with the service site defaults in the Customer field and cannot be changed or deleted. If the work order is for new service site, press F5 to access the SM Service Sites form. Once you have set up the service site and returned to this form, enter the new service site here.
Note: When setting up service sites on-the-fly, it is only necessary to enter the service site and owner. Remaining information can be entered later.

1. In the PR State and PR Local Code fields, enter the payroll state and local code for the work order. For information about how these fields are used, see the F1 help.

1. In the Lead Tech field, enter the lead technician for this work order or press F4 to select from a list of preferred technicians for the service site or customer.Leave this field blank to have the system auto-assign a lead technician for you. See the [F1 help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#ID-000454d2--en) for more information.

1. In the Reviewer field, enter a reviewer’s ID in this field to enable that user to mark work orders as ready to bill. Press F4 for a list of active reviewers.

1. Required. In the Center field, enter the service center that will be performing the requested work. Defaults the service center assigned to the service site or customer, if applicable.

1. In the Site Contact section, use the Name and Phone fields to enter the name and phone number of the service site contact for this work order.

1. In the Requested By section, use the Name and Phone fields to enter the name and phone number of the person who requested the service work.

1. In the Date and Time fields, enter the date and time of the service request.

1. Select the Certified Payroll checkbox to include this work order on Certified Payroll reports. Then use the Start Date for Certifieds field to enter the start date for certified payrolls (typically the date labor started).If you do not select the Certified Payroll checkbox, leave the Start Date for Certifieds field blank.

1. In the Craft Template field, accept the defaulted template (which defaults from the service site), or enter the craft template to apply to the work order. Press F4 to select from a list of valid craft templates.

1. Click Save.The system automatically generates a single work order scope, defaulting standard information (such as the rate template and 'bill to' customer). You are not required to fill out the remainder of the information to save the scope; it can be filled out later if needed.Note: If you have set up F3 overrides at the scope level for default behaviors or added "required value" validation, this may impact the system's ability to auto-add and save the work order scope. If the defaults are invalid or you require entry in a field and do not auto-default a value, the system displays an error indicating the problem. Although it creates the scope, you cannot save the record until the correct information is entered.

Enter remaining/additional information for the work order and scopes as needed. For more information, click on the links below.[Enter Time and Material Work Order Scopes](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-time-and-material-work-order-scopes)
[Enter Flat Price Work Order Scopes](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-flat-price-work-order-scopes)
[Enter Non-Billable Work Order Scopes](/en/vista/vista/service-management/work-orders/enter-customer-sm-work-orders/enter-non-billable-work-order-scopes)
[Set up a Trip via SM Work Orders](/en/vista/vista/service-management/call-handler--dispatch-board/sm-dispatch-board/about-using-the-dispatch-board/about-trips/set-up-a-trip-via-sm-work-orders)
[About Entering an SM Purchase Order](/en/vista/vista/service-management/purchase-orders/about-entering-an-sm-purchase-order)
[About Capturing Work Completed for a Work Order](/en/vista/vista/service-management/work-orders/about-capturing-work-completed-for-a-work-order)
[Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
