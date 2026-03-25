---
title: "Subscribe to an SSRS Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/business-intelligence/ssrs-reports/subscribe-to-an-ssrs-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/business-intelligence/ssrs-reports/subscribe-to-an-ssrs-report"
---

# Subscribe to an SSRS Report

You can use report subscriptions to email SSRS reports to a list of users at a regularly scheduled time.
If this is your first time creating a report subscription, and particularly if this subscription's intent is to send reports to other users, Viewpoint recommends testing a subscription by setting one up, for example, to email a report 5 minutes in the future and verify that it works.
You must have security access to the report(s) you wish to set up a subscription for. Access is granted using the the VA Report Security form.

An example of a report subscription might be the Worst Performing Jobs report as a PDF, HTML, or Excel file to a list of specific users each Monday. To set up a report subscription:

1. Open the RP Report Titles form.

1. Locate and select any SSRS report.Standard SSRS reports display only if the Business Intelligence module is turned on.Tip: Sort or filter the Grid by the Application Type column to more easily choose from only SSRS reports.

1. On the Info tab, click the Subscribe  button.A login screen appears.

1. Enter your Vista credentials.The SSRS Report Manager opens and displays a folder named VCS.

1. Click to open the VCS folder and subsequent folders to navigate to the SSRS report you want to subscribe to.

1. Click the ellipses pertaining to the report title and select Subscribe.

1. Note: If needed, refer to Microsoft online Help by selecting the question mark icon in the page's upper right corner.
Choose the report parameters by completing the fields, then click Create subscription at the bottom of the page.

1. The system creates your subscription and closes the page.

1. (Optional) To confirm your subscription, go to Settings > My subscriptions.The new subscription displays as a line item on the page.

At the scheduled time, the SQL application will use your credentials to access the Vista database and generate the report. It will then deliver the report to the recipients you indicated, and in the format you chose.

Related information

- [SSRS Overview and Security Considerations](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations)

- [Troubleshooting an SSRS Report Subscription](/en/vista/vista/system-tools/reports/ssrs-overview-and-security-considerations/troubleshooting-an-ssrs-report-subscription)

- [About the RP Report Titles Form](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form)

- [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)
