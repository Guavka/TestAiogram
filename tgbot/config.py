# Импорт для работы с датаклассами (как обычные классы но без проверок и __init__)
from dataclasses import dataclass

# Импорт для работы с данными из файла .env
from environs import Env


@dataclass
class DbConfig:
    """Клас настроек для базы данных

    Arguments:
        str: host - IP-адрес базы данных
        str: database - имя базы данных
        str: user - имя пользователя базы данных
        str: password - пароль для доступа в базу данных
    """
    host: str
    database: str

    user: str
    password: str


@dataclass
class TgBot:
    """Класс настроек бота

    Arguments:
        str: token - уникальный ключ для доступа к боту
        list[int]: admin_ids - список ID админов, которые могут вызывать дополнительные команды
        bool: use_redis - использовать ли базу данных для хранения состояний
    """
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    """Класс, для дополнительных параметров
    """
    other_params: str = None


@dataclass
class Config:
    """Класс, отвечающий за конфигурацию бота
        Arguments:
            TgBot: tg_bot - объект класса настроек бота
            DbConfig: db - объект класса настроек базы данных
            Miscellaneous: misc - объект класса второстепенных настроек 
    """
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    """Функция, которая загружает настройки из .env файла и создает объект со всеми настройкамии бота и БД

    Args:
        path (str, optional): Путь, где лежит .env файл, если None - ищет его в корне проекта. Defaults to None.

    Returns:
        Config: объект класса настроек
    """
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )
