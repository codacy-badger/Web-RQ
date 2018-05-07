from modules.web_tools.google_trends.insights.abstract.latest import AbstractLatest


class Latest(AbstractLatest):
    # TODO: Preciso adicionar algo para definir as constantes de categorias, pois as mesmas não valem para o tools\categories.py.
    def get_latest(self) -> dict:
        from modules.web_tools.google_trends.tools.url_setter import UrlSetter
        from modules.web_tools.google_trends.tools.fix import Fix
        import requests

        response = requests.get(UrlSetter.gen_url(self._api_url, self._params))

        latest = {}


        if response.status_code == 200:
            # Se obtivemos uma resposta positiva, vamos tratar o JSON
            json_str = Fix.google_json(response.text)

            import json
            latest = json.loads(json_str)

        else:
            raise ExceptionLatest("Status code: {0}".format(response.status_code))

        return latest


class ExceptionLatest(Exception):
    pass