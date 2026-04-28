from django.shortcuts import HttpResponse, render
from auth_app.models import Post_Wallpaper
from django.views.generic import ListView
from auth_app.models import Post_Wallpaper
from django.template.loader import render_to_string
from django.http import JsonResponse


class home(ListView):
    model = Post_Wallpaper
    template_name = 'home.html'
    context_object_name = 'uploaded_images'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset().select_related('user').prefetch_related('likes')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.session.session_key:
            self.request.session.create()
        context['session_key'] = self.request.session.session_key
        return context

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('image_list.html', context, request=request)
            return JsonResponse({
                'images_html': html,
                'has_next': context['page_obj'].has_next()
            })
        return self.render_to_response(context)
