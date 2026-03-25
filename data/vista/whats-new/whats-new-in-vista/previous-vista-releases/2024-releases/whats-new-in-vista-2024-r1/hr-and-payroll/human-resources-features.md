---
title: "Human Resources Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/hr-and-payroll/human-resources-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/hr-and-payroll/human-resources-features"
---

# Human Resources Features

Vista 2024 R1 delivers on user-requested Human Resources enhancements, fixes, and other improvements.

## Support Electronic OSHA 300 / 300A / 301 Reporting

Beginning January 1, 2024, the Department of Labor requires establishments in certain industries with more than 100 employees to electronically submit injury and illness information to the Occupational Safety and Health Administration (OSHA).
In accordance with these requirements, the following changes have been made:
HR AccidentsA new Case Number field was added to the HR Accidents form, More Info tab. This field is only enabled for OSHA accidents (those with a Type of OSHA) and is used to record the OSHA case number. This number is then used to populate the Case Number field on the HR OSHA Form 300 and HR OSHA Form 301 reports.
When you enter a new OSHA accident record, the system defaults the next available number based on the greatest case number in use for the HR company and year. For example, if the greatest case number in use is 100 (for the current HR company and year), the next new record entered defaults a case number of 101. You can override the defaulted value as needed with any value between 1 and 9999; however, entry is required so you cannot leave the field blank.
Note: When defaulting a case number value for
 new OSHA records, the system looks at both manual and
 system-assigned numbers to determine the greatest case number in
 use.

Once a new year begins, the system restarts auto-numbering with "1".
Note: Upon installation of this release, the system automatically assigns a Case Number to each existing OSHA accident record per company/year, beginning with a case number of "1". Case numbers are assigned in sequential order based on the Accident Date specified for each record.

HR OSHA Cases Export File / HR OSHA Summary Export FileThe HR OSHA Cases Export File and HR OSHA Summary Export File forms were added to enable generating export files of injury/illness information for electronic submission to the Occupational Safety and Health Administration (OSHA).
The export file generated via the HR OSHA Cases Export File form includes the same information that you normally report using the OSHA 300 and OSHA 301 reports.
 The export file generated via the HR OSHA Summary Export File form includes the same information that you normally report using the OSHA 300 and OSHA 300A reports.
If your company is required to electronically submit injury/illness information to OSHA, you must generate both of these files.
For more information, see [Export OSHA Injury / Illness Reports](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/accidents/export-osha-injury--illness-reports).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
