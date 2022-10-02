# импорт библиотеки для поддержки асинхронности
import asyncio
# импорт библиотеки для логирования происходящего (красиво пишет в консоль)
import logging

# импорт для работы бота и машины состояний
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

# импорт настроек
from tgbot.config import load_config

# импорт фильтров
from tgbot.filters.admin import AdminFilter

# импорт хендлеров
from tgbot.handlers.private.admin import register_admin as admin_private
from tgbot.handlers.private.user import register_user as user_private

# импорт middleware
from tgbot.middlewares.environment import EnvironmentMiddleware

# импорт комманд
from tgbot.misc.utils.commands import init_base_commands

logger = logging.getLogger(__name__)

# При развитии проект меняться будут только эти функции  и импорты


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp):
    admin_private(dp)
    user_private(dp)
# ---------------------


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp, config)
    register_all_filters(dp)
    register_all_handlers(dp)
    
    await init_base_commands(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
