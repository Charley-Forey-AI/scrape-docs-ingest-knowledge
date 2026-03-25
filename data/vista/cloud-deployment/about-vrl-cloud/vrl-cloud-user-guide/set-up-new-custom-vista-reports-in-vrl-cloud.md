---
title: "Set Up New Custom Vista Reports in VRL Cloud | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/set-up-new-custom-vista-reports-in-vrl-cloud"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/set-up-new-custom-vista-reports-in-vrl-cloud"
---

# Set Up New Custom Vista Reports in VRL Cloud

Use the RP Report Titles form to establish the link between each custom report and your Vista application.
You must upload a Crystal Reports .rpt file for each new report record you plan to create using the instructions on this page. If needed, see this page: [Upload Custom Crystal Report files to Vista in VRL Cloud](/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/upload-custom-crystal-report-files-to-vista-in-vrl-cloud).The instructions on this page provide guidance to users whose deployment method is VRL Cloud and assume you are familiar with setting up reports in general. If you also need broader information about setting up reports, please see [Link Report Files to Vista](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/link-report-files-to-vista).

The process of establishing the link between the report and the Vista application involves creating a new record in the RP Report Titles form.
To create new custom report records in VRL Cloud:

1. Open the RP Report Titles form and select the Info tab.

1. Select the New Record icon.

1. In the Report Location field, press F4.The Report Location Lookup form provides a list of specific report locations.

1. Select Custom, then select OK to close the Lookup form.

1. Select the FileName button.The RP Select Report window appears with a list of all reports in the Custom location (that is, the Custom location you selected in step 4).

1. Select the appropriate .rpt file for this record.

1. Complete the remaining fields and save the record.

The Vista record you just created is now linked to your custom report's Crystal Report (.rpt) file.
Grant security access to the users who need to view this report. For instructions, see [Manually Assign Security to Each Group or User](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-report-security-settings/manually-assign-security-to-each-group-or-user).

Related concepts

- [About VRL Cloud](/en/vista/vista/cloud-deployment/about-vrl-cloud#concept-7178--en__concept-7178)
