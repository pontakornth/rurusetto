from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rulesets/', views.listing, name='listing'),
    path('new/', views.create_ruleset, name='create_ruleset'),
    path('changelog/', views.changelog, name='changelog'),
    path('rulesets/<slug:slug>', views.wiki_page, name='wiki'),
    path('rulesets/<slug:slug>/beatmaps', views.recommend_beatmap, name='recommend_beatmap'),
    path('rulesets/<slug:slug>/edit', views.edit_ruleset_wiki, name='edit_wiki'),
    path('rulesets/<slug:slug>/new/subpage', views.add_subpage, name='add_subpage'),
    path('rulesets/<slug:rulesets_slug>/<slug:subpage_slug>', views.subpage, name='subpage'),
    path('rulesets/<slug:rulesets_slug>/<slug:subpage_slug>/edit', views.edit_subpage, name='edit_subpage'),
    path('rulesets/<slug:slug>/new/beatmaps', views.add_recommend_beatmap, name='add_recommend_beatmap'),
    path('rulesets/<slug:rulesets_slug>/manage/beatmaps', views.recommend_beatmap_approval, name='recommend_beatmap_approval'),
    path('rulesets/<slug:rulesets_slug>/manage/beatmaps/approve/<int:beatmap_id>', views.approve_recommend_beatmap, name='approve_recommend_beatmap'),
    path('rulesets/<slug:rulesets_slug>/manage/beatmaps/deny/<int:beatmap_id>', views.deny_recommend_beatmap, name='deny_recommend_beatmap'),
    path('install', views.install, name='install'),
    # URL path for API
    path('api/rulesets', views.ruleset_list),
    path('api/rulesets/<slug:slug>', views.ruleset_detail)
]