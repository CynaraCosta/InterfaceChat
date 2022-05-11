from datetime import datetime


class MessageHelper:
    INVALID_MESSAGE = "Favor digite uma mensagem válida antes de enviar!"

    def create_message(message, nickname):
        time_now = datetime.now()

        return f'< {time_now.strftime("%H:%M")} {nickname}: > {message}'

    def is_valid_to_send(message):
        notOnlySpaces = message.replace(' ', '') != ''

        return notOnlySpaces
