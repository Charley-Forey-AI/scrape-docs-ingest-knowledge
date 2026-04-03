---
title: "Import Pre-Time Cards - Error Correction Logs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-pre-time-cards---error-correction-logs"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/import-pre-time-cards---error-correction-logs"
---

# Import Pre-Time Cards - Error Correction Logs

To protect against importing invalid entries, if there are
 any errors in the lines for salaried employees, the erroneous lines will go directly to the
 Pre-Time Card import errors screen.
These records appear in the log for information only; corrections are not allowed. At this
 point you must enter the erroneous lines manually in the Pre-Time Card Entry screen.

- If you use the Unpaid pay type
 during import…a valid non-direct cost department code is required. The
 pay rate will automatically be set to $0.00 for the line and any wage, union, or tax
 code entries will be left blank during import. If the department code is invalid or a
 direct cost, the line will appear in the Error Correction list rather than in
 Pre-Time Card Entry.Note: You can view these error log screens
 by batch, or all at once.

- If you are using Web Portal…the import feature supports special amount pay types SA, C, M, 1, 2, and 3, and it allows for negative amounts and hours to be posted to pre-time cards. If the import does not include rates for the M or SA pay types, the import will use rates from the employee file (and if none exist in the employee file, the lines will go to the error screen).

- If you are using pay types of O, D, EO, and ED… these pay types are not allowed for salary employees during the import or Web Portal transfer, so these lines are sent to the error screen.

- If you are using pay type EU...you must include a valid employee code.

- If the pay type is ER, EO, ED or EU...if active attachments were found and corresponding EU time card lines were generated, any error with the new records will be sent to the error screen.

- If you have a Human Resources trigger to prevent timecard entry for an employee…then the import or Web Portal transfer will send the time card lines for this employee to the error screen.
In addition, if there are still records in either of the error logs during the transfer of pre-time cards to time cards, a warning message displays. You can still proceed with the transfer, but the records in the error log will not be included.
If no errors are found, then the pre-time card lines will be created using the information created during the validation/default process, and an update confirmation report will be produced. This upload will place all time card information from the file into Pre-Time Card Entry. Following import, any additions or corrections may be made in Pre-Time Card Entry. When the new payroll cycle which includes these hours has been set using Set Payroll Cycle, it will then be necessary to transfer these entries into Time Card Entry using Pre-Time Card Update.

For more information, see [Pre-Time Card Import Errors](/en/spectrum/spectrum/accounting/payroll/data-entry/import-pre-time-cards-from-text-file/pre-time-card-import-errors).
