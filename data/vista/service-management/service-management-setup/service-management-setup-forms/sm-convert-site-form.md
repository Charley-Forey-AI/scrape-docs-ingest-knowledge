---
title: "SM Convert Site Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-convert-site-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-convert-site-form"
---

# SM Convert Site Form

Use the SM Convert Site form to convert a job service site to
 a customer service site.
Access this form via the SM Service Sites form by selecting Tasks > Convert to Customer Site.
Upon access to this form, the system automatically
 defaults the customer assigned to the job's contract in JC
 Contracts. However, you can override the default with any valid
 customer (SM or AR). If you enter a customer that exists in AR
 Customers, but is not set up as an SM customer (in SM
 Customers), the system will automatically add the customer to SM
 Customers.
Note: If a customer does not exist in SM Customers or AR Customers, you
 must set them up before you can reference them on a service site here.
Once you specify the customer and select Convert, the system convert the job site to a customer site, displays a
 message indicating the conversion was successful, and then returns you to the SM Service
 Sites form. During conversion, the system changes the site Type to
 C-Customer, enables all customer-specific fields (Customer, Rate Template, Customer PO
 Override, Custom Invoice Report, Invoice Grouping, and Alternate Bill To), and hides all
 job-specific fields (Job and Costing Method).
Note: Although job-specific fields are hidden, the system
 retains the information so it is available should you wish to convert the service site
 back to a job site (by selecting Revert to Job Site from the Tasks
 drop-down in SM Service Sites).

Related information

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)
