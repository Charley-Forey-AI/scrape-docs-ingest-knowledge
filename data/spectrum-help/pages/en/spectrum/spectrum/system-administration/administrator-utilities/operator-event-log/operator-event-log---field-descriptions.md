---
title: "Operator Event Log - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/operator-event-log/operator-event-log---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/operator-event-log/operator-event-log---field-descriptions"
---

# Operator Event Log - Field Descriptions

Tip: These fields match the fields in the Purge Operator Event Log screen.
Fields/ButtonsDescriptions
OperatorEnter the operator or operators for whom you want to purge event activity, or press Enter to accept the default of ALL operators.
CompanyEnter the company code for which you want to purge event activity, or press Enter to accept the current company default. Do not use the default company when running this report for unsuccessful login attempts.
Database SessionEnter the database session ID for which you want to track event activity.
From/to event date


 Enter the start and end dates for your event purge or use the Date Calculator window to make your selection.
Include unsuccessful logon attempts?
 Select if you want to purge records of unsuccessful login attempts.
Include logon events?Choose which logon and logoff information you wish to purge.
Include logoff events?
Include menu selections?


 Select only if you want to purge operator menu selection information. Enables the Event field and Menu Search window in case you want to specify which modules and functions you want to purge activity for.
Event


 Lists any specific modules and functions selected for deletion using the Search button. If you don't make a selection, the report returns all events.
Sort byChoose how you want to sort the report data.
ContinueProceed with purging the specified operator events and return to the Utilities menu.
CancelExit without purging.
SearchAvailable only if the Include menu selections checkbox is selected. Select to display the Menu Search window, where you can select those modules or functions that you want to track event activity for, or you can keep the default of ALL modules and functions.
AllAvailable only if the Include menu selections checkbox is selected. Select to reset the Event field to include ALL modules and functions.
