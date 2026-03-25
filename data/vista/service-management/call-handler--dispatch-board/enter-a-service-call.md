---
title: "Enter a Service Call | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/enter-a-service-call"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/enter-a-service-call"
---

# Enter a Service Call

Use the SM Call Handler form to enter the information from a service call. Once set up, you can create a work order for the service call.

1. Open the SM Call Handler form using one of the following methods:

- In the main menu, select Service Management > Programs > SM Call Handler

- Open the SM Dispatch Board form and select Call Handler in the toolbar.

1. In the Call
 ID field, enter N, New, or +. The system automatically
 generates the next sequential call ID number, and selects the New Customer and New Site checkboxes.


1. If the service call is for an existing customer:

1. Clear the New Customer checkbox.

1. In the Customer field, enter the customer number or press F4 to select from a list of valid customers.Note: If you enter an inactive customer, the system displays a warning but allows you to save the call record. However, you must activate the customer (in SM Customers) before you can create a work order from the call record.
Tip: You can also use the Search field to locate an existing customer. Just enter any number of characters or words of the customer or service site name or number and press Return. If a single match is found, the system populates the call record with that customer/service site. If more than one match is found, the SM Customer Search Results window displays, showing a list of customers/service sites based on your search entry. Select the customer/service site from the search results list and choose Select. For more information, see the [F1 help](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form/field-definitions-sm-call-handler-form#ID-0004240d--en).

1. In the New Site field, do one of the following:

- If the call is for an existing service site, clear the New Site checkbox. Then use the Site ID field to enter the site ID or press F4 to select from a list of valid sites for the customer.Note: If you enter an inactive service site, the system displays a warning but allows you to save the call record. However, you must activate the service site (in SM Service Sites) before you can create a work order from the call record.

- If the call is for a new service site for the customer, leave the New Site checkbox selected. Use the Site ID field to enter a site ID or enter + to have the system assign an ID, and then enter a description of the new site in the text box to the right.

1. If the service call is for a new customer:

1. The New Customer checkbox defaults as selected; accept the default.

1. In the Customer field, enter a new customer number or enter N or + to have the system assign the customer number.

1. In the text field to the right of the Customer field, enter the customer's name.

1. In the Rate Template field, enter the rate template to use or press F4 to select from a list of valid rate templates.

1. The New Site checkbox defaults as selected; accept the default.

1. In the Site
 ID field, enter N or + to auto-generate a
 service site number or enter a unique service site code (alpha or
 numeric).

1. In the text field to the right of the Site ID field, enter the service site description.

1. If you entered a new site for the (new or existing) customer, use the Address fields to enter the customer's full address.

1. In the Center field, enter the service center that will handle the service call or accept the default service center (if applicable).

1. In the contact Name and Phone fields, enter the name and phone number of the person to contact about this service call or accept the default (if applicable).

1. In the Caller Name and Caller Phone fields, enter the name and phone number of the person placing the service call.

1. In the Details text box, enter details about the service call/problem.

1. Leave the Closed box unchecked until you are ready to close the call. Once you check this box, all fields are disabled.

1. Save the record.

1. [Create the work order](/en/vista/vista/service-management/call-handler--dispatch-board/enter-a-service-call/create-a-work-order-from-a-service-call).Note: You do not need to do this step to save the call record. You can add work order information and generate the work order at any time, as long as the service call record is open (that is, the Close checkbox is not selected).
