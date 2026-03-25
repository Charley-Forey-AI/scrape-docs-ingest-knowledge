---
title: "System Requirements | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view/system-requirements"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/user-database/user-defined-forms-and-lookups-integration-with-field-view/system-requirements"
---

# System Requirements

Make sure your system is set up to support User Defined forms and lookups integration.
Review the following requirements.

-  Make sure you are running:

- Team

- Field View

- Vista 6.18.0, 6.19.0, or later

- The latest version of the Vista-Team Connector (Vista_Team_Connector_x.x.x.x.exe)

- The latest version of the Vista Project Communication Database Server (Vista_ProjectCommunicationsDB_x.x.x.x.exe)

Find the Vista-Team Connector and Database Server installation files on the Viewpoint Customer Portal at the Products > Viewpoint Team > Downloads page. Important: Make sure to install the required Vista release *before* updating the database. If you update the database before installing the correct Vista release, you will need to uninstall the database update, and then reinstall once the correct Vista release is installed.
For installation instructions, see the *Viewpoint Team™ Installation Guide*, which is also provided in the Viewpoint Team > Downloads page on the Viewpoint Customer Portal.

-  If you are using Datatype Security in Vista, make sure to configure security to ensure successful integration between Team and Vista. For details, see "Configure Datatype Security in Vista" in either the Team online help or the *Viewpoint Team™ Installation Guide*.

- Make sure you have a license for the Vista UD module. If you are unsure, contact your Viewpoint representative for assistance.

-  You must be set up as an Administrator in Team and Field View.

- The User Defined Forms and User Defined Lookups features must be enabled in Team. To verify

1. In Team, click on your name in the upper right corner and select Admin Center. If you don't see Admin Center, you have not been set up as an administrator. Contact your System Administrator for assistance.

1. From the Admin Center, click Enterprise Settings. If you don’t see the option for User Defined Forms and User Defined Lookups, contact your Viewpoint representative for assistance.

- Team must be synchronized with Vista and mapped to Field View. If you have not already worked with Viewpoint to map your Team and Field View enterprises, contact your Viewpoint representative for assistance. For instructions on how to synchronize with Vista, see [Sync with your ERP System](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:Team_000008:Team:Team).

## UD Lookup Guidelines for Integration

In Vista, in your User Defined lookups, make sure the "Where Clause" includes specific identifiers for each record, and does *not* include a question mark as a parameter.
For example, if your lookup lists all the active equipment in your company, and, in Vista, your company is identified as "Company=1", in the "Where Clause," you must indicate "EMCo=1" instead of "EMCo=?".
Any UD lookups that are "parameter-based" (meaning they include a question mark parameter in the "Where Clause") will fail to convert to predefined answers in Field View.

Note: For information on the Vista User Database module, including creating custom lookups and adding a custom table, refer to the "User Database" section of the Vista online help or the "Introduction to Vista User Database" training in the Trimble Construction Academy.
