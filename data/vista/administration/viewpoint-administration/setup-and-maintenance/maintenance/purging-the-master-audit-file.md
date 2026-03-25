---
title: "Purging the Master Audit File | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/purging-the-master-audit-file"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/purging-the-master-audit-file"
---

# Purging the Master Audit File

Each time a change is made to a file or record in many forms,
 these changes are tracked in the Master Audit file (HQMA) if set up to do so in the
 Audit Options selections in a module’s Company Parameters or Company Setup forms.
Note: Not all modules have a Company Parameters or Company Setup form, and not all provide audit options.
You can periodically purge these records using the
 VA Purge Audit form.

1. Open the VA Purge Audit
 form.

1. Select one of the following options:

- All Tables – Purges all records in the Master Audit file through a specified date.

- All Tables in a Select Module – Purges all records in the Master Audit for a specific module, through a specific date.

- A Select Table – Purges all records for a specific table (e.g. APVM) through a specified date.

1. Enter a date in the
 Delete
 Entries Created On or Before field, or select a date using the
 Calendar button.

1. Click Purge. A
 message displays telling you how many records will be purged and asks if you want to
 continue.

1. Click Yes to
 continue, or No to cancel the purge.

Related information

- [About the VA Purge Audit Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-va-purge-audit-form)
