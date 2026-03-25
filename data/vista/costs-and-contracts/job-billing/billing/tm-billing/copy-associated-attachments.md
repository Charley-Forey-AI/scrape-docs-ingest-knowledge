---
title: "Copy Associated Attachments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/copy-associated-attachments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/copy-associated-attachments"
---

# Copy Associated Attachments

Attachments associated with the current billing can be copied to a directory and later used to generate a CD that can be sent along with the billing for additional detail.
To use this feature, you must set the JC Interface Level option in AP Company Parameters to “Line.”

1. From the JB T&M Bill Edit form, select File > Copy Associated Attachments.The Browse For Folder window displays.

1. Select a folder to copy the attachments to and click OK.Note: Once you have used this feature, the system will automatically place focus on the last folder selected. To create a new folder, click Make New Folder, enter the folder name, and then select the new folder and click OK.

The Sort Options window displays.

1. Select the order in which to list attachments in the XML (JBCD.xml) output file. If you select the Default option, the system will sort attachments based on the sort order returned from the database.

- Contract Item - Attachments will be listed in order by contract item.

- Phase - Attachments will be listed in order by phase.

- Date - Attachments will be listed in order by transaction date.

- Template Sequence - Attachments will be listed in order by template sequence.

- Line Number - Attachments will be listed in order by bill line number.

- Default - Attachments will be listed in the order returned from the database.

Depending on how the detail is set up, the sort order may appear to be the same for one or more of the sort options. For example, if you select to sort by contract item and the order of contract items matches the line number order, the sort will not appear any different than if sorting by line number (Example A). However, if the order of contract items does not match the line number order, the sort will appear different than when sorting by line number (Example B).
Example A
Example B

Line Number
Contract Item
Line Number
Contract Item

10
1
50
1

20
2
20
2

30
3
40
3

40
4
10
4

50
5
30
5

Note: You can only use the Phase and Date sort options if the template used to generate the bill has a Sort Order of J-Job/Phase or D-Date (respectively). Otherwise, a message displays when the copy process is complete indicating the system was unable to sort by the selected sort option and instead used the Default option.

1. In the Attachments to Include section, select the checkbox next to each module for which to include attachments in the copy. If there are attachments associated with the T&M bill in the selected module, the system will copy those attachments to the specified folder.

1. If you want the generated XML file to include transaction lines without attachments, select the Lines Without Attachments checkbox.Note: Transaction lines without attachments will not include links to attachments in the XML file.

1. Click OK.

The system searches all detail lines for any attachments added to the associated transactions (in AP, PR, etc.). If attachments are found, the system creates a new folder within the selected folder and places all attachments in the new folder. The folder name is based on the Bill Month and the Bill Number (e.g., 10-08 Bill 12), while attachment file names are a combination of the source attachment file name and the attachment ID. For example, if the source attachment file name is "Invoice.pdf" and the attachment ID is "13975", the new attachment file name will be "Invoice_13975.pdf". In addition, the system generates a viewable document (for example, JBCD.xml).
Note: If you edit a billing and recopy the attachments, the copy process does not overwrite the existing folder and data. It creates a new folder with the same naming convention and adds a sequential number (e.g. 04-08 Bill 3(1), 04-08 Bill 3(2), etc.).

Related information

- [JB T&M Bill Edit Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-bill-edit-form)
