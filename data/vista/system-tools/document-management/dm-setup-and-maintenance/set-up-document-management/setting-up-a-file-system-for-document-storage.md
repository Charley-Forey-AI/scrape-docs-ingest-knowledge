---
title: "Setting up a File System for Document Storage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage"
---

# Setting up a File System for Document Storage

 Neither the File System nor the Vista database are recommended for storing attachments. VPAttachments is the preferred storage location for DM attachments. For more information, see [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options).
To set up a user-defined network directory for storing documents added to the system:

1. In Vista™, open the DM Attachment Options form.

1. Select the File System radio button from the Attachment Storage Location section. The system enables the Root Directory field.

1. Enter the network directory in the Root Directory field. Optionally, you can click the Browse button to locate the directory. When entering a directory you must enter a UNC path; do not enter a mapped drive.Note: If you do not specify a root directory, users may encounter errors when adding documents to the system.

1. Define the subdirectory structure. Although this is not a required step, a subdirectory structure allows for a more organized method for storing documents. For more information, see [Defining the Subdirectory Structure for Document Storage in a File System](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage/defining-the-subdirectory-structure-for-documents-in-a-file-system). Note: If you do not set up a subdirectory structure, the system stores all images in the root directory.

1. Click OK to close DM Attachment Options.

1. Verify that the server with Remote Helper installed has access to the UNC path you specified in step 3. The system will now store documents in the file system.

Related information

- [Defining the Subdirectory Structure for Documents in a File System](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage/defining-the-subdirectory-structure-for-documents-in-a-file-system)

- [Setting up the Viewpoint Database for Document Storage](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-the-viewpoint-database-for-document-storage)

- [Moving Documents Between a File System and the Vista Database](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/changing-the-document-storage-location/moving-documents-between-a-file-system-and-the-vista-database)

- [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options)
