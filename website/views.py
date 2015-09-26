from django.views.generic import TemplateView
from website.models import MENU, PAGES, P404, SERVICES


class HtmlTemplate(TemplateView):

    def get_context_data(self, page_name='index.html', **kwargs):

        page=PAGES.get(page_name, P404)

        kwargs.update(
            dict((k, v[0] if len(v)==1 else v) for k,v in self.request.GET.items()),
            title='NCC 4 ROMA',
            author='Riccardo Federici',
            email='info@ncc4roma.it',
            phone='+39 338 96 69 491',
            menu=MENU,
            services=SERVICES,
            page_name=page.url,
            page=page
        )
        return super().get_context_data(**kwargs)

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template='html/%s' % context['page_name'],
            context=context,
            using=self.template_engine,
            **response_kwargs
        )