---
title: "Changing the Subdirectory Structure for Documents in a File System | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/changing-the-subdirectory-structure-for-documents-in-a-file-system"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/changing-the-subdirectory-structure-for-documents-in-a-file-system"
---

# Changing the Subdirectory Structure for Documents in a File System

When storing documents in a file system location, you may need to change the subdirectory structure.
The following information covers the process of changing a subdirectory structure.
Before changing the subdirectory structure, there are a few things to keep in mind:

- The Viewpoint Remote Service must have access to the file system location. If documents are stored on a local drive (for example, C:\), you might need to move them to a location that the service can access.

- System performance may temporarily degrade during the process. It is recommended that you run this process when system usage is minimal.

- The system deletes the documents from the original location after moving them to the new location.

- The system ignores any datatype or attachment type security settings.

The following steps guide you through changing the subdirectory structure.

1. Open the DM Attachment Options form.

1. Select each applicable checkbox in the Subdirectory Structure section for creating subdirectories. For more information, see [Defining the Subdirectory Structure for Document Storage in a File System](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage/defining-the-subdirectory-structure-for-documents-in-a-file-system).

1. Click Update Attachments. The system displays a dialog box.Note: If you define a new subdirectory structure and click OK without clicking Update Attachments, the system will display a message asking if you want to move existing documents. If you click Cancel, existing documents will remain in their current location, however new documents will use the new location.

1. Click Yes to continue. The system displays the DM Attachment Update form.

1. Click Update. The system moves the files to the new location.Note: If there is a file currently in the new location with the same name, the system appends a "1" in parenthesis to the new, duplicate file; for example, filename(1). If a second duplicate is added, the system appends an incremented number to the end of the new duplicate; for example, filename(2).
Tip: If any errors occur during the update, they will display in the Error List box at the bottom of the form. The Print Error List and Save Error List buttons allow you to print the error list or save it as a text file, respectively.

1. Click Close to close the DM Attachment Update form.

1. Click OK to close the DM Attachment Options form. The system will now use the new subdirectory structure to store documents.

Related information

- [About DM Attachment Options Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-dm-attachment-options-form)

- [DM Attachment Update](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/dm-attachment-update)

- [Setting up a File System for Document Storage](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage)

- [Document Management Storage Options](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/document-management-storage-options)
