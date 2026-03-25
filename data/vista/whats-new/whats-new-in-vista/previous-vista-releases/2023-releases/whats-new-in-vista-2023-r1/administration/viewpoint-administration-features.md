---
title: "Viewpoint Administration Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/viewpoint-administration-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/administration/viewpoint-administration-features"
---

# Viewpoint Administration Features

Vista 2023 R1 delivers on user-requested Viewpoint Administration enhancements, fixes, and other improvements.

## New Queries for Identifying Programs/Reports Requiring an Office License

 You now have the ability to identify Vista programs and reports that require an Office license.
 Two new queries were added to the VA Inquiries form:

- ProgramsWithOLRSetting (Programs With Office License Required Setting) — Use this query to show which Vista forms require an Office license. Information shown includes the Module, Form Title, Form Name, and Office License Required flag.

- ReportsWithOLRSetting (Reports With Office License Required Setting) — Use this query to show which Vista standard reports require an Office license. Information shown includes the Module, Report ID, Report Title, and Office License Required flag.

 To run these queries, add them to any Work Center as follows:

1. In the selected Work Center, right click on the folder in the menu tree where you want to add the query.

1.  Select Add Inquiry. This opens the Inquiry Settings form.

1. In the Base Inquiry field, enter or select the inquiry name (for example, ProgramsWithOLRSetting).

1.  In the Name field, enter the name to display in the menu or leave blank to display the default name.

1. Click OK.

## Aatrix History Path by User

You now have the ability to specify an Aatrix history path at the user level in VA Profile. History paths are used to store and maintain Aatrix data history.
To implement this functionality, a new History Path field was added to the Aatrix Installation Location section of the VA User Profile form. The history path defined for a user overrides the history path specified at the site level in VA Site Settings. If users do not have a history path defined in VA User Profile, the system uses the history path defined at the site level.
Note: If no history path is defined at the user or site levels, the system stores Aatrix history on each user's local drive.
 In a related feature, report type filtering was added for Aatrix history. For more information, see the [Aatrix History Filtering by Report Type](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/general-features#concept-7559--en__AatrixHistoryFiltering) section of General Features release notes.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
