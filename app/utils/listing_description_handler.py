from dataclasses import dataclass
from typing import List

from app.settings import ROOT_DIR


@dataclass
class ListingDescriptionHandler:
    def create_description(self, platform_id: str, item_type: str, dimensions: str):
        self.__description: str = self.get_description_template(platform_id, item_type)
        dimensions_cm = self.prepare_dimensions_cm(dimensions)
        dimensions_inch = self.prepare_dimensions_inch(dimensions)
        self.replace_dimensions(dimensions_cm, "cm")
        self.replace_dimensions(dimensions_inch, "inch")
        self.prepare_final_formatting()
        print(self.__description)
        return self.__description

    def get_description_template(self, platform_id: str, item_type: str) -> str:
        match platform_id:
            case "ETSY":
                path = ROOT_DIR + f"app/listing_descriptions/etsy/{item_type}.txt"
            case "EBAY_US" | "EBAY_GB":
                path = ROOT_DIR + f"app/listing_descriptions/ebay/en/{item_type}.txt"
            case "EBAY_DE":
                path = ROOT_DIR + f"app/listing_descriptions/ebay/de/{item_type}.txt"

        with open(path, "r") as description_file:
            return description_file.read()

    def prepare_dimensions_cm(self, dimensions: str) -> List[str]:
        dimensions = dimensions.replace(".", ",")
        dimensions_cm: List = dimensions.split(";")
        return dimensions_cm

    def prepare_dimensions_inch(self, dimensions: str) -> List[str]:
        dimensions = dimensions.replace(",", ".")
        dimensions_cm: List = dimensions.split(";")
        dimensions_inch: List = [str(round(float(dimension) / 2.54, 1)) for dimension in dimensions_cm]
        dimensions_inch = [dimension if dimension[-1] != "0" else dimension[:-2] for dimension in dimensions_inch]
        return dimensions_inch

    def replace_dimensions(self, dimensions_list: List, dimension_unit: str) -> None:
        index = 1
        for dimension in dimensions_list:
            dimension_replace_id = "{{ dimension_" + str(dimension_unit) + "_" + str(index) + " }}"
            self.__description = self.__description.replace(dimension_replace_id, dimension)
            index += 1

    def prepare_final_formatting(self) -> None:
        self.__description = self.__description.replace("\n", "")
        self.__description = self.__description.replace("\r", "")

        loop_index = 0
        for _ in range(len(self.__description)):
            if self.__description[loop_index] == "\"":
                self.__description = self.__description[:loop_index] + "\\" + self.__description[loop_index:]
                loop_index += 2
            else:
                loop_index += 1
