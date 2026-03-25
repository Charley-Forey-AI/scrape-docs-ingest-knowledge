---
title: "About Pricing Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/company/about-pricing-options"
---

#  About Pricing Options

Specify how materials are priced.
 Use the Pricing Options section on the [IN Company Parameters](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form to specify how materials are priced when they are sold to customers (in the Material Sales form), jobs, inventory (in Material Sales or the Usage Option section of this form), equipment, or service work orders (in the SM Work Orders form). In each case, there are four choices available:

- Average Cost Plus Markup – The unit price is calculated by using your average cost plus a specified markup rate.

- Last Cost Plus Markup – The unit price is calculated using your last cost plus a specified markup rate.

- Standard Cost Plus Markup – The unit price is calculated using the standard unit cost plus a specified markup rate.

- Standard Price Less Discount – The unit price is determined by the standard unit price, less a specified discount.

 Average Cost and Last Cost are pulled from IN Location Materials and are updated whenever a material is posted in AP Transaction Entry, PO Receipt Entry, or transferred to this location (IN Location Transfers). Standard Cost and Standard Price are also pulled from IN Location Materials, but are updated manually.
Note: Work completed Inventory lines entered for a service work order do not allow updates to the Cost Rate (unit cost); therefore, no updates will occur to the Average Unit Cost or Last Unit Cost for the location/material here.
The markup/discount rates used (in conjunction with the specified pricing option) when selling materials are defined by location in the Markup/Discount Rates section of IN Location Materials as follows:

- Customer – This rate is used for materials sold to customers from MS. Rates can be overridden by customer in AR Customers.

- Job – This rate is used for materials
 sold to jobs in JC. Rates may be overridden by job in JC Jobs.

- Inventory – This rate is used for materials sold to other Inventory locations in IN.

- Equipment – This rate is used for materials sold to equipment in EM. Rates may be overridden by equipment in EM Equipment.

- Service - This rate is used for materials used on a service work order (in SM Work Orders).
