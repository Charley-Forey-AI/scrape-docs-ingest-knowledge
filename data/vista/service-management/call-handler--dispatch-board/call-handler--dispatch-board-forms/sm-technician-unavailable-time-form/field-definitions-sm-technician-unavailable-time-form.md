---
title: "Field Definitions: SM Technician Unavailable Time Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-technician-unavailable-time-form/field-definitions-sm-technician-unavailable-time-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-technician-unavailable-time-form/field-definitions-sm-technician-unavailable-time-form"
---

# Field Definitions: SM Technician Unavailable Time Form

The following is a list of field descriptions for the SM
 Technician Unavailable Time form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Technician

This field automatically defaults the
 technician you selected on the Dispatch Board. You will typically not change this default
 unless you selected the wrong technician. If you elect to change the technician, the system
 displays a message indicating the record has changed and asking if you want to update
 before moving on. Select No to discard the current record and
 create a new one.

## Seq

This field automatically defaults a sequence number and cannot be changed.
If you are adding a new record, enter
 N,
 New,
 or + to have the system
 automatically assign the next sequential number available for this technician.

## Description

Enter a summarized description or reason for the unavailable time. The description entered here will display on the dispatch board for this event. If you leave this field blank, the event will display as "Unavailable"

## Start Date

Required.
Enter the date on which the technician's unavailable time begins.

## End Date

Enter the date on which the technician's unavailable time ends. Must be equal to or greater than the Start Date.
If this date is greater than the start date, the unavailable time event will cross over all indicated days on the dispatch board.

## All Day Event

Check this box if the technician is unavailable for the entire day. When you save the record, the system grays out the date on the dispatch board. However, if trips exist on the specified date, the system sets the date to a salmon color.
Leave this box unchecked if the technician is
 only unavailable for part of the day. Use the Duration field to specify the unavailable
 hours for the technician.
Note: The system requires that you either check this box or
 enter hours in the Duration field. If you enter a duration value and then check this box, the
 system will clear the duration value once you save the record.

## Start Time

The Start Time field on the SM Technician Unavailable Time form.
Required.
Enter the start time (in 24-hour format) for this unavailable time event.
Note: This field is disabled if you select the All Day Event
 checkbox.

## Duration

This field is only enabled and required if you
 did not select the All Day Event checkbox.
Enter the number of hours this technician will be unavailable for trips. If you enter incremental hours, the system will automatically round the hours up or down when you hover over the unavailable time event on the dispatch board. For example:
Hours Entered
Hover Text Display

4.00
4.00

4.25
4.00

4.50
5.00

Note: This field is disabled if you select the All Day Event
 checkbox.

## Details

Use this field to enter a detailed reason for the technician's unavailable time.
