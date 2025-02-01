# # # # # # import telebot
# # # # # # from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# # # # # # import os
# # # # # # import csv

# # # # # # ANNOUNCEMENT_CHANNEL = "@fakeannouncmentsadgame7766"
# # # # # # COMMANDS_CHANNEL = "@fakecommandssadgame7766"
# # # # # # BOT_TOKEN = "7585945637:AAHADs0n0PfRNd58vin29wdSTp6ybIH9sJQ"
# # # # # # ADMIN_ID = 642957912
# # # # # # ALLOWED_IDS_FILE = "allowed_ids.csv"
# # # # # # PASSWORD = 1

# # # # # # pending_bayanieh = {}
# # # # # # bot = telebot.TeleBot(BOT_TOKEN)

# # # # # # # Define states
# # # # # # (
# # # # # #     MAIN_MENU,
# # # # # #     CHOOSING,
# # # # # #     LASHGARKESHI,
# # # # # #     LASHGARKESHI_TYPE,
# # # # # #     SOURCE,
# # # # # #     DESTINATION,
# # # # # #     ARMY_STATS,
# # # # # #     ARRIVAL_TIME,
# # # # # #     ATTACK_OR_SIEGE,
# # # # # #     LOCATION,
# # # # # #     CONFIRMATION,
# # # # # # ) = range(11)
# # # # # # BAYANIEH_MEDIA, BAYANIEH_COUNTRY, BAYANIEH_TEXT = range(3)

# # # # # # # Store user data
# # # # # # user_data = {}
# # # # # # ALLOWED = []

# # # # # # # Define photo paths
# # # # # # CANCEL_LASHKARKESHI_PHOTO = os.path.join("photos/cancel_lashkarkeshy.jpg")
# # # # # # BAYANIEH_PHOTO = os.path.join("photos/bayanieh.jpg")
# # # # # # LASHGARKESHI_AIR_PHOTO = os.path.join("photos/lash_air.jpg")
# # # # # # LASHGARKESHI_GROUND_PHOTO = os.path.join("photos/lash_ground.jpg")
# # # # # # LASHGARKESHI_SEA_PHOTO = os.path.join("photos/lash_naval.jpg")
# # # # # # ATTACK_GROUND_PHOTO = os.path.join("photos/attack_ground.jpg")
# # # # # # ATTACK_AIR_PHOTO = os.path.join("photos/attack_air.jpg")
# # # # # # ATTACK_SEA_PHOTO = os.path.join("photos/attack_sea.jpg")
# # # # # # SIEGE_PHOTO = os.path.join("photos/siege.jpg")




# # # # # # def create_keyboard(buttons, include_back=True):
# # # # # #     keyboard = InlineKeyboardMarkup(row_width=2)
# # # # # #     for button in buttons:
# # # # # #         keyboard.add(InlineKeyboardButton(f" {button[0]} ", callback_data=button[1]))
# # # # # #     if include_back:
# # # # # #         keyboard.add(
# # # # # #             InlineKeyboardButton(
# # # # # #                 "📜 بازگشت به منوی اصلی 📜", callback_data="back_to_main"
# # # # # #             )
# # # # # #         )
# # # # # #     return keyboard


# # # # # # def get_user_link(user_id):
# # # # # #     return f'<a href="tg://user?id={user_id}">{user_id}</a>'


# # # # # # def get_user_mention(user_id, username=None):
# # # # # #     if username:
# # # # # #         return f"@{username}"
# # # # # #     else:
# # # # # #         return f'<a href="tg://user?id={user_id}">فرمانده</a>'


# # # # # # def clear_step_handler(message):
# # # # # #     bot.clear_step_handler_by_chat_id(message.chat.id)


# # # # # # def check_allowance(message):
# # # # # #     if message.from_user.id == ADMIN_ID or message.from_user.id in ALLOWED:
# # # # # #         return True
# # # # # #     else:
# # # # # #         bot.send_message(message.chat.id, "لطفا رمز عبور را وارد کنید:")
# # # # # #         bot.register_next_step_handler(message, validate_password)
# # # # # #         return False


# # # # # # def validate_password(message):
# # # # # #     try:
# # # # # #         if message.text.isdigit() and int(message.text) == PASSWORD:
# # # # # #             bot.send_message(message.chat.id, "رمز عبور صحیح است. خوش آمدید!")
# # # # # #             if message.from_user.id not in ALLOWED:
# # # # # #                 ALLOWED.append(message.from_user.id)
# # # # # #             start(message, allowed=True)
# # # # # #         else:
# # # # # #             bot.send_message(message.chat.id, "رمز عبور اشتباه است. لطفا دوباره تلاش کنید:")
# # # # # #             bot.register_next_step_handler(message, validate_password)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در اعتبارسنجی رمز عبور: {str(e)}")


# # # # # # @bot.message_handler(commands=["start"])
# # # # # # def start(message, allowed=False):
# # # # # #     try:
# # # # # #         get_user_mention(message, message.from_user.id)
# # # # # #         clear_step_handler(message)
# # # # # #         if not allowed:
# # # # # #             if message.from_user.id != ADMIN_ID:
# # # # # #                 if not check_allowance(message):
# # # # # #                     return

# # # # # #         buttons = [
# # # # # #             ("[⚔️] لشکرکشی ", "lashgarkeshi"),
# # # # # #             ("[📢] بیانیه ", "bayanieh"),
# # # # # #             ("[🧨] دستور حمله/محاصره ", "dastor"),
# # # # # #             ("[❌] لغو لشکرکشی ", "cancel_lashgarkeshi"),  # New button
# # # # # #         ]

# # # # # #         keyboard = create_keyboard(buttons, include_back=False)
# # # # # #         bot.send_message(message.chat.id, "یک گزینه را انتخاب کنید:", reply_markup=keyboard)
# # # # # #         user_data[message.from_user.id] = {"state": MAIN_MENU}
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در شروع: {str(e)}")


# # # # # # @bot.callback_query_handler(func=lambda call: True)
# # # # # # def callback_query(call):
# # # # # #     clear_step_handler(call.message)

# # # # # #     try:
# # # # # #         if call.data.startswith("allow_") or call.data.startswith("deny_"):
# # # # # #             handle_admin_response(call)

# # # # # #         elif call.data == "back_to_main":
# # # # # #             bot.delete_message(
# # # # # #                 chat_id=call.message.chat.id, message_id=call.message.message_id
# # # # # #             )
# # # # # #             start(call.message, True)
# # # # # #             return

# # # # # #         if call.data == "lashgarkeshi":
# # # # # #             keyboard = create_keyboard(
# # # # # #                 [
# # # # # #                     ("[⚓] لشکرکشی دریایی ", "sea"),
# # # # # #                     ("[✈️] لشکرکشی هوایی ", "air"),
# # # # # #                     ("[🪖] لشکرکشی زمینی ", "land"),
# # # # # #                 ]
# # # # # #             )
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="نوع لشگرکشی را انتخاب کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )

# # # # # #         elif call.data == "cancel_lashgarkeshi":
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً مبدا لشکرکشی را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, cancel_lashgarkeshi_source)

# # # # # #         elif call.data == "bayanieh":
# # # # # #             keyboard = create_keyboard([("[⏭️] استفاده از تصویر پیش‌فرض", "skip_media")])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً تصویر یا ویدیوی بیانیه را ارسال کنید یا از دکمه زیر برای استفاده از تصویر پیش‌فرض استفاده کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             user_data[call.from_user.id] = {"choice": "بیانیه", "state": BAYANIEH_MEDIA}

# # # # # #         elif call.data == "skip_media":
# # # # # #             user_data[call.from_user.id]["media"] = "default"
# # # # # #             user_data[call.from_user.id]["state"] = BAYANIEH_COUNTRY
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً نام کشور را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )

# # # # # #         elif call.data == "dastor":
# # # # # #             keyboard = create_keyboard(
# # # # # #                 [
# # # # # #                     ("[⚔️] حمله هوایی", "attack_air"),
# # # # # #                     ("[⚔️] حمله زمینی", "attack_ground"),
# # # # # #                     ("[⚔️] حمله دریایی", "attack_sea"),
# # # # # #                     ("[🗡️] دستور محاصره", "siege"),
# # # # # #                 ]
# # # # # #             )
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="نوع دستور را انتخاب کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )

# # # # # #         elif call.data == "siege":
# # # # # #             user_data[call.from_user.id] = {"order": call.data}
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً مبدا محاصره را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, siege_source)

# # # # # #         elif call.data in ["attack_air", "attack_ground", "attack_sea"]:
# # # # # #             user_data[call.from_user.id] = {"order": call.data}
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً نام کشور خود را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, attack_country)

# # # # # #         elif call.data in ["sea", "air", "land"]:
# # # # # #             user_data[call.from_user.id] = {"type": call.data}
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً نام کشور خود را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, lashgarkeshi_country)

# # # # # #         elif call.data in ["attack", "siege"]:
# # # # # #             user_data[call.from_user.id] = {"order": call.data}
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="مکان حمله/محاصره را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, attack_siege_location)

# # # # # #         elif call.data == "confirm":
# # # # # #             handle_confirmation(call)

# # # # # #         elif call.data == "cancel":
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="عملیات لغو شد.",
# # # # # #             )
# # # # # #             start(call.message, True)
# # # # # #         elif call.data == "add":
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً ID را که می‌خواهید اضافه کنید، وارد کنید:",
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, add_number)
# # # # # #         elif call.data == "remove":
# # # # # #             bot.edit_message_text(
# # # # # #                 chat_id=call.message.chat.id,
# # # # # #                 message_id=call.message.message_id,
# # # # # #                 text="لطفاً ID را که می‌خواهید حذف کنید، وارد کنید:",
# # # # # #             )
# # # # # #             bot.register_next_step_handler(call.message, remove_number)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(call.message.chat.id, f"خطا در پردازش درخواست: {str(e)}")


# # # # # # @bot.message_handler(content_types=["photo", "video"])
# # # # # # def handle_media(message):
# # # # # #     try:
# # # # # #         if user_data.get(message.from_user.id, {}).get("state") == BAYANIEH_MEDIA:
# # # # # #             if message.photo:
# # # # # #                 user_data[message.from_user.id]["media"] = message.photo[-1].file_id
# # # # # #                 user_data[message.from_user.id]["media_type"] = "photo"
# # # # # #             elif message.video:
# # # # # #                 user_data[message.from_user.id]["media"] = message.video.file_id
# # # # # #                 user_data[message.from_user.id]["media_type"] = "video"
# # # # # #             user_data[message.from_user.id]["state"] = BAYANIEH_COUNTRY
# # # # # #             keyboard = create_keyboard([])
# # # # # #             bot.reply_to(
# # # # # #                 message,
# # # # # #                 "تصویر/ویدیو دریافت شد. لطفاً نام کشور را وارد کنید:",
# # # # # #                 reply_markup=keyboard,
# # # # # #             )
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش رسانه: {str(e)}")


# # # # # # def lashgarkeshi_country(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["country"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(
# # # # # #             message.chat.id, "مبدا لشکرکشی را انتخاب کنید:", reply_markup=keyboard
# # # # # #         )
# # # # # #         bot.register_next_step_handler(message, lashgarkeshi_source)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش کشور لشکرکشی: {str(e)}")


# # # # # # def attack_country(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["country"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(message.chat.id, "مکان حمله را وارد کنید:", reply_markup=keyboard)
# # # # # #         bot.register_next_step_handler(message, attack_siege_location)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش کشور حمله: {str(e)}")


# # # # # # def cancel_lashgarkeshi_source(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id] = {"source": message.text}
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(
# # # # # #             message.chat.id, "مقصد لشکرکشی را وارد کنید:", reply_markup=keyboard
# # # # # #         )
# # # # # #         bot.register_next_step_handler(message, cancel_lashgarkeshi_destination)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مبدا لغو لشکرکشی: {str(e)}")


# # # # # # def cancel_lashgarkeshi_destination(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["destination"] = message.text
# # # # # #         data = user_data[message.from_user.id]

# # # # # #         cancel_message = f"🚫 لغو لشکرکشی\n\n🪖 لشکرکشی «{data['source']}» به سمت «{data['destination']}» لغو شد.\n\n👤فرمانده: {get_user_link(message.from_user.id)}"

# # # # # #         try:
# # # # # #             with open(CANCEL_LASHKARKESHI_PHOTO, "rb") as photo:
# # # # # #                 bot.send_photo(COMMANDS_CHANNEL, photo, caption=cancel_message, parse_mode='HTML')
# # # # # #         except FileNotFoundError:
# # # # # #             bot.send_message(COMMANDS_CHANNEL, cancel_message)

# # # # # #         bot.send_message(message.chat.id, "درخواست لغو لشکرکشی با موفقیت ارسال شد.")
# # # # # #         start(message, True)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مقصد لغو لشکرکشی: {str(e)}")


# # # # # # @bot.message_handler(func=lambda message: True)
# # # # # # def handle_all_messages(message):
# # # # # #     try:
# # # # # #         user_id = message.from_user.id
# # # # # #         user_state = user_data.get(user_id, {}).get("state")

# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return

# # # # # #         if user_data.get(user_id, {}).get("choice") == "بیانیه":
# # # # # #             if user_state == BAYANIEH_COUNTRY:
# # # # # #                 user_data.setdefault(user_id, {})["country"] = message.text
# # # # # #                 user_data[user_id]["state"] = BAYANIEH_TEXT
# # # # # #                 bot.reply_to(message, "اکنون متن بیانیه خود را ارسال کنید:")
# # # # # #             elif user_state == BAYANIEH_TEXT:
# # # # # #                 country = user_data.get(user_id, {}).get("country")
# # # # # #                 if not country:
# # # # # #                     bot.reply_to(message, "خطا: لطفاً ابتدا نام کشور را وارد کنید.")
# # # # # #                     user_data[user_id]["state"] = BAYANIEH_COUNTRY
# # # # # #                     return

# # # # # #                 media = user_data[user_id].get("media", "default")
# # # # # #                 caption = f"بیانیه از: {get_user_link(message.from_user.id)}\nکشور: {country}\n\n{message.text}"

# # # # # #                 # Store the bayanieh data in the global dictionary
# # # # # #                 pending_bayanieh[user_id] = {
# # # # # #                     "media": media,
# # # # # #                     "media_type": user_data[user_id].get("media_type"),
# # # # # #                     "caption": caption,
# # # # # #                 }

# # # # # #                 # Send message to admin for approval
# # # # # #                 keyboard = InlineKeyboardMarkup()
# # # # # #                 keyboard.row(
# # # # # #                     InlineKeyboardButton("Allow", callback_data=f"allow_{user_id}"),
# # # # # #                     InlineKeyboardButton("Deny", callback_data=f"deny_{user_id}"),
# # # # # #                 )

# # # # # #                 admin_message = f"New bayanieh from user {user_id}:\n\n{caption}\n\nDo you want to approve this bayanieh?"
# # # # # #                 bot.send_message(ADMIN_ID, admin_message, reply_markup=keyboard, parse_mode='HTML')

# # # # # #                 bot.reply_to(
# # # # # #                     message, "بیانیه شما برای تایید ارسال شد. لطفاً منتظر تایید ادمین باشید."
# # # # # #                 )
# # # # # #                 start(message, True)
# # # # # #                 user_data[user_id]["state"] = CHOOSING  # Reset state
# # # # # #             else:
# # # # # #                 bot.reply_to(message, "لطفا ابتدا تصویر یا ویدیوی بیانیه را ارسال کنید.")
# # # # # #         else:
# # # # # #             bot.reply_to(message, "لطفا یک گزینه معتبر انتخاب کنید.")
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش پیام: {str(e)}")


# # # # # # def handle_admin_response(call):
# # # # # #     global pending_bayanieh
# # # # # #     try:
# # # # # #         action, user_id = call.data.split("_")
# # # # # #         user_id = int(user_id)

# # # # # #         if user_id not in pending_bayanieh:
# # # # # #             bot.answer_callback_query(call.id, "Error: Bayanieh data not found.")
# # # # # #             return

# # # # # #         if action == "allow":
# # # # # #             bayanieh_data = pending_bayanieh[user_id]
# # # # # #             media = bayanieh_data["media"]
# # # # # #             caption = bayanieh_data["caption"]

# # # # # #             if media == "default":
# # # # # #                 try:
# # # # # #                     with open(BAYANIEH_PHOTO, "rb") as photo:
# # # # # #                         bot.send_photo(ANNOUNCEMENT_CHANNEL, photo, caption=caption, parse_mode='HTML')
# # # # # #                 except FileNotFoundError:
# # # # # #                     bot.send_message(ANNOUNCEMENT_CHANNEL, caption)
# # # # # #             else:
# # # # # #                 if bayanieh_data["media_type"] == "photo":
# # # # # #                     bot.send_photo(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')
# # # # # #                 elif bayanieh_data["media_type"] == "video":
# # # # # #                     bot.send_video(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')

# # # # # #             bot.answer_callback_query(call.id, "Bayanieh approved and sent to the channel.")
# # # # # #             bot.send_message(user_id, "بیانیه شما تایید و ارسال شد.")
# # # # # #         else:  # deny
# # # # # #             bot.answer_callback_query(call.id, "Bayanieh denied.")
# # # # # #             bot.send_message(user_id, "متاسفانه بیانیه شما تایید نشد.")

# # # # # #         # Remove the bayanieh data from the global dictionary
# # # # # #         del pending_bayanieh[user_id]

# # # # # #         # Edit the admin's message to remove the buttons
# # # # # #         bot.edit_message_reply_markup(
# # # # # #             call.message.chat.id, call.message.message_id, reply_markup=None
# # # # # #         )
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(call.message.chat.id, f"خطا در پردازش پاسخ ادمین: {str(e)}")


# # # # # # def add_number(message):
# # # # # #     try:
# # # # # #         number = message.text
# # # # # #         if not number.isdigit():
# # # # # #             bot.send_message(message.chat.id, "لطفاً یک ID معتبر وارد کنید.")
# # # # # #             return

# # # # # #         with open(ALLOWED_IDS_FILE, "r") as file:
# # # # # #             rows = list(csv.reader(file))

# # # # # #         for row in rows:
# # # # # #             if row and row[0] == number:
# # # # # #                 bot.send_message(message.chat.id, f"ID {number} قبلاً اضافه شده است.")
# # # # # #                 start(message)
# # # # # #                 return

# # # # # #         with open(ALLOWED_IDS_FILE, "a", newline="") as file:
# # # # # #             writer = csv.writer(file)
# # # # # #             writer.writerow([number])

# # # # # #         bot.send_message(message.chat.id, f"ID {number} با موفقیت اضافه شد.")
# # # # # #         start(message)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در افزودن شماره: {str(e)}")


# # # # # # def remove_number(message):
# # # # # #     try:
# # # # # #         number = message.text
# # # # # #         if not number.isdigit():
# # # # # #             bot.send_message(message.chat.id, "لطفاً یک ID معتبر وارد کنید.")
# # # # # #             return

# # # # # #         with open(ALLOWED_IDS_FILE, "r") as file:
# # # # # #             rows = list(csv.reader(file))

# # # # # #         for row in rows:
# # # # # #             if row and row[0] == number:
# # # # # #                 rows.remove(row)
# # # # # #                 with open(ALLOWED_IDS_FILE, "w", newline="") as file:
# # # # # #                     writer = csv.writer(file)
# # # # # #                     writer.writerows(rows)
# # # # # #                 bot.send_message(message.chat.id, f"عدد {number} با موفقیت حذف شد.")
# # # # # #                 start(message)
# # # # # #                 return

# # # # # #         bot.send_message(message.chat.id, f"عدد {number} وجود ندارد.")
# # # # # #         start(message)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در حذف شماره: {str(e)}")


# # # # # # def siege_source(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["source"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(
# # # # # #             message.chat.id, "لطفاً مقصد محاصره را وارد کنید:", reply_markup=keyboard
# # # # # #         )
# # # # # #         bot.register_next_step_handler(message, siege_destination)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مبدا محاصره: {str(e)}")


# # # # # # def siege_destination(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["destination"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
# # # # # #         bot.register_next_step_handler(message, attack_siege_army_stats)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مقصد محاصره: {str(e)}")


# # # # # # def lashgarkeshi_source(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["source"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(
# # # # # #             message.chat.id, "مقصد لشکرکشی را وارد کنید:", reply_markup=keyboard
# # # # # #         )
# # # # # #         bot.register_next_step_handler(message, lashgarkeshi_destination)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مبدا لشکرکشی: {str(e)}")


# # # # # # def lashgarkeshi_destination(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["destination"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
# # # # # #         bot.register_next_step_handler(message, lashgarkeshi_army_stats)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مقصد لشکرکشی: {str(e)}")


# # # # # # def lashgarkeshi_army_stats(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["army_stats"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(
# # # # # #             message.chat.id, "زمان رسیدن به مقصد را وارد کنید:", reply_markup=keyboard
# # # # # #         )
# # # # # #         bot.register_next_step_handler(message, lashgarkeshi_arrival_time)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش آمار ارتش: {str(e)}")


# # # # # # def lashgarkeshi_arrival_time(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["arrival_time"] = message.text
# # # # # #         data = user_data[message.from_user.id]
# # # # # #         confirmation_text = (
# # # # # #             f"لطفا اطلاعات زیر را تایید کنید:\n\n"
# # # # # #             f"لشگرکشی نوع: {data['type']}\n"
# # # # # #             f"فرمانده: {message.from_user.username}\n"
# # # # # #             f"مبدا: {data['source']}\n"
# # # # # #             f"مقصد: {data['destination']}\n"
# # # # # #             f"آمار ارتش: {data['army_stats']}\n"
# # # # # #             f"زمان رسیدن: {data['arrival_time']}\n\n"
# # # # # #             f"آیا این اطلاعات صحیح است؟"
# # # # # #         )
# # # # # #         keyboard = create_keyboard([("[✅] تایید", "confirm"), ("[❌] لغو", "cancel")])
# # # # # #         bot.send_message(message.chat.id, confirmation_text, reply_markup=keyboard)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش زمان رسیدن: {str(e)}")


# # # # # # def attack_siege_location(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["location"] = message.text
# # # # # #         keyboard = create_keyboard([])
# # # # # #         bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
# # # # # #         bot.register_next_step_handler(message, attack_siege_army_stats)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش مکان حمله/محاصره: {str(e)}")


# # # # # # def attack_siege_army_stats(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         user_data[message.from_user.id]["army_stats"] = message.text
# # # # # #         data = user_data[message.from_user.id]

# # # # # #         attack_type = ""
# # # # # #         photo_path = ""
# # # # # #         if data["order"] == "attack_air":
# # # # # #             attack_type = "هوایی"
# # # # # #             photo_path = ATTACK_AIR_PHOTO
# # # # # #         elif data["order"] == "attack_ground":
# # # # # #             attack_type = "زمینی"
# # # # # #             photo_path = ATTACK_GROUND_PHOTO
# # # # # #         elif data["order"] == "attack_sea":
# # # # # #             attack_type = "دریایی"
# # # # # #             photo_path = ATTACK_SEA_PHOTO
# # # # # #         elif data["order"] == "siege":
# # # # # #             photo_path = SIEGE_PHOTO

# # # # # #         if data["order"].startswith("attack"):
# # # # # #             attack_message = f"""⚔️دستور حمله {attack_type} ارتش «{data['country']}» به «{data['location']}» صادر شد.\n\n👤فرمانده : {message.from_user.id}\n🗣سناریو نبرد را طبق اعلام ادمین جنگ ارسال کنید."""
# # # # # #             with open(photo_path, "rb") as photo:
# # # # # #                 bot.send_photo(COMMANDS_CHANNEL, photo, caption=attack_message, parse_mode='HTML')
# # # # # #         else:  # siege
# # # # # #             siege_message = f"دستور محاصره «{data['source']}» توسط «{data['country']}» صادر شد.\n\n👤فرمانده: {message.from_user.id}"
# # # # # #             with open(photo_path, "rb") as photo:
# # # # # #                 bot.send_photo(COMMANDS_CHANNEL, photo, caption=siege_message, parse_mode='HTML')

# # # # # #         bot.send_message(message.chat.id, "اطلاعات شما با موفقیت ارسال شد.")
# # # # # #         start(message, True)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش آمار ارتش: {str(e)}")


# # # # # # @bot.message_handler(func=lambda message: True)
# # # # # # def bayanieh(message):
# # # # # #     try:
# # # # # #         if message.text == "بازگشت به منوی اصلی":
# # # # # #             start(message)
# # # # # #             return
# # # # # #         if user_data.get(message.from_user.id, {}).get("choice") == "بیانیه":
# # # # # #             with open(BAYANIEH_PHOTO, "rb") as photo:
# # # # # #                 bot.send_photo(
# # # # # #                     ANNOUNCEMENT_CHANNEL,
# # # # # #                     photo,
# # # # # #                     caption=f"بیانیه از: {message.from_user.id}\n\n{message.text}",
# # # # # #                     parse_mode='HTML',
# # # # # #                 )
# # # # # #             start(message, True)
# # # # # #         else:
# # # # # #             bot.reply_to(message, "لطفا یک گزینه معتبر انتخاب کنید.")
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(message.chat.id, f"خطا در پردازش بیانیه: {str(e)}")


# # # # # # def handle_confirmation(call):
# # # # # #     try:
# # # # # #         data = user_data[call.from_user.id]
# # # # # #         if data["type"] == "air":
# # # # # #             attack_type = "هوایی"
# # # # # #         elif data["type"] == "land":
# # # # # #             attack_type = "زمینی"
# # # # # #         elif data["type"] == "sea":
# # # # # #             attack_type = "دریایی"
# # # # # #         else:
# # # # # #             attack_type = ""

# # # # # #         channel_message_text = f"🪖 ناوگان {attack_type} «{data['country']}» از «{data['source']}» به سمت «{data['destination']}» حرکت کرد.\n\n⏳زمان رسیدن: {data['arrival_time']}\n👤فرمانده : {get_user_link(call.from_user.id)}\n"

# # # # # #         reply_message_text = (
# # # # # #             f"لشگرکشی نوع: {attack_type} \n"
# # # # # #             f"کشور: {data['country']}\n"
# # # # # #             f"فرمانده: @{call.from_user.username}\n"
# # # # # #             f"مبدا: {data['source']}\n"
# # # # # #             f"مقصد: {data['destination']}\n"
# # # # # #             f"آمار ارتش: {data['army_stats']}\n"
# # # # # #             f"زمان رسیدن: {data['arrival_time']}\n"
# # # # # #         )

# # # # # #         if data["type"] == "air":
# # # # # #             photo_path = LASHGARKESHI_AIR_PHOTO
# # # # # #         elif data["type"] == "land":
# # # # # #             photo_path = LASHGARKESHI_GROUND_PHOTO
# # # # # #         elif data["type"] == "sea":
# # # # # #             photo_path = LASHGARKESHI_SEA_PHOTO
# # # # # #         else:
# # # # # #             photo_path = LASHGARKESHI_GROUND_PHOTO

# # # # # #         with open(photo_path, "rb") as photo:
# # # # # #             bot.send_photo(COMMANDS_CHANNEL, photo, caption=channel_message_text, parse_mode='HTML')

# # # # # #         bot.edit_message_text(
# # # # # #             chat_id=call.message.chat.id,
# # # # # #             message_id=call.message.message_id,
# # # # # #             text="اطلاعات شما با موفقیت ارسال شد.",
# # # # # #         )
# # # # # #         bot.send_message(call.message.chat.id, reply_message_text)
# # # # # #         start(call.message, True)
# # # # # #     except Exception as e:
# # # # # #         bot.send_message(call.message.chat.id, f"خطا در پردازش تایید: {str(e)}")


# # # # # # if __name__ == "__main__":
# # # # # #     bot.polling(none_stop=True)



import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import csv

ANNOUNCEMENT_CHANNEL = "@FallOfWorldNews"
COMMANDS_CHANNEL = "@FallOfWorld"
BOT_TOKEN = "7731223537:AAG0CECDuuzPX0L1MtgtZak5LxxFNLJy7RA"  # Replace with your actual bot token
ADMIN_ID = 1552249508
ALLOWED_IDS_FILE = "allowed_ids.csv"
PASSWORD = RodeosGG2311

pending_bayanieh = {}
bot = telebot.TeleBot(BOT_TOKEN)

# Flag to allow all bayanieh messages
ALLOW_ALL_BAYANIEH = False

# Define states
(
    MAIN_MENU,
    CHOOSING,
    LASHGARKESHI,
    LASHGARKESHI_TYPE,
    SOURCE,
    DESTINATION,
    ARMY_STATS,
    ARRIVAL_TIME,
    ATTACK_OR_SIEGE,
    LOCATION,
    CONFIRMATION,
) = range(11)
BAYANIEH_MEDIA, BAYANIEH_COUNTRY, BAYANIEH_TEXT = range(3)

# Store user data
user_data = {}
ALLOWED = []

# Define photo paths
CANCEL_LASHKARKESHI_PHOTO = os.path.join("photos/cancel_lashkarkeshy.jpg")
BAYANIEH_PHOTO = os.path.join("photos/bayanieh.jpg")
LASHGARKESHI_AIR_PHOTO = os.path.join("photos/lash_air.jpg")
LASHGARKESHI_GROUND_PHOTO = os.path.join("photos/lash_ground.jpg")
LASHGARKESHI_SEA_PHOTO = os.path.join("photos/lash_naval.jpg")
ATTACK_GROUND_PHOTO = os.path.join("photos/attack_ground.jpg")
ATTACK_AIR_PHOTO = os.path.join("photos/attack_air.jpg")
ATTACK_SEA_PHOTO = os.path.join("photos/attack_sea.jpg")
SIEGE_PHOTO = os.path.join("photos/siege.jpg")


def create_keyboard(buttons, include_back=True):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for button in buttons:
        keyboard.add(InlineKeyboardButton(f" {button[0]} ", callback_data=button[1]))
    if include_back:
        keyboard.add(
            InlineKeyboardButton(
                "📜 بازگشت به منوی اصلی 📜", callback_data="back_to_main"
            )
        )
    return keyboard


def get_user_link(user_id):
    return f'<a href="tg://user?id={user_id}">{user_id}</a>'


def get_user_mention(user_id, username=None):
    if username:
        return f"@{username}"
    else:
        return f'<a href="tg://user?id={user_id}">فرمانده</a>'


def clear_step_handler(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)


def check_allowance(message):
    if message.from_user.id == ADMIN_ID or message.from_user.id in ALLOWED:
        return True
    else:
        bot.send_message(message.chat.id, "لطفا رمز عبور را وارد کنید:")
        bot.register_next_step_handler(message, validate_password)
        return False


def validate_password(message):
    try:
        if message.text.isdigit() and int(message.text) == PASSWORD:
            bot.send_message(message.chat.id, "رمز عبور صحیح است. خوش آمدید!")
            if message.from_user.id not in ALLOWED:
                ALLOWED.append(message.from_user.id)
            start(message, allowed=True)
        else:
            bot.send_message(message.chat.id, "رمز عبور اشتباه است. لطفا دوباره تلاش کنید:")
            bot.register_next_step_handler(message, validate_password)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در اعتبارسنجی رمز عبور: {str(e)}")


@bot.message_handler(commands=["start"])
def start(message, allowed=False):
    try:
        get_user_mention(message, message.from_user.id)
        clear_step_handler(message)
        if not allowed:
            if message.from_user.id != ADMIN_ID:
                if not check_allowance(message):
                    return

        buttons = [
            ("[⚔️] لشکرکشی ", "lashgarkeshi"),
            ("[📢] بیانیه ", "bayanieh"),
            ("[🧨] دستور حمله/محاصره ", "dastor"),
            ("[❌] لغو لشکرکشی ", "cancel_lashgarkeshi"),  # New button
        ]

        # Add Admin Panel button only for admin
        if message.from_user.id == ADMIN_ID:
            buttons.append(("[🔧] پنل ادمین", "admin_panel"))

        keyboard = create_keyboard(buttons, include_back=False)
        bot.send_message(message.chat.id, "یک گزینه را انتخاب کنید:", reply_markup=keyboard)
        user_data[message.from_user.id] = {"state": MAIN_MENU}
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در شروع: {str(e)}")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    clear_step_handler(call.message)

    try:
        if call.data.startswith("allow_") or call.data.startswith("deny_"):
            handle_admin_response(call)

        elif call.data == "back_to_main":
            bot.delete_message(
                chat_id=call.message.chat.id, message_id=call.message.message_id
            )
            start(call.message, True)
            return

        if call.data == "lashgarkeshi":
            keyboard = create_keyboard(
                [
                    ("[⚓] لشکرکشی دریایی ", "sea"),
                    ("[✈️] لشکرکشی هوایی ", "air"),
                    ("[🪖] لشکرکشی زمینی ", "land"),
                ]
            )
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="نوع لشگرکشی را انتخاب کنید:",
                reply_markup=keyboard,
            )

        elif call.data == "cancel_lashgarkeshi":
            keyboard = create_keyboard([])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً مبدا لشکرکشی را وارد کنید:",
                reply_markup=keyboard,
            )
            bot.register_next_step_handler(call.message, cancel_lashgarkeshi_source)

        elif call.data == "bayanieh":
            keyboard = create_keyboard([("[⏭️] استفاده از تصویر پیش‌فرض", "skip_media")])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً تصویر یا ویدیوی بیانیه را ارسال کنید یا از دکمه زیر برای استفاده از تصویر پیش‌فرض استفاده کنید:",
                reply_markup=keyboard,
            )
            user_data[call.from_user.id] = {"choice": "بیانیه", "state": BAYANIEH_MEDIA}

        elif call.data == "skip_media":
            user_data[call.from_user.id]["media"] = "default"
            user_data[call.from_user.id]["state"] = BAYANIEH_COUNTRY
            keyboard = create_keyboard([])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً نام کشور را وارد کنید:",
                reply_markup=keyboard,
            )

        elif call.data == "dastor":
            keyboard = create_keyboard(
                [
                    ("[⚔️] حمله هوایی", "attack_air"),
                    ("[⚔️] حمله زمینی", "attack_ground"),
                    ("[⚔️] حمله دریایی", "attack_sea"),
                    ("[🗡️] دستور محاصره", "siege"),
                ]
            )
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="نوع دستور را انتخاب کنید:",
                reply_markup=keyboard,
            )

        elif call.data == "admin_panel":
            # Ask for confirmation to allow all bayanieh messages
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton("بله", callback_data="confirm_allow_all"), 
                         InlineKeyboardButton("خیر", callback_data="cancel_allow_all"))
            bot.send_message(call.message.chat.id, "آیا می‌خواهید تمام بیانیه‌ها را به طور پیش‌فرض تایید کنید؟", reply_markup=keyboard)
            return  # Exit the function after sending the message

        elif call.data == "confirm_allow_all":
            global ALLOW_ALL_BAYANIEH
            ALLOW_ALL_BAYANIEH = True
            bot.send_message(call.message.chat.id, "تمام بیانیه‌ها به طور پیش‌فرض تایید خواهند شد.")
            return  # Exit the function after confirming

        elif call.data == "cancel_allow_all":
            bot.send_message(call.message.chat.id, "تایید تمام بیانیه‌ها لغو شد.")
            return  # Exit the function after canceling

        elif call.data in ["attack_air", "attack_ground", "attack_sea"]:
            user_data[call.from_user.id] = {"order": call.data}
            keyboard = create_keyboard([])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً نام کشور خود را وارد کنید:",
                reply_markup=keyboard,
            )
            bot.register_next_step_handler(call.message, attack_country)

        elif call.data in ["sea", "air", "land"]:
            user_data[call.from_user.id] = {"type": call.data}
            keyboard = create_keyboard([])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً نام کشور را وارد کنید:",
                reply_markup=keyboard,
            )
            bot.register_next_step_handler(call.message, lashgarkeshi_country)

        elif call.data in ["attack", "siege"]:
            user_data[call.from_user.id] = {"order": call.data}
            keyboard = create_keyboard([])
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="مکان حمله/محاصره را وارد کنید:",
                reply_markup=keyboard,
            )
            bot.register_next_step_handler(call.message, attack_siege_location)

        elif call.data == "confirm":
            handle_confirmation(call)

        elif call.data == "cancel":
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="عملیات لغو شد.",
            )
            start(call.message, True)
        elif call.data == "add":
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً ID را که می‌خواهید اضافه کنید، وارد کنید:",
            )
            bot.register_next_step_handler(call.message, add_number)
        elif call.data == "remove":
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text="لطفاً ID را که می‌خواهید حذف کنید، وارد کنید:",
            )
            bot.register_next_step_handler(call.message, remove_number)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"خطا در پردازش درخواست: {str(e)}")


@bot.message_handler(content_types=["photo", "video"])
def handle_media(message):
    try:
        if user_data.get(message.from_user.id, {}).get("state") == BAYANIEH_MEDIA:
            if message.photo:
                user_data[message.from_user.id]["media"] = message.photo[-1].file_id
                user_data[message.from_user.id]["media_type"] = "photo"
            elif message.video:
                user_data[message.from_user.id]["media"] = message.video.file_id
                user_data[message.from_user.id]["media_type"] = "video"
            user_data[message.from_user.id]["state"] = BAYANIEH_COUNTRY
            keyboard = create_keyboard([])
            bot.reply_to(
                message,
                "تصویر/ویدیو دریافت شد. لطفاً نام کشور را وارد کنید:",
                reply_markup=keyboard,
            )
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش رسانه: {str(e)}")


def lashgarkeshi_country(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["country"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(
            message.chat.id, "مبدا لشکرکشی را انتخاب کنید:", reply_markup=keyboard
        )
        bot.register_next_step_handler(message, lashgarkeshi_source)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش کشور لشکرکشی: {str(e)}")


def attack_country(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["country"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(message.chat.id, "مکان حمله را وارد کنید:", reply_markup=keyboard)
        bot.register_next_step_handler(message, attack_siege_location)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش کشور حمله: {str(e)}")


def cancel_lashgarkeshi_source(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id] = {"source": message.text}
        keyboard = create_keyboard([])
        bot.send_message(
            message.chat.id, "مقصد لشکرکشی را وارد کنید:", reply_markup=keyboard
        )
        bot.register_next_step_handler(message, cancel_lashgarkeshi_destination)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مبدا لغو لشکرکشی: {str(e)}")


def cancel_lashgarkeshi_destination(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["destination"] = message.text
        data = user_data[message.from_user.id]

        cancel_message = f"🚫 لغو لشکرکشی\n\n🪖 لشکرکشی «{data['source']}» به سمت «{data['destination']}» لغو شد.\n\n👤فرمانده: {get_user_link(message.from_user.id)}"

        try:
            with open(CANCEL_LASHKARKESHI_PHOTO, "rb") as photo:
                bot.send_photo(COMMANDS_CHANNEL, photo, caption=cancel_message, parse_mode='HTML')
        except FileNotFoundError:
            bot.send_message(COMMANDS_CHANNEL, cancel_message)

        bot.send_message(message.chat.id, "درخواست لغو لشکرکشی با موفقیت ارسال شد.")
        start(message, True)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مقصد لغو لشکرکشی: {str(e)}")


@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        user_id = message.from_user.id
        user_state = user_data.get(user_id, {}).get("state")

        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return

        if user_data.get(user_id, {}).get("choice") == "بیانیه":
            if user_state == BAYANIEH_COUNTRY:
                user_data.setdefault(user_id, {})["country"] = message.text
                user_data[user_id]["state"] = BAYANIEH_TEXT
                bot.reply_to(message, "اکنون متن بیانیه خود را ارسال کنید:")
            elif user_state == BAYANIEH_TEXT:
                country = user_data.get(user_id, {}).get("country")
                if not country:
                    bot.reply_to(message, "خطا: لطفاً ابتدا نام کشور را وارد کنید.")
                    user_data[user_id]["state"] = BAYANIEH_COUNTRY
                    return

                media = user_data[user_id].get("media", "default")
                caption = f"بیانیه از: {get_user_link(message.from_user.id)}\nکشور: {country}\n\n{message.text}"

                # Store the bayanieh data in the global dictionary
                pending_bayanieh[user_id] = {
                    "media": media,
                    "media_type": user_data[user_id].get("media_type"),
                    "caption": caption,
                }

                # Automatically allow bayanieh if the flag is set
                if ALLOW_ALL_BAYANIEH:
                    # Send the bayanieh to the announcement channel
                    if media == "default":
                        try:
                            with open(BAYANIEH_PHOTO, "rb") as photo:
                                bot.send_photo(ANNOUNCEMENT_CHANNEL, photo, caption=caption, parse_mode='HTML')
                        except FileNotFoundError:
                            bot.send_message(ANNOUNCEMENT_CHANNEL, caption)
                    else:
                        if user_data[user_id]["media_type"] == "photo":
                            bot.send_photo(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')
                        elif user_data[user_id]["media_type"] == "video":
                            bot.send_video(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')

                    bot.send_message(user_id, "بیانیه شما تایید و ارسال شد.")
                else:
                    # Send message to admin for approval
                    keyboard = InlineKeyboardMarkup()
                    keyboard.row(
                        InlineKeyboardButton("Allow", callback_data=f"allow_{user_id}"),
                        InlineKeyboardButton("Deny", callback_data=f"deny_{user_id}"),
                    )

                    admin_message = f"New bayanieh from user {user_id}:\n\n{caption}\n\nDo you want to approve this bayanieh?"
                    bot.send_message(ADMIN_ID, admin_message, reply_markup=keyboard, parse_mode='HTML')

                    bot.reply_to(
                        message, "بیانیه شما برای تایید ارسال شد. لطفاً منتظر تایید ادمین باشید."
                    )
                    start(message, True)
                    user_data[user_id]["state"] = CHOOSING  # Reset state
            else:
                bot.reply_to(message, "لطفا ابتدا تصویر یا ویدیوی بیانیه را ارسال کنید.")
        else:
            bot.reply_to(message, "لطفا یک گزینه معتبر انتخاب کنید.")
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش پیام: {str(e)}")


def handle_admin_response(call):
    global pending_bayanieh
    try:
        action, user_id = call.data.split("_")
        user_id = int(user_id)

        if action == "allow":
            bayanieh_data = pending_bayanieh[user_id]
            media = bayanieh_data["media"]
            caption = bayanieh_data["caption"]

            if media == "default":
                try:
                    with open(BAYANIEH_PHOTO, "rb") as photo:
                        bot.send_photo(ANNOUNCEMENT_CHANNEL, photo, caption=caption, parse_mode='HTML')
                except FileNotFoundError:
                    bot.send_message(ANNOUNCEMENT_CHANNEL, caption)
            else:
                if bayanieh_data["media_type"] == "photo":
                    bot.send_photo(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')
                elif bayanieh_data["media_type"] == "video":
                    bot.send_video(ANNOUNCEMENT_CHANNEL, media, caption=caption, parse_mode='HTML')

            bot.send_message(user_id, "بیانیه شما تایید و ارسال شد.")
        else:  # deny
            bot.send_message(user_id, "متاسفانه بیانیه شما تایید نشد.")

        # Remove the bayanieh data from the global dictionary
        del pending_bayanieh[user_id]

        # Edit the admin's message to remove the buttons
        bot.edit_message_reply_markup(
            call.message.chat.id, call.message.message_id, reply_markup=None
        )
    except Exception as e:
        bot.send_message(call.message.chat.id, f"خطا در پردازش پاسخ ادمین: {str(e)}")


def add_number(message):
    try:
        number = message.text
        if not number.isdigit():
            bot.send_message(message.chat.id, "لطفاً یک ID معتبر وارد کنید.")
            return

        with open(ALLOWED_IDS_FILE, "r") as file:
            rows = list(csv.reader(file))

        for row in rows:
            if row and row[0] == number:
                bot.send_message(message.chat.id, f"ID {number} قبلاً اضافه شده است.")
                start(message)
                return

        with open(ALLOWED_IDS_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([number])

        bot.send_message(message.chat.id, f"ID {number} با موفقیت اضافه شد.")
        start(message)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در افزودن شماره: {str(e)}")


def remove_number(message):
    try:
        number = message.text
        if not number.isdigit():
            bot.send_message(message.chat.id, "لطفاً یک ID معتبر وارد کنید.")
            return

        with open(ALLOWED_IDS_FILE, "r") as file:
            rows = list(csv.reader(file))

        for row in rows:
            if row and row[0] == number:
                rows.remove(row)
                with open(ALLOWED_IDS_FILE, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                bot.send_message(message.chat.id, f"عدد {number} با موفقیت حذف شد.")
                start(message)
                return

        bot.send_message(message.chat.id, f"عدد {number} وجود ندارد.")
        start(message)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در حذف شماره: {str(e)}")


def siege_source(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["source"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(
            message.chat.id, "لطفاً مقصد محاصره را وارد کنید:", reply_markup=keyboard
        )
        bot.register_next_step_handler(message, siege_destination)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مبدا محاصره: {str(e)}")


def siege_destination(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["destination"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
        bot.register_next_step_handler(message, attack_siege_army_stats)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مقصد محاصره: {str(e)}")


def lashgarkeshi_source(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["source"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(
            message.chat.id, "مقصد لشکرکشی را وارد کنید:", reply_markup=keyboard
        )
        bot.register_next_step_handler(message, lashgarkeshi_destination)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مبدا لشکرکشی: {str(e)}")


def lashgarkeshi_destination(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["destination"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
        bot.register_next_step_handler(message, lashgarkeshi_army_stats)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مقصد لشکرکشی: {str(e)}")


def lashgarkeshi_army_stats(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["army_stats"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(
            message.chat.id, "زمان رسیدن به مقصد را وارد کنید:", reply_markup=keyboard
        )
        bot.register_next_step_handler(message, lashgarkeshi_arrival_time)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش آمار ارتش: {str(e)}")


def lashgarkeshi_arrival_time(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["arrival_time"] = message.text
        data = user_data[message.from_user.id]
        confirmation_text = (
            f"لطفا اطلاعات زیر را تایید کنید:\n\n"
            f"لشگرکشی نوع: {data['type']}\n"
            f"فرمانده: {message.from_user.username}\n"
            f"مبدا: {data['source']}\n"
            f"مقصد: {data['destination']}\n"
            f"آمار ارتش: {data['army_stats']}\n"
            f"زمان رسیدن: {data['arrival_time']}\n\n"
            f"آیا این اطلاعات صحیح است؟"
        )
        keyboard = create_keyboard([("[✅] تایید", "confirm"), ("[❌] لغو", "cancel")])
        bot.send_message(message.chat.id, confirmation_text, reply_markup=keyboard)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش زمان رسیدن: {str(e)}")


def attack_siege_location(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["location"] = message.text
        keyboard = create_keyboard([])
        bot.send_message(message.chat.id, "آمار ارتش را وارد کنید:", reply_markup=keyboard)
        bot.register_next_step_handler(message, attack_siege_army_stats)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش مکان حمله/محاصره: {str(e)}")


def attack_siege_army_stats(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        user_data[message.from_user.id]["army_stats"] = message.text
        data = user_data[message.from_user.id]

        attack_type = ""
        photo_path = ""
        if data["order"] == "attack_air":
            attack_type = "هوایی"
            photo_path = ATTACK_AIR_PHOTO
        elif data["order"] == "attack_ground":
            attack_type = "زمینی"
            photo_path = ATTACK_GROUND_PHOTO
        elif data["order"] == "attack_sea":
            attack_type = "دریایی"
            photo_path = ATTACK_SEA_PHOTO
        elif data["order"] == "siege":
            photo_path = SIEGE_PHOTO

        if data["order"].startswith("attack"):
            attack_message = f"""⚔️دستور حمله {attack_type} ارتش «{data['country']}» به «{data['location']}» صادر شد.\n\n👤فرمانده : {data['country']}\n🗣سناریو نبرد را طبق اعلام ادمین جنگ ارسال کنید."""
            with open(photo_path, "rb") as photo:
                bot.send_photo(COMMANDS_CHANNEL, photo, caption=attack_message, parse_mode='HTML')
        else:  # siege
            siege_message = f"دستور محاصره «{data['source']}» توسط «{data['country']}» صادر شد.\n\n👤فرمانده: {data['country']}"
            with open(photo_path, "rb") as photo:
                bot.send_photo(COMMANDS_CHANNEL, photo, caption=siege_message, parse_mode='HTML')

        bot.send_message(message.chat.id, "اطلاعات شما با موفقیت ارسال شد.")
        start(message, True)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش آمار ارتش: {str(e)}")


@bot.message_handler(func=lambda message: True)
def bayanieh(message):
    try:
        if message.text == "بازگشت به منوی اصلی":
            start(message)
            return
        if user_data.get(message.from_user.id, {}).get("choice") == "بیانیه":
            with open(BAYANIEH_PHOTO, "rb") as photo:
                bot.send_photo(
                    ANNOUNCEMENT_CHANNEL,
                    photo,
                    caption=f"بیانیه از: {message.from_user.id}\n\n{message.text}",
                    parse_mode='HTML',
                )
            start(message, True)
        else:
            bot.reply_to(message, "لطفا یک گزینه معتبر انتخاب کنید.")
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش بیانیه: {str(e)}")


def handle_confirmation(call):
    try:
        data = user_data[call.from_user.id]
        if data["type"] == "air":
            attack_type = "هوایی"
        elif data["type"] == "land":
            attack_type = "زمینی"
        elif data["type"] == "sea":
            attack_type = "دریایی"
        else:
            attack_type = ""

        channel_message_text = f"🪖 ناوگان {attack_type} «{data['country']}» از «{data['source']}» به سمت «{data['destination']}» حرکت کرد.\n\n⏳زمان رسیدن: {data['arrival_time']}\n👤فرمانده : {get_user_link(call.from_user.id)}\n"

        reply_message_text = (
            f"لشگرکشی نوع: {attack_type} \n"
            f"کشور: {data['country']}\n"
            f"فرمانده: @{call.from_user.username}\n"
            f"مبدا: {data['source']}\n"
            f"مقصد: {data['destination']}\n"
            f"آمار ارتش: {data['army_stats']}\n"
            f"زمان رسیدن: {data['arrival_time']}\n"
        )

        if data["type"] == "air":
            photo_path = LASHGARKESHI_AIR_PHOTO
        elif data["type"] == "land":
            photo_path = LASHGARKESHI_GROUND_PHOTO
        elif data["type"] == "sea":
            photo_path = LASHGARKESHI_SEA_PHOTO
        else:
            photo_path = LASHGARKESHI_GROUND_PHOTO

        with open(photo_path, "rb") as photo:
            bot.send_photo(COMMANDS_CHANNEL, photo, caption=channel_message_text, parse_mode='HTML')

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="اطلاعات شما با موفقیت ارسال شد.",
        )
        bot.send_message(call.message.chat.id, reply_message_text)
        start(call.message, True)
    except Exception as e:
        bot.send_message(call.message.chat.id, f"خطا در پردازش تایید: {str(e)}")


if __name__ == "__main__":
    bot.polling(none_stop=True)
