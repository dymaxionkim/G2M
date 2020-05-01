
# G2M

_GanttProject로 작성한 간트챠트 데이타를 html 파일로 변환해 주는 유틸리티_

![](gantt.png)


## 전제조건

* 구글 크롬 브라우저를 깔아두어야 합니다. (`gantt.png` 그림파일 생성용)
* [GanttProject 프로그램](https://www.ganttproject.biz/)을 깔아서 프로젝트 관리를 합니다. (`gantt.csv` 데이타 파일 생성용)


## GanttProject로 간트챠트 작성시 유의사항

* GanttProject 프로그램의 설정(`메뉴 프로젝트 - 수정 - 설정`)에서, `챠트 - 사용자 지정 간단한 날짜 형식`은 `yyyy-MM-dd`로 써넣어 주고, `CSV 형식으로 내보내기`는 가능한 모든 항목을 전부 다 체크해 주면 문제가 없습니다.
* Ganttproject 프로그램을 사용하고 싶지 않다면, 그냥 엑셀로 `ID, 이름, 시작일, 종료일, 완료` 이름으로 항목을 만들어 작성해 주셔도 됩니다.  이때 이름은, 아래의 태스크들을 포함하는 섹션 이름의 경우에는 그냥 써 주시면 되고, 각각의 스크들은 앞에 빈문자(Space)를 2개 넣어 주고 이름을 써 넣으면 됩니다.  시작일,종료일은 `2018-12-01` 형식으로 날짜를 써 주면 됩니다.  완료 항목은, 아직 시작하지 않은 경우에는 0, 완료한 경우에는 100으로 해 주시고 현재 진행중이라면 그 사이의 숫자를 넣어주시면 됩니다.
* 작성된 간트챠트를 `gantt.csv` 파일로 출력해 줍니다. (`메뉴 프로젝트 - 내보내기 - 쉼표 구분자 데이터 파일`)


## 사용방법 (MS윈도우)

* [GanttProject 프로그램](https://www.ganttproject.biz/)으로 간트챠트를 작성합니다.
* 작성한 간트챠트 데이타를 `gantt.csv` 파일로 출력합니다. ([gantt.csv 예제](https://github.com/dymaxionkim/G2M/blob/master/gantt.csv))
* `g2m.exe`, `g2m.bat` 파일을 `gantt.csv`파일이 있는 장소에 넣습니다. ( [g2m.exe 다운로드 링크](https://github.com/dymaxionkim/G2M/releases/download/V01/g2m.exe) )
* `g2m.bat` 파일을 더블클릭해서 실행합니다.  (최초 실행할 때는 윈도우OS의 디펜더가 작동해서 출처를 모르니깐 위험할 수 있다는 둥의 경고를 보여주는데 역시 무시하시면 됩니다.)
* 그러면 `gantt.html`, `gantt.png` 파일이 생성됩니다.


## 사용방법 (리눅스)

* [GanttProject 프로그램](https://www.ganttproject.biz/)으로 간트챠트를 작성합니다.
* 작성한 간트챠트 데이타를 `gantt.csv` 파일로 출력합니다. ([gantt.csv 예제](https://github.com/dymaxionkim/G2M/blob/master/gantt.csv))
* `g2m.py`, `g2m.sh` 파일을 `gantt.csv`파일이 있는 장소에 넣습니다.
* `g2m.sh` 파일을 실행합니다.
* 그러면 `gantt.html`, `gantt.png` 파일이 생성됩니다.



## MS윈도우용 실행파일(`g2m.exe`)를 빌드한 조건

* 윈도우10
* Anaconda3 설치
* pyinstaller 설치 : `pip install pyinstaller`
* 빌드 명령 : `pyinstaller --onefile --noconsole --icon=g2m.ico g2m.py`
