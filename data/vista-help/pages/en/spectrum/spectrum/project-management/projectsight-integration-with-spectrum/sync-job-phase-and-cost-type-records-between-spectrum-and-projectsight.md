---
title: "Sync Job Phase and Cost Type Records Between Spectrum and ProjectSight | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/sync-job-phase-and-cost-type-records-between-spectrum-and-projectsight"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/sync-job-phase-and-cost-type-records-between-spectrum-and-projectsight"
---

# Sync Job Phase and Cost Type Records Between Spectrum and ProjectSight

Create a new job phase with cost estimates and sync this data
 so it flows between Spectrum and ProjectSight.
In order to sync budget data
 between Spectrum and ProjectSight, you must first link the projects
 together. For details, see [Link a Job from Spectrum to a ProjectSight Project](/en/spectrum/spectrum/project-management/projectsight-integration-with-spectrum/link-a-job-from-spectrum-to-a-projectsight-project).
If you are an
 existing ProjectSight customer, it is
 recommended that you create a new portfolio for new projects you want to link to
 Spectrum, as projects created in
 ProjectSight inherit the budget code
 structures and all the lookup values from the portfolio. Important: Keep the following in mind when integrating
 budget items:

- All the jobs you want to integrate between Spectrum and ProjectSight must use the same job
 phase format.

- Only the budget items with an Approved status are sent
 to Spectrum. Budget items created in Spectrum display as Approved in ProjectSight.

- You can create a budget record in either Spectrum or ProjectSight, and, with the
 appropriate approved workflow status, the data will automatically create
 a new record in the other application. However, once budget records have
 been created and exist in both platforms, you *must make all edits in ProjectSight*. Changes
 made in Spectrum will
 be overridden, as the budget item edits and transfer amount data flows
 from ProjectSight into
 Spectrum.

1. If you are starting in Spectrum:

1. Create a new phase for a job and enter
 cost estimates.For more information about
 creating new phases, see [Job Phases](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/job-phases).

1. New phases created in Spectrum sync
 automatically to ProjectSight. To view the data, open the project in ProjectSight and navigate to Budget Group
 Lookup.See the table below for the
 matched fields.

1. If you are starting in ProjectSight:

1. Add a new budget item.ProjectSight Help: For more information about creating new
 budget items, see the ProjectSight Help on [Adding Budget
 Items](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Budget-Items.htm#add).

1. Select a status to send the data to
 Spectrum. You
 must choose an Approved status.

1. New budget items created in ProjectSight sync automatically
 to Spectrum. To view
 the data, open the Job Phase record in Spectrum.

1. Edit budget items or transfer budget amounts in
 ProjectSight. Note: Edits to job phases and cost
 estimates in Spectrum
 will be overridden with the budget data from ProjectSight.

The following fields are synced between Spectrum and ProjectSight:Spectrum Job Phase Field NameProjectSight Budget Item Field Name
Phase
Cost Type
Budget Code

Original Cost
Original Budget
