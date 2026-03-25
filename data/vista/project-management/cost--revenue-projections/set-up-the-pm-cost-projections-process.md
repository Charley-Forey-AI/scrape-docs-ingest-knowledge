---
title: "Set up the PM Cost Projections Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/cost--revenue-projections/set-up-the-pm-cost-projections-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/cost--revenue-projections/set-up-the-pm-cost-projections-process"
---

# Set up the PM Cost Projections Process

There are certain setup requirements that must be met before
 you can begin using the Cost Projections feature in Projection Management.
The following guides you through the steps
 needed to implement the use of cost projections in Project Management.

1. Admin: The users entering projections will need access to
 several forms in the application. Use VA Form Security to grant access to these
 forms. List of new forms:

- PM Cost Projections

- PM Cost Projection
 Editor

- PM Projection Codes

- Create Proj Code from
 Item

- Create ProjCodes from CT


- Create ProjCodes from
 Phase

- Create ProjCodes from
 PhaseCT

- JC Projection Code
 Assign

1. Admin: Use VA Inquiry Security to give users access to the
 PMCostProjectionHistory and PMCostProjectionHistoryCodeLevel inquiries. The PM Cost
 Projection History option on the standard PM Work Center
 allows users to view previously posted projections. For example open a
 projection that you posted 3 months ago to review the past numbers and look
 at the progression of your projections over time.
 The PM Cost
 Projection History option on the PM Work Center uses the
 PMCostProjectionHistory and PMCostProjectionHistoryCodeLevel inquiries.
If you do not grant a user
 access to these inquiries, they will be able to access the PM Cost
 Projection History option on a standard PM Work Center that
 they added after upgrading to version 6.8.X or higher, but they will not be
 able to add the PM Cost Projection
 History option to an existing PM Work Center.

1. Configure the projection
 options on the Projections tab on the PM Company Parameters form. Most of these
 fields are on both the JC Company Parameters and PM Company Parameters forms.
 Changing an option in the PM Company Parameters form will
 not change the same option on the JC Company Parameters form.
 This allows you to maintain separate configurations for JC Cost Projections and
 PM Cost Projections.

1. Configure the projection
 options of the pending change order document types in the PM module. Check the Include in
 JC Projections box (PM Document Types ) if pending change
 orders of that document type in the PM module should be included cost
 projections. The pending change orders will display on the JC Projection
 Future CO form on the JC Cost Projections form. For more information, see
 [Include in Cost Projections](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form/field-definitions-pm-document-types-form#ID-00026b87--en).

1. Configure status codes
 using PM Status IDs, Projections Option drop-down. The status of a pending
 change order item determines if it will be included in projections. For more
 information about this option, see [Projections Option](/en/vista/vista/project-management/setupmaintenance/pm-status-ids-form/field-definitions-pm-status-ids-form#ID-0002d22c--en).

1. Configure the projection
 options on the project.

- [Update Plugged Projections
 Automatically](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form#ID-00018eeb--en) (JC Jobs > Additional Info tab)

- [Minimum Projection %](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form/field-definitions-jc-jobs-form#ID-00018cc7--en) (JC Jobs > Info
 tab)

- [Minimum Projection %](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form/field-definitions-jc-job-phases-form#ID-000191cc--en) (JC Job Phases>
 Info tab)

- [Buy Out](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-job-phases-form/field-definitions-jc-job-phases-form#ID-000192a1--en) (JC Job Phases> Cost Types
 tab)

1. Optional: Set up [linked cost types](/en/vista/vista/project-management/cost--revenue-projections/about-using-linked-cost-types).

1. Create the projection
 codes. You have to repeat this step each time you want to enter projections on a
 new project.Use the PM Projection Codes form
 to create the projection codes for a project. The projection codes determine
 the level of detail that you can use when creating the cost projections in
 the PM Cost Projections form.
There are a few ways to create
 the projection codes.

- Automatically create all of
 the projection codes for a job - You can
 automatically create all of the projection codes for a job based on
 the phases, cost types, phases and cost types, or contract items on
 that job.

- Quickly add/remove phases and cost types on a projection
 code - Use the  icon to quickly add or remove
 phase/cost types to an existing projection code.

- Copy the projection codes on
 another project - Copy the projection codes that
 have already been set up from one job to another.

- Copy projection codes when
 copying a project - When using the PM Copy Project
 form to create a new project, check the Projection Codes box. The projection codes on the
 source project will be copied to the new project.

- Manually - You
 can also manually add or remove the phase/cost types on a projection
 code using the Phase/Cost Type tab on the PM Projection Codes form.


Now you're ready to enter cost projections
 using the PM Cost Projections form.

Related concepts

- [About Setting Common UMs for Projection Codes](/en/vista/vista/project-management/cost--revenue-projections/about-setting-common-ums-for-projection-codes)

- [About the PM Cost Projections Form](/en/vista/vista/project-management/cost--revenue-projections/about-the-pm-cost-projections-form)

- [PM Projection Codes Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-codes-form)

- [PM Projection Code Copy Form](/en/vista/vista/project-management/cost--revenue-projections/pm-projection-code-copy-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)

Related tasks

- [Enter Cost Projections](/en/vista/vista/project-management/cost--revenue-projections/enter-cost-projections)

- [Create Projection Codes Automatically](/en/vista/vista/project-management/cost--revenue-projections/create-projection-codes-automatically)
