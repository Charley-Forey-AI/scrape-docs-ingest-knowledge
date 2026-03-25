---
title: "Refreshing Document Indexes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/refreshing-document-indexes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-indexes/refreshing-document-indexes"
---

# Refreshing Document Indexes

Once a document is attached to a data record, the system creates an index based on information in the data record.
At some point after the document is attached, a user could change some information on the data record. This could potentially affect the index for the document and prevent it from being located using the DM Attachment Index Search form.
For example, if you attached a document to an AP invoice associated with vendor number 200, and another user changed the vendor to number 320, the system would continue to search for the document using vendor number 200 as part of the index. In this case, you would need to refresh the document indexes to ensure that all attached documents had current information.
It is recommended that you refresh document indexes on a regular basis. Refreshing document indexes does not affect stand alone or deleted documents. You can refresh the indexes for all documents at once or you can refresh indexes for specific documents.
