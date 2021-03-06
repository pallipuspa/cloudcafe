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


from cafe.engine.behaviors import BaseBehavior

class ImagesV2Behaviors(BaseBehavior):
    """
    @summary: Base Behaviors class for Images V2 API tests
    """

    def __init__(self, images_client, images_config):
        super(ImagesV2Behaviors, self).__init__()
        self.config = images_config
        self.client = images_client
