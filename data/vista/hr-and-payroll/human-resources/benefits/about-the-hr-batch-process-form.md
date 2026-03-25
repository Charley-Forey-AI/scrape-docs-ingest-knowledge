---
title: "About the HR Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/about-the-hr-batch-process-form"
---

#  About the HR Batch Process Form

The HR Batch Process Form is used to process HR
 batches.
 This form can be accessed from the main
 menu, by selecting the Process Batch option from the File menu of HR Update
 Benefit/Salary to PR any of the posting programs in HR.
 This program is used to process batches
 created in the HR Update Benefit/Salary to PR program. Although this program can be
 accessed from the main menu, it is automatically accessed once you click on the Post
 button at the bottom of the HR Update Benefits/Salary to PR form.
Note: This is the only program in HR that requires batch
 processing, as most of the data is specific to HR only and is not updated to any other
 module. The only other update to PR that occurs is when HR Resource information is
 updated to the PR Employee Master; however, that information is updated online and does
 not require this program.
 Once you have specified the month and batch
 to process, the Info section displays information about the batch (i.e. creator,
 creation date, source, and status).

## Audit Reports

The program runs through all the data in
 the batch and creates Audit Reports that you can preview and/or print before you
 proceed with posting the batch.

- Batch List — Prints the HR
 Salary History Audit and/or HR Benefit Update Audit reports. Reports show
 all entries in the batch in sequence order.

- Error List — Prints the HQ Batch
 Control Error List. Report shows the sequence number and error message for
 any entries in the batch where errors were found in the validation process.
 Errors must be corrected before the batch can be posted.

It is recommended that you print the
 audit lists before posting a batch, because once the batch is posted, the audit
 lists are no longer available.
Note: Users who have access to batch processing forms
 do not automatically have access to the related audit reports. It is recommended
 that if they will be processing batches, you give them access to the related audit
 reports using VA Report Security. If users do not have access, they will receive an
 error message when trying to preview/print those reports to which they do not have
 access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature
 (assigned in HR Company Parameters), restricted access to one or more audit reports
 will prevent the user from posting the batch.
Once the batch is ready for processing,
 enter the posting date and click the Post button at the bottom of the screen.

## Clearing the Batch

When you create a batch, the system adds
 the data to a batch table and stores it until you are ready to post the batch. Data
 is not updated online; therefore, you can delete it completely without affecting any
 modules, including the module in which you created the batch. To clear a batch table
 of stored data, select ‘Clear Batch’ from the File menu. The system will
 clear/delete all data from the batch. (Note: Previously posted transactions added to
 the batch are only cleared from the batch—they are not deleted.)
Note: The system creates an audit record each time you
 clear a batch. For information about cleared batches (i.e. user who cleared batch,
 as well as the date and time the batch was cleared), use the VA 'Other Events'
 Statistics report.
The Clear Batch option is disabled if
 the batch’s status is 4 (Posting in Progress). This is to prevent partially updated
 batches from being deleted should the update process be interrupted (i.e. power
 outage, system failure, etc.). When a batch update is interrupted, only a portion of
 the intended updates may occur. If a user later clears the batch, there is no way to
 determine the updated data.
