---
title: "About the HR Resource Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form"
---

# About the HR Resource Purge Form

Use this program to purge a resource from HR.
When purging resource records, you must purge records that are at least 7 years old. Records that meet purge eligibility for that resource are deleted from the HR system.

Records that are eligible to be purged meet these criteria:

-

the resource must have a date in the Term Date field in the HR Resource Master form (Payroll Info tab)

-
if the resource has a corresponding record in the Payroll Employees form, the Termination Date field (Add'l Info tab) must have a date

-
both dates must be prior to the date specified in the Through Month field in this form.

When a resource is selected, all records for that resource are deleted from the HR system, with the exception of accident detail. If accident detail exists for the resource, the system purges all records except the accident detail and the resource’s record in HR Resources. You must manually delete the accident detail (in HR Accidents) before you can delete the resource (either using this program or manually in HR Resources).
