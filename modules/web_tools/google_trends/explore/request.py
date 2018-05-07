from modules.web_tools.google_trends.explore.abstract.explore_request import AbstractExploreRequest
from typing import Generator


class ExceptionExploreRequest(Exception):
    pass


class ExploreRequest(AbstractExploreRequest):
    __timeseries_widget_url = "https://trends.google.com.br/trends/api/widgetdata/multiline"
    __geo_map_widget_url = "https://trends.google.com.br/trends/api/widgetdata/comparedgeo"
    __related_searches_url = "https://trends.google.com.br/trends/api/widgetdata/relatedsearches"

    @property
    def timeseries_widgets(self) -> Generator[dict, None, None]:

        for widget in self.widgets:

            if "timeseries" in str(widget["id"]).lower():
                from modules.web_tools.google_trends.tools.url_setter import UrlSetter

                params = {
                    "hl": self.language,
                    "tz": self.timezone,
                    "req": widget["request"],
                    "token": widget["token"]
                }

                url = UrlSetter.gen_url(self.__timeseries_widget_url, params)

                response = self.session.get(url)

                if response.status_code != 200:
                    raise ExceptionExploreRequest(
                        "Não foi possível obter o Timeseries Widget. \n [Status Code: {0}]".format(
                            response.status_code))

                from modules.web_tools.google_trends.tools.fix import Fix
                import json

                yield json.loads(Fix.google_json(response.text))

    @property
    def geo_map(self) -> Generator[dict, None, None]:

        for widget in self.widgets:

            if "geo_map" in str(widget["id"]).lower():
                from modules.web_tools.google_trends.tools.url_setter import UrlSetter

                params = {
                    "hl": self.language,
                    "tz": self.timezone,
                    "req": widget["request"],
                    "token": widget["token"]
                }

                url = UrlSetter.gen_url(self.__geo_map_widget_url, params)

                response = self.session.get(url)

                if response.status_code != 200:
                    raise ExceptionExploreRequest(
                        "Não foi possível obter o Geo Map Widget. \n [Status Code: {0}]".format(
                            response.status_code))

                from modules.web_tools.google_trends.tools.fix import Fix
                import json

                yield json.loads(Fix.google_json(response.text))

    @property
    def related_topics(self) -> Generator[dict,None,None]:
        for widget in self.widgets:

            if "related_topics" in str(widget["id"]).lower():
                from modules.web_tools.google_trends.tools.url_setter import UrlSetter

                params = {
                    "hl": self.language,
                    "tz": self.timezone,
                    "req": widget["request"],
                    "token": widget["token"]
                }

                url = UrlSetter.gen_url(self.__related_searches_url, params)

                response = self.session.get(url)

                if response.status_code != 200:
                    raise ExceptionExploreRequest(
                        "Não foi possível obter o Related Topics Widget. \n [Status Code: {0}]".format(
                            response.status_code))

                from modules.web_tools.google_trends.tools.fix import Fix
                import json

                yield json.loads(Fix.google_json(response.text))

    @property
    def related_queries(self) -> Generator[dict,None,None]:
        for widget in self.widgets:

            if "related_queries" in str(widget["id"]).lower():
                from modules.web_tools.google_trends.tools.url_setter import UrlSetter

                params = {
                    "hl": self.language,
                    "tz": self.timezone,
                    "req": widget["request"],
                    "token": widget["token"]
                }

                url = UrlSetter.gen_url(self.__related_searches_url, params)

                response = self.session.get(url)

                if response.status_code != 200:
                    raise ExceptionExploreRequest(
                        "Não foi possível obter o Related Queries Widget. \n [Status Code: {0}]".format(
                            response.status_code))

                from modules.web_tools.google_trends.tools.fix import Fix
                import json

                yield json.loads(Fix.google_json(response.text))