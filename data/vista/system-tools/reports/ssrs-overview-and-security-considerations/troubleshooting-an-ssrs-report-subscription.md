---
title: "Troubleshooting an SSRS Report Subscription | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/troubleshooting-an-ssrs-report-subscription"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/troubleshooting-an-ssrs-report-subscription"
---

# Troubleshooting an SSRS Report Subscription

A report subscription allows you to set up an SSRS report to be emailed to a list of users at a regularly scheduled time. However, occasionally a subscription setup needs troubleshooting.
If recipients are not receiving the report at the scheduled time, there may be an error or an email address may not be valid.

1. In RP Report Titles,
 click the Subscribe  button on the Info
 tab. This will open the Report Manager.

1. In the Report Manager,
 examine the Status field, and then fix
 any errors thrown when the report was generated and sent.

1. If a message displays
 saying that the email address is not valid, this means that the
 rsreportserver.config file on the server is not set up correctly. Make a backup
 copy of this file.

1. Change the <SendEmailToUserAlias> parameter to False.<SendEmailToUserAlias>False</SendEmailToUserAlias>

1. Try the report
 subscription again. For more information, see [Subscribing To an
 SSRS Report](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/subscribe-to-an-ssrs-report).

Related information

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)
