Introduction
============

This product adds a viewlet which allows users to rate the usefulness of a
content item. Rating is simply a "Yes" or "No".

It also registers an Event which can be used in Plone's Content Rules so that
an e-mail can be sent immediately after a rating has been submitted.

Features
========

- Simple "Was this information useful?" form on Documents

  * Clicking "Yes" immediately submits
  * Clicking "No" shows a comment field and submit button
- Enables immediate e-mail notification, with the rating value ("Yes" or "No")
  and rating comment (in the case of "No") as e-mail variables.

Installation
============

To your `buildout.cfg`, add::
    
    eggs =
        ...
        collective.wasthisuseful

Usage
=====

Enable e-mail notification
--------------------------

Create a content rule which has "Usefulness rated" as a trigger. As the rule's
action, select "Send e-mail". In the e-mail message, you can use
`${usefulness_comment}` and `${usefulness_value}` as variables (in addition to
the usual `${url}` and `${title}`.

To do
=====

- Register viewlet, view and resources only for IThemeSpecific
- Show number of ratings
- Ability to disable rating on one content item
- Integrate with collective.contentratings_
- Translate rating value ("Yes"/"No") in content rule e-mail


.. _collective.contentratings: http://pypi.python.org/pypi/plone.contentratings
