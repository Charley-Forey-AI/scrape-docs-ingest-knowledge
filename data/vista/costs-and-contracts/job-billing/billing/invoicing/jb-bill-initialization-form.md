---
title: "JB Bill Initialization Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form"
---

# JB Bill Initialization Form

Use this form to generate Job Billing invoices based on completed progress and costs (progress billings) or cost data from the JC Cost Detail table (T&M billings).
You can access this form from the Programs menu of Job Billings or by selecting File > Initialize Billing from JB Progress Billing.
The Initialize Option allows you to specify what items to initialize. You can initialize only Progress or only T&M items, or you can initialize a combination of both. For a full description of these options, see the [Initialize Option](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form/field-definitions-jb-bill-initialization-form#ID-000149cd--en) F1 help.
Once you select the items to initialize, you can use the remaining selection criteria to filter the items to include, specify whether to create a separate invoice for each item bill group, specify the cost detail range and cutoff month, and specify whether to assign invoice numbers. If you select to assign invoice numbers, the system uses the Last Invoice # defined for the company in JB Company Parameters or AR Company Parameters (depending on the Last Invoice Option selected in JB Company Parameters) to assigns invoice numbers sequentially to each billing.
 In addition, if you are using the invoice review and approval workflow (that is, the Use Review and Approval Workflow checkbox is selected in JB Company Parameters), you can specify whether to auto-select the Ready for Review checkbox in JB Progress Billing and/or JB T&M Bill Edit for each billing creating during initialization. For information about the review and approval process for billings, see [About the Review and Approval Workflow for Job Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-review-and-approval-workflow-for-job-billings).
Once you have entered the appropriate criteria, click the Initialize Bill button to begin the initialization process. The system generates billings based on the selection criteria and adds them to the related billing form (JB Progress Billings or JB T&M Bill Edit).
 If you are using the Invoice Delivery feature and have set up recipients for the selected contract(s) in [JC Contract Recipients Detail](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-contract-recipients-detail-form), the initialization process automatically adds the recipients to the Recipients tab in JB Progress Billings or JB T&M Bill Edit. You can then modify, add, or delete recipients as needed for each billing.

## Billable Amount Calculations

During initialization, the system calculates billable amounts in the same manner used for the JB Contract Progress Worksheet report. The worksheet may show suggested billing amounts based on both units and dollars.
Calculation is as follows:

- If the contract item's unit of measure is LS (lump sum), the system calculates the current billing based on a percent complete of actual costs to current estimated or projected costs. The dollars included are for all phase/cost types assigned to the contract item with the Bill Flag set to 'Y-Units and Dollars' or 'C-Only Dollars' (in JC Job Phases).

- If the contract item's unit of measure is anything other than LS, the system calculates the current billing based on a percent complete of actual units to current estimated or projected units. The units included in the calculation are for all phase/cost types pointed to the contract item with the Bill Flag set to 'Y-Units'.

Multiple billings are allowed during a month. Although the progress worksheet will show previous amounts as the values for the previous month, initialization will include any prior billings for the month in the Previous Units and Previous Amount fields.

Click the links below for more information about initializing billings.
[About Initializing Progress Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-progress-billings)
[About Initializing T&M Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/about-initializing-tm-billings)
