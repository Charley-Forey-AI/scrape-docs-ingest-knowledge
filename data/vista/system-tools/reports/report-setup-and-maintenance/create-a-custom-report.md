---
title: "Create a Custom Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-a-custom-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/create-a-custom-report"
---

# Create a Custom Report

Creating a custom report begins by copying an existing Crystal or SSRS report.
You must know which existing report you want to use as your basis for the new report.
When you copy any report, the result is a custom report.Note: These steps work to copy a report within the same server only. If you are using dual SSRS Report Servers and want to copy an SSRS report from one server to the other, instead see [Copy an SSRS Report to a Different Server](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/copy-an-ssrs-report-to-a-different-server).
 not .
To make a custom report by copying a report within the same server:

1. Open the [RP Report Copy](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form) form.You can open this form using the Programs folder in the RP module, or you can click the Copy Report button on the [RP Report Titles](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form) form.

1. Use the Report ID field in the Source Report section to select the report that you would like to copy.Standard SSRS reports display only if the Business Intelligence module is turned on.
The New Report section in the lower portion of the form populates with information from the report you selected, and the next available number populates in the Report ID field.

1. Enter the title, location, and file name of the new report.The default values appearing in these fields also come from the source report.

1. Select the Show on Menu checkbox if the new report should display in the Reports folder of the assigned modules. For additional details, see [Show On Menu](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-copy-form/field-definitions-rp-report-copy-form#ID-0003d859--en).

1. (Optional) If you want to change the icon associated with the report, click the Change Icon button.This icon displays next to the report title in the Reports folders in Vista. You can change the icon associated with custom reports only.

1. Click Copy.

Your new custom report is stored alongside others of the same kind.

- Crystal Reports are stored in the RP Report Titles form.

- SSRS reports are stored on the SSRS Report Server, and the new
 report opens in Report Builder in your
 default browser.

Related information

- [Link Report Files to Vista](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/link-report-files-to-vista)

- [Reports](/en/vista/vista/system-tools/reports)

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [Crystal Reports Overview](/en/vista/vista/system-tools/reports/crystal-reports-overview)
