---
title: "Workflow Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features"
---

# Workflow Features

Vista 2023 R1 delivers on user-requested Workflow enhancements, fixes, and other improvements.

## New SL Review/Approval Workflows

You now have the ability to set up and implement process workflows for the review and approval of Subcontracts entered in the Project Management module.
Process workflows force documents that meet a defined criteria to follow a specific approval/review process. For example, if subcontracts that exceed $25,000 need to be reviewed before they are sent to accounting, setting up subcontract workflows enforce that review/approval process.
Changes implemented for the Subcontract Review/Approval Workflow feature include:
WF Workflow ProcessYou can now set up workflows for subcontract review/approval. A new SL - Subcontract option was added to the Document Type drop-down on the Info tab. Only processes with this document type (or a blank document type) can be selected when adding subcontract workflows via the Workflows tabs in the following locations:

- HQ Company Setup

- HQ Roles (Spending Limits tab)

- HQ User Spending Overrides

- JC Company Parameters

- JC Jobs

- PM Company Parameters

- PM Projects

For each subcontract workflow you create, you will use the Workflow Steps tab to define the review/approval steps, designate the roles and users that will be responsible for reviewing/approving subcontracts, and define the approval limits for each assigned role and/or user.
You can use the Assigned Companies tab to assign the workflow to specific module/company/document type combinations. However, you can only set up a module/company/document type combination once; it must be unique to all of the approval processes set up in WF Workflow Process form. For example, say you set up process workflow A and process workflow B, both for subcontracts. If you assign a JC/Company #1/SL-Subcontract combination to process workflow A, you cannot assign that same combination to process workflow B.
Assigned companies defined for a workflow are automatically updated to the company setup for their respective module. Using the JC/Co #1/SL-Subcontracts combination example above, once the record is saved, the system updates the workflow assignment to the Workflows tab in JC Company Parameters for Company 1.
WF Process CopyWhen copying workflows in WF Process Copy, you now have the ability to copy from or copy to a subcontract workflow. A new SL - Subcontracts option was added to the Document Type drop-down in the Copy To section of the form. You can select this option for the new process workflow regardless of the Document Type specified for the 'copy from' workflow. Once you successfully copy a workflow, you can make necessary edits to the workflow in WF Workflow Process. For more information, see [Copy an Existing Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/copy-an-existing-workflow-process).
The following modules were also updated for the SL Review/Approval Workflow feature. For more information about the changes made to these modules, see each module's release notes by clicking the links below.
[Headquarters](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/headquarters-features)
[Job Cost](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-cost-features)
[Project Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/project-management/project-management-features)
[Work Centers](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/work-center-features)

## New Notifier Queries for Workflow Notifications

If you are using the Review/Approval workflow process for purchase orders and subcontracts, you now have the ability to use predefined Notifier queries to send email notifications during the review/approval workflow process. When coupled with Notifier jobs, these queries allow you to schedule when notifications are sent to approvers and submitters and how often.
Two new Notifier queries were added for review notifications:

- PMDocumentApprovalList - Use this query for sending notifications to approvers when documents (purchase orders and subcontracts) are submitted for approval.

-  PMReviewedDocumentList - Use this query for sending notifications to submitters when documents are approved, rejected, or still awaiting review.

In order to use these queries, you must set up jobs in WF Notifier Job Manager and assign the new queries accordingly.
Once you complete this setup, the system uses the Notifier jobs you created to determine when and how often notifications are sent during the review/approval workflow process.
Additionally, you now have the ability to suppress the system notifications that are currently in use with the Process Workflow feature, so that reviewers and submitters only receive notifications via the Notifier jobs you create. This is done by selecting the new Using Review Workflow Notifier Queries checkbox added in PM Company Parameters. For more information, see the [Project Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/project-management/project-management-features#concept-8854--en__PMUseNotifierQueries) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
