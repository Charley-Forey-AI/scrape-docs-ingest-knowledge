---
title: "Transfer Pre-Time Cards to Pay Cycle | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/transfer-pre-time-cards-to-pay-cycle"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/time-card-entry/transfer-pre-time-cards-to-pay-cycle"
---

# Transfer Pre-Time Cards to Pay Cycle

This screen is used to transfer information, including Automatic Retro Pay records, from Pre-Time Card Entry to Time Card Entry.
Payroll hours as well as Job Cost quantities will update.

- Before running the update, be sure that the Payroll cycle is
 set correctly. If the Payroll Installation > Recalculate pay rates during pre-time card update checkbox is selected and you overwrite pay rates during Pre-Time
 Card Entry, the rate entered will NOT be retained during the transfer to Time
 Card Entry. Instead, the rate will be set as if the transaction had been entered
 directly in Time Card Entry, taking into account the other Payroll
 Installation screen settings.

- If the Payroll Installation > Recalculate pay rates during pre-time card update checkbox is selected, the update will reset time card pay rates
 based on the work date. If the Payroll Installation > Recalculate pay rates during pre-time card update checkbox is not selected, the same pay rates stored in Pre-Time
 Card Entry are transferred to Time Card Entry.

- When transferring pre-time card entries into the time card file, the corresponding sequence number from pre-time card is used. For example, sequence #1 pre-time card records are added to the time card sequence #1, sequence #2 records are added to sequence #2, and so forth If time card records already exist for a given sequence at the time the Transfer Pre-time Cards Update is performed, the software verifies that pre-time card lines are not added to a manual or void check in the time card file. In this case, the transferred records are added to the next available unused sequence number. Likewise, any manual or void entries in the Pre-time card file are transferred only into an unused sequence number in the time card file. A special listing will print if any sequence numbers were reassigned or if records were not transferred because all nine sequences were already in use.

- Manual and void checks are transferred in full from the Pre-Time Card Entry to Time Card Entry based on the first line of pre-time card. Therefore, if selecting to transfer based Job if the first line of the pre-time card is for the designated job, the manual (or void) check will be transferred, even if it includes other jobs on later pre-time card lines. Likewise, if Batch selection is specified, transfer for manual and void checks will be determined based on the file batch code of the first line.

- For [Time Card Approval Workflow](/en/spectrum/spectrum/tools/workflow/workflow-definition-field-descriptions/time-card-approval-workflow-definition) users, the update to transfer pre-time cards to the pay cycle will SKIP all pre-time cards that are still in open Workflows (that is, 'unapproved'), unless performed by an Override Operator.

- For prevailing wage jobs with non-stated fringe, the standard pay rate will include the non-stated fringe and the employee rate will be adjusted automatically.

The transaction update has two steps. Initially, a transaction/report register is printed and checked for accuracy. This should be saved as a permanent source document. After the report has printed, a second screen will appear that identifies which modules will be updated with this function and will prompt for affirmation if the update is to be completed. Images associated with updated time cards will also be transferred.
