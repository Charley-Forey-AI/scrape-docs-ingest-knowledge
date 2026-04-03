---
title: "Master Job Setup - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/master-job-setup/master-job-setup---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/master-job-setup/master-job-setup---field-descriptions"
---

# Master Job Setup - Field Descriptions

Use the table below for reference when completing fields on this screen.
Field
Description

New
Click this button to open the [New Job](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-properties/new-job) window to add the initial elements of a new job and contract. The master job will default in context. The software will attempt to sequentially number the new sub-job by following the numerical pattern of any previous sub-jobs. The user can change this as needed and the software will attempt to offer a new sub-job code in the future.

Job code
Enter a master job code in this field.

Modify
Click this button to open the Master Job - T+M Billings window to specify whether to submit time + material billings from the master job.

Add Job
Click this button to add a sub-job to the selected master job.

- If the specified job number does not exist, the system will prompt you to open the New Job window to define a new job.

- If the specified job is the same as the master job, already assigned to another master job, has sub-jobs of its own, does not have the same phase mask length as the master job, or has a status of 'Active' or 'Inactive' and the master job has a status of 'Complete', the job will not be allowed.

- If the operator does not have access to the specified job, or if cost centers are enabled and the operator does not have access to the cost center for the specified job, the job will not be allowed.
Note: This button will be unavailable if the job specified in the heading is a sub-job.

Remove
Click this button to remove the master job number from the selected sub-job, thus removing the master-sub relationship.
