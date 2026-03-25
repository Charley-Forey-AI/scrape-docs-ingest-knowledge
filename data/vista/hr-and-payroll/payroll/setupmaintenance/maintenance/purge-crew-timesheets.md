---
title: "Purge Crew Timesheets | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-crew-timesheets"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-crew-timesheets"
---

# Purge Crew Timesheets

You can use the Crew Timesheets tab in PR Purge to purge posted crew timesheets.
You can restrict purging by job, crew, and/or timecard date. Timesheets must have a status of "send complete" in order to be eligible for purge.
When purging with this tab, the system uses a view of PRRH and optional restrictions on JC company number, job, crew, and timecard date to delete entries in all of the crew timesheet related database tables (bPRRE, bPRRO, bPRRN, bPRRQ, and bPRRH).
The following instructions detail how to purge crew timesheets.

1. In PR Purge, select the Crew Timesheets tab.

1. Check the Purge Posted
 Crew Timecard Timesheets box. The system enables the Restrict by
 Job, Restrict by Crew, and
 Restrict by Timecard Date fields.

1. If you want to purge by
 a specific job, check the Restrict by Job box. The
 system enables the JC Co and Job
 fields.

1. If purging by a specific
 job, enter the company and job number in the JC
 Co and Job fields. Press F4
 from either field for a list of companies or jobs.

1. If you want to purge by
 a specific crew, check the Restrict by Crew box. The
 system enables the Crew field.

1. If purging by a specific
 crew, enter the number in the Crew field. Press F4
 for a list of crews.

1. If you want to purge
 based on timecard date, check the Restrict by Timecard Date
 box. The system enables the Through Timecard Date field.


1. Enter the month/year
 that the system should purge through in the Through Timecard Date field.
 Only timesheets posted on or before the date and meeting all other criteria will
 be purged.

1. Click Purge. The system displays a confirmation message.

1. Click Yes
 to purge crew timesheets. The system removes all timesheets that meet the
 specified criteria.

Related information

- [About the PR Purge Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-the-pr-purge-form)
