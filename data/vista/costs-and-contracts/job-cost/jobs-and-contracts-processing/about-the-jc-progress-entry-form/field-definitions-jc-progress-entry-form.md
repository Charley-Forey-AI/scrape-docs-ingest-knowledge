---
title: "Field Definitions: JC Progress Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form/field-definitions-jc-progress-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-progress-entry-form/field-definitions-jc-progress-entry-form"
---

# Field Definitions: JC Progress Entry Form

The following is a list of field descriptions for the JC
 Progress Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Actual Date

The Actual Date filter on the JC Progress Entry form, header section.

Enter the date for posting progress or leave blank if entering progress for more than one actual date in the same batch.
 Once you enter a value in this field, the grid below shows only existing sequences that match this date. In addition, this date defaults as the actual date for all new sequences added to the grid.
We recommend that the date be in the batch month. Posting to dates outside the batch month may cause discrepancies between progress and projections, since projections work strictly off the batch month, and Current Complete (in Progress Entry) includes any prior posting through the batch month and date entered.
For example, if you enter progress in Batch Month 06/XX, but Date 07/01/XX, and then go into Cost Projections for Batch Month 06/XX. Because projections look at only the batch month, the projections batch will include the posting for 07/01/XX. However, if you then open a progress batch in Batch Month 06/XX, Date 06/30/XX, Current Complete will not include the 07/01/XX posting.

### Importing Progress

When importing progress from a 3rd party application (for example Heavy Job or Bid2Win) and you have imported progress on multiple actual dates, you can use this field to filter the progress that displays in the lower portion of the form by actual date. For example select a date in this field and only progress with that actual date will display in the lower portion of the form.

## Job

The Job field on the JC Progress Entry form, header section.

Enter the job for which to post progress or press F4 to select from a list of valid jobs. Leave blank if entering progress for more than one job in the same batch.
Note: If you enter a soft- or hard-closed job and posting to closed jobs is not allowed, a message displays and you will not be able to enter progress. The Allow Posting to Soft-Closed Jobs and Allow Posting to Hard-Closed Jobs boxes on the Info tab of JC Company Parameters determine if you can post progress to soft or hard-closed jobs

### Importing Progress

When importing progress from a 3rd party application (for example Heavy Job or Bid2Win) and you have imported progress on multiple jobs, you can use this field to filter the progress that displays in the lower portion of the form. For example select a job in this field and only progress on that job will display in the lower portion of the form.

## Sequence

The Sequence field on the JC Progress Entry form.

 If you initialized phases to the grid (via JC Progress Filter), this field displays the sequence number assigned to each phase/cost type for the job.
 If you are manually entering phases/cost types, enter N, New, or + to add a new sequence. The system automatically assigns the next available sequential number.

## Actual Date

The Actual Date field on the JC Progress Entry form.

Use this field to enter the date of the progress. This allows you to have records with the same phase and cost type but different actual dates, for example if you import records from third-party applications like Heavy Job or Bid2Win.
 We recommend that the date entered in this field be in the batch month. Posting to dates outside the batch month may cause discrepancies between progress and projections since projections work strictly off the batch month, and Current Complete (in Progress Entry) includes any prior posting through the batch month and date entered.
For example, if you enter progress in Batch Month 06/XX, but Date 07/01/XX, and then go into Cost Projections for Batch Month 06/XX. Because projections look at only the batch month, the projections batch will include the posting for 07/01/XX. However, if you then open a progress batch in Batch Month 06/XX, Date 06/30/XX, Current Complete will not include the 07/01/XX posting.

## Job

The Job field on the JC Progress Entry form, Info tab.

Enter the job for which to enter progress or press F4 to select from a list of valid jobs.
If you enter a soft- or hard-closed job and posting to closed jobs is not allowed, a message displays and you will not be able to enter progress.
The Allow Posting to Soft-Closed Jobs and Allow Posting to Hard-Closed Jobs checkboxes on the Info tab of the JC Company Parameters form determine if you can post progress to soft- or hard-closed jobs.

## Phase

The Phase field on the JC Progress Entry form.

 Specify the phase for which to enter progress or press F4 to select it from a list. If you filtered the phases and cost types that display in the grid using the JC Progress Filter form, this field defaults a selected phase.
Note: You can use CTRL+N and CTRL+L to cycle through phases/cost types not already in the batch. CTRL+N moves you to the next phase/cost type; Ctrl+L moves you to the previous phase/cost type. To cycle through phases/cost types already in the batch, use the Page Up/Page Down keys.

## Cost Type

The Cost Type field on the JC Progress Entry form.

If you initialized cost types to the grid (via JC Progress Filter), displays all cost types specified for display. Otherwise, defaults as null.
Note: Regardless of the cost types selected for display, if you are using linked cost types, they will only display in the grid if you selected the Show Linked Cost Types option (in the Options menu), or if you overrode them using the JC Progress Link CT Detail form (accessed by selecting File > Maintain Progress Link Cost Types).

Enter the cost type to which you want progress posted for this phase or accept the defaulted cost type. For new sequences, you can cycle through cost types for the specified phase that are not already in the batch using the following methods:

- CTRL + N – moves you to the next cost type

- CTRL + L – moves you to the previous cost type

- Page Up/Page Down – cycles through phases/cost types already in the batch.

## Field Ticket

The Field Ticket field on the JC Progress Entry form, Info tab.
Enter the field ticket number for this progress entry or press F4 to select from a list of valid field tickets for the specified job/contract.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to JC progress entries is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

## Newly Completed

The Newly Completed field on the JC Progress Entry form.

Enter the new progress units for the phase/cost type (0 - 999,999,999.000). The system automatically calculates the Total Completed and Total Percent fields based on your entry.
If you enter a value in the Total Complete or Total Percent field, the system automatically calculates the newly completed units.

##  Total Completed

The Total Completed field on the JC Progress Entry form.

Enter the total number of units completed for this phase/cost type (0 - 999,999,999.000). This should be the total of current completed and newly completed units. If you specified newly completed units in the previous field, the total completed is calculated automatically. Changes to this calculation will change the Newly Completed units and Total Percent.

## Total Percent

The Total Percent field on the JC Progress Entry form.

Defaults a value based on Current Estimated and Total Completed.
Enter the new total percent complete (up to 9,999.99) or accept the system calculation. For example, enter 15% as 15.00.
If you override the calculated amount, the Newly Completed and Total Completed units are recalculated.
 Percent complete generally represents the percentage of estimated units that have been done. However, if you have plugged a different projected units figure in the Cost Projections program, that figure is used instead, and is identified by an asterisk (*) next to the projected number.

## PR Co

The PR Co field on the JC Progress Entry form.

This field only displays if you selected the Post Crews with progress entry checkbox in JC Company Parameters (Info tab).
If applicable, enter a crew in the PR Crew field or press F4 to select it from a list.

## Crew

The Crew field on the JC Progress Entry form.

After you select a Payroll company in the PR Co field, enter the crew that applies to the progress or press F4 to select from a list of valid crews.
PR crews are created and maintained using the PR Crews form. You can open this form from this field by pressing F5. For more information about crews, see [PR Crews Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-crews-form).
Note: This field only displays on the form when the Post Crews with progress entry box on the Info tab of JC Company Parameters.
