---
title: "SM Call Handler Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form"
---

# SM Call Handler Form

Use the SM Call Handler form to capture and track service calls.
When you receive a service call, you can capture basic information, such as the caller's name, phone number, and company, as well as a brief summary of the problem. If the call is for an existing customer, the Search and F4 functionalities allow you to easily find and select the customer and service site. If the call is for a new customer, you can enter a customer name and site description and have the system auto-generate customer and service site numbers for you. When you create a work order from the service call, the system automatically sets up the new customer in AR Customers and SM Customers, and sets up the new site (with minimal information) in SM Service Sites.
After you enter the appropriate information, you can generate a work order right from the service call by selecting Create Work Order. Once you create the work order, the system closes the call and disables all fields except the Closed checkbox and the Notes tab. You can modify the caller name, caller phone, and details if needed by selecting the Closed checkbox; however, all other fields will remain disabled.

## Activity History

When you receive a service call for an existing customer, you can view the customer's activity history to identify existing work orders, invoices, scheduled maintenance (if using the Agreements feature), quotes, serviceable items, and call history by selecting the corresponding tab. You can use this information, for example, to determine if there is already an open call and/or work order for the customer/service site related to the current call.Note: On any of the history tabs, double-clicking on a record in the grid opens the corresponding record in the applicable form (for example, double-clicking an invoice on the Invoices tab opens that invoice in SM Invoice Review (if a work order invoice) or SM Agreement Invoice Review (if an agreement invoice).

## Customer / Site Alerts

The Alerts field (just below the Call ID) displays alert messages specific to the selected customer and service site when applicable. These alerts are as follows:

- Under Contract - Displays when the customer has active Agreement.

- Maintenance Due - Displays when the customer/service site has agreement work orders that are not closed.

- Maintenance Scheduled - Displays when the customer/service site has agreement services scheduled in the next 7 days.

- Credit Hold - Displays when the "bill to" customer has a status of On Hold (in AR Customers).

- Customer Notes - Displays when notes exist for the customer in SM Customers. Hovering over the alert displays notes entered for the customer (in SM Customers) in a pop-up window. For extensive notes, selecting the alert displays the Customer Notes window so that you can see the notes in their entirety.

- Site Notes - Displays when notes exist for the service site in SM Service Sites. Hovering over the alert displays notes entered for the service site (in SM Service Sites) in a pop-up window. For extensive notes, selecting the alert displays the Site Notes window so that you can see the notes in their entirety.

- Past Due - Displays when the customer has past due balances. If you hover over the Past Due alert, the system displays the invoice aging history. Amounts are shown in the standard aging buckets: Total, Current, 31-60, 61-90, and Over 90. If an alternate Bill To customer is associated with the customer (in SM Customers), the grid shows the aging history for the alternate customer as well.

If you enter a call for a new customer and service site, you must create a work order to add the customer to AR and SM. Once the customer exists in AR and SM, then system can then apply alerts when applicable.

Select the following links for more information.
[Entering a Service Call](/en/vista/vista/service-management/call-handler--dispatch-board/enter-a-service-call)
[Create the Work Order](/en/vista/vista/service-management/call-handler--dispatch-board/enter-a-service-call)
