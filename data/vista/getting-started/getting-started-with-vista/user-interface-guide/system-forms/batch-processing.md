---
title: "Batch Processing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/batch-processing"
---

# Batch Processing

Posting programs in the system use batches to record data.
Most of the time spent in a posting program is for the purpose of adding new records, but you can edit records and remove records from a batch as well.
Before posting a batch, validate the batch to ensure the data is valid. If no errors are found, the appropriate audit reports are created. Although not required, it is recommended that you print these reports. If errors are found, an error report is created so that you can review the errors and correct them. Once you have corrected the errors, re-validate the batch (at which time the audit reports will be created and can be printed).
Note: Users who have access to batch processing forms do not automatically have access to the related audit reports. Users must have access assigned to them in VA Report Security.
Once you have finished entering or editing data, process (post) the batch to update the appropriate tables. Transactions are not ‘recognized’ until they are posted. You post batches using the Batch Process form, which you can access from the File menu of the posting form.
After the batch is posted, a message displays to let you know the batch was posted successfully. Click the Close button to clear the message. If you accessed the Batch Process form from within the posting form, the system returns to the posting form. If you accessed the Batch Process form from the main menu, you are returned to the Batch Process form, allowing you to select another batch to post.

## Clearing a batch

You can clear a batch of all transactions
 using the Clear Batch option in the File menu of the Batch Processing form. When a batch
 is cleared, all new transactions are deleted; however, previously posted transactions
 that were added to the batch will only be cleared from the batch — they are not deleted
 from your database.
Note: The system creates an audit record each time you
 clear a batch. For information about cleared batches (i.e. user who cleared batch, as
 well as the date and time the batch was cleared), use the VA 'Other Events' Statistics
 report.

## Editing Previously Posted Transactions

To edit a transaction that has already been
 posted, you can add the transaction to a current batch using the Add Transaction option
 in the File menu of the posting form. The existing transaction will be marked as ‘In
 use’ and no one else will be able to edit that transaction until it is released from the
 batch (by removing it from the batch or by posting the batch).

## Deleting Previously Posted Transactions

To delete a previously posted transaction,
 add the transaction to a current batch using the Add Transaction option in the File menu
 of the posting form, set the Action drop-down in the grid to
 D-Delete, and post the batch. Using the Delete function (menu or button)
 simply removes the transaction from the batch without saving any changes — it does not
 delete the transaction from your database.
Refer to the form help for each module’s
 Batch Process form for information specific to that batch processing form.

Related information

- [System Forms](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms)

- [Form Menu Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-menu-options)

- [Keyboard Shortcuts for Moving Through Form Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/keyboard-shortcuts-for-moving-through-form-fields)

- [Shortcut Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/shortcut-keys)

- [Date Field Shortcuts](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/date-field-shortcuts)

- [Toolbar Options](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/toolbar-options)

- [Function Keys](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/function-keys)

- [Status Bar](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/status-bar)

- [Record Deletion](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/record-deletion)

- [Email a Deep Link to a Record](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/email-a-deep-link-to-a-record)

- [About the Form Properties form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-form-properties-form)

- [Associate a Report with a Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/associate-a-report-with-a-form)

- [About the Field Properties Form](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/about-the-field-properties-form)

- [Field Validation](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/field-validation)

- [Schedule Data Changes for Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/schedule-data-changes-for-fields)

- [Search Form Records](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/search-form-records)

- [Group Custom Fields](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/group-custom-fields)

- [Add a Standard Note to a Field](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/add-a-standard-note-to-a-field)

- [Form Grids](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids)
