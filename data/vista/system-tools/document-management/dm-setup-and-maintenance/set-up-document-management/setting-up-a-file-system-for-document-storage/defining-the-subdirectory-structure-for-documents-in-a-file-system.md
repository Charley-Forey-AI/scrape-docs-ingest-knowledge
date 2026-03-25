---
title: "Defining the Subdirectory Structure for Documents in a File System | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage/defining-the-subdirectory-structure-for-documents-in-a-file-system"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage/defining-the-subdirectory-structure-for-documents-in-a-file-system"
---

# Defining the Subdirectory Structure for Documents in a File System

When you are storing documents using a File System location, a subdirectory structure allows you to create a more organized method for storage.
For example, you can set up your file system so that all images are grouped together based on company and module.
You will use the DM Attachment Options form to set the subdirectory structure. Once you set the document storage location, you can select a single option or a combination of options in the Subdirectory Structure section of the form.
There are four subdirectory options available:

- By Company – (C%) The system creates a subdirectory based on the active company and names it 'Company' followed by the company number (for example, \\server\Scanned Docs\Company1).

- By Module – (M%) The system creates a subdirectory based on the active module (for example, \\server\Scanned Docs\AP).

- By Form – (%F) The system creates a subdirectory based on the active form (for example, \\server\Scanned Docs\APEntry).

- By Month – (%D) The system creates a subdirectory based on the date the image was scanned (for example, \\server\Scanned Docs\11-2013).

Check the box for each option that you want to use as a subdirectory. When selecting multiple options, the system creates the subdirectory structure in order by checkbox. For example, if you want to store images based on company, module, and month, check the By Company, By Module, and By Month boxes. If you select all options, the subdirectory structure would be: \\server\Scanned Docs\Company\Module\Form\Month.
If you are using multiple options and you would like to define the order the system will use to create subdirectories, check the Custom box. The system will enable the Custom text box which you will use to create a custom subdirectory. When creating a custom subdirectory, enter the subdirectory options in the text box in the desired order using the corresponding letter and percent sign (%). Separate each option with a backslash. For example, if you want the system to order the directory by Module, Month, and Form, enter %M\%D\%F.
Tip: You can also combine variables to create a single folder. For example, if you enter %C\%M - %D, the system would create a subdirectory like this: \\server\Scanned Docs\Company1\AP - 05-2013.
Note: When you check the By Module and By Form boxes, the system saves Stand Alone documents in a directory path that looks like this: \\server\Scanned Docs\No Module\No Form. This is because Stand Alone documents are not associated with a particular form or module.

Related information

- [Setting up a File System for Document Storage](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/setting-up-a-file-system-for-document-storage)

- [About DM Attachment Options Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/about-dm-attachment-options-form)
