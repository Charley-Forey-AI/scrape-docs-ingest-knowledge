---
title: "Moving Documents Between a File System and the Vista Database | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/changing-the-document-storage-location/moving-documents-between-a-file-system-and-the-vista-database"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/changing-the-document-storage-location/moving-documents-between-a-file-system-and-the-vista-database"
---

# Moving Documents Between a File System and the Vista Database

Over time you may find that you need to change the location where you are storing your documents.
Note: Neither the File System nor the Vista database are recommended for storing attachments. VPAttachments is the preferred storage location for DM attachments. For more information, see [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options).

Note:Vista™'s Remote Service pulls documents from both the File System and Vista™'s database locations. This means that if you change the document location from a file system to the database, you do not need to move documents out of the file system and vice versa.
Before moving documents to a new location, there are a few things to keep in mind:

- The Viewpoint Remote Service must have access to the file system location. If documents are stored on a local drive (for example, C:\), you might need to move them to a location that the service can access.

- System performance may temporarily degrade during the process. It is recommended that you run this process when system usage is minimal.

- The system deletes the documents from the original location after moving them to the new location.

- The system ignores any datatype or attachment type security settings.

The following steps guide you through changing the document storage location from a file system to the Vista™ or vice versa.

1. In Vista™, open the DM Attachment Options form.

1. In the Attachment Storage Location section, select the option for the location that you are moving documents to: File System or Database.

1. If you select File System, enter the network directory in the Root Directory field. Optionally, you can click the Browse button to locate the directory. When entering a directory you must enter a UNC path; do not enter a mapped drive.Note: If you do not specify a root directory, users may encounter errors when adding documents to the system.

1. Click Update Attachments. The system displays a dialog box.Note: If you select a new storage location option and click OK without clicking Update Attachments, the system will display a message asking if you want to move existing documents. If you click Cancel, existing documents will remain in their current location, however new documents will use the new location.

1. Click Yes to continue. The system displays the DM Attachment Update form.

1. Click Update. The system moves the files to the new location.Note: If there is a file currently in the new location with the same name, the system appends a "1" in parenthesis to the new, duplicate file; for example, filename(1). If a second duplicate is added, the system appends an incremented number to the end of the new duplicate; for example, filename(2).
Tip: If any errors occur during the update, they will display in the Error List box at the bottom of the form. The Print Error List and Save Error List buttons allow you to print the error list or save it as a text file, respectively.

1. Click Close to close the DM Attachment Update form.The system will now use the new location to store documents.

Related information

- [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options)
