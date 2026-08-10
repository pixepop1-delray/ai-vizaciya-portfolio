# ИИ-Гараж — состояние проекта

Сайт-каталог кейсов ИИ-внедрений + SEO-блог. Все ссылки и карточка для портфолио — в `PROJECT-CARD.md`.

## Текущее состояние (10.08.2026)

Сайт полностью рабочий и готов к рекламе:

- **Главная**: hero с анимацией сборки робота, карусель 16 кейсов (стрелки снизу + точки, свайп на мобиле), услуги с роботами-иконками, живой скрин AI-офиса в «Команде», все CTA → t.me/stavzzz
- **Мобильная версия**: навигация-лента (была сломана — починена), бегущий робот в шве (<640px), карусель по 1 карточке со свайпом
- **Блог** (`/blog/`): Astro + Decap CMS, публикация из панели `/blog/admin/` (вход через GitHub), от Publish до сайта ~2 мин автоматически
- **SEO**: sitemap автогенерится при каждой статье, robots.txt, canonical, meta
- **Соцсети**: og-image (1200×630), favicon, og:/twitter:-теги на главной и статьях
- **Аналитика**: Microsoft Clarity, проект `y0aui9ba3z`, дашборд: https://clarity.microsoft.com/projects/view/y0aui9ba3z/dashboard (вход через Google-аккаунт владельца)

## Следующий шаг

1. **Купить домен** (владелец) → после покупки: подключить к GitHub Pages, обновить `site` в `blog-src/astro.config.mjs`, `siteOrigin/siteRoot` в `blog-src/src/layouts/BlogLayout.astro`, `public_folder` в `blog-src/public/admin/config.yml`, URL в og-тегах `index.html`, зарегистрировать в Google Search Console и отправить sitemap
2. **Писать статьи в блог** — через панель `/blog/admin/` (владелец+муж) или через Claude (Markdown в `blog-src/src/content/posts/`)

## Открытые вопросы

- Домен ещё не выбран/не куплен
- Блог пуст (тестовые статьи удалены) — для SEO нужно 3-5 реальных статей

## Технические факты

- Пайплайн блога: пуш в `blog-src/**` → Actions `build-blog.yml` (Node 22, concurrency guard) → собранный HTML коммитится в `blog/` + sitemap в корень → Pages публикует
- `.nojekyll` в корне обязателен (иначе Pages падает на `[...slug].astro`)
- Не пушить много коммитов подряд быстро — деплои Pages конфликтуют в очереди; лечение зависшего деплоя: пустой коммит-пуш
- OAuth для админки: GitHub OAuth App «ИИ-Гараж блог» + Cloudflare Worker `ii-garage-cms-auth.pixepop1.workers.dev` (код — sveltia-cms-auth; секреты в переменных воркера, в репо их НЕТ)
- og-image.png и favicon.png сгенерированы PIL-скриптом (стиль: слаты гаража + сетка + пиксель-робот)
