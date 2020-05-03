"C:\Program Files (x86)\GanttProject-2.8\ganttproject.exe" -export csv D:/git/G2M/gantt.gan
timeout 2 > NUL

D:/git/G2M/g2m.exe
timeout 2 > NUL

start chrome --headless --incognito --disable-gpu --window-size=1600,900 --screenshot=D:/git/G2M/gantt_mermaid.png D:/git/G2M/gantt.html
timeout 2 > NUL

"C:\Program Files (x86)\GanttProject-2.8\ganttproject.exe" -export png D:/git/G2M/gantt.gan
timeout 2 > NUL