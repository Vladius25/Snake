https://gitlab.com/sicamp-py/introductory-work-2018

# Описание параллели

Параллель для тех кому интересно не только олимпиадное программирование.

### Как это было в том году

В первой части смены мы:

 * вспоминали Python,
 * изучали основы ООП,
 * познакомились с юнит-тестированием, TDD и Mock'ами,
 * говорили про чистый код, как его писать и почему это важно,
 * учились пользоваться инструментами командной разработки, основной из которых -- система контроля версий Git.

Во второй части смены мы разбились на 2 команды, которые занимались независимыми проектами: новой реализацией серверной части проверяющей системы (на которой сейчас и работает вступительная в остальные параллели) и лагерным telegram-ботом.

### Что будет в этом

Как и в том году мы расскажем вам про unit-тестирование, проектирование, чистый код, TDD, git и другие темы, которые не только встречаются каждый день в разработке, но и очень интересны сами по себе.

В этом году мы попробуем больше времени уделить работе над проектами: смена не будет разделена на две части и будет возможно сразу попробовать в деле новые знания в своих проектах.

Кроме того мы попробуем парное программирование, посоревнуемся в написании ботов, поиграем в code-retreat и не только.

Также в этом году мы подготовили анкету для поступающих в параллель P. В зависимости от ответов мы можем изменить формат и программу параллели.

### Что мы ждём от поступающих в P

Если кратко, то:

 * умение писать код,
 * самостоятельность,
 * любознательность,
 * некоторый уровень знания Python.

Умение писать код значит, что программирование не должно быть для вас магией.
Вы должны понимать как работает код: тот, который пишете вы, и тот, который написан кем-то ещё.
И вы должны уметь писать код, который делает то, что вы хотите, и который способен понять кто-то ещё.
Нужно уметь это хотя бы для одного языка программирования.

Самостоятельность подразумевает, что столкнувшись с проблемой, вы пойдёте искать её решение и постараетесь справится с ней сами, перед тем как искать помощи извне. Мы считаем это важным, потому что именно при самостоятельном решении проблем и происходит рост. Если что, это не значит, что нужно ВСЕ проблемы решать самостоятельно: в лагере будет много замечательных людей, которые с радостью вам помогут.

Под любознательностью мы имеем в виду, что вам действительно нравится программирование и хочется изучать что-то новое. Согласитесь, как-то грустно ехать в эту параллель, если вы не любите программировать?

Некоторый уровень знания Python нужен потому, что задания для занятий мы подготовили именно на нём. Кроме того, для групповых активностей нужно чтобы был хотя бы один язык, который знают все.

Мы верим, что те, кто прошли параллель B' или выше в ЛКЛ или ЛКШ, обладают всем вышеперечисленным (ну, может кроме знания Python).

Для проверки того, насколько вы готовы к параллели P, мы подготовили вступительную работу. Ничего страшного, если вы еще не знакомы с Python. Вступительная работа нужна в том числе для того, чтобы освоиться в нём. Ниже вы сможете найти ссылки для его изучения.

## Подготовка к вступительной работе (и к работе в параллели P)

Программировать во вступительной и в течение смены будем в основном на Python 3. Основные причины такого выбора: кроссплатформенность, простота в освоении, огромное количество библиотек и готовых решений разных задач.

В связи с этим, для выполнения вступительной вам нужно:

 1.  Установить [Anaconda](https://www.anaconda.com/download/) - дистрибутив Питона (версии 3.6) с множеством полезных библиотек под любую ОС. Именно его мы будем использовать в течение смены.
 
 2.  Установить [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/). Создать проект PyCharm - это просто папка с исходниками на питоне. Выбрать в качестве интерпретатора питона `Anaconda`.
    Создайте в проекте `Python File` и можете писать код.

    ![как создать проект](/images/createProject.png)
 
 3. Изучить Python.

Anaconda и PyCharm доступны под Windows, Linux и Mac, для работы над вступительной и в лагере вам не нужно переходить на другую операционную систему.

#### Материалы на английском

 - http://www.learnpython.org - интерактивный самоучитель
 - https://docs.python.org/3/tutorial/index.html - официальное руководство на сайте Python'а
 - https://stephensugden.com/crash_into_python - Питон за пару часов, очень сжато основные особенности языка, для тех, кто уже хорошо знает несколько других языков
 - Курс на [Codecademy](https://www.codecademy.com/learn/python) - долгий и подробный курс на английском для новичков в программировании

#### Материалы на русском

 - [pythontutor](http://pythontutor.ru) - интерактивный, очень подробный самоучитель
 - https://ru.wikibooks.org/wiki/Python/Учебник_Python_3.1 - перевод руководства с официального сайта, немного устаревший

Если вы знаете какие-то другие хорошие материалы для изучения языка (особенно на русском) - мы будем рады о них узнать.

# Описание вступительной

В качестве вступительной вам требуется разобраться в уже написанной и работающей игре "Змейка" и реализовать в ней дополнительные функции.
Код программы находится в данном репозитории.

## Змейка

Мы уже реализовали для вас заготовку для игры "змейка", где:

- Имеется клеточное поле NxM.
- На поле находится змейка - цепь смежных по стороне клеток без самопересечений. У змейки имеется голова (один из концов цепи), которая смотрит в одном из четырех направлений (←, →, ↑, ↓).
- Каждые `UPDATE_INTERVAL` миллисекунд игра переходит в следующее состояние, а именно, змейка делает ход. Голова змеи двигается в смежную клетку в том направлении, куда она смотрит, а каждая из остальных клеток змейки переходит в следующую за ней клетку змейки (в ту, которая ближе к голове). Клетка, где был хвост змейки, при этом освобождается.
- Если змейка не может сделать ход (голова змеи уперлась в границу поля и смотрит в направлении стены), то игра заканчивается.
- Клавиши со стрелками позволяют менять направление, в котором смотрит голова змейки.
- На поле также имеются клетки с пищей. При попадании головы змейки на клетку с пищей длина змейки увеличивается на 1, и появляется новый кусочек пищи в произвольной свободной клетке поля. За съедание еды начисляются очки.

### Как скачать проект

**Способ 1** (предпочтительный): Склонировать проект по SSH или HTTPS с основной вкладки проекта.

**Способ 2**: В самом верху данной страницы щелкнуть по значку загрузки и выбрать любой из предложенных форматов архива

![как скачать проект](/images/download.png)


### Как запустить проект

Для запуска проект требует библиотеку PyQT5.
Она должна поставиться вместе с Anaconda и устанавливать её отдельно не требуется.

В PyCharm'е нужно открыть(File->Open) папку с проектом.

![как открыть проект](/images/open.png)

В открывшемся проекте найти файл `run.py`. Нажать правой кнопкой мыши по нему и выбрать в открывшемся контекстном меню пункт `Run 'run'`

![как запустить игру](/images/run.png)

Если всё хорошо, то откроется форма со змейкой, в которую можно поиграть.

Управление:
 * клавиши верх, вниз, влево, вправо - поворот змейки
 * пробел - начать или приостановить игру

## Задание

Вам нужно выполнить реализовать новые функции из списка, приведенного ниже, дописав/изменив код нашей программы. Не бойтесь экспериментировать и вносить изменения в наш код.

Не обязательно реализовывать всё: время выполнения вступительной работы ограничено.
Лучше сделать меньше, но качественней.

Список функций:
 1. Реализуйте два новых вида пищи:
    - Ядовитый: при поедании уменьшает длину змейки на 1 и появляется в другой свободной клетке поля
    - Смертельный: при его поедании игра заканчивается. Такая пища существует в единственном экземпляре и иногда меняет своё местоположение на другую свободную клетку
    
    Все виды пищи должны быть разных цветов, отличимых друг от друга человеческим глазом

 2. При смене направления змеи на противоположное к текущему, голова и хвост змейки меняются местами, и она ползёт в противоположном направлении.
 3. Окружите поле четырьмя стенами. В классическом варианте змейки столкновение со стеной смертельно. В вашей реализации стены должны быть следующих типов:
    - Упругая стена: при столкновении с ней голова и хвост змеи меняются местами и змейка движется в противоположном направлении.
    - Смертельная стена: при столкновении змейки со стеной игра заканчивается.
    - 2 стены-телепорта: змейка входит в одну из этих стен, а выходит из другой стены. Эти стены могут быть соседними или противоположными, решайте сами.
    
    Стены разных типов должны быть окрашены в разные цвета.
 4. Можете придумать что-нибудь ещё =)

Мы намеренно не уточняем некоторые детали. Попробуйте сами подумать в некоторых ньюансах и возможностях. Например, не сломается ли программа, если стены-телепорты окажутся не на противоположных сторонах. Или если змейка входит в восточную стену-телепорт, а выходит из западной, то на какой горизонтали поля она должна выходить.


## Что мы хотим увидеть в вашей работе

Во вступительной работе мы хотим проверить всё, что мы ждём от поступающих в P. В том числе:

 * насколько хорошо вы можете читать и разбираться в уже существующем коде,
 * насколько хорошо у вас получается писать код так, чтобы в нём смог разобраться кто-то кроме вас,
 * насколько хорошо вы освоили Python

Обратите внимание, что в отличии от олимпиадных параллелей мы не требуем писать наиболее эффективный код
или ставим какие-то жесткие ограничения по времени и памяти.

В написании понятного кода вам могут помочь советы ниже.

## Как сдать вступительную работу

В скором времени на сайте https://sicamp.ru можно будет прикрепить архив/ссылку на репозиторий с выполненной работой. Следите за новостями.

Не забудьте заполнить [тематическую анкету](https://sicamp.ru/forms/edit/lkl-2018-parallel-p) для поступающих в P.

Работы и анкеты принимаются до 27 мая, 23:59 по московскому времени.

## Советы по написанию "чистого" кода:

- Код должен быть читаемым
    - Соблюдайте отступы (Python же) и расставляйте пробелы, где это нужно. Мы рекомендуем придерживаться общепринятого стиля написания Python-кода: PEP 8 [(rus)](http://defpython.ru/pep8) [(eng)](https://www.python.org/dev/peps/pep-0008/)
    - Придумывайте хорошие имена переменным и параметрам функций/методов: они должны отражать смысл, а не тип содержимого. Избегайте коротких имён (1-2 символа), их использование допустимо разве что в циклах и лямбдах.
    - Правильное имя функции/метода должно содержать **глагол**: `get_distance`, `set_position`.
    - Тело функции должно вмещаться в один экран вашего монитора и не должно содержать большую вложенность из условий и/или циклов (в идеале, вложенность < 3). Если это не так, скорее всего, нужно выделить часть кода в отдельную функцию.
    - Ne ispol'zuyte [translit](https://ru.wikipedia.org/wiki/Транслитерация) v vashem kode.
- В задачах не требуется укладываться в жесткие ограничения по времени/памяти, поэтому между эффективностью кода и его читаемостью, выбирайте читаемость.
- Избегайте повторяющегося кода. Если два или более куска кода выглядят похоже, это сигнал к тому, что нужно выделить метод.
- Пишите структурированный код, это помогает уменьшить число зависимостей в вашей программе:
    - Используйте классы, прячьте связанную с ними логику в методы класса.
    - Избегайте использования глобальных переменных.
    - Объявляйте локальные переменные как можно ближе к месту использования
- Пользуйтесь возможностями языка, чтобы сделать код более лаконичным и понятным.


## Как с нами связаться?

Если у вас остались вопросы по поводу вступительной, не стесняйтесь задавать их нам в личных сообщениях в ВК:
- [Александр Анкудинов](https://vk.com/xelez)
- [Антон Чаплыгин](https://vk.com/anton92nd).

Успехов вам в выполнении вступительной работы! Следите за новостями в группе [ЛКЛ](https://vk.com/sicamp).
