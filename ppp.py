#!/usr/bin/env python
# encoding: utf-8

from bk3d_to_huxing_test import bk_3d_data
import uuid
import ujson as json
import copy

room_itemNo = "9d6f2c5c6a0811e79b2e000c29daddf7"
door_type = 201
opening_mirror = 0
opening_archHeight = 0
wall_bearing = 0
wall_parapet = 0
wall_structType = 101
wall_length = 12
wall_height = 280
room_interval = 120
scale = 0.1


def bk3d_to_hraw_data(bk_data):

    raw_data = dict()
    raw_data['setting'] = {
        "orientation": 0,
        "storeyHeight": 280,
        "rulerUnit": 1
    }
    raw_data['notes'] = []
    raw_data['models'] = []
    raw_data['rooms'] = []
    raw_data['openings'] = []
    raw_data['corners'] = []
    raw_data['walls'] = []

    room_name_dict = {}
    room_corner_dict = {}

    # rooms
    room_dict = {}
    room_info = bk_data["atadGvsPaminim"]
    for index, item in enumerate(room_info["gvsPaminim"][0]):
        tag = room_info["semanMoor"][index]
        name = create_uuid()
        room_data = {
            "name": name,
            "itemNo": room_itemNo,
            "tag": tag
        }
        points = []
        for coordinate in item:
            x = coordinate["x"]
            y = coordinate["y"]
            points.append(coordinate_convert(x,y,bk_data))
        room_data["points"] = points[:-1]
        raw_data['rooms'].append(room_data)

        room_dict[name] = room_data
        room_name_dict[tag] = name
        room_corner_dict[tag] = points

    # corners
    corner_dict = {}
    corners_list = []
    for tag, corners in room_corner_dict.items():
        for corner in corners:
            corners_list.append((corner["x"], corner["y"]))

    all_corners = list(set(corners_list))
    for corner in all_corners:
        name = create_uuid()
        corner_item = {
            "x": corner[0],
            "y": corner[1],
            "name": name
        }
        raw_data["corners"].append(corner_item)
        corner_dict["{}_{}".format(corner[0], corner[1])] = corner_item

    # update corners name
    for tag, points in room_corner_dict.items():
        points_new = []
        for point in points:
            points_new.append(corner_dict["{}_{}".format(point["x"], point["y"])])
        room_corner_dict[tag] = points_new

    # insert corners to walls
    for tag, corners in room_corner_dict.items():
        corners_tmp = copy.copy(corners)
        insert_count = 0
        for index, _ in enumerate(corners[:-1]):
            for corner in corner_dict.values():
                if corners[index]["x"] == corners[index+1]["x"]:
                    if corner["x"] == corners[index]["x"]:
                        if corners[index]["y"] > corners[index+1]["y"]:
                            if corners[index]["y"] > corner["y"] > corners[index+1]["y"]:
                                corners_tmp.insert(index+insert_count, corner)
                                insert_count += 1
                        elif corners[index]["y"] < corners[index+1]["y"]:
                            if corners[index]["y"] < corner["y"] < corners[index + 1]["y"]:
                                corners_tmp.insert(index + insert_count, corner)
                                insert_count += 1
                elif corners[index]["y"] == corners[index + 1]["y"]:
                    if corner["y"] == corners[index]["y"]:
                        if corners[index]["x"] > corners[index + 1]["x"]:
                            if corners[index]["x"] > corner["x"] > corners[index + 1]["x"]:
                                corners_tmp.insert(index + insert_count, corner)
                                insert_count += 1
                        elif corners[index]["x"] < corners[index + 1]["x"]:
                            if corners[index]["x"] < corner["x"] < corners[index + 1]["x"]:
                                corners_tmp.insert(index + insert_count, corner)
                                insert_count += 1
        room_corner_dict[tag] = corners_tmp

    # walls
    wall_dict = {}
    wall_data_list = {}
    for tag, corners in room_corner_dict.items():
        for index, _ in enumerate(corners[:-1]):
            name = create_uuid()
            wall_data = {
                "length": wall_length,
                "height": wall_height,
                "bearing": wall_bearing,
                "parapet": wall_parapet,
                "backwardRoomName": "",
                "forwardName": create_uuid(),
                "backwardName": create_uuid(),
                "startName": create_uuid(),
                "startCornerName": corners[index]["name"],
                "stopName": create_uuid(),
                "stopCornerName": corners[index+1]["name"],
                "name": name,
                "structType": wall_structType,
                "forwardRoomName": room_name_dict[tag]
            }
            # update backwardRoomName
            if "{}_{}".format(corners[index+1]["name"], corners[index]["name"]) in wall_dict:
                wall_data["backwardRoomName"] = wall_dict["{}_{}".format(corners[index]["name"], corners[index+1]["name"])]
                wall_data_list[wall_dict["{}_{}".format(corners[index]["name"], corners[index+1]["name"])]]["backwardRoomName"] = name
            wall_dict["{}_{}".format(corners[index]["name"], corners[index+1]["name"])] = name
            wall_data_list[name] = wall_data

    for name, wall_data in wall_data_list.items():
        raw_data["walls"].append(wall_data)

    # openings

    return json.dumps(raw_data)


def coordinate_convert(x, y, bk_data):
    origin = bk_data["minimap"]["bounding"]["origin"]
    xx = origin["x"]
    yy = origin["y"]
    xxx = (x-xx) * scale
    yyy = -(y-yy) * scale
    return {"x": xxx, "y": yyy}


def create_uuid():
    return str(uuid.uuid1()).replace('-', '')


if __name__ == '__main__':
    rs = bk3d_to_hraw_data(bk_3d_data)
    print(rs)

