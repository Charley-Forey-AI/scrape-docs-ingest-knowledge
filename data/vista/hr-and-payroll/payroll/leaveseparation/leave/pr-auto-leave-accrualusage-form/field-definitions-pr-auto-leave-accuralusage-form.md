---
title: "Field Definitions: PR Auto Leave AccuralUsage Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-auto-leave-accrualusage-form/field-definitions-pr-auto-leave-accuralusage-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/leaveseparation/leave/pr-auto-leave-accrualusage-form/field-definitions-pr-auto-leave-accuralusage-form"
---

# Field Definitions: PR Auto Leave AccuralUsage Form

The following is a list of field descriptions for the PR Auto
 Leave AccuralUsage form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Update Fixed Accruals

 Check this box to update fixed accruals (i.e. leave codes that accrue as a fixed amount on some regular basis).
 Leave this box unchecked if not processing fixed accruals.

##  Accrual Date

 Enabled only if Update Fixed Accruals is checked (above).
 Enter the date to be used as the 'actual date' for posted accruals. This date determines employee eligibility and whether Accrual Accumulators and Available Balance are updated. If this date is prior to an employee's Eligible Date, then accrual entry is not created. If this date is prior or equal to the Last Reset Date on an Accrual Accumulator or Available Balance, then the current amount does not update.

## Leave Code: All or Selected

The Leave Code: All or Selected field in PR Auto Leave Accrual/Usage form.
Enabled only if Update Fixed Accruals is checked (above).

- All – Select this option to process all fixed accrual leave codes.

- Selected – Select this option to process a selected fixed accrual leave code (indicated to the right).

Note: The system allows initializing only active leave codes. If you elect to initialize a single leave code and the leave code is inactive, a warning displays and you must enter an active code before proceeding. If you elect to initialize all leave codes, the initialization process skips all inactive leave codes.

##  Leave Code

The Leave Code field on the PR Auto Leave Accrual/Usage form.
 Enabled only if updating fixed accruals and you elect to update a specific leave code.

 Specify the fixed accrual leave code for which to update accruals. Must be an active leave code (that is, the Active checkbox must be selected for the leave code in PR Leave Codes).

## Frequency: All or Selected

Enabled only if Update Fixed Accruals is checked (above).

- All – Select this option to include all frequencies when updating accruals for the specified leave codes.

- Selected – Select this option to only update accruals for leave codes assigned the frequency code indicated to the right.

##  Frequency

 Enabled only if updating fixed accruals and you elect to update a specific frequency.
 Enter a valid frequency code. Only leave codes with the specified frequency are included when updating accruals.

##  Fixed Accruals: Description

Enter the description for fixed accruals, up to 30 characters. The description entered here defaults for each fixed accrual entry in PR Leave Entry and updates to the PRLH (Leave History) table when the batch is posted. Description may be overridden by sequence in PR Leave Entry.

## Delete Any Existing Accruals Posted with this Leave Code & Date

Enabled only if updating fixed accruals.
Check this box to delete existing accrual posted with this leave code and date. All accrual entries already posted on this date for the specified leave code(s) are deleted and balances adjusted. Use this option if you need to rerun a fixed accrual update because of an error or changes in accrual values.
Leave this box unchecked if you do not want existing accrual entries posted for this leave code and date deleted. All existing entries remain intact (in PR Leave History).

##  Use Pay Pd Earnings to Update Leave Usage...

 Check this box to update leave usage and rate-based accruals using earnings posted in one or more pay periods (open or closed).
 Leave this box unchecked if not processing leave usage and rate-based accruals.

##  PR Group

 Enabled only if updating leave usage and rate-based accruals.
 Enter the PR group for which to update leave usage and rate-based accruals.

## Beginning/Ending PR Ending Date

Enabled only if updating leave usage and rate-based accruals.
Enter the beginning and ending date in a range of PR ending dates that you want to process. Pay periods within this range must be valid for the batch month. For split-month pay periods (within the date range), the beginning or ending month of the pay period must be equal to the batch month (the F4 lookup includes pay periods where either the first or second month of the pay period matches the batch month).
If accrual and usage entries have already been posted for any pay period within the specified range (e.g. you are rerunning the update due to an error or changes in accrual values), make sure you check the 'Delete Any Existing Entries..' option (below) to delete existing entries and adjust balances. If you do not check the 'delete' option, the following message displays when you click the Update button:
"Leave has already been posted for one or more of these pay periods yet delete option was not selected. This could result in duplicate postings. Continue?"
Note: This does not apply to posted entries existing in a split-month pay period where the posted month was other than the current batch month. In this case, the update will result in duplicate entries, as the 'delete' option has no affect on entries in another month.

##  Usage and Rate Based Accruals: Description

Enter the description for usage and rate-based accruals, up to 30 characters. Initially defaults a description based on the specified payroll group and pay period range (e.g. Grp:# Pds:MM/DD/YY-MM/DD/YY). The description defaults for each usage or rate-based accrual entry in PR Leave Entry. You may override this description by sequence in PR Leave Entry.

## Delete Any Existing Entries Posted From This Range of Pay Pds

Check this box to delete all accrual and usage entries in the specified range of posted pay periods. Entries will be deleted and balances adjusted. Manually posted entries within this range of dates are not affected. Use this option to rerun the update because of an error or changes to accrual values.
Leave this box unchecked if you do not want existing accrual/usage entries deleted. Accrual/usage entries existing for any pay period in the specified range are left intact (in PR Leave History), which could result in duplicate postings. Leaving this option unchecked when accrual/usage entries exist causes a warning to display when the Update button is clicked. You will have the option to continue or cancel the process.
Note: Checking or unchecking this option does not have an affect on existing entries from a split-month pay period (in the specified range) where the posted month is other than the current batch month. Processing usage and accruals under these circumstances always results in duplicate postings.
