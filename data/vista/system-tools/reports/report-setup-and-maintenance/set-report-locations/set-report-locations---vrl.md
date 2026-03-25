---
title: "Set Report Locations - VRL | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations/set-report-locations---vrl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations/set-report-locations---vrl"
---

# Set Report Locations - VRL

Use the RP Report Locations form to set up report locations. Each module's reports are grouped into a single location, and this location is where the application goes to retrieve the report at run time. Each report is pointed to a single RP Report Location.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.
This topic only applies to you if your deployment method is either VRL on-premises or VRL Cloud. If your deployment method is any other, please see [Set Report Locations](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/set-report-locations).

To set a report location in the RP Report Locations form:

1. In the Location field, enter a name for the new report location.

1. In the Location Type field, select either a network or web location type for this report.

1. Your deployment method dictates what you should enter in the Report Path field:Deployment methodRequired Action
LAN *and*VRL on-premisesThe directory you enter must be a subdirectory of the directory defined in the API Settings tab of the Viewpoint Configuration form located on your app server. If you don't know what's been defined, ask your system administrator.
VRL Cloud Any entry is valid.
VRL on-premises onlyAny entry is valid.

1. For locations that point to an SSRS Report Server, in the RS Server Name field, press F4 to select the SSRS Report Server.

Once you have defined your report locations, assign them to reports using the RP Report Titles form.
