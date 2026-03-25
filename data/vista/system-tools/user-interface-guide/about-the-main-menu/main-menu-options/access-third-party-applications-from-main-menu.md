---
title: "Access Third-Party Applications from Main Menu | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/access-third-party-applications-from-main-menu"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/access-third-party-applications-from-main-menu"
---

# Access Third-Party Applications from Main Menu

You can set up access to third-party applications from the Main Menu.

1. In RP Report Locations, add a new location. You will typically want the location name to easily identify the file location. For example, if setting up access to Microsoft Word or other MS Office applications, you might call your location “Office” or “MS OFFICE”.

1. Set the Location Type to ‘UNC-Network Path’.

1. Specify the report path, using the Browse button () to locate the directory where the application executable resides.

1. In RP Report Titles, enter a report ID for the application. You might use a number range that you specifically set aside for non-report links (e.g. 99000-99999).

1. In the Title field, enter the name you want displayed on the menu. This will typically be application name (e.g. MS Word).

1. In the Application Type field select Other.

1. In the Report Location field, select the location you set up in Step 1.

1. In the FileName field, enter the application file name (e.g. winword.exe) or use the Browse button to locate the appropriate executable. (Note: The Browse button takes you directly to the directory specified in Step 1.) Note: You can enter parameters after the file name to implement an additional action. For example, using our example application “winword.exe”, you can specify to open a specific document by entering the FileName as follows: winword.exe (/t C:\directoryname\documentname.doc) When
 the application opens, it will immediately open the “documentname” document.


1. If desired, use the Change Icon button to select an icon to represent the application. If you do not change the icon, the standard reports icon will be used.

1. Save the record.

1. In VA Report Security, enter the Module as ‘RP’.

1. Specify the company and group/user to which you are assigning access. (Note: Users to which you are giving access must have the application on their system. In addition, if you included parameters to open a specific file, user must have access to that directory and file.)

1. Click Refresh to populate the grid and then locate the Report ID you assigned to the application.

1. In the Access Level field select Allowed.

1. Click Apply to set the permissions.

The application now resides on the RP Reports menu. You can drag and drop the application to selected folders (root folders or subfolders, except the standard Programs and Reports folders defined for each module). If you wish to add the application to the Reports folder of other modules, use the Assigned Modules tab in RP Report Titles.

Related information

- [Main Menu Options](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options)
