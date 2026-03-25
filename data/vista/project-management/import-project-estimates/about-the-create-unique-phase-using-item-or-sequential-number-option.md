---
title: "About the Create Unique Phase Using Item or Sequential Number Option | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-create-unique-phase-using-item-or-sequential-number-option"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-create-unique-phase-using-item-or-sequential-number-option"
---

# About the Create Unique Phase Using Item or Sequential Number
 Option

You can have the system create unique phases by appending the
 contract item or a sequential number to end of each phase.
In Vista, a phase can only appear once on a
 project. However, it is very common in estimating for phases to be
 assigned to multiple items on a job, each occurrence of the phase being
 assigned to a different contract item.
The Create Unique
 Phase Using Item or Sequential # as Last Part
 Phase checkbox in PM Import Estimates
 Template allows you to have the upload create
 unique phases by attaching either a sequential
 number or a contract item to the end of the phase.
 By doing this, duplicate phases become unique
 phases, each assigned to their previously assigned
 contract item. This ensures that quantities,
 hours, and costs for any phases used on multiple
 items remain specific to each item (and therefore
 contract item). It is important to note that this
 feature will only work if the last part of the
 phase code is 3 characters, and it is blank.
When using this option, you must specify when this feature will be used:

- D - Duplicates Only. With this option, unique phases
 will only be created for duplicate phases; in
 other words, for phases that are assigned to
 multiple contract items on a contract. For
 example:

Import Item
Import Phase
Import Contract Item
PM Phase
PM Contract Item

7
02220-10-
7
02220-10- 7
7

10
02220-10-
10
02220-10- 10
10

- A – Always. If you select this option, the import process will create a unique phase for every phase in the text file, regardless of whether it is a duplicate phase. For example:

Import Item
Import Phase
Import Contract Item
PM Phase
PM Contract Item

7
02220-10-
7
02220-10- 7
7

10
02220-10-
10
02220-10- 10
10

15
03110-20-
15
03110-20- 15
15

Note: If a phase exists multiple times in the text file and
 all occurrences have the same item and cost type, the import will roll all cost detail into
 the first occurrence of the phase and assign the last part of phase based on the item/bid
 number or a sequence number. All remaining occurrences of the phase will be removed.

- N – Never. Use this option if unique phases will
 never be generated for phases in the text file,
 even if there are duplicate phases on a contract.
 If duplicate phases exist, then their costs will
 be rolled into one contract item, using the
 contract item of the first occurrence of the
 phase. For example:

Import Item
Import Phase
Import Contract Item
PM Phase
PM Contract Item

7
02220-10-
7
02220-10-
7

10
02220-10-
10
**
**

15
03110-20-
15
03110-20-
15

** All quantities, hours, and costs for this item were rolled into Contract Item 7.

- S – Only Phase with Sub Cost Types. If using this option, the import will create a unique phase for only those phases in the text file with a cost type matching either of the two cost types defined for subcontracts in PM Company Parameters.

Import Item
Import Phase
CT
Import Contract Item
PM Phase
PM Contract Item

7
02220-10-
1 (Lab)
7
02220-10-
7

10
02220-10-
3 (Sub)
10
02220-10- 10
10

15
03110-20-
2 (Matl)
15
03110-20-
15

Note: When creating unique phases, the system will first try
 to attach the assigned contract item. If the contract item is too big, then a sequential
 number is applied instead.
