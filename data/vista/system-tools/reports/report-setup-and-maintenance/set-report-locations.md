---
title: "Set Report Locations | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations"
---

# Set Report Locations

Use the RP Report Locations form to set up report locations. Each module's reports are grouped into a single location, and this location is where the Vista application goes to retrieve the report at run time.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.
Before you proceed with the steps below, first please review the information in the [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form) topic.

To set a report location:

1. Do not proceed if your deployment method is either VRL on-premises or VRL Cloud. This topic does not apply to you. Please see [Set Report Locations - VRL](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations/set-report-locations---vrl).

1. In the Location field, enter a report location. You must define a location for each directory or subdirectory.

1. In the Location Type field, select either a network or web location type for this report.

1. In the Report Path field, enter the path. This differs depending on if you are creating a Cystal Reports or SSRS report location, and on which option you selected in the Location Type field. See the [Report Path](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form/field-definitions-rp-report-locations-form#ID-0003d94b--en) field help for important information.

1.  For locations that
 point to an SSRS Report Server, in the RS Server Name field, press F4
 to select the SSRS Report Server.

Once you have defined your
 report locations, assign them to reports using the RP Report Titles form. Each report is pointed to a single RP Report Location.

Related information

- [About the RP Report Locations Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-locations-form)
