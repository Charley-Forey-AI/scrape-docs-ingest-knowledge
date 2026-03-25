---
title: "About Importing Files Automatically | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically"
---

# About Importing Files Automatically

Your Vista application can automatically import data files
 into your database. How you proceed depends on your deployment method.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.

To set up automatic imports:

1. Create an automatic
 import profile using the IM Auto Import Profile Setup form in the Vista
 application.

- If your deployment method is VRL cloud, see [Create an Auto Import Profile - VRL Cloud](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/create-an-auto-import-profile---vrl-cloud).

- If your deployment method is VRL on-premises, LAN, or RDP see [Create an Auto Import Profile - on-premises](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/create-an-auto-import-profile---on-premises).

1. Enable your server to process automatic imports
 using the Server Configuration form.

- If your deployment method is VRL cloud, see [Configure Automated Document Upload for
 Imports - VRL Cloud](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/configure-automated-document-upload-for-imports---vrl-cloud).

- If your deployment method is VRL on-premises, LAN, or RDP, use the Server
 Configuration form. See [Server Setup for Automatic Imports: On-premises](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/server-setup-for-automatic-imports-on-premises).

1. If your deployment method is:

1. VRL Cloud: skip this step.

1. VRL on-premises, LAN, or RDP: Ensure that
 any auto import profiles are already set up - *even those not being used* - have
 valid directories assigned in their Pickup, Archive, Error, and Log directory
 fields.Important: Profiles that are set up
 incorrectly will cause system-wide automatic import failure even on
 profiles you have set up correctly. As you see fit, delete unused
 profiles or make directory corrections.

1. (Optional) If you or others want to be notified on the status of each automatic import, [set up import notifications](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically/set-import-notifications).

Related information

- [About the IM Auto Import Profile Setup Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-auto-import-profile-setup-form)
