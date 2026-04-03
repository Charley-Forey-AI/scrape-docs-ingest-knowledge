---
title: "New/Edit Employee Time Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-time-entry/newedit-employee-time-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/human-resources/employee-kiosk-module/my-time-entry/newedit-employee-time-entry"
---

# New/Edit Employee Time Entry

The New/Edit Employee Time Entry window displays after a
 new entry is saved in My Time Entry.
After completing the
 fields as shown below, the entry will be validated by the system before saving and writing
 it to Pre-Time Card.
Once you click OK, the records are saved directly into
 Pre-Time Card Entry with batch code KIOSK. The records remain available for modification
 until it is transferred to Time Card Entry in Payment Processing.

## Initial Entry Fields

- Work date

- Company

- Department

- Pay type - A list of authorized pay types for the employee
 displays. There is no need to use the "ER" pay type here. To charge a piece of
 equipment to the job, simply enter its code on this screen. Behind the scenes,
 Spectrum will set the pay type accordingly. Likewise, the window does not ask for
 a cost type because it will be assigned by the system.

- Hours

## Window Variations Based on the Direct Cost Setting

## New Direct Job Entry

If the 'direct cost' flag in the designated Payroll department is
 'Direct job cost', the New Employee Time Entry window displays the current employee, the
 initial entry fields shown above, plus the following:

- Job

- Phase - If this is a sub-job transaction set up on a master
 job, double-click on this field to search phases for the sub-job. This will allow
 you to easily select a phase set up on a master job, but not present on the
 sub-job. Spectrum will add a new phase to the sub job if the current job is a
 sub-job of a valid master job, the phase lengths of both jobs match, and the Phase
 + Cost type combination for the current job is valid and not 'Complete'.

- Message

- Notice to Employee

If the Equipment Control module is present, this window will include
 the following additional fields:

- Equipment

- Eq usage hours

## New Direct Equipment Entry

If the 'direct cost' flag in the designated Payroll department is
 'Direct equipment cost', the New Employee Time Entry window displays the current
 employee, the initial entry fields, plus the following:

- Equipment

- Cost category

- Equipment W/O

- Certified job

- Message

- Notice to Employee
Note: When equipment is assigned to an entry, the
 system will check to see if the equipment has attached equipment and if so, it
 will create the pre-time card lines for the attached equipment.

## New Indirect Entry

If the 'direct cost' flag in the designated Payroll department is 'No
 direct cost', the New Employee Time Entry window displays the current employee, the
 initial entry fields, plus the following:

- Equipment

- Eq usage hours

- Message

- Notice to Employee
