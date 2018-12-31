from django.views.generic import ListView,DetailView,TemplateView 
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView 
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.views.generic import FormView #클래스형 제네릭뷰
# Create your views here.
from django.views.generic.edit import FormView
from streaming.forms import MusicSearchForm
from django.db.models import Q 
from django.shortcuts import render #단축함수 render
from streaming.models import * 



class StreamingView(TemplateView): 
    template_name="streaming/streaming.html"


class SearchFormView(FormView): 
    form_class = MusicSearchForm 
    template_name = 'streaming/streaming_search.html'

    def form_vaild(self,form): 
        schWord = '%s' % self.request.POST['search_word']
        music_list = Music.objects.filter(Q(title__icontains=schWord) | Q(artist__icontains=schWord) | Q(album__icontains=schWord) 
                    | Q(genre__icontains=schWord)).distinct() 

        context = {}
        context['form'] = form 
        context['search_term'] = schWord 
        context['object_list'] = music_list 

        return render(self.request, self.template_name, context) 

class StreamingDetail(DetailView): 
    model = Music 


