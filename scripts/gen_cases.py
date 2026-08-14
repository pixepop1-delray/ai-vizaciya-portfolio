# -*- coding: utf-8 -*-
"""Генератор 6 страниц-разборов кейсов для ai-garage.tech → /cases/<slug>/index.html"""
import os, urllib.parse, html

ROOT = "/Users/uliana/Desktop/VIBE CODING/ai-vizaciya-portfolio"

CASES = [
dict(
  slug="ii-sekretar",
  doctitle="Кейс: ИИ-секретарь для Google Calendar — ИИ-Гараж",
  metadesc="Разбор кейса: Telegram-агент ведёт Google Календарь голосом — встречи, переносы, таймзоны, брифинги. 207 автотестов, ноль ручного ввода.",
  eyebrow="разбор кейса · операционка",
  h1="ИИ-секретарь: календарь, который ведёт себя сам",
  lead="Планирование съедает внимание каждый день: переписки «когда вам удобно?», каскадные переносы, забытые звонки. Мы отдали календарь агенту в Telegram — и вернули руководителю около часа в день.",
  metrics=[("207", "автотестов в системе"), ("0", "ручного ввода в календарь"), ("24/7", "работает без выходных")],
  task=[
    "Клиент — руководитель консалтинговой практики: 15–20 встреч в неделю, клиенты и подрядчики в трёх часовых поясах. Календарь вёлся руками: каждая договорённость — это переписка, перенос одной встречи тянул за собой три другие, а пару раз звонки просто терялись.",
    "Задача: чтобы календарь можно было вести голосом на ходу — а система сама следила за конфликтами, ссылками на видеозвонки и напоминаниями.",
  ],
  chat=[
    ("Клиент", "Перенеси завтрашний звонок с подрядчиком на четверг после обеда и добавь Meet"),
    ("Агент", "Готово: «Звонок с подрядчиком» → четверг 14:30. Meet-ссылка добавлена в приглашение. Конфликтов с другими встречами нет."),
    ("Клиент", "Поставь йогу каждый понедельник и пятницу в 8 утра на 8 недель"),
    ("Агент", "Создана серия: 16 событий «Йога», пн и пт 08:00, до 9 октября. Первое — уже в понедельник."),
  ],
  features=[
    "Встречи создаются, переносятся и отменяются голосом или текстом — прямо из Telegram",
    "Ссылки Google Meet или Zoom добавляются в приглашение автоматически",
    "Часовые пояса пересчитываются сами; конфликты времени агент перехватывает до того, как они случились",
    "Повторяющиеся серии понимает с одной фразы — «каждый пн и пт на 8 недель»",
    "Утром — брифинг дня, перед встречами — напоминания",
    "Массовые действия (снести неделю, перенести всё) — только после подтверждения",
  ],
  principles=[
    "Даты, пересечения и таймзоны считает программный код, а не нейросеть — одна и та же команда всегда даёт один и тот же результат",
    "Система покрыта 207 автотестами и живёт на отдельном сервере клиента",
  ],
  results=[
    "Календарь полностью ведётся голосом — ручной ввод исчез",
    "Конфликты времени перехватываются автоматически, встречи не теряются",
    "Около часа в день вернулось руководителю",
  ],
  stack=["Telegram", "Google Calendar API", "Meet / Zoom", "Voice", "Docker"],
  related=("Как внедрить ИИ-ассистента в бизнес — гайд в блоге", "../../blog/kak-vnedrit-ii-assistenta-v-biznes/"),
  cta="Здравствуйте! Видел(а) разбор кейса «ИИ-секретарь». Хочу похожее решение для своего календаря.",
),
dict(
  slug="menedzher-zadach",
  doctitle="Кейс: менеджер задач голосом с Trello — ИИ-Гараж",
  metadesc="Разбор кейса: руководитель ставит задачи голосом в Telegram, бот сам создаёт карточки в Trello, следит за статусами и не даёт задачам потеряться.",
  eyebrow="разбор кейса · операционка",
  h1="Менеджер задач: из голосового — в карточку на доске",
  lead="Задачи, поставленные в общем чате, живут три часа: их перечитывают, переспрашивают и забывают. Мы сделали бота, который превращает голосовое сообщение в карточку на доске — с исполнителем и сроком.",
  metrics=[("100%", "задач доходят до доски"), ("2 клика", "на отчёт о статусе"), ("24/7", "мониторинг доски")],
  task=[
    "Клиент — команда из десяти человек: монтажники, снабжение, офис. Руководитель ставил задачи голосом в общий чат — на бегу, между объектами. Дальше начиналось: «а кому это было?», «а до какого числа?», «а это вообще сделали?». Планёрки уходили на восстановление картины.",
    "Задача: сохранить привычный способ — голос в Telegram — но чтобы каждая задача автоматически попадала на доску с исполнителем, сроком и статусом.",
  ],
  chat=[
    ("Руководитель", "Запиши на Диму: до пятницы собрать смету по объекту на Лесной"),
    ("Бот", "Карточка создана: «Смета — объект на Лесной» · исполнитель Дима · срок пятница. Дима получил уведомление."),
    ("Дима", "[нажимает кнопку «Выполнено» под задачей]"),
    ("Бот", "«Смета — объект на Лесной» → Готово. Руководитель уведомлён, карточка перенесена в Done."),
  ],
  features=[
    "Задача голосом или текстом — бот сам вытаскивает суть, исполнителя и срок",
    "Каждая задача — карточка в Trello; доска и чат синхронизированы в обе стороны",
    "Сотрудники отчитываются кнопками, а не сочинениями в чате",
    "Изменения на доске — мгновенные уведомления тем, кого касается",
    "Новый сотрудник подключается за минуты: бот сам проводит онбординг",
    "Сторож-процесс следит за системой и сам восстанавливает её после сбоев",
  ],
  principles=[
    "Бот не «додумывает» задачи: если исполнитель или срок неясны — переспросит, а не назначит наугад",
    "Система живёт на отдельном сервере клиента и не зависит от наших мощностей",
  ],
  results=[
    "Ни одна задача из чата больше не теряется — всё на доске",
    "Руководитель видит статусы без вопросов «ну что там?»",
    "Планёрки сократились: картина дня всегда актуальна",
  ],
  stack=["Telegram", "Trello API", "Voice", "Docker"],
  related=("Telegram-бот с ИИ для бизнеса: 7 задач — статья в блоге", "../../blog/telegram-bot-s-ii-dlya-biznesa/"),
  cta="Здравствуйте! Видел(а) разбор кейса «Менеджер задач». Хочу такой же порядок в задачах своей команды.",
),
dict(
  slug="uchet-rashodov",
  doctitle="Кейс: финансовый бот и авто-P&L — ИИ-Гараж",
  metadesc="Разбор кейса: сотрудники присылают траты текстом, голосом или фото чека — бот пишет их в P&L-таблицу с конвертацией валют. 120 автотестов.",
  eyebrow="разбор кейса · финансы",
  h1="Финансовый бот: P&L собирается сам",
  lead="Деньги компании терялись в чеках и памяти сотрудников, а P&L собирался раз в месяц — со слезами. Теперь трата попадает в таблицу за секунды после того, как случилась.",
  metrics=[("120", "автотестов в системе"), ("3", "способа ввода: текст · голос · чек"), ("live", "P&L в реальном времени")],
  task=[
    "Клиент — компания с разъездной командой: закупки, транспорт, подрядчики, расходы в трёх валютах. Чеки копились в карманах и галереях телефонов, к концу месяца половину трат восстанавливали по памяти, а руководитель узнавал «где деньги» с опозданием на недели.",
    "Задача: чтобы сотрудник фиксировал трату за пять секунд в привычном мессенджере, а таблица с P&L обновлялась сама — без бухгалтера-переписчика.",
  ],
  chat=[
    ("Сотрудник", "🎤 Потратил 2400 бат на такси до склада"),
    ("Бот", "Записал: Транспорт · 2 400 THB ≈ 68,50 USD по курсу дня · сегодня. Руководителю отправлена копия операции."),
    ("Сотрудник", "[фото чека из строительного магазина]"),
    ("Бот", "Распознал чек: Материалы · 1 340 USD · 14 позиций. Подтвердить запись? [Да] [Исправить]"),
  ],
  features=[
    "Трата — текстом, голосом или фото чека; бот сам разберёт сумму, категорию и дату",
    "Валюты пересчитываются в базовую валюту компании по курсу дня — автоматически",
    "Каждая операция мгновенно дублируется руководителю с именем автора",
    "Свои записи можно править и удалять — с полным следом изменений",
    "Аналитика по кнопкам: итоги месяца, план/факт, динамика, топ статей расходов",
    "Роли и доступы: кто пишет, кто видит всё, кто только своё",
  ],
  principles=[
    "Суммы, проценты и курсы валют считает код — модель только разбирает фразу и читает чек. Финансы не доверяются генерации",
    "120 автотестов; таблица остаётся обычной Google-таблицей клиента — данные всегда его",
  ],
  results=[
    "P&L собирается сам, в реальном времени — бухгалтерская рутина исчезла",
    "Руководитель видит каждую операцию в момент, когда она случилась",
    "«Потерянные» траты кончились: фиксация занимает пять секунд",
  ],
  stack=["Telegram", "Google Sheets API", "OCR", "Voice", "Docker"],
  related=None,
  cta="Здравствуйте! Видел(а) разбор кейса «Финансовый бот». Хочу такой же учёт расходов для своей компании.",
),
dict(
  slug="baza-znaniy",
  doctitle="Кейс: ИИ-база знаний по документам — ИИ-Гараж",
  metadesc="Разбор кейса: бот отвечает сотрудникам строго по регламентам и прайсам компании, со ссылкой на источник. 322 автотеста, защита от выдуманных ответов.",
  eyebrow="разбор кейса · знания",
  h1="База знаний: ответы по документам за секунды",
  lead="Регламенты, прайсы и инструкции жили в переписках и головах старожилов. Новички дёргали коллег, коллеги отвлекались, знания терялись с людьми. Теперь на вопросы отвечает бот — строго по документам, со ссылкой на источник.",
  metrics=[("322", "автотеста в системе"), ("4", "контура защиты от выдумок"), ("сек.", "вместо часов на поиск ответа")],
  task=[
    "Клиент — компания, где ответ на вопрос «какие условия доставки для опта?» требовал найти нужного человека, дождаться его и надеяться, что он помнит актуальную версию. Документы лежали в пяти местах, а какая версия свежая — знали не все.",
    "Задача: единое окно вопросов для сотрудников — с ответами по актуальным документам, правами доступа по отделам и без «фантазий» нейросети.",
  ],
  chat=[
    ("Сотрудник", "Какие условия доставки для оптовых заказов?"),
    ("Бот", "По регламенту: для опта от 50 000 ₽ доставка бесплатна, до — по тарифу перевозчика. Источник: «Условия доставки», раздел 3, версия от 12 мая."),
    ("Сотрудник", "[фото страницы старого прайса] Это ещё актуально?"),
    ("Бот", "Нет: этот прайс заменён 1 июля. Актуальные цены — в «Прайс-лист, лист „Опт“». Прислать таблицей?"),
  ],
  features=[
    "Вопрос текстом или голосом — ответ со ссылкой на документ, раздел и версию",
    "Документы загружаются файлом, ссылкой или даже фотографией — система разберёт PDF, Word, Excel и сканы",
    "Права по отделам: недоступный сотруднику документ физически не попадает в его поиск",
    "Ничего не публикуется само: документ попадает в базу только после подтверждения владельцем",
    "Цены подставляются из таблиц напрямую — не генерируются моделью",
    "Раз в неделю руководитель получает список вопросов без ответа — готовую карту пробелов в базе",
  ],
  principles=[
    "Четыре контура защиты от выдуманных ответов: система скорее скажет «в документах этого нет», чем сочинит",
    "322 автотеста; документы и база остаются на сервере клиента",
  ],
  results=[
    "Ответ по регламентам — за секунды вместо поиска по чатам и людям",
    "Старожилов больше не дёргают по типовым вопросам",
    "Руководитель впервые видит, каких знаний в компании не хватает",
  ],
  stack=["Telegram", "RAG", "Vector Search", "Google Drive", "Docker"],
  related=("ИИ-консультант по базе знаний (RAG) — статья в блоге", "../../blog/ii-konsultant-po-baze-znaniy-rag/"),
  cta="Здравствуйте! Видел(а) разбор кейса «База знаний». Хочу, чтобы мои регламенты и прайсы так же отвечали сами.",
),
dict(
  slug="transkribator",
  doctitle="Кейс: транскрибатор встреч в Telegram — ИИ-Гараж",
  metadesc="Разбор кейса: голосовые, встречи и видео превращаются в текст с резюме, протоколом и задачами — и складываются в архив с поиском. 130 автотестов.",
  eyebrow="разбор кейса · продуктивность",
  h1="Транскрибатор: из часовой встречи — протокол за минуту",
  lead="Встречи, созвоны, голосовые на 6 минут, идеи, наговорённые на ходу — всё это исчезало бесследно. Теперь любая запись превращается в текст с резюме и задачами и ложится в архив, по которому работает поиск.",
  metrics=[("130", "автотестов в системе"), ("~1 мин", "от записи до текста"), ("100%", "данных на своём сервере")],
  task=[
    "Клиент — предприниматель с плотным графиком: по несколько созвонов в день, договорённости в голосовых, мысли — на диктофон между встречами. Восстанавливать «о чём договорились в четверг» приходилось перематыванием записей, а половина идей терялась навсегда.",
    "Задача: одна точка входа для любых записей — голосовых, видео, ссылок на YouTube — и на выходе структурированный текст, который сохраняется и ищется.",
  ],
  chat=[
    ("Клиент", "[пересылает запись созвона на 47 минут]"),
    ("Бот", "Готово: «Созвон по запуску курса» · расшифровка + резюме в 6 пунктах. Что сделать? [Чистовик] [Протокол встречи] [Список задач]"),
    ("Клиент", "[нажимает «Список задач»]"),
    ("Бот", "Выделил 7 задач с ответственными и сроками. Сохранил в архив: проект «Запуск курса», теги added. Найдёшь по слову «лендинг»."),
  ],
  features=[
    "Принимает голосовые, аудио, видео и ссылки на YouTube — прямо в Telegram",
    "Расшифровка + автоматический заголовок и резюме — сразу",
    "Кнопки-обработки: чистовик, протокол встречи, список задач, теги",
    "Всё складывается в личный «второй мозг» — приватный архив с полнотекстовым поиском",
    "Архив синхронизируется на компьютер и открывается в привычном редакторе заметок",
    "Аудио удаляется сразу после обработки — хранится только текст",
  ],
  principles=[
    "Все данные — на собственном сервере клиента, ни одна запись не уходит в чужие облака насовсем",
    "130 автотестов покрывают весь конвейер — от приёма файла до записи в архив",
  ],
  results=[
    "Протокол часовой встречи — через минуту после её конца",
    "Договорённости и идеи перестали теряться: всё ищется по одному слову",
    "Архив стал рабочим инструментом: прошлые решения подсказывают новые",
  ],
  stack=["Telegram", "Whisper", "Obsidian", "GitHub", "Docker"],
  related=None,
  cta="Здравствуйте! Видел(а) разбор кейса «Транскрибатор». Хочу так же превращать встречи и голосовые в текст.",
),
dict(
  slug="ii-prodazhi",
  doctitle="Кейс: ИИ-менеджер продаж 24/7 — ИИ-Гараж",
  metadesc="Разбор кейса: ИИ-агент отвечает лидам за секунды в любое время суток, квалифицирует и передаёт менеджеру тёплого клиента. Единицы рублей за диалог.",
  eyebrow="разбор кейса · продажи",
  h1="ИИ-менеджер продаж: отвечает лидам за секунды, 24/7",
  lead="Лид, которому ответили через час, уже написал трём конкурентам. Мы поставили на первую линию ИИ-агента: он отвечает мгновенно, в выходные и ночью, и передаёт менеджеру уже тёплого, квалифицированного клиента.",
  metrics=[("< 1 мин", "ответ на заявку в любое время"), ("24/7", "без выходных и отпусков"), ("₽", "единицы рублей за диалог")],
  task=[
    "Клиент — компания с потоком заявок из рекламы. Менеджеры отвечали в рабочие часы и «по очереди»: типичная задержка — час, ночные и выходные заявки ждали до утра понедельника. По вечерним лидам конверсия была почти нулевой — люди просто остывали.",
    "Задача: мгновенная первая линия, которая отвечает по фактам компании (цены, условия, сроки), задаёт уточняющие вопросы и вовремя зовёт человека — без найма ночной смены.",
  ],
  chat=[
    ("Клиент, 23:40", "Сколько стоит и когда сможете начать?"),
    ("ИИ-агент, 23:40", "Здравствуйте! Базовый тариф — от 30 000 ₽, старт — в течение недели. Подскажите, для какого объёма вам нужно? Посчитаю точнее."),
    ("Клиент, 23:43", "Примерно 200 заказов в месяц"),
    ("ИИ-агент, 23:43", "Для 200 заказов подойдёт тариф «Стандарт». Утром наш менеджер пришлёт расчёт — оставьте, пожалуйста, удобный контакт."),
  ],
  features=[
    "Отвечает на заявки мгновенно — ночью, в выходные, в праздники",
    "Говорит по фактам компании: цены, условия, сроки — из её базы знаний, а не из фантазий",
    "Квалифицирует лида уточняющими вопросами и собирает контакт",
    "Чувствует момент, когда нужен человек, — и передаёт диалог менеджеру",
    "Подключается к Telegram, WhatsApp и CRM компании",
    "Обкатка на тестовой ссылке до боевого запуска — агент не выходит к клиентам сырым",
  ],
  principles=[
    "Поведение агента задаёт инструкция, факты — база знаний: они не смешиваются, поэтому агент не «сочиняет» цены",
    "Решение собрано на проверенной платформе — запуск занимает дни, а не месяцы, и не требует своего сервера",
  ],
  results=[
    "Ответ за секунды вместо часа — лиды перестали остывать",
    "Менеджеры получают тёплых, квалифицированных клиентов, а не «алло, вы писали»",
    "Экономика — единицы рублей за диалог: дешевле одного пропущенного лида",
  ],
  stack=["Telegram", "Платформа ИИ-агентов", "База знаний", "CRM"],
  related=("Telegram-бот с ИИ для бизнеса: 7 задач — статья в блоге", "../../blog/telegram-bot-s-ii-dlya-biznesa/"),
  cta="Здравствуйте! Видел(а) разбор кейса «ИИ-менеджер продаж». Хочу, чтобы мои заявки не ждали до утра.",
),
]

TITLES = {c["slug"]: c["h1"] for c in CASES}

PAGE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{doctitle}</title>
<meta name="description" content="{metadesc}">
<link rel="icon" type="image/png" href="../../favicon.png?v=4">
<link rel="icon" href="../../favicon.ico?v=4" sizes="any">
<link rel="apple-touch-icon" href="../../apple-touch-icon.png">
<link rel="canonical" href="https://ai-garage.tech/cases/{slug}/">
<meta property="og:type" content="article">
<meta property="og:title" content="{doctitle}">
<meta property="og:description" content="{metadesc}">
<meta property="og:url" content="https://ai-garage.tech/cases/{slug}/">
<meta property="og:image" content="https://ai-garage.tech/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {jsonh1},
  "description": {jsondesc},
  "image": "https://ai-garage.tech/og-image.png",
  "author": {{ "@type": "Organization", "name": "ИИ-Гараж", "url": "https://ai-garage.tech/" }},
  "publisher": {{ "@type": "Organization", "name": "ИИ-Гараж", "logo": {{ "@type": "ImageObject", "url": "https://ai-garage.tech/logo-mark-transparent.png" }} }},
  "mainEntityOfPage": "https://ai-garage.tech/cases/{slug}/"
}}
</script>
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "y0aui9ba3z");
    document.addEventListener('click', function(e){{
      var a = e.target.closest && e.target.closest('a[href*="t.me/stavzzz"]');
      if (a && window.clarity) clarity('event', 'telegram_click');
    }});
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
  @font-face {{ font-family: 'JetBrains Mono'; src: local('JetBrains Mono'); font-weight: 400 800; }}
  :root {{
    --bg: #17181A; --surface: #1E1F22; --surface-2: #26272B;
    --ink: #F5F5F5; --ink-soft: #9EA3A8; --ink-faint: #6d7278;
    --line: #2c2e31; --accent: #4CAE86; --accent-dim: #2c4438; --accent-soft: #20302a;
    --mono: 'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
    --serif: 'Manrope', -apple-system, 'Segoe UI', Roboto, sans-serif;
    color-scheme: dark;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font-family: var(--mono); font-size: 15px; line-height: 1.65;
    -webkit-font-smoothing: antialiased;
  }}
  .wrap {{ max-width: 1100px; margin: 0 auto; padding: 0 28px; }}
  a {{ color: inherit; }}
  header.site {{
    position: sticky; top: 0; z-index: 50;
    background: rgba(10,10,10,.88); backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
  }}
  .site-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 18px 0; }}
  .logo {{ display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 14px; letter-spacing: 0.02em; text-decoration: none; }}
  .logo img {{ height: 22px; width: auto; display: block; }}
  .logo .dot {{ color: var(--accent); }}
  nav.main {{ display: flex; align-items: center; gap: 26px; }}
  nav.main a {{ font-size: 12.5px; color: var(--ink-soft); text-decoration: none; }}
  nav.main a:hover {{ color: var(--ink); }}
  @media (max-width: 760px) {{
    .site-inner {{ flex-wrap: wrap; gap: 8px 14px; padding: 12px 0; }}
    nav.main {{ order: 3; width: 100%; gap: 18px; overflow-x: auto; }}
    nav.main a {{ white-space: nowrap; font-size: 12px; }}
  }}
  main.wrap {{ padding: 56px 0 80px; max-width: 760px; }}
  .eyebrow {{ font-size: 12px; color: var(--accent); text-transform: uppercase; letter-spacing: .06em; margin-bottom: 12px; }}
  .eyebrow::before {{ content: '// '; opacity: .6; }}
  h1 {{ font-family: var(--serif); font-weight: 600; font-size: clamp(26px, 4vw, 38px); line-height: 1.25; margin: 0 0 18px; }}
  .lead {{ font-size: 16px; color: var(--ink-soft); margin: 0 0 34px; }}
  p {{ margin: 0 0 20px; color: var(--ink-soft); }}
  h2 {{ font-family: var(--serif); font-weight: 600; font-size: 21px; color: var(--ink); margin: 40px 0 16px; }}
  a.link {{ color: var(--accent); }}

  .metrics {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 0 0 8px; }}
  .metric {{
    background: linear-gradient(160deg, rgba(255,255,255,.045), transparent 40%), color-mix(in srgb, var(--surface-2) 92%, transparent);
    border: 1px solid rgba(255,255,255,.08); border-radius: 10px; padding: 16px 18px;
    box-shadow: 0 1px 0 rgba(255,255,255,.06) inset, 0 20px 48px rgba(0,0,0,.4);
  }}
  .metric b {{ display: block; font-size: 22px; color: var(--accent); font-weight: 700; margin-bottom: 4px; }}
  .metric span {{ font-size: 11.5px; color: var(--ink-soft); line-height: 1.4; display: block; }}
  @media (max-width: 640px) {{ .metrics {{ grid-template-columns: 1fr; }} }}

  .chat {{
    background: linear-gradient(160deg, rgba(255,255,255,.045), transparent 40%), color-mix(in srgb, var(--surface-2) 92%, transparent);
    border: 1px solid rgba(255,255,255,.08); border-radius: 12px; padding: 20px 22px;
    box-shadow: 0 1px 0 rgba(255,255,255,.06) inset, 0 20px 48px rgba(0,0,0,.4);
    display: grid; gap: 12px; margin: 22px 0 8px;
  }}
  .msg {{ max-width: 88%; font-size: 13px; line-height: 1.6; padding: 10px 14px; border-radius: 10px; }}
  .msg .who {{ display: block; font-size: 10.5px; color: var(--ink-faint); margin-bottom: 4px; text-transform: uppercase; letter-spacing: .05em; }}
  .msg.user {{ justify-self: end; background: var(--surface-2); border: 1px solid var(--line); color: var(--ink); }}
  .msg.bot {{ justify-self: start; background: var(--accent-soft); border: 1px solid var(--accent-dim); color: var(--ink); }}
  .msg.bot .who {{ color: var(--accent); }}

  ul.features {{ list-style: none; padding: 0; margin: 0 0 8px; display: grid; gap: 10px; }}
  ul.features li {{ padding-left: 24px; position: relative; color: var(--ink-soft); font-size: 14px; line-height: 1.6; }}
  ul.features li::before {{ content: '✓'; position: absolute; left: 0; color: var(--accent); font-family: var(--mono); }}

  .result-box {{
    background: var(--accent-soft); border: 1px solid var(--accent-dim); border-radius: 12px;
    padding: 22px 24px; margin: 22px 0 8px; display: grid; gap: 10px;
  }}
  .result-box div {{ font-size: 13.5px; line-height: 1.6; color: var(--ink); }}
  .result-box div::before {{ content: '▸ '; color: var(--accent); }}

  .stack {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 4px 0 8px; }}
  .stack span {{ font-size: 11px; color: var(--accent); background: var(--accent-soft); padding: 3px 10px; border-radius: 100px; }}

  .cta-box {{
    text-align: center; margin: 48px 0 8px; padding: 34px 28px;
    background: linear-gradient(160deg, rgba(255,255,255,.045), transparent 40%), color-mix(in srgb, var(--surface-2) 92%, transparent);
    border: 1px solid rgba(255,255,255,.08); border-radius: 14px;
    box-shadow: 0 1px 0 rgba(255,255,255,.06) inset, 0 20px 48px rgba(0,0,0,.4);
  }}
  .cta-box h2 {{ margin: 0 0 10px; }}
  .cta-box p {{ margin: 0 auto 22px; max-width: 480px; font-size: 13.5px; }}
  .btn {{
    display: inline-block; background: var(--accent); color: #10120f; font-weight: 700;
    font-size: 14px; padding: 13px 28px; border-radius: 10px; text-decoration: none;
    box-shadow: 0 8px 24px rgba(76,174,134,.25); transition: transform .15s, box-shadow .15s;
  }}
  .btn:hover {{ transform: translateY(-1px); box-shadow: 0 12px 30px rgba(76,174,134,.35); }}

  .next-btn {{
    display: flex; align-items: center; justify-content: space-between; gap: 14px;
    margin: 0 0 16px; padding: 18px 22px; text-decoration: none;
    background: color-mix(in srgb, var(--surface-2) 92%, transparent);
    border: 1px solid var(--accent-dim); border-radius: 12px; transition: border-color .15s;
  }}
  .next-btn:hover {{ border-color: var(--accent); }}
  .next-btn .k {{ font-size: 10.5px; color: var(--ink-faint); text-transform: uppercase; letter-spacing: .06em; display: block; margin-bottom: 4px; }}
  .next-btn .t {{ font-weight: 700; font-size: 14.5px; color: var(--ink); }}
  .next-btn .arr {{ color: var(--accent); font-size: 20px; flex: none; }}
  .others {{ display: grid; gap: 8px; margin: 0 0 8px; }}
  .others a {{
    display: block; padding: 13px 18px; border: 1px solid rgba(255,255,255,.08); border-radius: 10px;
    background: color-mix(in srgb, var(--surface-2) 92%, transparent);
    font-size: 13px; color: var(--ink-soft); text-decoration: none; transition: border-color .15s, color .15s;
  }}
  .others a:hover {{ border-color: var(--accent-dim); color: var(--ink); }}
  .others a::after {{ content: ' →'; color: var(--accent); }}

  footer.site {{ padding: 28px 0; text-align: center; font-size: 12px; color: var(--ink-faint); border-top: 1px solid var(--line); margin-top: 60px; }}
  footer.site a {{ color: var(--ink-faint); text-decoration: underline; }}
  .footer-socials {{ display: flex; gap: 14px; justify-content: center; margin-top: 14px; }}
  .footer-socials a {{ color: var(--ink-faint); transition: color .15s; }}
  .footer-socials a:hover {{ color: var(--accent); }}
  .footer-socials svg {{ width: 17px; height: 17px; fill: currentColor; display: block; }}
</style>
</head>
<body>
<header class="site">
  <div class="wrap site-inner">
    <a class="logo" href="../../"><img src="../../logo-mark-transparent.png" alt="" width="22" height="22">гараж<span class="dot">_</span></a>
    <nav class="main">
      <a href="../../#cases">кейсы</a>
      <a href="../../#services">услуги</a>
      <a href="../../blog/">блог</a>
      <a href="../../#contact">контакты</a>
    </nav>
  </div>
</header>

<main class="wrap">
  <div class="eyebrow">{eyebrow}</div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>

  <div class="metrics">
{metrics_html}
  </div>

  <h2>Задача</h2>
{task_html}

  <h2>Как это выглядит</h2>
  <div class="chat">
{chat_html}
  </div>

  <h2>Что делает система</h2>
  <ul class="features">
{features_html}
  </ul>

  <h2>Принципы, на которых это держится</h2>
  <ul class="features">
{principles_html}
  </ul>

  <h2>Результат</h2>
  <div class="result-box">
{results_html}
  </div>

  <h2>Стек</h2>
  <div class="stack">
{stack_html}
  </div>
{related_html}
  <div class="cta-box">
    <h2>Хотите так же?</h2>
    <p>Расскажите, где у вас больше всего рутины, — предложим решение и честно скажем, если автоматизация не нужна.</p>
    <a class="btn" href="https://t.me/stavzzz?text={cta_enc}" target="_blank" rel="noopener">Обсудить в Telegram</a>
  </div>

  <h2>Другие разборы</h2>
  <a class="next-btn" href="../{next_slug}/">
    <div>
      <span class="k">следующий разбор</span>
      <span class="t">{next_h1}</span>
    </div>
    <span class="arr">→</span>
  </a>
  <div class="others">
{others_html}
  </div>
</main>

<footer class="site">
  ИИ-Гараж · <a href="../../about/">О нас</a> · <a href="../../privacy/">Политика конфиденциальности</a>
  <div class="footer-socials">
    <a href="https://t.me/ai_garage_crew" target="_blank" rel="noopener" aria-label="Telegram-канал" title="Telegram-канал"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg></a>
    <a href="https://www.instagram.com/ai_garage_crew/" target="_blank" rel="noopener" aria-label="Instagram" title="Instagram"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0C8.74 0 8.333.015 7.053.072 5.775.132 4.905.333 4.14.63c-.789.306-1.459.717-2.126 1.384S.935 3.35.63 4.14C.333 4.905.131 5.775.072 7.053.012 8.333 0 8.74 0 12s.015 3.667.072 4.947c.06 1.277.261 2.148.558 2.913.306.788.717 1.459 1.384 2.126.667.666 1.336 1.079 2.126 1.384.766.296 1.636.499 2.913.558C8.333 23.988 8.74 24 12 24s3.667-.015 4.947-.072c1.277-.06 2.148-.262 2.913-.558.788-.306 1.459-.718 2.126-1.384.666-.667 1.079-1.335 1.384-2.126.296-.765.499-1.636.558-2.913.06-1.28.072-1.687.072-4.947s-.015-3.667-.072-4.947c-.06-1.277-.262-2.149-.558-2.913-.306-.789-.718-1.459-1.384-2.126C21.319 1.347 20.651.935 19.86.63c-.765-.297-1.636-.499-2.913-.558C15.667.012 15.26 0 12 0zm0 2.16c3.203 0 3.585.016 4.85.071 1.17.055 1.805.249 2.227.415.562.217.96.477 1.382.896.419.42.679.819.896 1.381.164.422.36 1.057.413 2.227.057 1.266.07 1.646.07 4.85s-.015 3.585-.074 4.85c-.061 1.17-.256 1.805-.421 2.227-.224.562-.479.96-.899 1.382-.419.419-.824.679-1.38.896-.42.164-1.065.36-2.235.413-1.274.057-1.649.07-4.859.07-3.211 0-3.586-.015-4.859-.074-1.171-.061-1.816-.256-2.236-.421-.569-.224-.96-.479-1.379-.899-.421-.419-.69-.824-.9-1.38-.165-.42-.359-1.065-.42-2.235-.045-1.26-.061-1.649-.061-4.844 0-3.196.016-3.586.061-4.861.061-1.17.255-1.814.42-2.234.21-.57.479-.96.9-1.381.419-.419.81-.689 1.379-.898.42-.166 1.051-.361 2.221-.421 1.275-.045 1.65-.06 4.859-.06zm0 5.678c-3.405 0-6.162 2.76-6.162 6.162 0 3.405 2.757 6.162 6.162 6.162 3.405 0 6.162-2.757 6.162-6.162 0-3.402-2.757-6.162-6.162-6.162zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405c0 .795-.646 1.44-1.44 1.44-.795 0-1.44-.645-1.44-1.44 0-.794.646-1.439 1.44-1.439.793 0 1.44.645 1.44 1.439z"/></svg></a>
    <a href="https://www.youtube.com/@aigarage_tech" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
    <a href="mailto:ai-garage.tech@proton.me" aria-label="Написать на почту" title="Написать на почту"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M1.5 4.5h21c.55 0 1 .45 1 1v13c0 .55-.45 1-1 1h-21c-.55 0-1-.45-1-1v-13c0-.55.45-1 1-1zm10.5 7.6L3.2 6.5h17.6L12 12.1zm-9.5 6.4h19V8.2l-9.5 5.9-9.5-5.9v10.3z"/></svg></a>
  </div>
</footer>
</body>
</html>
"""

import json

def esc(s):
    return html.escape(s, quote=True)

for c in CASES:
    metrics_html = "\n".join(
        '    <div class="metric"><b>{}</b><span>{}</span></div>'.format(esc(n), esc(l))
        for n, l in c["metrics"])
    task_html = "\n".join("  <p>{}</p>".format(esc(p)) for p in c["task"])
    chat_rows = []
    for who, text in c["chat"]:
        cls = "bot" if ("бот" in who.lower() or "агент" in who.lower()) else "user"
        chat_rows.append('    <div class="msg {}"><span class="who">{}</span>{}</div>'.format(cls, esc(who), esc(text)))
    chat_html = "\n".join(chat_rows)
    features_html = "\n".join("    <li>{}</li>".format(esc(f)) for f in c["features"])
    principles_html = "\n".join("    <li>{}</li>".format(esc(p)) for p in c["principles"])
    results_html = "\n".join("    <div>{}</div>".format(esc(r)) for r in c["results"])
    stack_html = "\n".join("    <span>{}</span>".format(esc(s)) for s in c["stack"])
    if c["related"]:
        related_html = '\n  <p style="margin-top:26px">Читать по теме: <a class="link" href="{}">{}</a></p>\n'.format(
            c["related"][1], esc(c["related"][0]))
    else:
        related_html = "\n"
    idx = CASES.index(c)
    nxt = CASES[(idx + 1) % len(CASES)]
    others_html = "\n".join(
        '    <a href="../{}/">{}</a>'.format(o["slug"], esc(o["h1"]))
        for o in CASES if o["slug"] not in (c["slug"], nxt["slug"]))
    page = PAGE.format(
        doctitle=esc(c["doctitle"]), metadesc=esc(c["metadesc"]), slug=c["slug"],
        jsonh1=json.dumps(c["h1"], ensure_ascii=False), jsondesc=json.dumps(c["metadesc"], ensure_ascii=False),
        eyebrow=esc(c["eyebrow"]), h1=esc(c["h1"]), lead=esc(c["lead"]),
        metrics_html=metrics_html, task_html=task_html, chat_html=chat_html,
        features_html=features_html, principles_html=principles_html,
        results_html=results_html, stack_html=stack_html, related_html=related_html,
        cta_enc=urllib.parse.quote(c["cta"]), others_html=others_html,
        next_slug=nxt["slug"], next_h1=esc(nxt["h1"]),
    )
    # типографика по Ководству (typograf.py лежит рядом)
    import sys as _sys
    _sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from typograf import typo_html
    page = typo_html(page)
    outdir = os.path.join(ROOT, "cases", c["slug"])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("written:", outdir, len(page), "bytes, title", len(c["doctitle"]), "chars")
