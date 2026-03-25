---
title: "How the System Prints Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/checks/how-the-system-prints-checks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/checks/how-the-system-prints-checks"
---

# How the System Prints Checks

Overview of how the system prints checks based on whether printing a range of vendors or a range of sequence numbers.
When printing AP checks, you can select a specific group of checks to print from the current AP Payment Posting batch. You can print checks by vendor sort name, by sequence, or a combination of both. Regardless of the filter setting you select, the system prints checks in alphabetical order by vendor sort name, and then by sequence number order. This section explains how the system prints, depending on the filter settings you select.

## Printing Checks for a Range of Vendors

You can specify a range of vendors in the Begin Printing with Sort Name and the End Printing with Sort Name fields. If you specify a single vendor in these fields, the system prints checks for that vendor in order by sequence number. If you enter a range of vendors, the system prints checks in alphabetical order, and then in sequence order by associated vendor. The following example displays the order in which checks might print for three different vendors and their sequence numbers.
Table 1
Vendor
Payment Sequence
Check Number

ABC Construction
2
1000

4
1001

GHI Construction
1
1002

6
1003

XYZ Suppliers
3
1004

5
1005

## Printing Checks for a Range of Sequence Numbers

The sequence numbers that the system prints, and the order of printing, depends on the associated vendors. Typically, you will use the Beginning Sequence # and Ending Sequence # fields in conjunction with a specific vendor. For instance, using the example in Table 1 above, if you specified GHI Construction in the Sort Name fields and entered 1 in both sequence number fields, the system would only print the check associated with payment sequence 1.
Because the system prints checks alphabetically by vendor, and then by sequence number, printing checks based on a range of sequence numbers that spans multiple vendors is generally not recommended - you may get undesirable results.
For example, you may have three vendors in your batch, each with three associated sequences. ABC Construction has sequence numbers 2, 4, and 7; GHI Construction has sequence numbers 1, 5, and 9; while XYZ Construction has sequence numbers 3, 6, and 8. If you enter 7 in the Beginning Sequence # field and enter 9 in the Ending Sequence # field (expecting to print sequences 7-9), the system prints the following transactions in the order displayed in Table 2:
Table 2
Vendor
Payment Sequence
Check Number

ABC Construction
7
1000

GHI Construction
1
1001

5
1002

9
1003

The system only uses the 7 and 9 as beginning and ending points, so once it prints sequence 7, it moves to the next vendor alphabetically, and prints all sequences that occur prior to 9. Because sequence 9 occurs prior to sequence 8 (alphabetically by vendor) the system stops printing checks, and sequence 8 never prints.
