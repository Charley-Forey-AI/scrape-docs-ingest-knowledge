---
title: "Purge T4s (CA) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-t4s-ca"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-t4s-ca"
---

# Purge T4s (CA)

(Canada only) Use the T4/ROE tab on the PR Purge form to purge federal and provincial T4 records for a given tax year.
Note: The T4/ROE tab displays only if the default country for the
 company you are processing in has been set to Canada in the Default
 Country field, HQ Company Setup form.

This action purges the associated records from the PR Canada T4 and PR Canada T4 Employees forms. The records are from these database tables:

- bPRCAEmployer

- bPRCAEmployerItems

- bPRCAEmployerCodes

- bPRCAEmployerProvince

- bPRCAEmployees

- bPRCAEmployeeCodes

- bPRCAEmployeeItems

- bPRCAEmployeeProvince

To purge T4 data:

1. In the PRPurge form, select the
 T4/ROE tab.

1. Select the Purge T4
 Data checkbox.The system enables the Tax
 Year field.

1. In the Tax
 Year field, enter the year for purging T4 records. Press
 F4 to select from a list of valid years.

1. Click Purge.The system displays a confirmation message.

1. Click Yes
 to purge T4 records.

The system purges all T4 records meeting the specified
 criteria.

Related tasks

- [Purge W-2s (US)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-w-2s-us)

- [Purge ATO Data (AU)](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/purge-ato-data-au)

Related information

- [About the PR Purge Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/maintenance/about-the-pr-purge-form)
