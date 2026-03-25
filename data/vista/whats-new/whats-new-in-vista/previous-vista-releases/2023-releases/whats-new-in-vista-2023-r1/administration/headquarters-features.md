---
title: "Headquarters Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/headquarters-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/headquarters-features"
---

# Headquarters Features

Vista 2023 R1 delivers on user-requested Headquarters enhancements, fixes, and other improvements.

## Added Support for Subcontract Workflow Process

With this release, you now have the ability to create workflows for the review/approval of pending subcontracts.
The following changes support this functionality:
HQ Company SetupThe Document Type drop-down on the Workflow tab now includes an SL-Subcontracts option. When you select this option, the workflow process you assign must be associated with a Subcontract document type or have no document type designation.Each HQ company can have only one Subcontract workflow assigned. However, you can override the Subcontract workflow assigned to an HQ Company by JC/PM company (in JC Company Parameters/PM Company Parameters) or at the job level in JC Jobs/PM Projects.
HQ Roles / HQ User Spending OverridesThe Document Type drop-down on the Spending Limits tab in [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) and in [HQ User Spending Overrides](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form) now includes a SL-Subcontracts option. When you select this option, the Sub Type field automatically defaults to Job. This is the only option that is valid for Subcontracts.The system uses the Spending Limits and Spending Overrides defined for roles/users to determine whether a subcontract must go through the review/approval workflow process.

 Process workflows are set up in the WF Workflow Process form. For more information about process workflows, see [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) and [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).
 For more information about the Subcontract Review/Approval feature added in this release, see the [Workflow](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/system-tools/workflow-features) release notes.

## Project Structure Types for Trimble Analytics Reporting

You now have the ability to set up project structure types and assign them to jobs so they can be used for reporting project data in Trimble Analytics.
Project structure types are used to identify and group project data (for example, estimates, actuals, change orders, etc.) in a more accurate and meaningful manner for Analytics reporting.
To implement this functionality, a new HQ Project Structure Types form was added for setting up project structure types. Vista provides a set of standard project structure types (based on industry standards), but also allows you to set up custom project structure types. If you elect to set up custom project types, you must link them to standard project structure types for reporting purposes. For more information, see [HQ Project Structure Types](/en/vista/vista/administration/headquarters/company-setup/hq-project-structure-types).
Once set up, project structure types are then assigned to applicable jobs (in JC Jobs) and projects (in PM Projects). For more information, see the [Job Cost](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-cost-features#concept-409--en__ProjStructTypesJobs) and [Project Management](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/project-management/project-management-features#concept-8854--en__PMProjStructTypes) release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
