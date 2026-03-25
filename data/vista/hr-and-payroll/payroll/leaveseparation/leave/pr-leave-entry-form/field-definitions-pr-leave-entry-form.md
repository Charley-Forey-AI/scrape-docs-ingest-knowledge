---
title: "Field Definitions: PR Leave Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form/field-definitions-pr-leave-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-leave-entry-form/field-definitions-pr-leave-entry-form"
---

# Field Definitions: PR Leave Entry Form

The following is a list of field descriptions for the PR
 Leave Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

The Seq # field on the PR Leave Entry form.
Enter N, NEW, or + to create a new entry or enter the batch sequence number of an existing entry you wish to display.

##  Action

The Action field on the PR Leave Entry form.
When adding new entries, this field defaults to A-Add and is not accessible. If this is an existing transaction, specify the action for this entry.

- C-Change. Use this action to make changes to processed transactions.

- D-Delete. Use this action to delete the transaction from all files in PR. The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  Employee

The Employee field on the PR Leave Entry form.
Enter the employee for this leave entry. Must be a valid, active employee. Press F4 to select from a list of valid, active employees.

##  Leave Code

The Leave Code field on the PR Leave Entry form.
Enter an active leave code that has been set up and assigned to the employee. When validating the employee/leave code, the PR Leave Codes form locks so that no one else may post to this combination of employee/leave code; this guarantees accurate balance updates. Multiple entries within the same batch are allowed.
 The specified leave code must have a limit setup in PR Leave Codes for generating leave entries with this form.
Note: The system allows initializing only active leave codes. If you select an inactive leave code in this field, a warning displays and you must enter an active code before proceeding.

##  Date

The Date field on the PR Leave Entry form.
Enter the date on which the accrual or usage occurred.
This date posts with the Leave transaction and is compared to the Last Reset Dates. If the transaction date is equal to or earlier than the Last Reset Date, then current balances do not update. A warning is displayed if this date is earlier than the Employee's Eligible Date for the leave code.

## Type

The Type field on the PR Leave Entry form.
Select the appropriate leave type for this leave entry:

- Usage – Select this type to enter leave time that has already been taken.

- Accrual – Select this type to enter leave time that will be added to the available time for this leave code.

- Reset – This type is automatically assigned to leave reset transactions and leave reset 'reversal' transactions; you cannot assign this type to manual entries.

##  Amount

The Amount field on the PR Leave Entry form.
Enter the number of units accrued or used (depending on the Type you selected).
 You can enter negative values if needed, but the sign is reversed if the Type is Usage. If the entry is an accrual, then only amounts up to the limits of the Accrual Accumulators and Available Balance are allowed.

##  Description

The Description field on the PR Leave Entry form.
Enter a 30-character description for this transaction. Initially defaults the description assigned to this accrual (fixed, usage, or rate-based) in PR Auto Leave/Accrual Usage.
