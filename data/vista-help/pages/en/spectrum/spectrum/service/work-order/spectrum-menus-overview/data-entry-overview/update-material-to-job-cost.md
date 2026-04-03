---
title: "Update Material to Job Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-material-to-job-cost"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/update-material-to-job-cost"
---

# Update Material to Job Cost

You can update the work order materials for
 jobs.
This update will transfer material data entered through the [Work Order Materials for Job Work Orders](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/data-entry-overview/work-order-materials/work-order-materials-for-job-work-orders) screen to the Job
 Cost module, creating entries in the JC Transaction File.
Before running this update, two things should occur:

- The materials edit list should be carefully checked for accuracy


- J/C transactions should be updated in the Job Cost module

If the 'Post material transactions as inventory type (IC)' option is
 selected on Work Order Installation, job cost transaction entries will be posted as an IC
 transaction type. When the job is time + materials (T+M), it will post to the T+M job for
 billing.
Running this update for non-job work orders has no effect; nothing will
 be updated to Job Cost Transaction Entry. After this update has transferred materials data
 to Job Cost, those transactions should be updated.
Note: This screen is only available if the 'Allow job work orders?'
 checkbox is selected in Work Order Installation.
