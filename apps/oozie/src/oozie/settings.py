# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DJANGO_APPS=['oozie']
NICE_NAME = "Oozie Editor/Dashboard"
REQUIRES_HADOOP = True

# Unused
PERMISSION_ACTIONS = (
  ("launch_editor", "Launch the Oozie Editor"),
  ("launch_dashboard", "Launch the Oozie Dashboard"),
  ("launch_jobs", "Can submit Oozie jobs"),
)

ICON = "/oozie/static/art/icon.png"
MENU_INDEX = 41

IS_URL_NAMESPACED = True