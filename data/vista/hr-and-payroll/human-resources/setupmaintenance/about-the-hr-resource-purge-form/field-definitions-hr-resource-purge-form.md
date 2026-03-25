---
title: "Field Definitions: HR Resource Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form/field-definitions-hr-resource-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form/field-definitions-hr-resource-purge-form"
---

# Field Definitions: HR Resource Purge Form

The following is a list of field descriptions for the HR
 Resource Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Specific Resource

The Specific Resource checkbox in the HR Resource Purge form.
Select this checkbox (default) to purge records for one terminated resource only. When selected, the Resource # field is enabled.
Clear this checkbox to purge all terminated resource records. Clearing this checkbox disables the Resource # field and enables the Through Month field.
For information about record purge eligibility, see [About the HR Resource Purge Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form).

##  Resource #

The Resource # field on the HR Resource Purge form.
 This field is enabled only when the Specific Resource checkbox is selected.
Specify the resource (employee/applicant) you
 wish to purge from HR. All records for this resource will be purged from the HR system,
 with the exception of accident detail. If accident detail exists for this resource, then
 all detail except the accident detail and the resource’s record in HR Resources will be
 purged. You will need to manually purge the accident detail before you can purge the
 resource.

## Through Month

The Through Month field on the HR Resource Purge form
Enter the month through which to purge resource records.
All records dated before and including the month you select here are included in the purge process. You must select a month at least 7 years prior to the current month.
For additional information about record purge eligibility, see [About the HR Resource Purge Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-resource-purge-form).
