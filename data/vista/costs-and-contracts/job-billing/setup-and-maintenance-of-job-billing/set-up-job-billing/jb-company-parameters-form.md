---
title: "JB Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form"
---

# JB Company Parameters Form

Use this form to set up various control options for job billing processing in a company.
 You must define these options before processing can begin in Job Billing. Each company number in which Job Billing processing occurs must be set up here.
It is important that you take time to understand the effects of all of the choices for each setup option. The selected options affect how forms work and how other modules such as Job Cost and Accounts Receivable interact with Job Billing. It is suggested that this form be restricted so that only the System Administrator has access.
Once defined, changes are usually rare to settings in the form. Because
 changing an option may affect processing or stored information, you
 should make changes carefully. If you want to change an option but are
 unsure of its effect on existing data in the system, contact Viewpoint
 Support. For more information, see [JB Company Control Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-control-options).

## Invoice Delivery Setup

If you will be using the invoice delivery feature for Progress and T&M billings, you will need to specify the format to use for Progress and T&M invoices, as well as define the email settings for invoices delivered via email.
The Progress Bills Invoice Format and T&M Bills Invoice Format fields (on the JB Info tab) are used to specify which invoice formats to use for invoice delivery. You can override these invoice formats at the customer level (in AR Customers) and/or contract level (in JC Contracts) if the customer or contract requires a different invoice format than the ones specified at the company level.
Note: There are multiple standard invoice reports available for both progress and T&M invoices, so if you leave these fields blank at the company, customer, and contract levels, there is no way for the system to know which invoice to use. Therefore, you will be unable to use the invoice delivery feature and instead, will need to manually print and email Job Billing invoices

The Email Settings tab is used to define the email parameters for delivering invoices to recipients via email (that is, the from address, subject line, and email body). Text formatting options, such as font type, size, and color, as well as justification and bullets/numbering, allow you to tailor the email body to meet your needs.
 For more information about setting these options, see [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options).
Additional setup options will need to be completed at the contract level in JC Contracts (on the JB Info tab). For more information, see [Set Up Recipients for JB Invoice Delivery](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/set-up-recipients-for-jb-invoice-delivery).
