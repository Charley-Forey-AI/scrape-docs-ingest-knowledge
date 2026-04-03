---
title: "Equipment Tracking Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-tracking-installation---properties"
---

# Equipment Tracking Installation - Properties

Use this tab to select default properties settings for the Equipment Tracking module. You can change these settings as needed at any time.
Fields/ButtonsDescriptions
Full charge on Saturday?
Full charge on Sunday?
This option will be used when the system has to calculate a bill for the number of days that a piece of equipment has been out, either for the Recurring Equipment Tracking Report or when a final bill is created when the equipment is returned. Select the checkbox for each weekend day want the system to calculate billing days for purposes of calculating equipment billing in Recurring Equipment Tracking Update. To exclude either day, leave its checkbox clear.
If both the Full charge on Saturday and Full charge on Sunday checkboxes are blank, a 5-day workweek is indicated. If the Full charge on Saturday checkbox is selected, but the Full charge on Sunday checkbox is not selected (and vice versa), a 6-day workweek is indicated. If the Full charge on Saturday and Full charge on Sunday checkboxes are selected, a 7-day work week is indicated. Use the following equation to determine daily equipment revenue amounts:
Equipment revenue per week / Days per week = Equipment revenue per day

Units of measureEnter the stand-by units of measure for the hourly, daily, weekly, and monthly job/rental rates for equipment. For reference, these units of measure display in Equipment. They are used in the transaction update and the recurring billing system to post the unit of measure to 'ES' source transactions in Equipment Control.
Enable HILTI OnTrack equipment/tool management?Select this checkbox to activate Spectrum's integration with Hilti ON!Track. This allows you to manage
 equipment in Spectrum
 using Hilti's equipment tracking functionality, which is different from
 Spectrum's
 standard equipment management. For more information, see [Enable Hilti ON!Track in Equipment Tracking Installation](/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/set-up-the-hilti-ontrack-integration-in-spectrum/enable-hilti-ontrack-in-equipment-tracking-installation).
