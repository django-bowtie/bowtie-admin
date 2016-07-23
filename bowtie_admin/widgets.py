from django.contrib.admin.widgets import AdminTextareaWidget
from django.contrib.admin.widgets import AdminTextInputWidget
from django.utils.encoding import force_unicode, force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.utils.translation import ugettext_lazy as _


class WithCounterMixin(object):

    class Media:
        css = {'screen': ('css/character_counter.css',)}
        js = ('js/character_counter.js',)


class TextInputWithCounterWidget(WithCounterMixin, AdminTextInputWidget):

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        max_length = final_attrs.get('maxlength', False)

        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))

        html = format_html(
            '<input{} />'
            '<div id="{}-counter" class="character-counter">'
            '<span><span class="counter">{}{}</span> {}</span>'
            '</div>',
            flatatt(final_attrs),
            final_attrs['id'],
            force_unicode(len(value)),
            '' if not max_length else ' / %s' % (int(max_length) - len(value)),
            _('characters')
        )
        return mark_safe(html)


class TextAreaWithCounterWidget(WithCounterMixin, AdminTextareaWidget):

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, name=name)
        max_length = final_attrs.get('maxlength', False)

        html = format_html(
            '<textarea{}>\r\n{}</textarea>'
            '<div id="{}-counter" class="character-counter">'
            '<span><span class="counter">{}{}</span> {}</span>'
            '</div>',
            flatatt(final_attrs),
            force_text(value),
            final_attrs['id'],
            force_unicode(len(value)),
            '' if not max_length else ' / %s' % (int(max_length) - len(value)),
            _('characters')
        )
        return mark_safe(html)
