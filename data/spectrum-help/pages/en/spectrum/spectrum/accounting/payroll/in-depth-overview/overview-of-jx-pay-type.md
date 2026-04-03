---
title: "Overview of JX Pay Type | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/in-depth-overview/overview-of-jx-pay-type"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/in-depth-overview/overview-of-jx-pay-type"
---

# Overview of JX Pay Type

JX pay types, or non-paying job-only adjustments, are
 usually used when you want to record hours worked as they relate to a job without affecting
 the payroll amount.
For example, if a salaried employee put in 60 hours in a given week while working on a job,
 but her payroll is set for 40 hours, she could record the additional 20 hours as a JX pay
 type and this would allow these hours to be transferred to the job costs once the payroll
 has been updated. In order for the JX hours to be posted to the job, you must run the Job
 Cost Transaction Report and Update.
JX Pay Type as it applies to Time Card Entry:
The purpose of the JX pay type is as a front-end to auto-create job cost transactions so that you can enter the information for the job in one place instead of two. The JX lines are not intended to be posted in the payroll update; instead, they are posted to history when the job cost transactions you create are posted. Therefore, no reports (for example, job distribution, labor distribution, and so forth) show these JX. You receive a hard copy of transactions to the job when you run the job cost transaction listing and update. The costs for JX also post to G/L at this point, not during Payroll Update. The payroll update is intended to create the unposted job cost transactions in Job Cost Transaction Entry. You must then use Job Cost Transaction Report and Update to complete the process.
JX Pay Type as it relates to Payroll Update:
JX pay type transactions recorded in Time Card Entry will result in unposted Job Cost transaction entries recorded in Job Cost Transaction Entry as part of this update. It is recommended that those transactions be updated using the Job Cost Transaction Report and Update, then the Job Cost G/L Detail Report and Update.
