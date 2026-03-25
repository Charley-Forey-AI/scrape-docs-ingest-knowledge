---
title: "JC Jobs Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form"
---

# JC Jobs Form

Use the JC Jobs form to set up jobs.
Because of the nature of Job Cost, many of the fields relate to other programs, such as the Markup/Discount rate (Info tab), which is used by Inventory, the Price Template and Haul Tax Option (Add'l Info tab), which are used by Material Sales, and the fields on the PR Info tab, which are used by Payroll.

## Locking Job Phases

You can limit the phases that can be used on a job when posting
 transactions by 'locking' the job's phases. This is done by selecting the Phases on
 this Job are Locked checkbox. When selected, users can only use phases that are set
 up for the job in JC Job Phases, JC Original Estimates, or Project Management, or
 that have been used on the job prior to selecting this checkbox. If you do not
 select this checkbox, you can use any phase set up in the JC Phases form.Note: Selecting this checkbox does not affect the ability to
 set up phases for a job in JC Job Phases, JC Original Estimates, or in the PM
 module.

## Analytics

If you are using Trimble Analytics, the Analytics section of JC Jobs allows you to assign structure types to jobs for project data reporting.
 Structure types are set up in HQ Project Structure Types and, when assigned to jobs, are used during Analytics reporting to aggregate project data in a more accurate and meaningful manner.
If you have jobs that should not be included in Analytics reporting, select the Exclude from Analytics checkbox for each applicable job. Even if you have assigned a structure type to a job, selecting this checkbox ensures that the job is excluded from your project data during Analytics reporting.

## Applying Price Escalators

If you are using the oil price escalation/de-escalation feature (in HQ/MS), you will need to check this box for each job that uses materials defined for price escalation (in HQ Escalation Index and HQ Materials). When checked, the MS Oil Price Escalation report tracks sales of the applicable materials (e.g. asphalt mix) to the job (via MS Ticket Entry) and determines increases/decreases in pricing based on the bid index (job start date) and pricing index (monthly escalation/de-escalation).Note: If a quote exists for the job in MS Quotes and you have checked the Apply Price Escalators box for the quote, the system will use the bid index date specified on the quote instead of the job/contract start date.

You can use the MS Oil Price Setup report to easily review jobs, by state, that are using this feature. To review the pricing adjustments for a job, run the MS Oil Price Escalation report. For more information about this feature, see [About the HQ Escalation Index Form](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form).

## Reusing Job Numbers

You can reuse job/contract numbers that you have previously purged as long as no history records exist in the JC History by Job table (JCJH) and no detail exists in AP, PO, and/or SL. If you enter a job number that does not meet these requirements, you will receive a message indicating that history records exist or that detail exists in AP, PO, and/or SL. You will need to purge the job/contract history in JC Contract Purge (Purge Contract History tab) and then run the AP, PO, and/or SL purge programs to purge the related AP/PO/SL detail.

## Roles

Use the Roles tab to set up roles and users on the job. For
 example, you can define which user is the project manager of the job. This allows
 users to filter by job phase/role when posting progress in JC Progress Entry and
 cost projections in JC Cost Projections.Note: This does not
 apply to the PM Cost Projection process. For more information about cost
 projections in PM, see [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form).

You can also assign roles at the job phase level in JC Job Phases
 or through initialization in JC Job Phase Roles Initialize (which you can access
 from this form by selecting File > Job Phase Roles
 Initialize.
If you use the Process Workflow feature, you can use this tab to
 assign users to specific roles. The following rules apply when adding
 roles/users:

- Users can only be associated with a role that they have been
 set up with using the HQ Roles tab.

- Users can be assigned to more than one role - for example a
 single user can have multiple roles.

- Roles can be used more than once.

## Workflows

If you have the Workflow module, you can use the Workflow tab to set up workflows for a job. The workflow processes added here override those set up on the Workflow tab of the JC Company Parameters form and HQ Company Setup forms. For example, any process set up on a specific job overrides the more generic processes set up at the module and application level.

## Deleting a Job

In most cases, deleting a job will require using the JC Contract Purge form. However, you can use this form to delete a job if you have not posted any activity to that job (e.g. cost or revenue adjustments, change orders, purchase orders, etc.). If you have already set up phases/cost types and estimates, you will need to delete those records before you can delete the job.

When you delete a job here, the system checks for and deletes any related PM records (e.g. project firms, issue history, document history, punch lists, submittals, etc.).

Click the links below for related information.
[Job Level Security](/en/vista/vista/costs-and-contracts/job-cost/job-level-security)
[About Updating Actual Units from AP/MS](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-updating-actual-units-from-apms)
[Defining Overtime Calculations](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/defining-overtime-calculations)
[About Using Weighted Average Overtime Rates](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/about-using-weighted-average-overtime-rates)

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)
