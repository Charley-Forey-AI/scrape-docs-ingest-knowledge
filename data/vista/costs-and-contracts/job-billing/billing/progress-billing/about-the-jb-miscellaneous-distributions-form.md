---
title: "About the JB Miscellaneous Distributions Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-jb-miscellaneous-distributions-form"
---

# About the JB Miscellaneous Distributions Form

This form can only be accessed by double-clicking a record on the Misc Distributions tabs in JB Progress Billing or JB T&M Bill Edit and is used to distribute any amount of a billing that requires separate accounting by your company.
 Any type of distribution that you want to track can be entered using distribution codes that were set up in AR Misc Distribution Codes.
For example, miscellaneous distributions can be used to track city business tax. In most cases city business taxes are paid annually or semi-annually. By distributing billed amounts subject to city business tax, you can keep a record of your taxable amounts and create a report that gives you an accounting of taxable amounts. When you are ready to pay business taxes, run the report to generate the accumulated taxable amounts for each city to which you owe a business tax and calculate the amounts due.
When a billing is created (either through initialization or manually), indicate which miscellaneous distribution code applies to that billing, and specify the amount to which the distribution will be applied. If using miscellaneous distributions with Progress billings, you must manually assign miscellaneous distribution codes to the designated portion of the invoice balance. If using with T & M billings, distributions can be set up as sequences on a template (Miscellaneous type). During initialization, an entry is generated for each miscellaneous distribution code, with the total billed amount distributed to the first code. Remaining distribution codes will default as 0.00. Access this form to edit distributions as necessary. For more information, see JB T&M Template Setup in Related Topics below.
Distributed amounts do not appear on the invoice, nor do they affect the invoice amount. They are not interfaced to JC or GL; however, they are interfaced to AR and will update the AR Miscellaneous Distributions table (ARMD). The distribution codes can then be used in conjunction with Crystal Reports to create reports that can generate the needed information and totals for each type of distribution you use.
The following are related topics:

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

- [JB T&M Template Setup Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)

- [About the AR Misc Distribution Codes Form](/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-misc-distribution-codes-form)
