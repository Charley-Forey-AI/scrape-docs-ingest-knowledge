---
title: "Copy an SSRS Report to a Different Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/business-intelligence/ssrs-reports/copy-an-ssrs-report-to-a-different-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/business-intelligence/ssrs-reports/copy-an-ssrs-report-to-a-different-server"
---

# Copy an SSRS Report to a Different Server

Copy a report from one SSRS
 Report Server to another.
You need access to both SSRS Report Servers.

When you copy any report, the outcome is a custom report.Note: These steps work to copy an SSRS report from one server to the other.If instead you want to save the copy
 on the same SSRS Report Server as the original, see [Create a Custom Report](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-a-custom-report).

To copy a report from one server to another:

1. Open the RP Report Copy
 form.

1. Select the report that
 you would like to copy in the Report ID field.

1. Use the Location field to copy the report to the /VCS/Custom folder on
 the same SSRS server.

1. Click the Copy button to copy the report. This only copies the report to
 the same SSRS server, but it copies all of the information associated with the
 report so that you do not have to manually enter it.

1. Open the SSRS Report
 Manager on the server where you copied the report - generally the Report Manager
 URL is <server_name>/Reports.

1. Locate the report in the
 VCS/Custom folder.

1. Open the report in
 Report Builder. To do this click the drop down arrow next to the report name and
 select Edit in Report Builder.

1. Once the report opens in
 Report Builder, select Save As, and then save the
 report in the VCS/Custom folder on the SSRS Report Server that you would like to
 copy the report to.

1. Open the SSRS Report
 Manager on the server where you just saved the report and verify that it saved
 correctly.

1. Open the RP Report
 Titles form.

1. Open the report that you
 created and change the Location field to the new
 server where you saved the report. To see the SSRS Report Server associated with
 a location, press F5 in this field and refer to
 the RS
 Server Name field on the form that displays.

1. Use the VA Report
 Security form to set up security on the copied report.

Related information

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [About the RP Report Copy Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form)

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
