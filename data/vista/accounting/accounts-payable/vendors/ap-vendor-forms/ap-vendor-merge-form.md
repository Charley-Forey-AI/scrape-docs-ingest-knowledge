---
title: "AP Vendor Merge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendor-merge-form"
---

# AP Vendor Merge Form

Use this form to identify vendors with the same or similar information so that you can determine if they are duplicates and then merge them if applicable.
The search criteria allows you specify a confidence level that controls how restrictive the system is when comparing data between vendors to identify potential duplicates. The High level is the most restrictive and will generally produce less potential duplicates, since it is looking for vendors with the most similarities. The Low level is the least restrictive and will generally produce more potential duplicates, since it includes vendors with less similarities. However, the Low level will exclude vendors that have significant differences.Note: It is important to note that if you have an extensive list of vendors, the search for duplicate vendors may take a while. However, using the High confidence level takes less time than using the Low confidence level.

In addition to confidence level, you can specify what information you want the system to use in identifying potential duplicates. For example, you can search by vendor name, purchasing address, payment address, or phone/email, or you can use a combination of these options for a more thorough search.
Note: The system saves your Confidence Level and Identify By settings, as well as the propagated list from your last session. You can change the settings as needed.

If you have some idea of who your duplicate vendors might be, you can limit the search to a single vendor using the Limit To Vendor field. This method compares all vendors to the specified vendor to determine potential duplicates, which is less time-consuming than the "all vendors to all vendors" method.
Once you run the Identify Duplicates process, the system populates the grid with all vendors identified as potential duplicates. Potential similar information is highlighted in red and vendors with similarities are grouped together using a Match ID.Note: If you used the Limit To Vendor option, the system displays the vendor and its potential duplicates at the bottom of the grid. You can sort by the MatchID column in descending order to display the vendors at the top of the grid.

You can then review the list to determine the actual, duplicate, and unique vendors (those that are not duplicates of any other vendor). You can only designate one vendor in a session as an actual vendor, so if you have multiple groups of duplicate vendors, you will need to run the process multiple times.
When marking duplicate vendors, only mark those that are duplicates of the actual vendor. Leave all other vendors blank so they can be included in future sessions. If a vendor is not a duplicate of any other vendor, mark it as unique. This prevents the vendor from showing up in future sessions.
Once you have completed designating the actual, duplicate, and unique vendors
 for the current session, process the session. The system deactivates all duplicate
 vendors and adds them to the Duplicate Vendors tab for the actual vendor in AP
 Vendors.Note: If a duplicate vendor with open invoices is
 encountered during processing, the system skips that vendor. You must process or
 void the invoices before you can mark that vendor as a duplicate. And since Actual
 vendors are available in all sessions, you can link the skipped vendor to the actual
 vendor in any future session.

## Clear Grid

You can clear the grid of search results using the Clear Grid button. This allows you to start over with a fresh search. This is especially useful if you are using the Limit by Vendor option and want to do multiple single vendor searches. When you click Clear Grid, a message displays asking if you are sure you would like to clear all vendors from the grid and start again. Click Yes to clear the grid, No to leave the existing results intact.

For more information about linking duplicate vendors, see [Identify and Link Duplicate AP Vendors - Video](/en/vista/vista/videos/accounting/identify-and-link-duplicate-ap-vendors---video).
