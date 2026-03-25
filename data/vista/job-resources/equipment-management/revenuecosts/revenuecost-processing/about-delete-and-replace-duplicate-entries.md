---
title: "About Delete and Replace Duplicate Entries | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-delete-and-replace-duplicate-entries"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-delete-and-replace-duplicate-entries"
---

# About Delete and Replace Duplicate Entries

To prevent duplicate billings, it is suggested that you not
 run this program more than once for any given billing period.
However, if you need to run this program multiple
 times in the same billing period, check the Delete and Replace Duplicate Entries
 box to prevent doubling entries.
When this option is checked, the system runs
 a check for any existing entries with the same batch month, batch, equipment, day, job,
 and revenue code. If any duplicate entries are found, they are deleted and replaced with
 the new entries. The system also checks for any usage batches posted in the same day and
 if found, checks for entries with the same equipment, day, job, and revenue code. If a
 matching entry is found, it is added to the batch and marked for deletion (i.e. the
 Action flag is set to ‘Delete’). New entries are added and processed as normal.
