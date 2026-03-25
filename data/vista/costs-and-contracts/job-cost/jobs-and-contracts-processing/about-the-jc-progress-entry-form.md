---
title: "About the JC Progress Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form"
---

# About the JC Progress Entry Form

Use this form to record the progress on a job by posting quantities completed and/or percent of units complete to a job’s phases/cost types.
Actual costs in Job Cost include units, hours, and dollars. Hours and dollars are updated by posting transactions throughout the software. Units complete are also updated by posting transactions; however, you can also enter them here. You will typically use this form to update units complete for labor and equipment. It is important to note that units should refer to physical units (e.g. cubic yards, square feet, etc.), not hours. Hours are stored in a separate column in the job cost tables and will be updated automatically from Payroll. If entered as units here, hours will be duplicated and will not be an accurate accounting of progress completed on the job.
Posting progress on units in this form is not required; however, it is needed for production-based reporting. It is also used to initialize job billings (JB) and/or calculate projections (JC Cost Projections) based on units complete. Therefore, it is expected that this program be updated before cost projections are calculated.
Although progress can be entered on either the Info or Grid tabs, it is typically easier to use the grid due to its spreadsheet format. In addition to showing the current estimated, projected, and completed units for each phase/cost type, columns are provided for entering newly complete and total complete units, as well as total percent complete. If you allow posting crews with progress (flag in JC Company Parameters), you can also specify the PR Co and crew to which the progress entry applies.
If you are using the PR Crew Timesheets feature, the grid is automatically populated with any progress units posted with the crew timesheets (depending on the phases and cost types you selected for display) and will include the PR company and crew to which the progress units apply.
Note: All units shown or entered on this screen reflect the unit of measure designated for the Job/Phase/Cost Type in the Phase Master or Job Phases files. Progress can only be posted to the specified unit of measure.

## Manual Entry

You can manually enter phases/cost types regardless of whether you elected to initialize the entries (via JC Progress Filter). If you initialized phases/cost types, you will typically only need to use manual entry for those phases/cost types that were not initialized to the batch.
If you are using the Info tab to post progress, you can cycle through the job's phases/cost type using Ctrl+N (next phase/cost type) and/or Ctrl+L (previous phase/cost type). Once you enter the sequence number and move to the Phase field, the system automatically defaults the first phase on the job. You can accept the phase, enter another phase, or use Ctrl+N to cycle through the phases/cost types until you access the one you want.
 If using Ctrl+N in the Cost Type field, the program will only cycle through the cost types for the specified phase. To access a previous phase/cost type, use Ctrl+L. If you initialized phases/cost types, you can use the Ctrl+N or Ctrl+L functions when adding new sequences to the batch; however, the program will only cycle through those phases/cost types not already in the batch. To cycle through phases/cost types already in the batch, use the Page Up or Page Down keys.

## Updating Units Complete

You have the option to update units complete for each phase/cost type by entering the newly completed units, total completed units, or the percent complete. Entering newly complete or total complete units will automatically calculate the percent complete. If you elect to enter percent complete, newly complete and total complete units will be calculated automatically. Percent complete generally represents the percentage of estimated units that have been done. However, if you have plugged a different projected units figure in the Cost Projections program, that figure is used instead, and is identified by an asterisk (*) next to the projected number.

## Cost Detail

The Cost button at the top of the form provides access to the JC Job Phase Cost Detail form, allowing you to review cost detail for a selected phase/cost type. For more information, see [JC Job Phase Cost Detail Form](/en/vista/vista/costs-and-contracts/job-cost/costs/jc-job-phase-cost-detail-form).

## Sort by Phase or Contract Item

Records are automatically sorted by phase in the progress entry grid. However, you have the option to sort records by contract item by clicking the heading of the Contract Item column. Clicking this column once will cause records to be sorted in ascending order (1, 2, 3, etc.), clicking again will cause records to sort in descending order (3, 2, 1)

## Filter by Phase and Cost Type

You may enter units complete for any or all phases/cost types on the job. However, if you will be posting units complete for specific phases/cost types, such as labor and/or equipment, you can use the JC Progress Filter form (accessed by selecting File >  Filter by Phase and Cost Types) to restrict the display of phases/cost types to only those that you need.Note: If you are using the [job roles](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form) functionality and have assigned roles at the phase level (in JC Job Phases), users assigned job roles will have access to only those phases assigned to their role. However, setting the filter to 'All Phases' will allow users to see all phases, regardless of job phase role assignment.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you enter a progress entry sequence, you can assign it to a field ticket associated with the contract for the specified job. You can assign multiple progress entry sequences to a single field ticket, as long as the ticket is still open (that is, it has a status of O-Open in JC Field Ticket). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to progress entry sequences is only useful if the job's contract/contract item has a bill type of T&M or Both. Additionally, once you process a progress entry batch, entries associated with approved field tickets appear on the Cost Detail tab in JC Field Ticket for the specified field ticket.

 For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

The links below contain information on tasks related to JC Progress Entry.
[Enter Progress](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/enter-progress#task-2316--en__task-2316)
[Linked Cost Types](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/linked-cost-types#concept-3502--en__concept-3502)

Related information

- [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form)
