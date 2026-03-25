---
title: "General Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/general-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2024-releases/whats-new-in-vista-2024-r1/general-features"
---

# General Features

Vista 2024 R1 delivers on General user-requested enhancements, fixes, and other improvements.

## Aatrix Auto Updates

Aatrix has implemented an auto update process which provides users with the latest updates without them having to manually run an update process.
The changes implemented are as follows:

- When you first launch an Aatrix report after the auto-update rollout (by selecting History or Continue in the report launcher), a new "Forms Update" window displays with multiple update options (Automatic Update, Download Update, Continue Expired, and Cancel). Select the Automatic Update option and Aatrix will run an update which includes setting up an update task in the Windows Task Scheduler (one-time setup only). The Aatrix task is set to run hourly, checking for any updates and then running the updates as applicable. Note: The task set up by Aatrix is titled based on the vendor code (for example, VST060AatrixAutoUpdate).

Once this initial setup is completed, the only time you should encounter the Forms Update screen is when you attempt to run an Aatrix report between two scheduled runs and an update is found. For example, if an update task is run at 10:00 AM and you select to run an Aatrix report at 10:45 AM (15 min prior to the next run), if the system determines an update exists, it displays the Forms Updater window. When this happens, it is recommended that you select Cancel and wait for the next scheduled task to run to get the Aatrix update.
Note: If you select the Continue Expired option, your report will run without the required update; however, Aatrix will mark it as expired and you will be unable to file the report. Additionally, if your report is still running when the next scheduled task is run, it will interfere with the update.

- Another change implemented for this feature is a new warning that displays if you attempt to run an Aatrix report when either the update task or another Aatrix report is running. In this case, the system displays the following message: "Aatrix is currently in use or being updated; please try again in a few minutes". You will need to cancel out and wait until the report is closed or the update is complete.

- Vista no longer runs Aatrix updates, so you will no longer receive the Vista prompt to update Aatrix, nor will you see the red message displayed on the report launcher screen.Note: If you do not have Aatrix on your system and you attempt to run a report, a dialog box appears, directing you to a download URL (https://updates.aatrix.com.s3.amazonaws.com/web/Vista/AatrixVistaTaxForms.exe). You must install Aatrix to continue. For more information, see [Enable Aatrix on a Workstation](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/enable-aatrix-on-a-workstation).

## Support Four-Digit Years for Month Fields

You now have the ability to set month fields to use a four-digit year format using the Field Properties form (accessed by pressing F3 in a field).
The Display 4 digit year checkbox on the System Overrides tab in the Field Properties form is now available for month fields using the bMonth datatype. When you select this checkbox for a valid month field, months entered in that field display in a four-digit year format. You can enter a two or four-digit year in the field, however, if you enter a two-digit year, the system automatically converts it to a four-digit year format. For example, 0723 is converted to 7/2023 or 07/2023 (depending on the field).
Note: You can only set this checkbox if you are designated as a Form Administrator in VA User Profile.

## Updates to Software Requirements

Microsoft .NET Framework RequirementsASP.NET Core 8.0 Runtime Windows Hosting Bundle is now the minimum required framework to be installed on the Vista Application server. You can download the installer from Microsoft's [Download .NET 8.0](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) page.
.NETCore 2.2 and .NETCore 3.1 are no longer used and can be safely removed.
Operating System RequirementsWindows Server 2012 is no longer a supported operating system as of October 2023.

## Updated URL for Vista Web Next Gen Billing Compiler

In the Vista Web 24.10 release, the Classic Billing Compiler was removed, replaced by the Next Gen Billing Compiler. In Vista, the URL defined for the Billing Compiler (in DD Form Header) has been updated to /Field/FieldBillingCompiler (from /Field/BillingCompiler). This allows users with Vista Web to access the Next Gen Billing Compiler from Vista when selecting JB Billing Compiler from the Job Billing > Programs menu.
For more information about the Vista Web Next Gen Billing Compiler, see [Use the Next Gen Billing Compiler](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FC_000011:FC:FC).
