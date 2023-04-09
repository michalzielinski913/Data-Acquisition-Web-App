from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Answer, RR_User

class AnswerCreateView(CreateView):
    model = Answer
    fields = ['text', 'title', 'wants_contact']

    def form_valid(self, form):

        form.instance.author = RR_User.objects.get(user_hash=self.id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('create_answer', kwargs={'id': self.id})

    def dispatch(self, request, *args, **kwargs):
        self.id = kwargs['id']  # Retrieve the ID from the URL
        if not RR_User.objects.filter(user_hash=self.id).exists():
            return HttpResponse(status=403)
        user=RR_User.objects.filter(user_hash=self.id)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user=RR_User.objects.filter(user_hash=self.id).get()
        context['total']=user.total_answers()
        context['new']=user.total_answers("NW")
        context['accepted']=user.total_answers("AC")
        context['rejected']=user.total_answers("RJ")
        # Add your custom logic here

        return context