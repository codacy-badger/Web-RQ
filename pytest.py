# !/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from code_test import packages_check

from modules.web_tools.google_trends.explore.request import ExploreRequest

explore = ExploreRequest()

# Search settings
explore.category = ""  # empty = all
explore.timezone = 180
explore.language = "en-US"

# We can define where these data will come from, I want it to be from the searches made.
from modules.web_tools.google_trends.explore.consts.sources import WEB

explore.source = WEB

# Now, let's define the items that will be searched.
# In geo you can also use cities, for example if I wanted to get the Federal District of Brazil, I could use: BR-DF
# Google has some different methods for picking up a date.
from modules.web_tools.google_trends.explore.consts.date import EVER

explore.add_item(explore.new_item(keyword="carro", geo="BR", time=EVER)). \
    add_item(explore.new_item(keyword="moto", geo="BR", time=EVER))

# Attention, the first item added will be who will define the "geo" of the explore, however the widgets will respect the geo that was selected in your item.
# We can get the dataset from explore.
print(explore.explore)

# And you can also get the data for each widget.
for widget in explore.timeseries_widgets:
    print(widget)

for widget in explore.geo_map:
    print(widget)

for widget in explore.related_topics:
    print(widget)

for widget in explore.related_queries:
    print(widget)