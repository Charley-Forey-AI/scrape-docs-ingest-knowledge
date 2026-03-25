---
title: "Set Up a Customer Service Site | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site"
---

# Set Up a Customer Service Site

You must set up service sites for each customer location that has equipment or other items that your company will service.
You must [set up the
 customer](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer) in SM Customers before you set up service sites for the customer
 here.
In addition to static information about each site, there are several options that provide default settings for work orders and work completed transactions, as well as determine how invoices are generated and what rates to use when capturing labor, materials, equipment, and miscellaneous costs on a work order.

1. In the Service Site field, enter a name or code to represent the service site.

1. From the Type drop-down, select C-Customer (default).

1. In the Customer field, enter the customer to which this site is associated or press F4 to select from a list of valid SM customers.

1. In the Site Description field, enter a description of the service site.

1. Use the address fields (Address, City, State, Zip, and Country) to enter an address for this service site or accept the default address (from AR Customers).

1. In the Phone field, enter the service site phone number.

1. In the Billing Email field, enter the billing email address for this service site. If you have specified to deliver invoices to service sites (in SM Customers), this is the email address that will be used for invoice delivery. (May be overridden on the Recipients tab of SM Invoice Review.) Note: You can enter multiple email addresses if applicable; however, you must separate them with a semi-colon (for example, jane.doe@email.com; johnd@email.com; joe.smith@email.com). The system will send an email to each address specified here.

1. In the Default Service Center field, enter the default service center for this service site. This service center will default when entering work orders for this customer/service site.

1. In the Default Contact field, enter the default contact for this service site or press F4 to select from a list of valid customer or HQ contacts. This contact will default when entering work orders for this customer/service site.

1. In the Rate Template field, enter the rate template to use for this service site or press F4 to select from a list of valid rate templates. You will only need to enter a template here if you are overriding the rate template assigned at the customer level.

1. In the Tax Code field, enter the default tax code to use for calculating taxes for work completed.Leave the tax code blank if taxes will not be applied to work orders for this service site or if you want tax codes to be entered manually at the time of work order entry.
Note: The tax code entered here will only be used as the default if the Tax Source is set to Service Site for the work order scope.

1. Select the Use Tax Code checkbox, and enter the tax code to use for Use tax. Press F4 to select from a list of valid tax codes.If you do not pay Use tax or if you use the same tax code for Sales and Use tax, leave this checkbox unselected and the field blank.

1. In the Primary Technician field, enter the primary technician for the service site.

1. In the Reviewer field, enter a reviewer’s ID in this field to enable that user to mark work orders as ready to bill. Press F4 for a list of active reviewers. Press F5 to access HQ Reviewers.

1. In the Customer PO Override field, select R-Required or N-Not Required to indicate if customer POs are required when entering work orders (in SM Work Orders) for this service site.Leave blank to use the Customer PO Setting defined for the customer (in SM Customers).

1. In the Custom Invoice Report field, enter the custom report to use for printing work order invoices for this service site.Leave blank if using the custom report specified for the customer in SM Customers.

1. From the Invoice Grouping drop-down, select S-One per service site, W-One per work order, or P-One per work order scope to indicate how the system should generate invoices for work orders posted to this service site. Leave blank to use the invoicing grouping option defined for the customer in SM Customers.For information about how this option works, see [Invoice Grouping](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping).

1. From the PO Override drop-down, select Yes or No to indicate whether to group work order scopes with the same Customer PO number on the same invoice. Leave blank to use the PO Override setting defined for the Customer in SM Customers.For more information, see the [PO Override](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form#ID-00044100--en) F1 help.

1. Select the Alternate Bill To checkbox if you will bill work orders associated with this service site to a different customer than the customer associated with this service site. Then use the field to the right of this checkbox to specify the bill to customer for this service site.

1. In the PR Local Code field, enter the default local code to use for work orders associated with this service site.

1. In the Insurance Code field, enter the default insurance code for work orders associated with this service site or press F4 to select from a list of valid insurance codes.

1. In the Craft Template field, enter the default craft template for work orders associated with this service site. Press F4 to select from a list of valid craft templates.

1. Select the Certified Payroll checkbox to default the Certified Payroll checkbox in SM Work Orders as selected on all work orders created for this service site.

1. Select the Non-Billable checkbox to default work orders for this service site as Non-Billable. For information about defaulting for this field, as well as when this field is enabled/disabled, see the [F1 help](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form#ID-0004401c--en).  Leave this box unchecked to default work orders for this service site as Time and Material.

1. Select the Active checkbox to activate the service site.

1. Save the record. Once you have set up a customer service site, you can set up override rates, standard charges, technician preferences, service sites, and contacts as needed. For more information, click on the links below.
[Set Up Rate Overrides by Customer, Service Site, or Quote](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote)
[Set Up Standard Charges for a Customer or Service Site](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-standard-charges-for-a-customer-or-service-site)
[Set Up Technician Preferences](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-technician-preferences)
[Set Up Serviceable Items](/en/vista/vista/service-management/service-management-setup/set-up-serviceable-items)
[Assign Contacts to a Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/assign-contacts-to-a-service-site)

Related information

- [Set Up a Job Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-job-service-site)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)
