---
title: "About the JC Detail Roll-up Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-detail-roll-up-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-processing/about-the-jc-detail-roll-up-form"
---

# About the JC Detail Roll-up Form

Use this form to roll up contract revenue and/or job costs based on parameters defined in JC Detail Roll-Up Codes.
Rolling up revenue and/or job costs allows you to control the amount of disk space the system uses to store contract and/or job data. If you elect to use this feature, you will typically want to run this program after you have run all necessary monthly reports and have closed the month in all subledgers.
Note: Roll-ups summarize related detail entries into a single record and are permanent; they cannot be reversed. Therefore, it is important that you only run this program when you no longer need the current level of detail at which your contract revenue and/or job cost data is stored.

- GL Postings - Once you have performed a roll-up, the GL accounts for each detail line item are no longer itemized and can no longer be seen on any report. If you sometimes post costs to accounts other than those indicated in the department file, and you need a record of these entries so that you can make the proper adjustments when you close the job, make sure you run a report that prints out the GL accounts used before rolling up your detail.

- T&M Billings - The roll-up process performs some checks that prevent you from removing detail information needed by Job Billing. If you are using Job Billing and the detail being rolled up is related to a contract item flagged as a 'T&M' bill type, it will be skipped during the roll-up if it has not been fully processed in JB.
