---
title: "Overriding Report Parameter Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/overriding-report-parameter-defaults"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/overriding-report-parameter-defaults"
---

# Overriding Report Parameter Defaults

Use the RP Reports by Form form to override report parameter
 default values.

Many of the standard reports are set up with default parameter values. For example, the Company parameter on many reports will default the active company, and date parameters will default the current date (today’s date). If you plan to run reports from within their related forms, you can set them up to default parameter values from the current record using RP Reports by Form.
For example, say you want to run JC Contract Status
 Report from within JC Contracts. You will first need to assign the JC Contract
 Status report to the JC Contracts form via RP Report Titles. Then, using RP Reports
 by Form (Parameter Defaults tab), select the “?BegContract” parameter and set the
 Override Default Type to ‘4-Field Value’ and the Override Default to ‘%FI0’ (where 0
 is the field’s sequence number). When you run the report from JC Contracts, the
 Beginning and Ending Contract parameters will default the contract on which you
 currently have focus.

Related information

- [About the RP Reports by Form Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-reports-by-form-form)

- [About the RP Report Launcher Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-launcher-form)

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

- [RP Report Export Options Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-report-export-options-form)
