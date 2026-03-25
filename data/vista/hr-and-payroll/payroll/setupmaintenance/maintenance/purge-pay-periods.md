---
title: "Purge Pay Periods | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-pay-periods"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-pay-periods"
---

# Purge Pay Periods

Use the Pay Periods tab on the PR Purge form to remove all closed and fully interfaced pay periods with ending dates equal to or earlier than the date you enter. You can do this for a single payroll group or for all payroll groups.
Database information removed with this tab includes the following through the payroll ending date that you specify:

- timecard detail (bPRTA, bPRTL, bPRTH)

- deleted timecard records (vPRTimeCardSafetyNet)

- processing detail and payment sequence information (bPRDS, bPRDT, bPRSQ, bPRPS, bPRAF, bPRHD, bPRPC)

- ledger distributions (bPRGL, bPRJC, bPREM, bPRER, bPRAP, bPRVP)

- insurance and craft report detail (bPRIA, bPRCA, bPRCX)

- arrears/payback history (vPRArrears)

- JC, EM, CM, AP, and GL interface data

1. In the PR Purge form, select the Pay Periods tab.

1. To purge by payroll group:

1. Select the Purge Pay
 Periods by Payroll Group checkbox.

1. In the PR
 Group field, enter the payroll group.

1. In the Through PR Ending Date field, enter a payroll ending
 date that is at least 3 years prior.
 The system will purge closed and fully interfaced pay periods equal to or
 earlier than this date.

1. To purge multiple payroll groups:

1. Select the Purge all PR Groups where PR End Dates are less than or equal to Through Date checkbox.

1. In the Through Date field, enter a date through which to purge pay periods.The system will purge closed and fully interfaced pay periods for groups where the payroll ending date is equal to or
 earlier than this date.

1. In the
 PR
 Arrears through date for manually entered records field, enter the through date. The
 system will purge all manually entered arrears/payback records that are equal to
 or earlier than this date. If you leave this field blank, the system will not
 purge any manually entered arrears/payback records. For more information on
 arrears/payback records, see [Manually Entering Arrears and Payback Records](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/employee-arrears-australia/manually-enter-arrears-and-payback-records).

1. Click Purge.The system displays a confirmation message.

1. Click Yes
 to purge accumulations.

The system purges all pay period records meeting the
 specified criteria.

Related information

- [About the PR Purge Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-the-pr-purge-form)
