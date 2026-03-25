---
title: "PR Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/pr-batch-process-form"
---

# PR Batch Process Form

This form can be accessed from the main menu or by selecting the Process Batch option from the File menu of any of the posting programs in PR (PR Auto Leave Accrual/Usage, PR Auto Overtime, PR Leave Entry, PR Post Auto Earnings, PR Salary Distribution, and PR Timecard Entry).
 Once you have specified the month and batch to process, the Info section of the screen displays the batch’s creator and creation date, the batch source, and the batch’s status, which is typically “open.”

- Audit Reports - The next step in batch processing is to
 validate the information in the batch. Click on the
 Validate button. The program runs through all the data
 in the batch, creates Audit Reports (Batch List and
 Error List) that you can preview and/or print before
 you proceed with posting the batch. It is recommended
 that you print the audit lists before posting a batch;
 once the batch is posted, the audit lists are no longer
 available.

- Batch List – Prints the audit list, depending on the batch
 you are processing. Shows related information for each
 entry in the batch, in sequence order, with totals by
 batch sequence and batch.

- Error List – Lists the sequence number and the error message
 for any entries where orders were found in the
 validation process. You must correct the errors before
 you can post the batch. Users who have access to batch
 processing forms do not automatically have access to
 the related audit reports. It is recommended that if
 they will be processing batches, you give them access
 to the related audit reports using VA Report Security.
 If users do not have access, they will receive an error
 message when trying to preview/print those reports to
 which they do not have access. In addition, if using
 the ‘Attach Batch Report to HQ Batch Control’ feature
 (assigned in PR Company Parameters), restricted access
 to one or more audit reports will prevent the user from
 posting the batch. Once the batch is ready for
 processing, enter the posting date and click the Post
 button at the bottom of the screen.

- Clearing the Batch - When you create a batch, the system
 adds the data to a batch table and stores it until you
 are ready to post the batch. Data is not updated
 online; therefore, you can delete it completely without
 affecting any modules, including the module in which
 you created the batch. To clear a batch table of stored
 data, select ‘Clear Batch’ from the File menu. The
 system will clear/delete all data from the batch.
 (Note: Previously posted transactions added to the
 batch are only cleared from the batch—they are not
 deleted.)Note:
 The system creates an audit record each time you
 clear a batch. For information about cleared
 batches (i.e. user who cleared batch, as well as
 the date and time the batch was cleared), use the
 VA 'Other Events' Statistics report.
Note: The Clear Batch
 option is disabled if the batch’s status is 4
 (Posting in Progress). This is to prevent
 partially updated batches from being deleted
 should the update process be interrupted (i.e.
 power outage, system failure, etc.). When a batch
 update is interrupted, only a portion of the
 intended updates may occur. If a user later clears
 the batch, there is no way to determine the
 updated data.

Related information

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
