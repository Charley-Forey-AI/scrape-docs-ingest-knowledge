---
title: "About Aatrix Auto Updates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-aatrix-auto-updates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-aatrix-auto-updates"
---

# About Aatrix Auto Updates

If you have Aatrix installed on your system, Aatrix uses an automated update process to provide you with the latest updates without you having to manually run the update process.

Beginning year-end 2023, Aatrix implemented a new auto-update process. This process automatically updates your system each time there is an Aatrix update, whether it be new or updated regulatory reports or new tax types.
Note: If you do not have Aatrix on your system and need to install it, see [Enable Aatrix on a Workstation](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/enable-aatrix-on-a-workstation).

 Once Aatrix has implemented the auto-update process on your system, the first time you run an Aatrix report (by selecting History or Continue from the report launcher), you will be presented with a Forms Update window. This window includes the following update options:

- Automatic Update

- Download Update

- Continue Expired

- Cancel

 For detailed information about these options, select the Help button () in the Forms Update window.
To fully enable the auto-update process, you must select the Automatic Update option. Once selected, Aatrix runs an update and as part of that update, creates an auto-update task in the Windows Task Scheduler (one-time setup only), and sets the task to run hourly.
Note: Aatrix names the task based on the vendor code (for example, VST060AatrixAutoUpdate).

Once this initial setup is completed, the Windows Task Scheduler runs the auto-update task each hour and checks for any Aatrix updates. If any are found, Aatrix automatically runs the update.
If you select to run an Aatrix report and the update task is running, the system displays the following message:
 "Aatrix is currently in use or being updated; please try again in a few minutes."
 You will need to cancel out and wait until the report is closed or the update is complete. This message also displays if you attempt to run a report when another Aatrix report is already running.
If you launch an Aatrix report between the auto-update task runs and the system determines there is a new Aatrix update, the Forms Update screen displays. When this happens, it is recommended that you select Cancel and wait for the next scheduled task to run and install the update.
 You can select the Continue Expired option to proceed with running your report; however, Aatrix will mark the report as expired and you will be unable to file it with the designated reporting authority. You will need to rerun your report after the next auto-update task runs and installs the update, before you can file it.
Note: If you select Continue Expired and your report is still running when the next scheduled task is run, it will interfere with the auto-update process.

Note: If your auto-updates are failing, review your folder permissions. You may also need to check Network Security applications and local firewalls, as they can stop Aatrix from updating.
