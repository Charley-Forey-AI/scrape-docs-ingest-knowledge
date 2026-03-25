---
title: "About the Review and Approval Workflow for Job Billings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-review-and-approval-workflow-for-job-billings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-the-review-and-approval-workflow-for-job-billings"
---

# About the Review and Approval Workflow for Job Billings

If your company requires approval of Job Billing invoices before they are sent to Accounts Receivable for payment, you can use the Review and Approval Workflow feature in Job Billing to track the review and approval process for progress and T&M billings.
The Review and Approval Workflow feature allows you to flag a bill (invoice) as "ready to review" and then track it through the review and approval process. In addition, you can set a review level to control the minimum level required before you can interface a billing to Accounts Receivable for payment. For example, if you do not want invoices sent to Accounts Receivable until they are approved for billing, you can set the review level to 4 - Approve for Billing to prevent invoices from being interfaced until the billing is flagged as "approved for billing".
Note:Viewpoint's web-based Financial Controls application includes integration with this feature to allow a more collaborative review and approval process. For more information, see [Job Billing](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FC_000013:FC:FC).

In order to use the Review and Approval process, you must:

- Set up at least one reviewer group in the HQ Reviewer Groups form with a Reviewer Group Type of 3-Job Billing. For more information, see [Create Reviewer Groups for Job Billing Invoices](/en/vista/vista/administration/headquarters/reviewer-setup/create-reviewer-groups-for-job-billing-invoices).

- Enable the Review and Approval process by selecting the Use Review and Approval Workflow checkbox in the JB Company Parameters form.

- Set the default minimum review level for interfacing billings using the Review Level drop-down in the JB Company Parameters form. See the [Review Level](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form#concept-54150001--en) F1 help for a description of each review level available.

- Assign the Job Billing reviewer group(s) you set up in the HQ Reviewer Groups form to each applicable contract in the JB Contract Info form. Each time you create a billing, the billing automatically defaults the reviewer group associated with the contract. You can override the default for a billing as needed.

Once you are set up to use this feature, you can then track the review/approval process for each billing. A typical workflow might be as follows:

- Create the billing either by initialization (in JB Bill Initialize) or manual entry in the applicable form (JB Progress Billing or JB T&M Edit Bill).

-  For each bill, use the Bill Status Tracking section on the applicable form (JB Progress Billings or JB T&M Bill Edit) to initiate and track the review process.

- When the bill is ready to review, select the Ready for Review checkbox.

- Once all reviewers approve the bill, select the Draft Approved checkbox.

- Send the draft billing to the customer and select the Sent to Customers checkbox.

- Once the customer approves the bill, select the Approved for Billing checkbox.

- Interface the bill to Accounts Receivable (via the JB Interface form).

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

- [JB Contract Info Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-contract-info-form)

- [JB Bill Initialization Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-bill-initialization-form)

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)

- [JB Progress Billing Form](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/jb-progress-billing-form)

- [JB Interface Form](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-interface-form)
