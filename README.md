thefuck-gradle
==============

The Fuck rule for Gradle

As simple as the tool the fuck. [The Fuck][fuck] is a magnificent app which corrects your previous console command.

Usage
-----

When you type a Gradle task wrong, just type `fuck` after that and corrected task will be run. 

Install
-------

Copy the `gradle.py` file to `~/.thefuck/rules/` folder.

After that you have to enable it. 

First way is to edit `~/.thefuck/settings.py` file and it to the rules. 

```
rules = ['gradle']
require_confirmation = False
wait_command = 10
no_colors = False
debug = False
```

When it is done this way, I couldn't find a way to keep `DEFAULT_RULES`, you have to add the other rules manually, which is bad. 

The other way is to add an environment variable. In environment variable, you can directly add `DEFAULT_RULES`. Here is how:

```
export THEFUCK_RULES=DEFAULT_RULES:gradle
```

License
-------

    Copyright (C) 2016 Said Tahsin Dane

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.


[fuck]: https://github.com/nvbn/thefuck
