---
title: "Enter an SM Work Order Quote | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote"
---

# Enter an SM Work Order Quote

You can set up work order quotes for services you will perform on customer work orders.
Quotes define the scope of work requested by the customer, along with the estimated costs to perform the work. When you enter a quote, you can set up tasks to represent the different scopes of work, as well as define the material, labor, equipment, and miscellaneous requirements, along with their cost estimates. If you prefer a summarized level of cost estimates, you can enter them using the SM WO Quote Cost Detail form.

1. Open the SM Work Order Quotes form.

1.  In the Quote ID field, enter a quote ID or enter N, New, or + to have the system automatically assign the next sequential quote number.

1. Enter a description of the quote in the Description field.

1. If the work order is for an existing customer and you want to use an existing work order, use the Work Order field to enter the work order number or press F4 to select from a list of valid work orders. The system automatically populates the customer ID, name, and address fields from AR Customers, and disables those fields. To create a new work order during the approval process (new or existing customers), leave the Work Order field blank.

1. If you left the Work Order field blank:OptionDescription
 and the quote is for an existing customer

1. Deselect the New Customer checkbox

1. In the Customer ID field, enter the the customer number or press F4 to select from a list of valid SM customers. The customer's name and address information populates from AR Customers and cannot be changed.

and the quote is for a new customer

1. Leave the New Customer checkbox selected.

1. In the Customer ID field, enter N or + to have the system auto-assign the number for you. You can also manually enter a customer number, as long as the number is not already in use in AR Customers or SM Customers.

1. In the Customer Name field, enter the customer's name.

1. Use the address fields to enter the customer's address information.

1. Specify the service site for the work order quote as follows:OptionDescription
If the quote is for an existing service site (existing customers only)

1. Deselect the New Site checkbox.

1. In the Site ID field enter the service site ID or press F4 to select from a list of valid service sites for the customer. The system populates the site address information from SM Service Sites.

If the quote is for a new service site (existing or new customers)

1. Select the New Site checkbox (if not already selected).

1. In the Site ID field, enter N or + to have the system auto-assign the number for you. You can also manually enter a service site ID, as long as it is not already in use in SM Service Sites.

1. Use the address fields to enter the service site's address information.
If the site address is the same as the customer address, you can click Copy in the Customer section to auto-populate the site address from the customer address.

1. In the Customer Contact section, enter the name and phone number of the contact for the specified customer in the Name and Phone fields.

1. In the Center field, enter the service center performing the quoted work.

1. In the Requested By section, enter the name and phone number of the person who requested the service work in the Name and Phone fields.

1. In the Date field, enter the date this work order quote was requested.

1. In the Sales Rep field, enter the sales representative for this work order quote. Press F4 for a list of valid employees for the SM company.

1. [Enter scopes for the work order quote.](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote/enter-scopes-for-a-work-order-quote)

To auto-add a new customer and/or service site from a quote to AR Customers,SM Customers, and/or SM Service Sites, respectively, you must click the Create Customer / Site button at the bottom of the SM Work Order Quotes form. The system sets up the customer and/or site with the ID, name or description, and address information, along with any user-defined field values from the quote that exist on the destination form(s).
