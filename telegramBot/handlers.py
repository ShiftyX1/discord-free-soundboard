from aiogram import types, F, Router, Bot
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
import asyncio

import kb
import texts


router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(texts.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)