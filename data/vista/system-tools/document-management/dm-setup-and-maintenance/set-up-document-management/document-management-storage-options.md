---
title: "Document Management Storage Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options"
---

# Document Management Storage Options

VPAttachments is the preferred storage location for DM attachments in Vista.
Vista offers three options for storing and managing documents:

- Recommended: using VPAttachments, which is a separate document database

- Not recommended: in a user-defined network directory (File System)

- Not recommended: the Viewpoint Database

Note: Multiple Viewpoint databases cannot use the same document database. If you are going to use documents in a test environment, you must have a separate document storage location and separate Vista application server.

File System (not recommended)
Viewpoint Database (not recommended)
VPAttachments (recommended)

Summary
Works well for managing separate area for documents. Good for large document management environments.
Acceptable for small document management environments (8 or less) Vista licenses.
Flexible control of document location and storage size. Works well for almost any size document management environments.

Storage Space
Variable depending on the disk space allocated. Storage can reside on separate server. Controlled by system administrator. Access to documents is done through UNC; no drive mapping.
Document storage is integrated into Viewpoint database.
Document storage is allocated to a separate database. This database can be moved to a separate SQL server.

Performance
If documents are located on a separate server, the performance is limited by network access. Windows also has limitations on the number of files that can be stored in directories.
This can slow the performance of the Vista application. It is best to have the database growth option set to expand database file size.
It is best to have database growth options set to expand database file size. If document database is located on a separate SQL server then performance is limited by network access.

Security
Windows security, along with Vista security is required to manage access to these files. File names are encrypted.
Documents can be accessed only through the Vista application.
Documents can be accessed only through the Vista application.

Backups
Backups are handled separate from the Viewpoint database. Data may not be in sync.
Backups are handled through SQL Agent. Application and Document data are in sync.
Backups are handled through SQL Agent. Since the Vista application and documents are on separate databases there is the potential that data will not be in sync.

Additional Benefits
Independent storage.
None.
Independent storage and full text search capability.

Related information

- [Setting up a File System for Document Storage](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage)
