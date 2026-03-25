---
title: "HQ Roles Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/role-setup/hq-roles-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/role-setup/hq-roles-form"
---

# HQ Roles Form

Use this form to create and maintain roles.

Roles are used in two ways:

- Approval/review processes: You can assign roles to
 approval/review processes in the Process Workflow feature. To use this feature
 you must have the Workflow module.

- Job/project responsibilities: You can use the Roles tab on the
 JC Jobs and PM Projects forms to add roles and specific users to the
 job/project. Once you have set up roles, you can assign them (manually or by
 initialization) to jobs, projects, and/or phases. Assigning roles at the job or
 project phase level will allow for filtering phases by role for cost projections
 (in JC Cost Projections) or progress posting (in JC Progress Entry) so that
 users can see only those phases and cost type to which they are assigned.

## Spending Limits

The Spending Limits tab only applies to the WF module Process Workflow feature. If you do not use this feature, this tab has no function.
 Spending limits allow you to specify the maximum amount that a user can spend before a workflow will apply. They are defined by document type (purchase order or subcontract) and sub type (that is, the line type of the purchase order or subcontract item).
 For purchase orders, you can set up limits for job, inventory, expense, and equipment sub types. For example, a Project Manager role may have a higher spending limit for Job lines, while a Purchaser role might have a higher spending limit for Inventory lines. If the spending limit for a role does not apply to a specific line type, you can select to apply it to 'all' line types.
For subcontracts, only the Job sub type is valid.
Note: You can also customize the spending limits on specific users associated with the role using the User Spending Overrides button the Users tab. For more information, see [HQ User Spending Overrides Form](/en/vista/vista/administration/headquarters/role-setup/hq-user-spending-overrides-form).

## Users

The Users tab is used to associate specific users with a role. For example, you can assign all of your job superintendents to a Job Superintendent role. However, you must activate the user (that is, select the Active flag) before you can assign the user to roles on jobs (in JC Jobs or PM Projects).
Note: You can also assign roles to a specific user using the Roles tab on the VA User Profile form. Roles set up in VA User Profile are automatically set up for the role in HQ Roles. Likewise, if you assign a user to a role in HQ Roles, the role is automatically set up for the user in VA User Profile. Any updates to the role/user in either form automatically updates the other form. For more information, see [About Assigning Roles to User Accounts](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/about-assigning-roles-to-user-accounts).

Related information

- [JC Jobs Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)

- [About the JC Cost Projections Form](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-projections-form)

- [About the JC Progress Entry Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form)

- [PM Projects Form](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)

- [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

- [Role](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form#ID-0000f8c8--en)

- [Description](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form#ID-0000f8de--en)

- [Active](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form#ID-0000f8e6--en)

- [Usable In](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form/field-definitions-hq-roles-form#ID-0000f8f0--en)
