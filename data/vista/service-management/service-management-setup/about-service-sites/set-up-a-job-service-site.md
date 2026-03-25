---
title: "Set Up a Job Service Site | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-job-service-site"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-job-service-site"
---

# Set Up a Job Service Site

Job sites containing equipment or other items that will be
 serviced by your company will need to be set up as service sites in
 SM Service Sites.
Before you set up a job service site, the job must
 first be set up in JC Jobs.Note: You can set up service
 sites for jobs from any Job Cost company; however, intercompany accounts must exist for the
 SM and JC companies in [GL Intercompany Accounts ](/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-intercompany-accounts-form). This will ensure costs incurred on
 a work order are updated to the correct JC company.
To set up a job service site:

1. In the Service Site field, enter a name or code to represent the service site.

1. From the Type drop-down, select J-Job.

1. In the JC Co field, enter the Job Cost company for the job associated with this service site.

1. Select the Non-Billable checkbox to default work orders for this service site as Non-Billable. For information about defaulting for this field, as well as when this field is enabled/disabled, see the [F1 help](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form#ID-0004401c--en).  Leave this box unchecked to default work orders for this service site as Time and Material.

1. In the Job field, enter the JC job to which this site is associated. Press F4 for a list of valid jobs for the specified JC company.

1. From the Costing Method drop-down, select Actual Cost or Markup to identify how the system should send costs to Job Cost for work completed on a job work order. For more information, see the [F1 help](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form#ID-00044039--en).

1. In the Site Description field, enter a description of the service site.

1. Use the address
 fields to enter an address for this service site
 or accept the default address (from JC Jobs).


1. In the Phone field, enter the phone number of the service site.

1. In the Billing Email field, enter the billing email address for this service site.

1. In the Default Service Center field, enter the default service center for this service site. This service center will default when entering work orders for job/service site (in SM Work Orders).

1. In the Default Contact field, enter the default contact for this service site or press F4 to select from a list of valid customer or HQ contacts. This contact will default when entering work orders for this job/service site. Note: The default contact might typically be a project manager for the job (as defined in JC Project Managers); however, you can also specify any contact set up in HQ Contacts.

1. In the Rate Template field, enter the rate template to use for this service site or press F4 to select from a list of valid rate templates.Note: Rate templates are used to determine labor, equipment, and material rates for a work order. However, job work orders created for this service site will only use this rate template if the Costing Method selected for the work order is Markup.

1. In the Tax Code field, for customer sites, enter the default tax code to use for calculating taxes when entering work orders for this service site. You may leave the tax code blank if taxes will not be applied to work orders for this service site or if you want tax codes to be entered manually at the time of work order entry.

1. In the Primary Technician field, enter the primary technician for the service site. This will generally be the technician preferred by the service site or the technician most qualified to handle service calls for the service site.

1. Select the Active checkbox to activate the service site. Note: Inactive service sites do not display in F4 lookups, nor can they be referenced when setting up a work order (in SM Work Orders).

1. Save the record. Once you have set up a job service site, you can set up override rates, standard charges, technician preferences, and contacts as needed. For more information, click on the links below.
[Set Up Rate Overrides by Customer, Service Site, or Quote](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-rate-overrides-by-customer-service-site-or-quote)
[Set Up Standard Charges for a Customer or Service Site](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-standard-charges-for-a-customer-or-service-site)
[Set Up Technician Preferences](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-technician-preferences)
[Set Up Serviceable Items](/en/vista/vista/service-management/service-management-setup/set-up-serviceable-items)
[Assign Contacts to a Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/assign-contacts-to-a-service-site)

Related information

- [Set Up a Customer Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)
