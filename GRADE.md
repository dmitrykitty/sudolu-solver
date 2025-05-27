Dear Student,

I'm happy to announce that you've managed to get **12** out of 15 points for this assignment.
<details><summary>You have already managed to pass 12 tests, so that is encouraging!</summary>&emsp;☑&nbsp;[1p]&nbsp;Grid&nbsp;post&nbsp;init&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Block&nbsp;size&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Block&nbsp;index&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Block&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Grid&nbsp;is&nbsp;printed&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;From&nbsp;text&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Main&nbsp;can&nbsp;solve&nbsp;puzzles<br>&emsp;☑&nbsp;[1p]&nbsp;Increment&nbsp;coordinates&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;Is&nbsp;excluded&nbsp;is&nbsp;implemented&nbsp;correctly<br>&emsp;☑&nbsp;[1p]&nbsp;DFS&nbsp;handles&nbsp;timeouts<br>&emsp;☑&nbsp;[1p]&nbsp;DFS&nbsp;detects&nbsp;end<br>&emsp;☑&nbsp;[1p]&nbsp;DFS&nbsp;finds&nbsp;correct&nbsp;solutions</details>

There still exist some issues that should be addressed before the deadline: **2025-05-28 08:00:00 CEST (+0200)**. For further details, please refer to the following list:

<details><summary>[1p] Project is configured correctly &gt;&gt; `pyproject.toml` is missing the `[project].description` config</summary></details>
<details><summary>[1p] Main handles puzzles with no solution &gt;&gt; `python -t 0.1 puzzles/unsolvableN2num1.txt` produces incorrect standard output:</summary>-&nbsp;got:<br>INFEASIBLE&nbsp;-&nbsp;puzzle&nbsp;grid:1,3,2,03,2,0,00,0,1,02,0,0,4<br>-&nbsp;expected:<br>INFEASIBLE<br>&emsp;-&nbsp;puzzle&nbsp;grid:<br>1,3,2,0<br>3,2,0,0<br>0,0,1,0<br>2,0,0,4</details>
<details><summary>[1p] Main handles timeout &gt;&gt; `python -t 0.0001 puzzles/sudokuN7num0.txt` produces incorrect standard output:</summary>-&nbsp;got:<br>timeout<br>-&nbsp;expected:<br>TIMEOUT</details>

-----------
I remain your faithful servant\
_Bobot_\
_May 26, AD 2025, 23:59:12 (UTC)_