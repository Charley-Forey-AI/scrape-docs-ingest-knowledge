---
title: "Configuring Document Retention and Auditing Settings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/configuring-document-retention-and-auditing-settings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/configuring-document-retention-and-auditing-settings"
---

# Configuring Document Retention and Auditing Settings

When storing documents in Vista, you can configure retention and auditing settings in DM Attachment Options.
If you want attached documents to stay in the system after the associated data record is deleted, check the Retain Attachments after Record Delete box. Once you delete the data record, the system will store the document as a stand alone document. You will be able to locate the document by searching or using the Stand Alone Documents form. This functionality only works for maintenance forms, not batch processing forms.
If you want to archive documents when a user deletes them, check the Archive Deleted Attachments box. The system will assign a document status of Deleted to the document, but you can still view and locate it using DM Attachment Index Search.
If you want to keep an audit record for a document, check the Use Attachment Auditing box. Once you check this box, you can view the audit record for each document on the Log tab of the Attachment/Stand Alone Document form. If users need access to the Log tab, you must give them access to the DM Attachment Audit Log in VA Form Security.
Note: You can also set a retention time for documents based on attachment type. Once the retention time is reached, document with the associated attachment type will be available for purging in the DM Expired Documents Purge form. For more information on retention time, see [Setting Up Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types).

Related information

- [Search for and View Documents in DM](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm)

- [Viewing Documents Using the Attachment/Stand Alone Documents Form](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/viewing-documents-using-the-attachmentstand-alone-documents-form)
