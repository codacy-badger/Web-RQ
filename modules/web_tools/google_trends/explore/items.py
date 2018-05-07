from modules.web_tools.google_trends.explore.item import ExploreItem
from typing import List


class ExploreItems(object):
    __items = []

    def new_item(self, keyword: str, geo: str = "", time: str = "now 1-H") -> ExploreItem:
        item = ExploreItem()
        item.keyword = keyword
        item.geo = geo
        item.time = time
        return item

    def add_item(self, item: ExploreItem):
        self.__items.append(item)
        return self

    @property
    def items(self) -> List[ExploreItem]:
        return self.__items

    @property
    def comparison_list(self) -> List[dict]:
        comparison: List[dict] = []

        for item in self.items:
            comparison.append(item._item_dict)

        return comparison
