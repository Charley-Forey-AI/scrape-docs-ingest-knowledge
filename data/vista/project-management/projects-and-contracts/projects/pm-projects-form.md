---
title: "PM Projects Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form"
---

# PM Projects Form

Use this form to create and maintain projects in Project Management.

 Information entered in this form automatically updates the JC Jobs form, but projects/jobs set up in the PM module have a “pending” status and cannot be accessed in the Job Cost module until the project has been interfaced using [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form).
You can set up default document templates for a project using the Distribution Templates () icon in the toolbar. For example, if all of the RFI documents generated using the Create and Send feature in a specific company should use a specific document template (have a specific logo and format), you should set up that RFI document template as the default for that company. For more information, see [Assign a Project Template](/en/vista/vista/project-management/create-and-send/assign-a-project-template).

## Project Code Length and Format

All Project Management files are stored by project code. The length and format of your project code was defined when your system was installed. Typically, project codes are multi-part codes, (dashes between certain characters) to allow you to set up sub categories and sub-sub categories within a project.
For example, a project with multiple buildings could be set up as follows if you use multi-part project codes:
Project:
1025
Industrial Park

Sub-project:
1025-1
Building one

1025-2
Building two

Sub-sub-project:
1025-1-1
Bldg 1, 1st floor

1025-1-2
Bldg 1, 2nd floor

Note: Your project code format must be identical to your job code format, which was set up when Vista was implemented in your organization.

## Analytics

If you are using Trimble Analytics, the Analytics section allows you to assign structure types to projects for project data reporting.
 Structure types are set up in HQ Project Structure Types and, when assigned to projects, are used during Analytics reporting to aggregate project data in a more accurate and meaningful manner.
If you have projects that should not be included in Analytics reporting, select the Exclude from Analytics checkbox for each applicable job. Even if you have assigned a structure type to a project, selecting this checkbox ensures that the project is excluded from your project data during Analytics reporting.

## Add-Ons, Locations, Firms, and Phases Tabs

The Add-Ons, Locations, Firms, and Phases tabs all provide quick access to related project information forms. For example the Firms tab provides quick access to the PM Project Firms, which is used to associate firms with the project. You can either enter information directly into the Firms tab, or you can double-click on a record to launch the PM Project Firms form.
Click on a link below for information about a tab and its related form:

- [Add-Ons](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-add-ons-form)

- [Locations](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-locations-form)

- [Firms](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-firms-form)

- [Phases](/en/vista/vista/project-management/projects-and-contracts/projects/pm-project-phases-form)

## Roles

Use the Roles tab to assign users and roles to a project. For example, you can define which user is the project manager of the project. Once the project is interfaced with the JC module, users can filter by job phase/role when posting progress in JC Progress Entry and cost projections in JC Cost Projections.
Roles are created and maintained using the HQ Roles form, and they can also be assigned at the project phase level in PM Project Phases or using the JC Phase Roles Initialize form (accessed by selecting File > Job Phase Roles Initialize).
YThe following rules apply when adding roles/users:

- Users can only be associated with a role that they have been set up with using the [HQ Roles](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) tab.

- Users can be assigned to more than one role - for example a single user can have multiple roles.

- Roles can be used more than once.

## M/WBE Goals

This tab displays the certificates on the project and allows you to view the SWMBE goals. This tab is only available if you have the Pre-Construction module and created the project from a PC potential project using [PC Create PM Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-create-pm-project-form).
Changes made to the certificates on this tab will update the potential project on [PC Potential Project](/en/vista/vista/costs-and-contracts/pre-construction/pc-potential-projects/potential-project-setup/about-the-pc-potential-projects-form). Certificate types are created and maintained using [PC M/WBE Certificate Types](/en/vista/vista/costs-and-contracts/pre-construction/pc-setupmaintenance/about-the-pc-mwbe-certificate-types-form).

## Workflow

If you have the Workflow module and are using the Process Workflow feature, you can use the Workflow tab to define which workflows apply to the entire company. The workflow processes set up here override the workflow processes set up using the Workflow tab on the HQ Company Setup form.Note: You can also set up company-level workflow processes using the Assigned Companies tab on the [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process) form.

## Deleting a Project

In most cases, deleting a job will require using the JC Contract Purge form. However, you can use this form to delete a job if you have not posted any activity to that job (e.g. cost or revenue adjustments, change orders, purchase orders, etc.). If you have already set up phases/cost types and estimates, you will need to delete those records before you can delete the job.
When you delete a job here, the system will check for and delete any related PM records (e.g. project firms, issue history, document history, punch lists, submittals, etc.). It will not delete records if the job is not in a pending state.

## Viewpoint For Projects™

Viewpoint For Projects™ (VPC) integration allows you to manage the publication of Vista Project Management Word or PDF documents (such as RFIs, Change Orders, etc.) to the web-based, collaborative work space provided by Viewpoint For Projects.
You can associate a Vista project with a Viewpoint For Projects™ project using the Select button at the bottom of the Info tab in PM Projects. However, to use this feature, you must have a Viewpoint For Projects™ user account associated with your Vista user account in the VA User Profile form, Project Collaboration tab.
For more information about Viewpoint For Projects™ integration, see [Viewpoint For Projects (VFP) Integration Overview](/en/vista/vista/project-management/viewpoint-for-projects-vfp-integration/viewpoint-for-projects-vfp-integration-overview).

[About Project Setup](/en/vista/vista/project-management/projects-and-contracts/projects/about-project-setup)
[Set up Job Level Security](/en/vista/vista/project-management/projects-and-contracts/projects/set-up-job-level-security)
[Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)
[About Distribution Groups/Default Distribution](/en/vista/vista/project-management/create-and-send/about-distribution-groupsdefault-distribution)
[PM Distribution Groups Form](/en/vista/vista/project-management/create-and-send/pm-distribution-groups-form)

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)
