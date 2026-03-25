---
title: "Customer Sites vs. Job Sites | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/customer-sites-vs.-job-sites"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/customer-sites-vs.-job-sites"
---

# Customer Sites vs. Job Sites

You can set up both customer sites and job sites for a Service Management customer.
 When you set up a service site in SM Service Sites, the Type field allows you to specify whether you are setting up a customer service site or a job service site. Most of the information entered for a service site applies to both customer and job service sites; however, there are fields that are specific to the service site type.
 For example, customer-specified fields include (but are not limited to) Customer, Custom Invoice Report, Invoice Grouping, and payroll-related fields such as Local Code, Insurance Code, and Craft Template. Job-specific fields include JC Co, Job, and Costing Method.

## Invoices

The Invoices tab in SM Service Sites applies to customer service sites only, and allows you to review the invoice history for the selected service site. Invoices are generated in SM Work Orders or SM Work Order Billing, and are based on work completed equipment, labor, miscellaneous, inventory, and purchase lines on a work order. For each invoice, you can track its status, the date it was created, and the invoice amounts.
 Work orders associated with a job are billed in Job Billing (via Job Cost) or directly in Accounts Receivable (if not using Job Billing).

## Agreements

The Agreements tab in SM Service Sites applies to customer service sites only, and displays all agreements that are associated with the selected service site. Although agreements are set up by customer, they are associated to service sites via the services that are defined for the agreement; only those agreements with services referencing the selected service site will display here.Note: You cannot add agreements using this grid; however, you can access the agreement by double-clicking the related grid record. For more information about agreements and services, see [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form) and [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form).

## Closed Jobs

All job sites must be assigned a JC company and job. You can close the contract and job associated with a job service site; however, once closed, the ability to enter work orders and/or work completed for the service site is determined by the Allow Posting to Hard-Closed Jobs and Allow Posting to Soft-Closed Jobs checkboxes in JC Company Parameters (for the JC company associated with the service site).

- If you allow posting to closed jobs (both checkboxes are selected), the system allows entry of work orders and work completed for the service site, and updates the costs to Job Cost.

- If you do not allow posting to closed jobs (neither of the checkboxes is selected), the system does not allow entry of work orders or work completed for the service site.

If you close a job after you have already entered work orders for the service site, existing work completed entries are not affected; however, no new entries are allowed, nor will costs be updated to Job Cost.
If work completed labor or work completed purchase entries exist, but you have not posted actual costs to Job Cost (by running PR Ledger Update or AP Transaction Entry), you will be unable to close the job until you have correctly processed the entries.

Related information

- [Set Up a Customer Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site)

- [Set Up a Job Service Site](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-job-service-site)
