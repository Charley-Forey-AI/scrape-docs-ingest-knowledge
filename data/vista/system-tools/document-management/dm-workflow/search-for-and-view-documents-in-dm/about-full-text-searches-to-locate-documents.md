---
title: "About Full Text Searches to Locate Documents | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-full-text-searches-to-locate-documents"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-full-text-searches-to-locate-documents"
---

# About Full Text Searches to Locate Documents

You can use full text searching to locate documents within your document database.
When using a full text search, the system checks all of the words within a document as it tries to match the words that you specify when initiating a search. The system does not search through the contents of JPEG or PDF files.
Note: To use full text search, your documents must be located on a separate document database and not your Viewpoint database.
To use a full text search, enter the keyword(s) in
 the Keyword field in DM Attachment Index Search and click Search. The
 Results grid displays all documents that contain the keyword(s) that you specified (and
 meet any additional search criteria you specified).
In addition to using keywords, you can use wildcards for advanced searches. The following wildcards are available for use:
Wildcard
Description

*
Typing an asterisk at the end of a word in quotes allows you to perform searches like the following:

- House* returns results like "Houses" and "Household"

- "House Plan*" returns results like "House planner" and "House plant"

and
Placing and between two words will return a document that has both words. Documents containing neither or only one of the words will not be returned. For example:

- House and boat returns documents with both house and boat in the text.

- House and "plan*" returns documents that have the word house and words that begin with plan (plan, planner, plans, etc.).

or
Placing or between two words will return a document that has either word. For example, if you enter house or boat, the search returns documents that contain either word.
Note: You can use the pipe sign (|) to perform the same search.

and not
Placing and not between two words will return a document that contains the first word, but not the second. For example:

- House and not boat will return all documents with house in the text, but will exclude documents that contain both house and boat.

- House and not "plan*" will return all documents with house in the text, but will exclude all documents with words beginning with plan (plan, planner, plans, etc.).

Note: You can use &! to perform the same search.

Related information

- [Enabling Full Text Searching to Locate Documents](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/enabling-full-text-searching-to-locate-documents)

- [About the DM Attachment Index Search Form](/en/vista/vista/system-tools/document-management/dm-workflow/search-for-and-view-documents-in-dm/about-the-dm-attachment-index-search-form)
