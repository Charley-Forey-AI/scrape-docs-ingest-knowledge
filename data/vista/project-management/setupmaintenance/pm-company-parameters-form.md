---
title: "PM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form"
---

# PM Company Parameters Form

Use this form to set up the various control options for Project Management processing in a company.
You must define these setup options before you begin processing in Project Management. Each company in which Project Management processing will occur must be set up here.
It is important that you understand the effects of each setup option because the options you select affect which Project Management forms you use, how the forms work, and how other modules (Job Cost, Job Billing, Subcontract Ledger, Inventory, Material Sales, and Requisitions) are affected. You should restrict this form so only the system administrator has access to it.

- Default Document Templates - You can set up document templates at the company level and at the project level.

- Company - Use the Document Templates tab on the PM Company Parameters form to assign document templates to the company. For example, if all RFI documents generated in a company should use a specific RFI document template, add that template to the Document Templates tab on the PM Company Parameters form. When the Create and Send feature is used to generate an RFI document for any project in that company, by default the RFI document will be generated using the selected template.

- Project - Click the Distribution Templates icon to set up the default document templates on a project, and/or configure which document templates can be used to generate project documents. For more information, see [Assign a Project Template](/en/vista/vista/project-management/create-and-send/assign-a-project-template).Note: If there are document templates set up for both the company and a project, the templates set up for the project will alwaysoverride any templates set up for the company.

- Cost Type Display - This tab allows you to specify which cost types should display when entering phases for a project in PM Project Phases. You can specify as little as one cost type or as many as ten cost types. However, you should consider screen size and system performance in determining how many cost types you select for display. You may typically only want to show those cost types for which you standardly enter original estimates when adding phases to a project.

- Add-Ons - The Add-Ons tab is used to set up company defaults for add-on cost calculations - typically add-ons are used for adding things like overhead, profit, bonds, taxes, and other indirect costs to change orders. When a project is created and associated with this company, the project will inherit the add-on costs setup on the company record. Then when pending change orders are created on that project in PM Pending Change Orders, the add-on cost calculations will populate on the PCO. For information on adding an add-on to the company record, see [PM Company Add-ons Form](/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form).

- Workflow - This tab only applies if you have the Workflow module and use the Process Workflow feature. Use this tab to define which workflows should be used for each company. The workflow processes set up here override the workflow processes set up using the Workflow tab on the HQ Company Setup form..Note: Workflows assigned here are updated to the Assigned Companies tab in WF Workflow Process. However, they will show the assigned company as JC, not PM. For more information, see the F1 help for the [Module](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow/wf-workflow-process/field-definitions-wf-workflow-process-form#ID-0004e45b--en__JC-PMModuleAssign) field in WF Workflow Process, Assigned Companies tab.

- Projections - Use the Projections tab to configure the cost projections created in the PM Cost Projections form. For general information on the PM Cost Projections process, including how to set it up, see [About Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/about-cost-projections). There are cost projection settings on both the JC Company Parameters and PM Company Parameters forms; however, these forms do not update each other, so changing the options on one form has no impact on the other form. This allows you to maintain separate configurations for JC Cost Projections and PM Cost Projections.

Once you start using the application, be careful about changing a set up option, as it can impact processing or stored information. Contact Support if you want to change an option but are unsure of its impact on existing data.
You can track changes to this form, including additions and deletions. The HQ Master Audit (HQMA) table contains a list of changes to records in the application. For more information, see [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log).
For additional information about using this form, click the links below.
[About Subcontract, PO, and MO Number Formats](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats)
[About Using Significant Part of Job](/en/vista/vista/project-management/setupmaintenance/about-using-significant-part-of-job)
[About the Add Items to Approved MOs/POs Options](/en/vista/vista/project-management/setupmaintenance/about-the-add-items-to-approved-mospos-options)
[PM Company Add-ons Form](/en/vista/vista/project-management/setupmaintenance/pm-company-add-ons-form)
[About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
[Use Notifier Queries for Workflow Notifications](/en/vista/vista/project-management/setupmaintenance/use-notifier-queries-for-workflow-notifications)
