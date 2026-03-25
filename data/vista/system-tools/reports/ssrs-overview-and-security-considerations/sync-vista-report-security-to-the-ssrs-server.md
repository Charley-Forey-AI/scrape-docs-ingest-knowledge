---
title: "Sync Vista Report Security to the SSRS Server | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/sync-vista-report-security-to-the-ssrs-server"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/sync-vista-report-security-to-the-ssrs-server"
---

# Sync Vista Report Security to the SSRS Server

Ensure report security settings you have chosen for the Vista application are assigned to the SSRS report server.
Back up your ReportServer database in case you decide to revert to the prior state.
Take these steps to remove and replace security settings on the SSRS server with those in Vista.

When the Sync Security checkbox on the Info tab of the RP RS Server form is selected, Vista syncs SSRS report security automatically, but only when applying report security in the VA Report Security form or when running a program that updates report security.
Since there are certain reasons this checkbox might not always have been checked, security settings in Vista for one or or more SSRS reports may be out of sync with those on the SSRS report server.

To push Vista report security settings to the SSRS report server:

1. Open the RP RS Server form.The grid lists the SSRS Report Servers that have been set up using the Viewpoint SSRS Reports installer.

1. In the Server Name column, select the report server in question.

1. If not already selected, select the Sync Security checkbox and click Save.

1. In the form menu, select Tools > SSRS Security. The Sync SSRS Security form opens, displaying your organization's SSRS reports in the grid.

1. Make your selections using the checkboxes and the All and None buttons.

1. Click Sync Security.

The Vista report security settings for each selected SSRS report are applied to those in the SSRS report server.

Related information

- [Sync Security](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/rp-rs-server-form/field-definitions-rp-rs-server-form#ID-0003deae--en)
