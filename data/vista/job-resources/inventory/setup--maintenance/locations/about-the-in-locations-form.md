---
title: "About the IN Locations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form"
---

# About the IN Locations Form

Use this form to create and maintain the locations where stocked materials are stored - for example warehouses, job sites, batch plants, and quarries.
You must set up at least one location per Inventory company.
The Info and Add'l Info tabs contain static information about the location, such as the invoice reviewer (for AP unapproved invoices), purchase reviewer (for requisitions), mailing and shipping addresses, weight option for tickets entered in Material Sales, override cost method, tax code, and so forth. The system uses many of these field values as default values as you work in the module.
Once you have set up a location, you can initialize materials to the current location (from HQ Materials) by selecting File > Initialize Materials.

## Accounts Tabs

These tabs are used to specify the various GL accounts used when processing inventory transactions. If needed, you can override the accounts defined here by company, category, and/or company/category. Use the IN Location Category Override, IN Location Company Override, or the IN Location Co/Cat Override related grid tabs to override settings. Double-click on a record in these tabs to access the related form

- Inventory Accounts - This tab is used to set up the primary accounts for each location. With the exception of the Inventory, Adjustments, and Cost Of Goods accounts, which are required, the remaining accounts defined on this tab are dependent on specific factors. For instance, the Cost Variance account is only needed if using the Standard Cost Valuation Method (IN Company Parameters), and the Misc and Tax Expense accounts are needed to override the default accounts specified in IN Company Parameters.

- Sales Accounts - This tab is used to set up the GL Revenue and Quantity GL accounts, as well as the AR Discount account. The Revenue accounts are used for tracking total revenue dollars for materials sold to customers, jobs, other Inventory locations, and equipment. The Quantity accounts are used to track units sold. The AR Discount account will be used for discounts taken when entering cash receipts against MS invoices where an Inventory location is specified. If no location is specified on the MS invoice, or a location is specified but no AR Discount account has been defined for the location, the Discount account assigned to the invoice's receivable type will be used.

- Other Revenue - This tab is used to define the GL accounts for haul and surcharge revenue. Haul and surcharge revenue (what you charge the customer for delivery) may be classified based on whether delivery was made using your own equipment or using an outside haul vendor.

- Expense - This tab is used to define the GL accounts for haul, material, and surcharge expense. Haul expense (what you pay for delivery) may be classified based on whether delivery was made using your own equipment or using an outside haul vendor.

## Roles Tab

This tab only applies if you have the Workflow module and use the [Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow) feature. Use this tab to assign a user to a specific role.
The following rules apply when adding roles/users:

- Users can only be associated with a role that they have been set up with using the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) tab.

- Users can be assigned to more than one role - for example a single user can have multiple roles.

- Roles can be used more than once.

## Workflow Tab

If you have the Workflow module, you can use the Workflow tab to set up workflows for an inventory location. The workflow processes added here override those set up on the Workflow tab of the IN Company Parameters form and HQ Company Setup forms. For example, any process set up on a specific location overrides the more generic processes set up at the module and application level. For more information, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

Related information

- [Plant Costing Links](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/plant-costing-links)

- [About the IN Location Company Override Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-company-override-form)

- [About the IN Location Category Override Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-category-override-form)

- [About the IN Location Co & Category Override Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-co--category-override-form)

- [Material Units](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-units)
