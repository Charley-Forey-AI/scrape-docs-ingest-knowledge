---
title: "Master Job Setup - Rules | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/master-job-setup/master-job-setup---rules"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/master-job-setup/master-job-setup---rules"
---

# Master Job Setup - Rules

Learn about the Master Job Setup rules.

- A job can be a master job or a sub-job, but not both. Only one layer of master + sub-jobs is supported. This means that a sub-job cannot be a sub of another sub-job, and a master job cannot be a sub-job of another master job.

- To facilitate rolling up values, sub-jobs must use the same phase structure as the master.

- Additional job status protection is available for master and sub-jobs. The master cannot be set to 'Complete' while any of its sub-jobs are still open. Likewise, sub-jobs cannot be reopened until its master job is also reopened.

- To assist in setting up new phases on sub-jobs, the system automatically creates the phase on the sub-job when it already exists on the master job. Not only does this make setting up sub-jobs easier, reports and inquiries only have the phases actually used instead of copying the complete master job list. The status of the phase on the master job must be 'Active' or 'Inactive'.

- Sub-jobs billed out using the T+M module automatically use the master job's billing rates.

- Sub-jobs use the master job's equipment charge rates defined on the Job Specific Equipment Charge Rates page.
