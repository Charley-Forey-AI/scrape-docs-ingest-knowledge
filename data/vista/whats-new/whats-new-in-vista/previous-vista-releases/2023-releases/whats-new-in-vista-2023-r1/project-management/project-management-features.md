---
title: "Project Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/project-management/project-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/project-management/project-management-features"
---

# Project Management Features

Vista 2023 R1 delivers on user-requested Project Management enhancements, fixes, and other improvements.

## Added Support for Subcontract Workflow Process

In support of the Subcontract review and approval workflow added in this release, you now have the ability to assign Subcontract workflows to a PM company or to specific projects, submit eligible subcontracts for review/approval, and review/approve subcontracts in Work Centers.
The following changes support this functionality:
PM Company ParametersYou can now assign Subcontract workflows to a PM company using the Workflow tab in PM Company Parameters. An SL - Subcontracts option was added to the Document Type drop-down. When selected, you must assign either a subcontract workflow (one with a Subcontract document type) or a generic workflow (one that is not associated with a document type). Subcontract workflows assigned to PM companies override those defined in HQ Company Setup.
PM ProjectsYou can now assign Subcontract workflows to specific projects using the Workflow tab in PM Projects. An SL - Subcontracts option was added to the Document Type drop-down. When selected, you must assign either a subcontract workflow (one with a Subcontract document type) or a generic workflow (one that is not associated with a document type). Subcontract workflows assigned to projects override those assigned to the associated PM company or in HQ Company Setup.
PM SubcontractsYou can now submit eligible subcontracts for review/approval using the Process Workflow feature.The following changes were made to the PM Subcontracts form:

- Added a Workflow button and Workflow Status field to the bottom left corner of the screen. When you add a subcontract that the system determines requires approval, the Workflow Status field changes to Approval Required. If you select the Workflow button at this stage, the Pending Reviewers form opens, listing all reviewers assigned to review/approve the subcontract. Reviewers are assigned based on the roles/users designated for the process workflow in WF Workflow Process.If you select the Workflow button after you submit a subcontract for review/approval, the PM SL Work Flow Item Reviewers form displays, showing the approval steps, approvers, and approval limits, as well as any comments and notes.

- Added a Submit for Approval button to the lower right corner of the form. This button is enabled only when a subcontract requires approval; that is the Workflow Status field changes to Approval Required. Once you select this button, the subcontract is submitted for review/approval and all assigned reviewers are notified via email or VP message (depending on the notification designation for each reviewer in the Notify field of VA User Profile). For more information about submitting subcontracts for review, see [Initiate the Review/Approval Workflow for Subcontracts](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/initiate-the-reviewapproval-workflow-for-subcontracts). Reviewers must review and approve/reject all subcontracts assigned to them using the PM Work Center. For more information, see [Review Subcontracts Submitted for Approval](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/review-subcontracts-submitted-for-approval).

- Added a Workflow History tab, which shows the subcontract approval workflow history. Information includes when the subcontract was submitted for approval, when it was approved or rejected, and who the reviewer

Pending Reviewers / PM SL Work Flow Item Reviewers

- Pending Reviewer - This form is now available in PM Subcontracts and shows a list of reviewers assigned to subcontracts requiring the review/approval process. You can only access this form by selecting the Workflow button in PM Subcontracts after the system determines a subcontract requires approval (that is, the Workflow Status is set to Approval Required). This form is display only and shows all reviewers assigned to review the subcontract based on the roles/users defined for the associated subcontract process workflow.

- PM SL Work Flow Item Reviewers - This new form shows the approval process for subcontracts submitted for review/approval. You can only access this form by selecting the Workflow button in PM Subcontracts after a subcontract is submitted for review/approval (using the Submit for Approval button). This form is display only, with the exception of the Notes field, and shows the steps associated with the subcontract process workflow, along with the assigned approver, the approval status, and any comments or notes. The Notes fields is enabled to allow anyone to enter notes for an approval step. You can access this form to see the workflow history until the subcontract has been approved and interfaced (indicated by a Workflow Status of Processed).

Note: The Project Management and Job Cost company and job files share information. Therefore, workflows assigned in PM Company Parameters and PM Projects automatically update the corresponding companies and jobs in Job Cost. Likewise, workflows assigned in JC Company Parameters and JC Jobs automatically update the corresponding companies and projects in Project Management.

Process workflows are set up in the WF Workflow Process form. For more information about process workflows, see [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) and [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
 For more information about the Subcontract Review/Approval feature added in this release, see the [Workflow](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features) release notes.

## Ability to Use Notifier Queries for Workflow Review Process

If you are using the Review/Approval workflow process for purchase orders and subcontracts, you now have the ability to use predefined Notifier queries to send email notifications during the review/approval workflow process. When coupled with Notifier jobs, these queries allow you to schedule when notifications are sent to approvers and submitters and how often. For more information about creating Notifier jobs, see [Set up a Notifier Job](/en/vista/vista/system-tools/work-flow/about-automated-notifications/set-up-a-notifier-job).
As part of this new functionality, a new Using Review Workflow Notifier Queries checkbox was added to the PM Company Parameters form. Selecting this checkbox suppresses the system notifications that are currently in use with the Process Workflow feature, so that reviewers and submitters only receive notifications via the Notifier jobs you create. If you leave this checkbox unselected, reviewers and submitters will continue to receive the standard system notifications, along with the notifications sent via the Notifier jobs. For more information, see [Using Review Workflow Notifier Queries](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form/field-definitions-pm-company-parameters-form#concept-3175--en).
For more information about the new Notifier queries, see the [Workflow](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features#concept-9086--en__NewWFNotifierQueries) release notes.

## Assign Project Structure Types to Projects for Trimble Analytics Reporting

You now have the ability to set up project structure types and assign them to projects so they can be used for reporting project data in Viewpoint Analytics.
 Project structure types are used to identify and group project data in a more accurate and meaningful manner for Analytics reporting.
 In conjunction with the addition of project structure types in the Headquarters module (new HQ Project Structure Types form), you now have the ability to assign these structure types to projects.
 To implement this functionality, the following fields were added to the new Analytics section of the PM Projects form (Add'l Info tab):

- Structure Type - Use this field to assign a predefined or custom project structure type to each applicable project.

-  Exclude from Analytics - Use this checkbox to exclude the selected project from project type Analytics. This is useful for dummy jobs set up for testing or any other project that should not be included in Analytics reporting.

For more information about assigning structure types to projects, see [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
 For more information about the new HQ Project Structure Types form, see the [Headquarters](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/headquarters-features#concept-5952--en__ProjStructTypeHQ) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
