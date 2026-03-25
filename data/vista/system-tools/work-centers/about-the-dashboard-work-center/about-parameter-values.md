---
title: "About Parameter Values | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center/about-parameter-values"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-centers/about-the-dashboard-work-center/about-parameter-values"
---

# About Parameter Values

View the available parameter values for the Value field on
 either the Report or Grid sections of the Dashboard Work Center.
Note: If you specify one of the parameter values below, and you
 have not opened a form to activate a parameter, the system displays an error stating that
 the parameter is missing a value. For example, if you use the %Job
 parameter, but have not yet opened a form to activate the current job, the system is unable
 to determine what the current job is. If you open a form and then refresh the My Viewpoint
 report, the parameter displays the pertinent information.
The parameter values given must be used exactly as shown. For example, for the Active Company parameter, you must use %C. If you attempt to use %Co - or anything else - the dashboard or report won't filter as you might expect. Default Type
 Value
 Definition

Fixed Value
 Specify a value. For example if
 you have a Y/N input, you might enter Y as the default value.
Current Date (+/-)%DTo set a different value, add
 or subtract from the current date. For example, %D+1 is
 the current date plus one.
Current Month (+/-)%MTo set a different value, add
 or subtract from the current month. For example, %M+1 is
 the current month plus one.
Active Company%CThe currently selected
 company.
Active Project
 %ProjectThe last company selected in
 the PM Projects form.
Active Job%JobThe last job selected in the JC
 Jobs form.
Active Contract%ContractThe last contract selected in
 the JC Contracts or PM Contracts forms.
Active PR Group%PR GroupThe last PR Group selected in
 the PR Pay Period Control or PR Timecard Entry forms.
Active PR End Date%PR End DateThe last PR End Date selected
 in the PR Pay Period Control or PR Timecard Entry forms.
Active JB Prog Bill Mth%JB Prog MthThe last progress billing month
 selected in the JB Progress Billing form.
Active JB Prog Bill #%JB Prog BillThe last progress billing
 number selected in the JB Progress Billing form.
Active JB TM Bill Mth%JB TM MthThe last T&M billing month
 selected in the JB T&M Bill Edit form.
Active JB TM Bill #%JB TM BillThe last T&M billing number
 selected in the JB T&M Bill Edit form.
