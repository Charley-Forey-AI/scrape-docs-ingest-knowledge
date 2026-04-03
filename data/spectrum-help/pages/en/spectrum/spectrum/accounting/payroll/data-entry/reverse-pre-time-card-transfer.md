---
title: "Reverse Pre-Time Card Transfer | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/reverse-pre-time-card-transfer"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/reverse-pre-time-card-transfer"
---

# Reverse Pre-Time Card Transfer

Use this screen to undo pre-time card transfers.
Important: You can only reverse pre-time card batches if the
 Payroll cycle has NOT been updated. Also, any existing pre-time card batches should be
 reversed BEFORE resetting/clearing the pay cycle. When entries are
 reversed, the time card lines are copied back to the pre-time card file. This update
 will additionally record Work order, Site equipment, component, Contract, WO/TC control
 code, the 'Available for billing' flag and billing rate information in the new time card
 entry when specified in the pre-time card table.The software
 does not remove the lines from the time card entry files. When time card entries
 transferred from Pre-Time Card Processing are reversed, a unique file key is assigned to
 each line when it is stored in the pre-time card file. This allows reversed entries to
 be transferred again and updated. Only time card lines originating from the pre-time
 card file will be reversed.
This reverse can be run while there are entries in Time Card Entry or immediately after a new pay cycle has been set. If the current time cards are not cleared out when the pre-time cards are re-transferred to Time Card Entry, the entries will double up in Time Card Entry.
The transaction update has two steps. Initially, a transaction/report register is printed and checked for accuracy. This should be saved as a permanent source document. After the report has printed, a second screen will appear that identifies which modules will be updated with this function and will prompt for affirmation if the update is to be completed. Any images associated with the updated time cards will also be transferred.
