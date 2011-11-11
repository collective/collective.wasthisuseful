Introduction
============

This product adds a viewlet which allows users to rate the usefulness of a
content item.

It also registers an Event which can be used in Plone's Content Rules so that
an e-mail can be sent immediately after a rating has been submitted.

Features
========

- Viewlet (below content) presents a form with the question 
  "Was this information useful?":

  * Clicking "Yes" immediately submits
  * Clicking "No" shows a comment field and submit button
- By default, enabled for "Document" types, others selectable.
- Enables immediate e-mail notification, with the rating value ("Yes" or "No")
  and rating comment (in the case of "No") as e-mail variables.

Installation
============

To your `buildout.cfg`, add::
    
    eggs =
        ...
        collective.wasthisuseful

After that, just install via the "Add-on" controlpanel.

Usage
=====

Enable e-mail notification
--------------------------

Create a content rule which has "Usefulness rated" as a trigger. As the rule's
action, select "Send e-mail". In the e-mail message, you can use
`${usefulness_comment}` and `${usefulness_value}` as variables (in addition to
the usual `${url}` and `${title}`.

Select enabled types
--------------------

The settings form which enables you to select on which content types the
viewlet is available via the Plone control panel ("Site setup").

Disabling specific folders
--------------------------

Once you've set the enabled types, you can override this behaviour by going to
the "Usefulness ratings" tab. On folderish objects, you can disable rating for
this object and its children.

To do
=====

- Show warning when viewing settings of item that is default view (like Topic
  `aggregator` in News Folder).
- Show number of ratings
- Integrate with collective.contentratings_
- Translate rating value ("Yes"/"No") in content rule e-mail

.. _collective.contentratings: http://pypi.python.org/pypi/plone.contentratings
