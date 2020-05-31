from typing import Dict, List
from ...domain.util import list_to_str
from .data_validation import check_rgb_list

class color_map:
    def __init__(self, rgbs: List[List[int]], indices: List[int]):
        self.rgbs = rgbs
        self.indices = indices

    def __repr__(self) -> str:
        return ",".join(str(e) for e in self.get_rgbs_flat()) + ":" + ",".join(str(e) for e in self.indices)

    def get_rgbs_flat(self) -> List[int]:
        retVal = []
        for i in range(len(self.rgbs)):
            curr = self.rgbs[i]
            retVal.append(curr[0])
            retVal.append(curr[1])
            retVal.append(curr[2])
        return retVal

    def get_matrix(self) -> List[List[int]]:
        retVal = []
        for i in range(0, len(self.indices)):
            rgbIndex = self.indices[i]
            retVal.append(self.rgbs[rgbIndex])
        return retVal

    @classmethod
    def from_rep(cls, repr: str):
        comps = repr.split(":")
        if len(comps) == 2:
            rgbStrs = comps[0].split(",")
            indicesStrs = comps[1].split(",")
            indices = [int(s) for s in indicesStrs]
            rgbs = []
            for i in range(0, len(rgbStrs), 3):
                rgbs.append([int(rgbStrs[i]), int(rgbStrs[i + 1]), int(rgbStrs[i + 2])])
            return cls(rgbs, indices)


class color_dict_entry:
    def __init__(self, i: int, rgb: List[int]):
        self.index = i
        self.rgb = [rgb[0], rgb[1], rgb[2]]

    def __str__(self) -> str:
        return "index: " + str(self.index) + ", rgb: " + str(self.rgb)
    def __repr__(self) -> str:
        return self.__str__()

SENSE_HAT_LED_MATRIX_SIDE = 8

class color_map_builder:
    def __init__(self, matrix_side: int = SENSE_HAT_LED_MATRIX_SIDE):
        self.clear(matrix_side)

    def __str__(self) -> str:
        return "color_map: " + str(self.color_dict) + '\n' + "indices: " + list_to_str(self.indices)

    def clear(self, matrix_side: int = SENSE_HAT_LED_MATRIX_SIDE) -> None:
        if matrix_side < 1:
            raise ValueError("matrix_side < 1 : " + str(matrix_side))

        self.matrix_side = matrix_side
        self.matrix_pixel_count = matrix_side * matrix_side
        self.matrix_size = self.matrix_pixel_count * 3

        self.color_dict = {}
        self.indices = []
        self.__next_index = 0        


    def get_pixel_count(self):
        return len(self.indices)

    def get_missing_pixels(self) -> int:
        return self.matrix_pixel_count - self.get_pixel_count()

    def is_complete(self) -> bool:
        return self.get_missing_pixels() == 0

    def add(self, rgb: List[int]) -> None:
        check_rgb_list(rgb)

        if (self.is_complete()):
            raise ValueError("Matrix is complete")

        key = str(rgb[0]) + '_' + str(rgb[1]) + '_' + str(rgb[2])
        if key in self.color_dict:
            self.indices.append(self.color_dict[key].index)
            return
        entry = color_dict_entry(self.__next_index, rgb)
        self.color_dict[key] = entry
        self.indices.append(self.__next_index)
        self.__next_index = self.__next_index + 1

    def build(self) -> color_map:
        if not self.is_complete():
            raise ValueError("Missing pixels: got " + str(self.get_pixel_count()) + " but matrix has " + str(self.matrix_pixel_count))

        colors = [[]] * len(self.color_dict)
        for e in self.color_dict.values():
            colors[e.index] = e.rgb
        return color_map(colors, self.indices.copy())
    