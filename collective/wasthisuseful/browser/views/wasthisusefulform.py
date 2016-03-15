from AccessControl.unauthorized import Unauthorized
from collective.wasthisuseful import wasthisusefulMessageFactory as _
from collective.wasthisuseful.event import UsefulnessEvent
from collective.wasthisuseful.interfaces import IUsefulnessManager
from DateTime import DateTime
from plone.directives import form
from plone.formwidget.recaptcha import ReCaptchaFieldWidget
from plone.formwidget.recaptcha.validator import ReCaptchaValidator,\
    WrongCaptchaCode
from Products.Archetypes import PloneMessageFactory as __
from Products.statusmessages.interfaces import IStatusMessage
from z3c.form import button, validator
from z3c.form.interfaces import HIDDEN_MODE, IErrorViewSnippet
from zope import schema
from zope.component import getMultiAdapter
from zope.interface import Interface
import zope.event
from plone.protect.utils import addTokenToUrl


class INotUsefulForm(Interface):
    """ Schema for not-usefulness """

    useful = schema.Bool(title=_(u"label_was_this_useful",
                                 default=u"Was this information useful?"),
                         default=False)

    comment = schema.Text(
        title=_(u'label_why',
                default=u'Can you explain why it was not useful?'))

    email = schema.TextLine(
        title=_(u'label_email',
                default=u"Please enter your email address so we can"
                        u" reply to your comment."),
        required=False)

    captcha = schema.TextLine(title=u"Captcha", required=False)


class IUsefulForm(Interface):
    """ Schema for useful """
    useful = schema.Bool(title=_(u"label_was_this_useful",
                                 default=u"Was this information useful?"),
                         default=True)


class WasThisUseful(object):
    """ Mixing class for the forms to process voting """
    useful = None

    def _processVote(self, data):
        """ Process the data into a vote """
        if self.useful is not None:
            vote = self._createVote(**data)

            # Get the manager and add the vote
            manager = IUsefulnessManager(self.context)
            manager.addVote(vote)

            # Fire off evemt
            event = UsefulnessEvent(self.context)
            zope.event.notify(event)

    def _createVote(self, comment=None, email=None, **kwargs):
        """ Use a helper for easier dealing for no comment and
        no e-mail in data """
        now = DateTime()
        useful_int = int(self.useful)
        vote = dict(
            useful=useful_int,
            comment=comment,
            date=now,
            ip_adress=self.request.getClientAddr(),
            email=email
            )
        return vote


class NotUsefulForm(form.SchemaForm, WasThisUseful):
    """ Not useful form """
    schema = INotUsefulForm
    ignoreContext = True
    useful = False
    label = _(u"Information was not useful")
    description = ""
    name = "not-useful-form"

    def action(self):
        """ We nest the form, need a proper action """
        url = self.context.absolute_url() + "/@@not-useful-form"
        url = addTokenToUrl(url)
        return url

    def updateFields(self):
        """ Set the ReCaptchaFieldWidget factory """
        super(NotUsefulForm, self).updateFields()
        self.fields['captcha'].widgetFactory = \
            ReCaptchaFieldWidget

    def update(self):
        """ Hide the useful field, we set it per default """
        super(NotUsefulForm, self).update()
        self.widgets['useful'].mode = HIDDEN_MODE

    @button.buttonAndHandler(__(u'Submit'))
    def handleApply(self, action):
        data, errors = self.extractData()

        # CSRF
        authenticator = getMultiAdapter(
            (self.context, self.request), name=u"authenticator")
        if not authenticator.verify():
            raise Unauthorized

        # Check the captcha, this checks the REQUEST
        # not the actual field. And we don't need any other
        # checks, so just pass an empty value
        captcha = ReCaptchaValidator(
            self.context,
            self.request,
            None,
            INotUsefulForm['captcha'],
            None)
        try:
            captcha.validate(u'')
        except WrongCaptchaCode as e:
            widget = self.widgets['captcha']
            field = self.fields['captcha']
            # Wrap the error in ErrorViewSnippit
            captcha_error = getMultiAdapter(
                # (error, request, widget, field, form, content):
                (e, self.request, widget, field, self, self.context),
                IErrorViewSnippet)
            errors += (captcha_error, )

        if errors:
            self.status = self.formErrorsMessage
            return

        # Process the voting
        self._processVote(data)

        self.status = _(u'message_thank_you',
                        default=u'Thank you for voting!')
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(_(u'message_thank_you',
                                    default=u'Thank you for voting!'))
        came_from = self.request.get("HTTP_REFERER",
                                     self.context.absolute_url())
        self.request.response.redirect(came_from)


class UsefulForm(form.SchemaForm, WasThisUseful):
    """ Was useful form """
    schema = IUsefulForm
    ignoreContext = True
    useful = True
    label = _(u"Information was useful")
    description = ""
    name = "useful-form"

    def action(self):
        """ We nest the form, need a proper action """
        url = self.context.absolute_url() + "/@@useful-form"
        url = addTokenToUrl(url)
        return url

    def update(self):
        """ Hide the useful field, we set it per default """
        super(UsefulForm, self).update()
        self.widgets['useful'].mode = HIDDEN_MODE

    @button.buttonAndHandler(__(u'Submit'))
    def handleApply(self, action):
        data, errors = self.extractData()

        # CSRF
        authenticator = getMultiAdapter(
            (self.context, self.request), name=u"authenticator")
        if not authenticator.verify():
            raise Unauthorized

        # Process the voting
        self._processVote(data)

        self.status = _(u'message_thank_you',
                        default=u'Thank you for voting!')
        messages = IStatusMessage(self.request)
        messages.addStatusMessage(_(u'message_thank_you',
                                    default=u'Thank you for voting!'))
        came_from = self.request.get("HTTP_REFERER",
                                     self.context.absolute_url())
        self.request.response.redirect(came_from)

validator.WidgetValidatorDiscriminators(ReCaptchaValidator,
                                        field=INotUsefulForm['captcha'])
