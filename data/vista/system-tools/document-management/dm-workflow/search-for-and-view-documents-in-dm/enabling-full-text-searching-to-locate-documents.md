---
title: "Enabling Full Text Searching to Locate Documents | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/enabling-full-text-searching-to-locate-documents"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/enabling-full-text-searching-to-locate-documents"
---

# Enabling Full Text Searching to Locate Documents

When you are storing documents in a separate document database, you will have the capability to perform full text searches.
This type of search scans all of the words in each document trying to match search criteria entered by the user using the DM Attachment Index Search form. In order to perform full text searches, you must first enable full text searching.
The following instructions detail how to enable full text searching for your system.
Note: In order to enable full text searching, the following prerequisites must be met:

- All documents/attachments must be stored in a document database (which is separate from the Vista database).

- The instance of SQL Server on the attachment database must have full text installed.

1. On the Viewpoint server, select Programs > Viewpoint Construction Software > Configure Remote Service. The Viewpoint Server Configuration form displays.

1. Click Full Text Search. The Full Text Search Config form displays.

1. Ensure that the Vista database and attachment database information is accurate in the Viewpoint Database Server, Viewpoint Database Name, Document Database Server, and Document Database Name display fields.

1. Ensure that Yes displays in the Full Text Search Installed display field.

1. Click Create Document Catalog. The system begins indexing the documents.Note: This process may take several hours and is resource intensive. You should run this process at a time of minimal use for the system (e.g., overnight).

1. Click Refresh to update the indexing status in the Catalog Population Status field. When the process is finished, the term Idle displays in the field.

1. Close the Full Text Config and Viewpoint Server Configuration forms.

1. Open a Vista™ client.

1. Open the DM Attachment Options form and verify that the Use Full Text Search box is checked.Note: The Use Full Text Search box is disabled and you cannot change its setting here.
You can now perform full text searches using DM Attachment Index Search. For more information, see [Using Full Text Searches to Locate Documents](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-full-text-searches-to-locate-documents).

Related information

- [About the DM Attachment Index Search Form](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-the-dm-attachment-index-search-form)

- [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options)
