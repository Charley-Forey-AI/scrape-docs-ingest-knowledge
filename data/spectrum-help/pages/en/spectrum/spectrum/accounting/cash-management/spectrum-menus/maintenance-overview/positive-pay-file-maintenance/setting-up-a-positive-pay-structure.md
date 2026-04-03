---
title: "Setting Up a Positive Pay Structure | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/setting-up-a-positive-pay-structure"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/cash-management/spectrum-menus/maintenance-overview/positive-pay-file-maintenance/setting-up-a-positive-pay-structure"
---

# Setting Up a Positive Pay Structure

Learn how to set up a positive pay structure for your
 company.
It is important to note that your bank will provided the
 majority of information needed to complete this procedure.

1. On the Site Map screen, select Cash Management > Maintenance > Positive Pay File.

1. Click the New button.

1. In the Format code field, enter the bank's name.Note: Bank names entered in this field
 must first be set up in Bank Account Maintenance.

1. In the Description field, enter a format code description. The information
 in this field identifies which bank format is associated with the positive pay
 file.

1. In the Data type field, use the drop-down menu to select whether the data
 will be in a Fixed width or
 a Delimited format.Note: If you select Fixed width, the
 Delimiter field is not available for use.

1. In the Delimiter field, select which delimination format the positive pay
 file uses. This field is not available if the Date type field is set to
 Fixed width. Select from
 the following options:

- Comma

- Tab

- Semicolon

- Space

1. In the Transfer file name field, enter the name of the file. This file will
 be saved to a location on your workstation or on the server, depending upon where
 your organization stores the positive pay file.

1. In the Identifier file name field, enter the path of the document used to identify your company. This field is typically blank, unless your bank directs you to include an identifying letter or number.

1. In the Issued check code field, enter the letter or number established by your bank that will allow the bank to identify the check. This field is frequently left blank.

1. In the Void check code field, enter the letter or number established by your bank to identify void checks, this is frequently the letter V or the number 2.

1. In the Detail options section, select the three checkboxes (Include net-zero checks ($0.00),
 Show original check amount on void
 records, and Automatically capitalize alpha characters), unless instructed to do
 otherwise by your bank.

1. In the Footer options section, leave the three checkboxes (Include void amounts in standard footer totals, Suppress standard footer if no checks issued, Suppress void footer if no void checks) clear, unless instructed to do otherwise by your bank.

1. Select the Positive Pay File Maintenance -
 Detail tab.

1. In the Variable type field, use the drop-down menu to select Single, Multiple, or Constant. If you select Single, the Search File Variable window displays. If you select Multiple, the Concatenate Multiple Variable window display.

1. In the Description field, enter the description that will display for the
 constant variable type's information. For example: 001.

1. In the Len (Length)field, enter the number of characters for the variable. This
 information is provided by your bank.

1. In the Just (Justification) field, enter how you want Spectrum to align the
 numeral. Use the drop-down menu to select Left, Right, or the Spectrum Default. If the Variable type field is set to
 Single, set the
 Just field to Right.

1. In the Fill field, enter the letter Z if you want leading zeros (for
 Right justification) or
 trailing zeros (for Left
 justification) to display. Leave this field blank if you do not want leading/trailing
 zeros to display.

1. On the next transaction line, set the Variable field to Single.

1. In the Search File Variables window, use the File drop-down menu to select the
 BR.CHK option and
 complete the remaining fields per your bank's instructions.

1. Complete the Header tab, Footer tab, and Void Footer tab per your bank's
 instructions.

1. Click OK until you return to the Site Map screen.

1. Click Cash Management > Data Entry > Export Positive Pay. Use this screen to create an ASCII for your bank.

1. Complete the Bank account code and Positive pay file format fields so
 they match the Positive Pay File Maintenance field
 entries.

1. In the From check date field, enter the date that is the day after the most
 recent ASCII file was sent to your bank. For example, if the last ASCII file was sent
 on 07/15/20, enter 07/16/20 in this field.

1. In the To check date field, press Enter to accept the default of the current Cash Management processing date.

1. Complete the Transaction types and Transaction source checkboxes so
 they match the fields in the Positive Pay File Maintenance
 screen.

1. Click the Preview button to preview the report.
