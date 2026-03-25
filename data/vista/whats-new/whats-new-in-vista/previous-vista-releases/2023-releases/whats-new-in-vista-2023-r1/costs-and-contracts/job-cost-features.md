---
title: "Job Cost Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-cost-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-cost-features"
---

# Job Cost Features

Vista 2023 R1 delivers on user-requested Job Cost enhancements, fixes, and other improvements.

## Added Support for Subcontract Workflow Process

In support of the Subcontract review and approval workflow added in this release, you now have the ability to assign Subcontract workflows to a Job Cost company or to specific jobs.
The following changes support this functionality:
JC Company ParametersYou can now assign Subcontract workflows to a company using the Workflow tab in JC Company Parameters. An SL - Subcontracts option was added to the Document Type drop-down. When selected, you must assign either a subcontract workflow (one with a Subcontract document type) or a generic workflow (one that is not associated with a document type). Subcontract workflows assigned to Job Cost companies override those defined in HQ Company Setup.
Each Job Cost company can have only one Subcontract workflow assigned. However, you can override the Subcontract workflow assigned to a Job Cost company by job in JC Jobs.
JC JobsYou can now assign Subcontract workflows to specific jobs using the Workflow tab in JC Jobs. An SL - Subcontracts option was added to the Document Type drop-down. When selected, you must assign either a subcontract workflow (one with a Subcontract document type) or a generic workflow (one that is not associated with a document type). Subcontract workflows assigned to jobs override those assigned to the associated Job Cost company or in HQ Company Setup.

Note: The Job Cost and Project Management company and job files share information. Therefore, workflows assigned in JC Company Parameters and JC Jobs automatically update the corresponding companies and projects in Project Management. Likewise, workflows assigned in PM Company Parameters and PM Projects automatically update the corresponding companies and jobs in Job Cost.

Process workflows are set up in the WF Workflow Process form. For more information about process workflows, see [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) and [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
 For more information about the Subcontract Review/Approval feature added in this release, see the [Workflow](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features) release notes.

## Recipient / Invoice Format Setup for JB Invoice Delivery

In support of the JB Invoice Delivery feature added in this release, you can now assign the recipients and invoice formats to use when delivering Job Billing invoices.
Set Up Contract Recipients for JB Invoice DeliveryA new JC Contract Recipients Detail form was added for setting up recipients for invoice delivery. You can access this form by selecting the Recipients button in the new JB Email Delivery section of the JC Contracts form (JB Info tab) or in JB Contract Info (Info tab).
 For each recipient you add, you specify the delivery method (print or email) and then the mailing address or email address (respectively) to use when delivering invoices.
When you create a billing (manually or by initialization), the recipients set up here default to the Recipients tab of the related billing form (JB Progress Billings or JB T&M Bill Edit). You can then modify, add, or delete recipients for each billing as needed. Modifications to the recipients list on a billing are not updated to JC Contract Recipients Detail.
For more information, see [Set Up Recipients for JB Invoice Delivery](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/set-up-recipients-for-jb-invoice-delivery).
Assign Progress and T&M Invoice Formats by ContractTwo new fields were added to the JB Email Delivery section in JC Contracts (JB Info tab) for designating the invoice formats to use when delivering Progress and T&M invoices:

- Progress Bills Invoice Format

- T&M Bills Invoice Format

You will only need to enter values in these fields for contracts that require a different invoice format than the one you have defined for the associated customer (in AR Customers) or the Job Billing company (in JB Company Parameters). When delivering invoices (in JB Invoice Delivery), the invoice formats defined for a contract override those defined for the customer and company (respectively).

For more information about the JB Invoice Delivery feature, see the [Job Billing](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-billing-features) release notes.

## Assign Project Structure Types to Jobs for Trimble Analytics Reporting

You now have the ability to set up project structure types and assign them to jobs so they can be used for reporting project data in Trimble Analytics.
Project structure types are used to identify and group project data (for example, estimates, actuals, change orders, etc.) in a more accurate and meaningful manner for Analytics reporting.
In conjunction with the addition of project structure types in the Headquarters module (new HQ Project Structure Types form), you now have the ability to assign these structure types to jobs.
 To implement this functionality, the following fields were added to the new Analytics section of the JC Jobs form:

- Structure Type - Use this field to assign a predefined or custom project structure type to each applicable job.

- Exclude from Analytics - Use this checkbox to exclude the selected job from project type Analytics. This is useful for dummy jobs set up for testing or any other job that should not be included in Analytics reporting.

For more information about assigning structure types to jobs, see the [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form).
For more information about the new HQ Project Structure Types form, see the [Headquarters](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/headquarters-features#concept-5952--en__ProjStructTypeHQ) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
