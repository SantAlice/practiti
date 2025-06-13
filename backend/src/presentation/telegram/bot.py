"""
🤖 Основной класс Telegram Bot

Центральный класс для управления Telegram Bot.
Принцип CyberKitty: простота превыше всего.
"""

import asyncio
import logging
from typing import Optional

from telegram import BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import ContextTypes
from telegram import Update

from ...config.settings import TelegramConfig
from ...services.protocols.client_service import ClientServiceProtocol
from .handlers.command_handlers import CommandHandlers

logger = logging.getLogger(__name__)


class PrakritiTelegramBot:
    """
    Основной класс Telegram Bot для CyberKitty Practiti.
    
    Управляет:
    - Инициализацией бота
    - Регистрацией обработчиков команд
    - Запуском и остановкой
    - Обработкой ошибок
    """
    
    def __init__(
        self, 
        config: TelegramConfig,
        client_service: ClientServiceProtocol
    ):
        """
        Инициализация Telegram Bot.
        
        Args:
            config: Конфигурация Telegram Bot
            client_service: Сервис для работы с клиентами
        """
        self.config = config
        self.client_service = client_service
        
        # Создаем приложение бота
        self.application: Optional[Application] = None
        
        # Инициализируем обработчики
        self.command_handlers = CommandHandlers(client_service)
        
        logger.info("PrakritiTelegramBot инициализирован")
    
    async def initialize(self) -> None:
        """
        Инициализация приложения бота.
        """
        logger.info("Инициализация Telegram Bot...")
        
        # Создаем приложение
        self.application = (
            Application.builder()
            .token(self.config.bot_token)
            .build()
        )
        
        # Регистрируем обработчики
        await self._register_handlers()
        
        # Настраиваем команды бота
        await self._setup_bot_commands()
        
        # Регистрируем обработчик ошибок
        self.application.add_error_handler(self._error_handler)
        
        logger.info("Telegram Bot успешно инициализирован")
    
    async def _register_handlers(self) -> None:
        """
        Регистрация всех обработчиков команд.
        """
        logger.info("Регистрация обработчиков команд...")
        
        # Основные команды
        self.application.add_handler(
            CommandHandler("start", self.command_handlers.start_command)
        )
        self.application.add_handler(
            CommandHandler("help", self.command_handlers.help_command)
        )
        self.application.add_handler(
            CommandHandler("info", self.command_handlers.info_command)
        )
        
        # Обработчик неизвестных команд (должен быть последним)
        self.application.add_handler(
            MessageHandler(
                filters.COMMAND, 
                self.command_handlers.unknown_command
            )
        )
        
        logger.info("Обработчики команд зарегистрированы")
    
    async def _setup_bot_commands(self) -> None:
        """
        Настройка меню команд бота.
        """
        logger.info("Настройка меню команд...")
        
        commands = [
            BotCommand("start", "🌟 Главное меню"),
            BotCommand("help", "📋 Справка по командам"),
            BotCommand("info", "🧘‍♀️ О студии"),
            BotCommand("register", "📝 Регистрация"),
            BotCommand("contact", "📞 Контакты"),
        ]
        
        if self.application and self.application.bot:
            await self.application.bot.set_my_commands(commands)
            logger.info("Меню команд настроено")
    
    async def _error_handler(self, update: Optional[Update], context: ContextTypes.DEFAULT_TYPE) -> None:
        """
        Глобальный обработчик ошибок.
        
        Args:
            update: Telegram обновление (может быть None)
            context: Контекст бота
        """
        error = context.error
        
        # Логируем ошибку
        if update:
            user_info = "неизвестно"
            if update.effective_user:
                user_info = f"@{update.effective_user.username} (ID: {update.effective_user.id})"
            
            logger.error(
                f"Ошибка при обработке обновления от {user_info}: {error}",
                exc_info=True
            )
        else:
            logger.error(f"Глобальная ошибка бота: {error}", exc_info=True)
        
        # Пытаемся отправить пользователю сообщение об ошибке
        if update and update.effective_chat:
            try:
                await update.effective_chat.send_message(
                    "🚫 Произошла неожиданная ошибка. "
                    "Администратор уведомлен. Попробуйте позже."
                )
            except Exception as send_error:
                logger.error(f"Не удалось отправить сообщение об ошибке: {send_error}")
        
        # Уведомляем администратора о критических ошибках
        if self.config.admin_chat_id:
            try:
                admin_message = (
                    f"🚨 **Ошибка в боте:**\n\n"
                    f"**Ошибка:** `{str(error)[:200]}`\n"
                    f"**Пользователь:** {user_info if update else 'системная'}\n"
                    f"**Время:** {context.user_data.get('timestamp', 'неизвестно')}"
                )
                
                if self.application and self.application.bot:
                    await self.application.bot.send_message(
                        chat_id=self.config.admin_chat_id,
                        text=admin_message,
                        parse_mode='Markdown'
                    )
            except Exception as admin_error:
                logger.error(f"Не удалось уведомить администратора: {admin_error}")
    
    async def start_polling(self) -> None:
        """
        Запуск бота в режиме polling.
        """
        if not self.application:
            await self.initialize()
        
        logger.info("Запуск Telegram Bot в режиме polling...")
        
        try:
            if self.application:
                await self.application.initialize()
                await self.application.start()
                await self.application.updater.start_polling(drop_pending_updates=True)
                
                # Держим бота запущенным
                import asyncio
                try:
                    while True:
                        await asyncio.sleep(1)
                except KeyboardInterrupt:
                    pass
        except Exception as e:
            logger.error(f"Ошибка при запуске polling: {e}")
            raise
    
    async def start_webhook(self, webhook_url: str, port: int = 8080) -> None:
        """
        Запуск бота в режиме webhook.
        
        Args:
            webhook_url: URL для webhook
            port: Порт для прослушивания
        """
        if not self.application:
            await self.initialize()
        
        logger.info(f"Запуск Telegram Bot в режиме webhook: {webhook_url}")
        
        try:
            if self.application:
                await self.application.run_webhook(
                    listen="0.0.0.0",
                    port=port,
                    webhook_url=webhook_url,
                    drop_pending_updates=True
                )
        except Exception as e:
            logger.error(f"Ошибка при запуске webhook: {e}")
            raise
    
    async def stop(self) -> None:
        """
        Остановка бота.
        """
        logger.info("Остановка Telegram Bot...")
        
        if self.application:
            try:
                await self.application.updater.stop()
                await self.application.stop()
                await self.application.shutdown()
            except Exception as e:
                logger.warning(f"Ошибка при остановке: {e}")
        
        logger.info("Telegram Bot остановлен")
    
    async def send_message_to_admin(self, message: str) -> bool:
        """
        Отправить сообщение администратору.
        
        Args:
            message: Текст сообщения
            
        Returns:
            True если сообщение отправлено успешно
        """
        if not self.config.admin_chat_id:
            logger.warning("Admin chat ID не настроен")
            return False
        
        try:
            if self.application and self.application.bot:
                await self.application.bot.send_message(
                    chat_id=self.config.admin_chat_id,
                    text=message
                )
                return True
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения администратору: {e}")
        
        return False
    
    def is_running(self) -> bool:
        """
        Проверить, запущен ли бот.
        
        Returns:
            True если бот запущен
        """
        return (
            self.application is not None and 
            self.application.running
        ) 