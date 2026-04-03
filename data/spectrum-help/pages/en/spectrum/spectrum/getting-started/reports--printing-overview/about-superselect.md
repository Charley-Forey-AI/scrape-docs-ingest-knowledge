---
title: "About SuperSelect | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/reports--printing-overview/about-superselect"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/reports--printing-overview/about-superselect"
---

# About SuperSelect

A green asterisks signals that a field includes special
 selection capability called SuperSelect. Become familiar with the different selection types
 to be able to filter your data records quickly and efficiently.
SuperSelect options allow flexibility in defining which records are to be included on a
 report or listing.

SuperSelect options can be used individually or in combination with one another. The
 SuperSelect icon displays adjacent to any field offering SuperSelect options. Click this
 icon to look up the SuperSelect options, which include Wildcard Match, Character Match,
 List, Range, Everything But, All, Exact Match, Contains, and Combination.

- Wildcard Match selects everything beginning with letters
 specified by using an asterisk (*) to stand in for any number of
 characters. This can be used to select records with a certain grouping of
 letters in common. For example, to select all customers beginning with the
 letter L, at a customer prompt type L*. All customer codes beginning with
 L will be selected.

- Character Match uses question marks (?) to stand in for
 each character. To select all customers with six-character names, at a customer
 prompt type six question marks, for example, ??????.

- List specifies exact records to be included. To use this
 option, type the names of each record; separate the records by commas, but no
 spaces.

- Range specifies a range of records to be included. To use
 this option, type the first and last record names, separated by a forward slash
 (/) and no spaces.

- Everything But selects all records except the one record
 specified. To use this option, type a number sign (#) followed by the
 name of the record to be excluded; to indicate additional exclusions, use a
 comma (excluding spaces) after each excluded record.

- ALL selects all records. To select all records, type
 ALL or an asterisk (*).

- Exact Match selects one record to be included. To use this
 option, type the name of the record to be included and press
 Enter.

- Contains selects every record that contains the specified
 combination of letters in the record name. For example, to include every record
 with the letters SMI, type *SMI*.

- Combination selects records based on the combination of up
 to two SuperSelect options. Some combinations cannot be applied simultaneously;
 for example, you *cannot* use Everything But in combination with other
 search methods, and you cannot use the Wildcard match (*) in combination
 with the character match ? or when searching for a range (/) of
 records. Therefore, if you use departmentalized account codes 25505010,
 43435011, 23245012, and so forth, with the first 4 digits being the department
 and the last 4 digits being the G/L cost code, you must enter
 *5010,*5011,*5012 to conduct your search (instead of
 *5010/*5012).
