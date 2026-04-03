---
title: "Dispatch Status | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-tech/mobile-overview/dispatch-status"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/service-tech/mobile-overview/dispatch-status"
---

# Dispatch Status

The Service Tech mobile app automatically sets the work order status.
To prevent conflicting statuses, the Service Tech app prevents technicians from setting them. This is because the app:

- accommodates multiple assignments across multiple technicians

- is specifically designed to capture data offline, then sync each technician's updates upon reconnecting

- compares new data uploaded by other technicians and reconciles any conflictsNote: The one exception is the Hold status.

To some degree, Spectrum uses your settings to assign the status. In System Administration > Installation > Service Tech, you can choose the desired automation.Note: The online vs offline behavior of these example settings is described below.

## Online vs Offline

If the mobile device is online:

- When the tech clocks in to a work order, Spectrum changes the status to Arrived.

- Upon clocking out, if any assignments are incomplete, Spectrum changes the work order status to Assigned.

- If all assignments are complete, clocking out prompts a work order status change to Finished.

If the mobile device is offline,

- the mobile app retains the information

- Spectrum doesn't yet have the information, so no changes are made

- the technician uses the Is Assignment Done? button to indicate whether all required work order assignments are done

Once the mobile device reestablishes a connection, Spectrum updates the status accordingly.

## Completed Assignments

Work orders can be assigned concurrently to multiple technicians.
On behalf of any other technician assigned, you can mark the assignment as done:

- navigate to the Assignments page

- select the technician(s)

- mark the assignment as done.

The default action for tapping the Is Assignment Done? toggle switch is to mark the assignment as done only for the technician logged in to the app.
Here are multiple technicians assigned to the job and you:
