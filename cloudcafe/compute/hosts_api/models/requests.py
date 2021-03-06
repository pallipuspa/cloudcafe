"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import json
import xml.etree.ElementTree as ET

from cafe.engine.models.base import AutoMarshallingModel
from cloudcafe.compute.common.constants import Constants


class UpdateHostRequest(AutoMarshallingModel):
    """
    @summary: Update Request for a Host
    """
    ROOT_TAG_XML = "updates"

    def __init__(self, status=None, maintenance_mode=None):
        if status is not None:
            self.status = status
        if maintenance_mode is not None:
            self.maintenance_mode = maintenance_mode

    def _obj_to_json(self):
        return json.dumps(self.__dict__)

    def _obj_to_xml(self):
        xml = Constants.XML_HEADER
        element = ET.Element(self.ROOT_TAG_XML)
        for key, value in self.__dict__.iteritems():
            child = ET.Element(key)
            child.text = value
            element.append(child)
        xml += ET.tostring(element)
        return xml
